---
phase: 08-search-functionality-across-all-models
plan: 01
subsystem: ui
 tags: [django, search, q-objects, navigation]

# Dependency graph
requires:
  - phase: 07-storyboard-display
    provides: Episode/Sequence/Shot models with storyboard views, base.html template structure
provides:
  - Global search functionality across all models
  - Search form in header navigation
  - Search results page with relevance ranking
affects: [09-filtering, 10-export]

# Tech tracking
added: []
patterns:
  - "Q objects with icontains for case-insensitive multi-field search"
  - "Relevance scoring: exact match (100) > partial title (50) > description (10)"
  - "GET method form with query parameter"

key-files:
  created:
    - templates/series/search_results.html
  modified:
    - series/views.py (search function)
    - series/urls.py (search URL pattern)
    - templates/base.html (search form in header)

key-decisions:
  - "Used Django ORM Q objects instead of external search libraries (haystack, elasticsearch)"
  - "Searches across 8 models: Series, Season, Episode, Sequence, Shot, Character, Prop, WardrobeItem"
  - "Props link to Django admin (no user-facing detail view exists)"
  - "Results limited to top 50 by relevance score"

requirements-completed: [FEAT-01]

# Metrics
duration: 5 min
completed: 2026-03-12
---

# Phase 8 Plan 1: Search Functionality Summary

## What Was Built

Global search functionality that allows users to search across all content models in the Memoon application.

### Features Implemented

1. **Search Box in Header** — Visible on all pages, styled consistently with existing dark mode theme
2. **Multi-Model Search** — Searches Series, Seasons, Episodes, Sequences, Shots, Characters, Props, and Wardrobe Items
3. **Relevance Ranking** — Results ranked by match quality:
   - Exact match in title/name field = 100 points
   - Partial match in title/name field = 50 points  
   - Match in description/secondary fields = 10 points
4. **Type Badges** — Each result shows its model type (Series, Episode, Character, etc.)
5. **Direct Links** — Each result links to its detail page (except Props which link to admin)
6. **Query Validation** — Requires at least 2 characters, shows appropriate messages for empty/short queries

### Technical Implementation

- **Backend:** Django Q objects with `icontains` lookups for case-insensitive partial matching
- **Frontend:** GET form submission, results template extending base.html
- **URL:** `/search/?q=query` maps to `series:search`
- **Limit:** Top 50 results returned

### Success Criteria Met

✓ Global search form visible in navigation/header on all pages  
✓ Search returns results from Series, Episodes, Sequences, Shots, Characters, and Props  
✓ Each result displays its type and clickable title  
✓ Each result links to appropriate detail page  
✓ Results ordered by relevance (exact matches appear before partial matches)  
✓ Search handles empty/small queries gracefully  
✓ UI consistent with existing dark mode and styling  

### Notes

- Wardrobe items link to their associated character's detail page
- Props link to Django admin change page (no user-facing Prop detail view exists)
- Shot search covers script, background, camera angle, movement, and notes fields
- Future enhancement: Full-text search with PostgreSQL or dedicated search engine

---

*Phase 08 - Search functionality across all models*  
*Completed: 2026-03-12*
