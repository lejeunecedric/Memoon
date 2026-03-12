# Memoon

## What This Is

A Django-powered content structure manager for creative teams and solo storytellers. Organize animated series, screenplays, or multimedia projects hierarchically — from the big picture down to the finest detail.

## Core Value

A simple, clean way to organize production assets for stories — Series → Seasons → Episodes → Sequences → Shots.

## Requirements

### Validated (v1.0)

- ✅ CORE-01: Application runs without errors
- ✅ CORE-02: All CRUD operations work
- ✅ CORE-03: CSV import functions correctly
- ✅ AUTH-01: User authentication (login/logout) functionality
- ✅ AUTH-02: User roles (Admin, Power User, User)
- ✅ AUTH-03: Permission checks based on roles
- ✅ AUTH-04: User menu in UI
- ✅ FEAT-01: Dark mode with theme toggle
- ✅ FEAT-02: Props model for tracking physical objects
- ✅ STORY-01: Storyboard grid display at Episode level (sequences/shots as visual cards)
- ✅ STORY-02: Storyboard grid display at Sequence level (shots as visual cards)
- ✅ STORY-03: Optional image upload per shot
- ✅ STORY-04: Image display in storyboard grids (when uploaded)

### Active (v1.2)

- [ ] FEAT-01: Search functionality across all models
- [ ] FEAT-02: Better filtering and sorting
- [ ] FEAT-03: Export to common formats (JSON, CSV)

### Out of Scope

- [Real-time collaboration] — Single user for now
- [Cloud storage] — Local SQLite is fine

## Context

- Existing Django 6.0.2 application
- SQLite database
- Already has: Series, Seasons, Episodes, Sequences, Shots, Characters, Wardrobe, Props
- Already has: Web UI, Admin interface, CSV import, Dark mode, User authentication

## Constraints

- **[Tech]**: Django + SQLite — Simple, no complex dependencies

---

*Last updated: 2026-03-12 after v1.1 milestone complete*
