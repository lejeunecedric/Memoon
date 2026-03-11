# Codebase Concerns

**Analysis Date:** 2026-03-11

## Tech Debt

**Empty Test Suite:**
- Issue: `series/tests.py` contains only the default Django test placeholder comment
- Files: `series/tests.py`
- Impact: No automated testing for models, views, or business logic - high risk of regressions
- Fix approach: Create comprehensive tests using Django's TestCase for models, views, and import/export functionality

**Hardcoded Development Paths:**
- Issue: Import script contains hardcoded absolute paths that won't work on different systems
- Files: `import_lessisters.py`
- Current: `sys.path.insert(0, "/home/c/Dev/Memoon")` (line 12) and `SCRIPTS_DIR = "/home/c/Dev/CartoonMem/LesSisters_scripts"` (line 26)
- Impact: Import script fails when run on any system except the original developer's machine
- Fix approach: Use relative paths or environment variables for configuration

**No Database Indexes:**
- Issue: Frequently queried foreign key and field lookups lack explicit database indexes
- Files: `series/models.py`
- Impact: Query performance degrades significantly as data grows, especially on Shot, Episode, and Character queries
- Fix approach: Add `db_index=True` to frequently filtered fields (e.g., `Episode.script_status`, `Shot.number`, `Character.name`)

**No Pagination on List Views:**
- Issue: All ListView classes load all objects without pagination
- Files: `series/views.py`
- Impact: Performance degrades with large datasets; no user-friendly browsing for large collections
- Fix approach: Add `paginate_by = 50` to ListView classes or implement cursor-based pagination

**Unused Configuration:**
- Issue: `OTIO_MEDIA_BASE_PATH` defaults to None, and `OTIO_DEFAULT_FRAMERATE` is set but not validated
- Files: `cartoon_manager/settings.py` (lines 120-121)
- Impact: Export functionality may fail silently or produce incorrect output when settings are not configured
- Fix approach: Add validation in exporter or provide sensible defaults

## Known Bugs

**CSV Import Numeric Validation:**
- Symptoms: Import fails with unclear error when `sequence_number` or `shot_number` fields contain non-numeric values
- Files: `series/views.py` (lines 145-146)
- Trigger: Upload CSV with invalid numeric data
- Workaround: Users must manually validate CSV before import
- Fix approach: Add try/except with specific error message, or validate in form

**Character Shot Limit:**
- Symptoms: Only 20 shots displayed on character detail page despite character having more
- Files: `series/views.py` (line 104-106)
- Trigger: Character with more than 20 shots
- Workaround: None - shots beyond first 20 are hidden
- Fix approach: Implement pagination or lazy loading on character detail view

**Episode Export Duplicate Queries:**
- Symptoms: Export operation makes duplicate database queries for sequences and shots
- Files: `series/exporters/otio_exporter.py` (lines 23 and 73-74)
- Trigger: Export any episode with multiple sequences
- Impact: Performance degrades with episode complexity (N+2 queries per sequence)
- Fix approach: Use `select_related` and cache the sequence/shot iteration

## Security Considerations

**Hardcoded Secret Key:**
- Risk: Django SECRET key is hardcoded in source code
- Files: `cartoon_manager/settings.py` (line 23)
- Current mitigation: None
- Recommendations: Move to environment variable or secrets management; regenerate key for production

**Debug Mode Enabled:**
- Risk: `DEBUG = True` exposes detailed error pages with stack traces and settings information
- Files: `cartoon_manager/settings.py` (line 26)
- Current mitigation: None
- Recommendations: Set `DEBUG = False` in production; use environment-based configuration

**Empty ALLOWED_HOSTS:**
- Risk: Django will not validate HTTP Host header, potential for DNS rebinding attacks
- Files: `cartoon_manager/settings.py` (line 28)
- Current mitigation: None
- Recommendations: Add production domain(s) to `ALLOWED_HOSTS`

**No Authentication:**
- Risk: Entire application is publicly accessible with no access control
- Files: All views in `series/views.py`
- Current mitigation: None
- Recommendations: Implement Django authentication (login/logout), consider @login_required decorators

**No CSRF Exemptions for API Views:**
- Risk: CSV import form uses Django's CSRF protection but could be bypassed by API clients
- Files: `series/views.py` (CSVImportView)
- Current mitigation: Using Django FormView with CSRF
- Recommendations: Consider token-based authentication for programmatic imports

## Performance Bottlenecks

**N+1 Query Pattern in Views:**
- Problem: Detail views use prefetch_related but don't optimize foreign key access
- Files: `series/views.py`
- Specific: `CharacterDetailView` line 104 uses `select_related` but still fetches related separately
- Cause: Missing `prefetch_related` for reverse foreign key relationships
- Improvement path: Add `prefetch_related("shots__sequence__episode__season__series")`

**Duplicate Database Hits in Exporter:**
- Problem: `episode_to_timeline()` iterates sequences twice (video track and audio track)
- Files: `series/exporters/otio_exporter.py` (lines 23 and 73)
- Cause: Separate loops for video and audio without caching results
- Improvement path: Fetch sequences once, cache shots, iterate cached data

**Large CSV Import Without Progress:**
- Problem: Large CSV imports run in single transaction without progress indication
- Files: `series/views.py` (CSVImportView.form_valid)
- Cause: No chunking or background task processing
- Improvement path: Use Django Q tasks or chunked processing with progress updates

## Fragile Areas

**Import Script Path Handling:**
- Why fragile: Hardcoded Unix-style paths break on Windows
- Files: `import_lessisters.py`
- Safe modification: Use `pathlib.Path` with environment variable fallback
- Test coverage: None - manual testing only

**CSV Field Mapping:**
- Why fragile: No validation of expected CSV columns; silently skips unknown fields
- Files: `series/views.py` (lines 144-206)
- Safe modification: Add explicit column validation and user feedback
- Test coverage: None

**OTIO Format Fallback:**
- Why fragile: Silent fallback to OTIO JSON if FCPXML adapter unavailable
- Files: `series/exporters/otio_exporter.py` (lines 109-113)
- Safe modification: Log warning when fallback occurs
- Test coverage: None

## Scaling Limits

**SQLite Database:**
- Current capacity: Single-user development scale (~10K records reasonable)
- Limit: SQLite has write contention limits; no concurrent write support
- Scaling path: Migrate to PostgreSQL for production with concurrent access

**File-Based Media:**
- Current capacity: Local filesystem storage
- Limit: No cloud storage integration; single-server deployment
- Scaling path: Add Django-storages with S3/GCS for media files

**Synchronous CSV Import:**
- Current capacity: Small to medium files (~1000 shots)
- Limit: Timeout risk for large files; blocks request/response
- Scaling path: Implement Celery/Redis for background processing

## Dependencies at Risk

**Django 4.0+:**
- Risk: Using `Django>=4.0` is too loose - could auto-upgrade to incompatible version
- Impact: Breaking changes in minor releases could break application
- Migration plan: Pin to specific version (e.g., `Django>=4.0,<5.0`)

**pdfplumber:**
- Risk: PDF parsing library may fail on malformed PDFs
- Impact: Import script crashes on invalid PDFs with no graceful error handling
- Migration plan: Add try/except with detailed logging around pdfplumber calls

**opentimelineio:**
- Risk: Heavy dependency for timeline export; version compatibility issues common
- Impact: Installation failures on some platforms; adapter availability inconsistent
- Migration plan: Pin to tested version; add graceful degradation when unavailable

## Missing Critical Features

**User Authentication:**
- Problem: No user accounts, authentication, or authorization
- Blocks: Multi-user access, permission management, audit logging

**API Endpoints:**
- Problem: No REST/GraphQL API for programmatic access
- Blocks: External integrations, mobile apps, automation

**Data Validation:**
- Problem: Minimal validation on model fields and imports
- Blocks: Data quality guarantees, import reliability

**Backup/Export:**
- Problem: No database backup or full export functionality
- Blocks: Disaster recovery, data portability

## Test Coverage Gaps

**Models:**
- What's not tested: All model validation, unique constraints, `__str__` methods
- Files: `series/models.py`
- Risk: Model changes could break data integrity without detection
- Priority: High

**Views:**
- What's not tested: All CRUD views, CSV import, OTIO export
- Files: `series/views.py`
- Risk: View changes could break functionality without detection
- Priority: High

**Import Logic:**
- What's not tested: PDF parsing, character extraction, scene parsing
- Files: `import_lessisters.py`
- Risk: PDF format changes break import silently
- Priority: Medium

**Export Logic:**
- What's not tested: Timeline generation, format conversion, edge cases
- Files: `series/exporters/otio_exporter.py`
- Risk: Export produces invalid files without detection
- Priority: Medium

---

*Concerns audit: 2026-03-11*
