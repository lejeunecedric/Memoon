# Codebase Structure

**Analysis Date:** 2026-03-11

## Directory Layout

```
Memoon/
├── cartoon_manager/          # Django project root
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
├── series/                   # Main application
│   ├── __init__.py
│   ├── models.py             # Database models
│   ├── views.py              # View handlers
│   ├── urls.py               # App URL configuration
│   ├── forms.py              # Form definitions
│   ├── admin.py              # Admin configuration
│   ├── admin_config.py       # Admin extras
│   ├── apps.py               # App configuration
│   ├── tests.py              # Unit tests
│   ├── migrations/           # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_episode_script_...
│   ├── management/           # Management commands
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_70s_series.py
│   └── exporters/           # Export utilities
│       ├── __init__.py
│       └── otio_exporter.py
├── templates/                # Global templates
│   ├── base.html
│   ├── series/               # App templates
│   │   ├── series_list.html
│   │   ├── series_detail.html
│   │   ├── season_detail.html
│   │   ├── episode_detail.html
│   │   ├── sequence_detail.html
│   │   ├── shot_detail.html
│   │   ├── character_list.html
│   │   ├── character_detail.html
│   │   └── csv_import.html
│   └── admin/
│       └── base_site.html
├── manage.py                 # Django CLI
├── db.sqlite3                # SQLite database
├── requirements.txt          # Python dependencies
├── create_sample_data.py     # Data generation script
├── import_lessisters.py      # Data import script
├── sample_import.csv         # Sample CSV file
├── start.sh                  # Startup script
└── .gitignore
```

## Directory Purposes

**cartoon_manager/:**
- Purpose: Django project configuration
- Contains: Settings, URL routing, WSGI/ASGI entry points
- Key files: `settings.py`, `urls.py`, `wsgi.py`

**series/:**
- Purpose: Main application for cartoon/series management
- Contains: Models, Views, Forms, Admin, Exporters
- Key files: `models.py`, `views.py`, `urls.py`, `forms.py`

**templates/:**
- Purpose: HTML templates for rendering
- Contains: Base template and series-specific templates
- Key files: `base.html`, `series/episode_detail.html`

## Key File Locations

**Entry Points:**
- `manage.py`: Django management CLI
- `cartoon_manager/wsgi.py`: WSGI application for deployment

**Configuration:**
- `cartoon_manager/settings.py`: Django settings (database, installed apps, middleware, templates)
- `requirements.txt`: Python dependencies

**Core Logic:**
- `series/models.py`: Database schema definition (8 models)
- `series/views.py`: HTTP request handlers (10 views)
- `series/forms.py`: Form validation (1 form)
- `series/exporters/otio_exporter.py`: Timeline export functionality

**Testing:**
- `series/tests.py`: Unit tests (currently minimal)

**Management:**
- `series/management/commands/populate_70s_series.py`: Data population command

## Naming Conventions

**Files:**
- `snake_case.py`: Standard Python naming
- `series/models.py`: App-specific singular noun
- `series/urls.py`: Domain-specific noun
- `otio_exporter.py`: Function-specific noun phrase

**Directories:**
- `snake_case/`: Standard Python naming
- `series/`: App name matching Django convention
- `management/commands/`: Django management command structure

**Models (in `series/models.py`):**
- PascalCase: `Series`, `Season`, `Episode`, `Sequence`, `Shot`
- Singular noun for model class
- Related name patterns: `related_name="seasons"`, `related_name="episodes"`

**Views (in `series/views.py`):**
- PascalCase with View suffix: `SeriesListView`, `SeriesDetailView`
- Function views: `episode_otio_export` (snake_case)

**URL Patterns (in `series/urls.py`):**
- kebab-case in URLs: `series/<int:pk>/`, `episode/<int:pk>/export/otio/`
- Name suffix in URL names: `name="series_detail"`, `name="episode_otio_export"`

**Templates:**
- snake_case.html: `series_list.html`, `episode_detail.html`
- Directory matches app name: `templates/series/`

## Where to Add New Code

**New Model:**
- Add to `series/models.py`
- Create migration: `python manage.py makemigrations`
- Register in `series/admin.py` (if admin needed)

**New View:**
- Add to `series/views.py`
- Add URL pattern to `series/urls.py`
- Create template in `templates/series/`

**New Template:**
- Add to `templates/series/`
- Extend from `templates/base.html`

**New Form:**
- Add to `series/forms.py`
- Use in view via FormView or function view

**New Exporter:**
- Add to `series/exporters/` (create directory if needed)
- Import in `series/views.py`

**Management Command:**
- Add to `series/management/commands/<command_name>.py`
- Inherit from `BaseCommand`

## Special Directories

**migrations/:**
- Purpose: Database schema migrations
- Generated: Yes (via `makemigrations`)
- Committed: Yes (track schema changes)

**management/commands/:**
- Purpose: Django management commands
- Generated: No (custom code)
- Committed: Yes

**exporters/:**
- Purpose: Export functionality
- Generated: No (custom code)
- Committed: Yes

---

*Structure analysis: 2026-03-11*
