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

### Active

- [ ] Keep the Django app running smoothly
- [ ] Add new features as needed
- [ ] Improve the user interface

### Out of Scope

- [Real-time collaboration] — Single user for now
- [Cloud storage] — Local SQLite is fine

## Context

- Existing Django 6.0.2 application
- SQLite database
- Already has: Series, Seasons, Episodes, Sequences, Shots, Characters, Wardrobe
- Already has: Web UI, Admin interface, CSV import

## Constraints

- **[Tech]**: Django + SQLite — Simple, no complex dependencies

---

*Last updated: 2025-03-11 after initialization*
