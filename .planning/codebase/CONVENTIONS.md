# Coding Conventions

**Analysis Date:** 2026-03-11

## Language & Framework

**Primary:**
- Python 3.x - Core application logic
- Django 4.0+ - Web framework

**Project Type:** Django web application for cartoon/animation production management

## Naming Patterns

**Files:**
- snake_case: `models.py`, `views.py`, `forms.py`, `admin.py`
- Management commands: `populate_70s_series.py`

**Classes:**
- PascalCase: `Series`, `Season`, `Episode`, `Sequence`, `Shot`
- Django admin: `SeriesAdmin`, `SeasonAdmin`, `CSVImportForm`
- Management command: `Command(BaseCommand)`

**Functions:**
- snake_case: `duration_to_frames()`, `episode_to_timeline()`, `export_episode()`
- Views: Class-based using `.as_view()`

**Variables:**
- snake_case: `csv_file`, `series_queryset`, `shot_count`
- Django model instances: `series`, `season`, `episode`
- Loop variables: `row`, `char_name`, `wardrobe_item`

**Constants:**
- UPPER_SNAKE_CASE: `DEFAULT_FRAMERATE = 24`

## Code Style

**Formatting:**
- 4 spaces for indentation (Python standard)
- No enforced formatter (Black not configured)
- Line lengths not strictly enforced

**Linting:**
- No linter configured (flake8, pylint not found)
- Django's built-in validation used

**Django Model Style:**
```python
class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ["title"]

    def __str__(self):
        return self.title
```

**Key Patterns:**
- ForeignKey with `on_delete=models.CASCADE` and `related_name`
- Unique constraints via `unique_together` in Meta
- Choices defined as tuples of tuples: `choices=[("draft", "Draft"), ...]`
- Blank=True for optional CharField/TextField

## Import Organization

**Order:**
1. Standard library: `from django.shortcuts import ...`
2. Django imports: `from django.views.generic import ...`
3. Third-party: `import csv`, `import io`
4. Local imports: `from .models import ...`, `from .forms import ...`

**Grouping:**
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.conf import settings
import csv
import io
from .models import (
    Series,
    Season,
    Episode,
    # ...
)
```

## Django Patterns

**Views:**
- Class-based views using Django generics: `ListView`, `DetailView`, `FormView`
- Custom form validations in `form_valid()` method
- Use `get_object_or_404()` for single object retrieval
- Query optimization with `prefetch_related()` and `select_related()`

**Forms:**
- Extend `forms.Form` for non-model forms
- Custom `__init__` for dynamic queryset injection

**Admin:**
- Use `@admin.register(Model)` decorator
- TabularInlines for related objects
- Fieldsets for organizing form sections

**URLs:**
- Use `app_name` for namespacing
- Class-based views: `views.SeriesListView.as_view()`
- Function views: `views.episode_otio_export`

## Error Handling

**Patterns:**
- Try/except blocks for file processing:
```python
try:
    decoded_file = csv_file.read().decode("utf-8")
    # processing...
except Exception as e:
    messages.error(self.request, f"Error importing CSV: {str(e)}")
    return self.form_invalid(form)
```

- Database operations wrapped in `transaction.atomic()`:
```python
with transaction.atomic():
    # database operations
```

- Use Django messages framework for user feedback

## Logging

**Approach:** Django's logging not configured; uses `self.stdout.write()` in management commands:
```python
self.stdout.write('Creating The Rockford Files...')
self.stdout.write(self.style.SUCCESS('Successfully created 70s TV series data!'))
```

## Comments

**When to Comment:**
- Help text on model fields: `help_text="Full episode script"`
- Inline comments in complex logic (management commands)
- Minimal docstrings used in some functions

**Not Used:**
- Extensive JSDoc/TSDoc (Python project)
- Type hints not commonly used

## Function Design

**Size:** Varies; management commands are large (900+ lines), views are moderate (250 lines)

**Parameters:**
- Clear naming, no type hints
- Django request object for views
- Explicit keyword arguments with defaults

**Return Values:**
- Views return `HttpResponse` or rendered templates
- Export functions return string content

## Module Design

**Django App Structure:**
```
series/
├── __init__.py
├── models.py       # All models in single file
├── views.py        # All views (mix of CBV and functions)
├── forms.py        # Forms
├── urls.py         # URL routing
├── admin.py        # Admin registration
├── admin_config.py # Admin site configuration
├── apps.py         # App config
├── exporters/      # Export functionality
│   └── otio_exporter.py
├── management/    # Management commands
│   └── commands/
│       └── populate_70s_series.py
├── migrations/    # Database migrations
└── tests.py       # Tests (currently empty)
```

**No barrel files** - Direct imports from modules

---

*Convention analysis: 2026-03-11*
