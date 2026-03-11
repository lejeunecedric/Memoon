# Architecture

**Analysis Date:** 2026-03-11

## Pattern Overview

**Overall:** Django MVT (Model-View-Template)

**Key Characteristics:**
- Classic Django web application following MVT pattern
- Single app architecture with `series` app handling all domain logic
- SQLite database for persistence
- Generic class-based views (CBV) for web interface
- REST-adjacent export functionality via OTIO

## Layers

**Models (Data Layer):**
- Purpose: Define data schema and relationships for cartoon/series production
- Location: `series/models.py`
- Contains: 8 models (Series, Season, Episode, Sequence, Shot, Character, WardrobeItem, ShotCharacter)
- Depends on: Django ORM (`django.db.models`)
- Used by: Views, Admin, Exporters

**Views (Business Logic Layer):**
- Purpose: Handle HTTP requests, orchestrate data flow, render responses
- Location: `series/views.py`
- Contains: 6 ListView/DetailView classes, 1 FormView class, 1 function view
- Depends on: Models, Forms, Exporters
- Used by: URL router

**Templates (Presentation Layer):**
- Purpose: Render HTML responses to users
- Location: `templates/series/`
- Contains: 9 template files + 1 base template
- Depends on: Django template engine
- Used by: Views (via render())

**Forms (Input Validation Layer):**
- Purpose: Validate and process user input
- Location: `series/forms.py`
- Contains: CSVImportForm
- Depends on: Django forms
- Used by: CSVImportView

**Exporters (Integration Layer):**
- Purpose: Convert episode data to external timeline formats
- Location: `series/exporters/otio_exporter.py`
- Contains: Functions for OTIO/FCPXML export
- Depends on: opentimelineio library
- Used by: Views (episode_otio_export)

**Admin (Management Layer):**
- Purpose: Provide admin interface for data management
- Location: `series/admin.py`, `series/admin_config.py`
- Contains: ModelAdmin configurations with inlines
- Depends on: Django admin
- Used by: Django admin site

## Data Flow

**Standard Request Flow:**

1. HTTP Request → `cartoon_manager/urls.py` → routes to `series/urls.py`
2. URL pattern matches → dispatches to View class/function in `series/views.py`
3. View queries Models → Django ORM retrieves data from SQLite
4. View prepares context → renders Template with data
5. Template produces HTML → HTTP Response returned to client

**CSV Import Flow:**

1. GET request → `CSVImportView` renders form in `series/csv_import.html`
2. POST with CSV file → `form_valid()` processes file
3. `csv.DictReader` parses rows → `transaction.atomic()` ensures consistency
4. Models created/updated: Season → Episode → Sequence → Shot → Character/WardrobeItem/ShotCharacter
5. Success message flashed → redirect to series list

**Export Flow:**

1. GET request to `/episode/<pk>/export/otio/`
2. `episode_otio_export()` function retrieves Episode with prefetched relations
3. Calls `export_episode()` in `series/exporters/otio_exporter.py`
4. Creates OTIO timeline structure with video/audio tracks
5. Returns file as HTTP response with appropriate content-type

## Key Abstractions

**Django ORM Models:**
- Purpose: Represent production data entities with relationships
- Examples: `series/models.py` - Series, Season, Episode, Sequence, Shot
- Pattern: Django Model with ForeignKey, ManyToManyField, through tables

**Class-Based Views:**
- Purpose: Reusable request handlers with common patterns
- Examples: `SeriesListView`, `SeriesDetailView`, `SeasonDetailView`
- Pattern: Django generic views (ListView, DetailView, FormView)

**Inline Admin Configurations:**
- Purpose: Hierarchical data entry in admin interface
- Examples: SeasonInline in SeriesAdmin, ShotInline in SequenceAdmin
- Pattern: TabularInline with nested relationships

## Entry Points

**Django Development Server:**
- Location: `manage.py`
- Triggers: `python manage.py runserver`
- Responsibilities: Initialize Django, load settings, start WSGI server

**WSGI Application:**
- Location: `cartoon_manager/wsgi.py`
- Triggers: Production deployment via Gunicorn/uWSGI
- Responsibilities: WSGI callable, settings configuration

**URL Router (Root):**
- Location: `cartoon_manager/urls.py`
- Triggers: Every HTTP request
- Responsibilities: Route to admin or series app

**URL Router (App):**
- Location: `series/urls.py`
- Triggers: Requests to `/`, `/series/`, `/season/`, `/episode/`, etc.
- Responsibilities: Map URLs to View classes/functions

**Management Commands:**
- Location: `series/management/commands/`
- Triggers: `python manage.py populate_70s_series`
- Responsibilities: Data population scripts

## Error Handling

**Strategy:** Django default exception handling

**Patterns:**
- `get_object_or_404()` for 404 on missing objects
- Try/except in CSVImportView with transaction rollback
- Django messages framework for user feedback
- Model validation via `unique_together` constraints

## Cross-Cutting Concerns

**Logging:** Not explicitly configured - uses Django defaults

**Validation:** 
- Django model field validation (max_length, choices)
- Form validation in `series/forms.py`
- Database constraints (unique_together)

**Authentication:** Not implemented - open access to all views

---

*Architecture analysis: 2026-03-11*
