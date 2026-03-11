# Technology Stack

**Analysis Date:** 2026-03-11

## Languages

**Primary:**
- Python 3.x - Full application (Django backend, models, views, management commands)

**Secondary:**
- HTML/CSS - Templates for web interface (Django Templates engine)
- SQL - Database queries (via Django ORM)

## Runtime

**Environment:**
- Python - Standard Python runtime
- Virtual environment recommended (per README)

**Package Manager:**
- pip - Python package manager
- Lockfile: Not detected (requirements.txt only)

## Frameworks

**Core:**
- Django 6.0.2 - Full-stack web framework
  - Built-in admin interface
  - Django ORM for database
  - Django Templates for rendering

**Data Processing:**
- pdfplumber >= 0.11.0 - PDF text extraction (per requirements.txt)

**Media/Timeline:**
- opentimelineio >= 0.18.0 - Video timeline export
  - Used in `series/exporters/otio_exporter.py`
  - Supports OTIO JSON and Final Cut Pro XML export formats

**Testing:**
- Not detected - No explicit test framework configured

## Key Dependencies

**Core Django:**
- Django >= 4.0 - Web framework (installed: 6.0.2)

**Media Processing:**
- opentimelineio >= 0.18.0 - Video timeline interchange format
  - Used in `series/exporters/otio_exporter.py` for episode export
  - Supports FCP XML and OTIO JSON formats

**PDF Processing:**
- pdfplumber >= 0.11.0 - PDF text extraction
  - Listed in requirements but not currently imported in codebase

## Configuration

**Environment:**
- Django settings in `cartoon_manager/settings.py`
- Database: SQLite3 at `db.sqlite3`
- Debug: True (development mode)
- ALLOWED_HOSTS: Empty (all hosts allowed in DEBUG mode)

**Django-Specific Settings:**
```python
SECRET_KEY: "django-insecure-3o(%yn@@knl&wsxx*8*0nvvdg8#&)jh_6rj1915)0-8vy6@ey@"
DEBUG: True
ALLOWED_HOSTS: []
OTIO_MEDIA_BASE_PATH: None
OTIO_DEFAULT_FRAMERATE: 24
```

**Build:**
- No build tools (pure Python/Django)
- manage.py for Django commands (default port 8089)

## Platform Requirements

**Development:**
- Python 3.x
- Django 6.0.2
- SQLite3 (bundled with Python)
- Virtual environment recommended

**Production:**
- Not configured for production deployment
- Would require: WSGI server (gunicorn/uwsgi), production database, proper SECRET_KEY, ALLOWED_HOSTS configuration

**Database:**
- SQLite3 - Local file-based database
- Location: `db.sqlite3` in project root
- Migrations present in `series/migrations/`

---

*Stack analysis: 2026-03-11*
