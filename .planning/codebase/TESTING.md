# Testing Patterns

**Analysis Date:** 2026-03-11

## Test Framework

**Runner:**
- Django's built-in test framework
- Version: Django 4.0+ (from requirements.txt)
- Config: No custom test configuration detected

**Run Commands:**
```bash
python manage.py test              # Run all tests
python manage.py test series      # Run tests for series app
python manage.py test --verbosity=2  # Verbose output
```

**Assertion Library:**
- Django's `django.test.TestCase` with `assertEqual`, `assertTrue`, `assertFalse`, etc.
- Django's `assertRaises`, `assertQuerySetEqual`

## Test File Organization

**Location:**
- `series/tests.py` - Main test file for series app

**Naming:**
- Django convention: `tests.py` (not `test_*.py`)

**Structure:**
- Currently empty (only contains comment: `# Create your tests here.`)

## Test Structure

**Current State:**
- No tests written yet - `series/tests.py` is essentially empty

**Expected Pattern (Django Standard):**
```python
from django.test import TestCase
from django.urls import reverse
from series.models import Series, Season, Episode

class SeriesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Series.objects.create(title="Test Series")

    def test_series_title(self):
        series = Series.objects.get(title="Test Series")
        self.assertEqual(series.title, "Test Series")

    def test_series_str(self):
        series = Series.objects.get(title="Test Series")
        self.assertEqual(str(series), "Test Series")
```

## Mocking

**Framework:** Django's test client and request factory

**Patterns:**
- Use `django.test.Client` for HTTP requests
- Use `django.test.RequestFactory` for view testing
- Model mocking via direct creation in `setUpTestData()`

**Example (not in codebase but standard):**
```python
from django.test import TestCase, Client
from django.urls import reverse

class SeriesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_series_list_view(self):
        response = self.client.get(reverse('series:series_list'))
        self.assertEqual(response.status_code, 200)
```

## Fixtures and Factories

**Test Data:**
- No test fixtures detected (no `.json` or `.yaml` fixtures)
- Management command `populate_70s_series.py` creates sample data but is not a test fixture

**Location:**
- Django fixtures typically in `series/fixtures/`
- Not present in this codebase

**Alternative:**
- Use `setUpTestData()` class method or `setUp()` method for creating test data
- Management commands can be used to create test data manually

## Coverage

**Requirements:** None enforced

**View Coverage:**
```bash
python manage.py test --coverage=1  # If coverage installed
```

**Note:** No coverage tool configured

## Test Types

**Unit Tests:**
- Not currently implemented
- Would test model methods, form validation, utility functions

**Integration Tests:**
- Not currently implemented
- Would test views, URLs, database operations

**E2E Tests:**
- Not used - no Selenium or Playwright configured

## Missing Testing Infrastructure

**No pytest:**
- No `pytest` or `pytest-django` installed
- No `pytest.ini` or `conftest.py`

**No additional testing packages:**
- No `factory_boy` for test fixtures
- No `pytest-cov` for coverage

**Django TestCase available but not used:**
- `django.test.TestCase`
- `django.test.TransactionTestCase`
- `django.test.Client`
- `django.test.RequestFactory`

## Best Practices (Not Yet Applied)

1. **Add tests to `series/tests.py`:**
   ```python
   from django.test import TestCase
   from series.models import Series
   
   class SeriesModelTest(TestCase):
       def test_str_method(self):
           series = Series(title="Test Series")
           self.assertEqual(str(series), "Test Series")
   ```

2. **Consider adding pytest:**
   ```bash
   pip install pytest pytest-django
   ```
   
   Then create `pytest.ini`:
   ```ini
   [pytest]
   DJANGO_SETTINGS_MODULE = cartoon_manager.settings
   python_files = tests.py test_*.py *_tests.py
   ```

3. **Add factories for test data:**
   ```python
   # series/tests/factories.py
   import factory
   from series.models import Series
   
   class SeriesFactory(factory.django.DjangoModelFactory):
       class Meta:
           model = Series
       title = factory.Sequence(lambda n: f"Series {n}")
   ```

---

*Testing analysis: 2026-03-11*
