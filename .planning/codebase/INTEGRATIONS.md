# External Integrations

**Analysis Date:** 2026-03-11

## APIs & External Services

**No external REST APIs detected.**

The application is a self-contained Django application without external API integrations.

## Data Storage

**Databases:**
- SQLite3 (local file-based)
  - Connection: `db.sqlite3` file in project root
  - Client: Django ORM (django.db.backends.sqlite3)
  - Configuration: `cartoon_manager/settings.py` lines 76-81

**File Storage:**
- Local filesystem only
  - SQLite database: `db.sqlite3`
  - Static files: `static/` directory (Django static files)
  - Templates: `templates/` directory

**Caching:**
- None - No caching framework configured

## Authentication & Identity

**Auth Provider:**
- Django built-in authentication
  - User model: Django's default `auth.User`
  - Session-based authentication (django.contrib.sessions)
  - Password validation: 4 validators configured (UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator)
  - No external auth providers (no OAuth, no LDAP)

## Media Processing

**OpenTimelineIO:**
- Library: opentimelineio >= 0.18.0
- Purpose: Export episode timelines to industry-standard formats
- Implementation: `series/exporters/otio_exporter.py`
- Export formats:
  - OTIO JSON (default)
  - Final Cut Pro XML (fcpxml)
- Configuration:
  - `OTIO_MEDIA_BASE_PATH` - Base path for media files (optional, defaults to None)
  - `OTIO_DEFAULT_FRAMERATE` - Default frame rate (default: 24)
- Usage: `/episode/<pk>/export/otio/?format=otio|fcpxml&media_path=<path>&framerate=<int>`

**PDF Processing:**
- Library: pdfplumber >= 0.11.0
- Purpose: PDF text extraction (listed in requirements)
- Current status: Not currently imported or used in codebase

## Monitoring & Observability

**Error Tracking:**
- None - No external error tracking service

**Logs:**
- Django logging: Default console logging
- No structured logging or external log aggregation

## CI/CD & Deployment

**Hosting:**
- Not configured for deployment
- Development server: `python manage.py runserver` (default port 8089)
- WSGI: `cartoon_manager/wsgi.py` available
- ASGI: `cartoon_manager/asgi.py` available

**CI Pipeline:**
- None detected

## Environment Configuration

**Required settings (in `cartoon_manager/settings.py`):**
- `SECRET_KEY` - Django secret key (hardcoded, should be env var in production)
- `DEBUG` - Debug mode flag (True)
- `ALLOWED_HOSTS` - Allowed hosts list (empty)
- `OTIO_MEDIA_BASE_PATH` - Media path for OTIO exports
- `OTIO_DEFAULT_FRAMERATE` - Default frame rate for exports

**Secrets location:**
- `cartoon_manager/settings.py` - Contains hardcoded SECRET_KEY
- No .env file detected

## Webhooks & Callbacks

**Incoming:**
- None - No webhook endpoints

**Outgoing:**
- None - No outgoing webhook calls

## Project Structure Summary

**Django Apps:**
- `series` - Main application for cartoon series management
  - Models: Series, Season, Episode, Sequence, Shot, Character, WardrobeItem, ShotCharacter
  - Views: ListView, DetailView, FormView for CRUD operations
  - Exporters: OpenTimelineIO integration

**URL Endpoints:**
- `/` - Series list
- `/series/<pk>/` - Series detail
- `/season/<pk>/` - Season detail
- `/episode/<pk>/` - Episode detail
- `/episode/<pk>/export/otio/` - Export episode to OTIO/FCPXML
- `/sequence/<pk>/` - Sequence detail
- `/shot/<pk>/` - Shot detail
- `/characters/` - Character list
- `/character/<pk>/` - Character detail
- `/import-csv/` - CSV import form
- `/admin/` - Django admin interface

---

*Integration audit: 2026-03-11*
