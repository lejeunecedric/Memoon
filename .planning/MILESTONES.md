# Milestones

## v1.0 - Initial Release

**Status:** ✅ Complete  
**Date:** 2026-03-12  
**Progress:** 100%

### Overview

Foundation release of Memoon with core features for managing animated series content structure.

### Phases Included

- **Foundation** (Phases 01-03): Core application stability and usability
- **Phase 04:** Dark mode with theme toggle and persistence
- **Phase 05:** Prop model for tracking physical objects in shots
- **Phase 06:** User authentication, roles, and permissions

### Accomplishments

#### Phase 04: Dark Mode
- CSS custom properties for theming with dark theme support
- Theme toggle button in header with 🌓 icon
- localStorage persistence for user preference
- System preference detection (`prefers-color-scheme`)
- FOUC prevention with inline script
- All templates updated to use CSS variables

#### Phase 05: Props Model
- Prop model with name and description fields
- ManyToMany relationship between Shot and Prop
- Prop admin interface with search functionality
- Props display in shot detail page
- Database migration applied successfully

#### Phase 06: User Authentication & Roles
- UserProfile model with role field (Admin, Power User, User)
- Login/logout views using Django's built-in authentication
- User menu in header showing auth state
- Admin interface for managing user profiles and roles
- Role helper methods: `has_role()` and `is_admin()`
- Security: POST method for logout with CSRF protection

### Requirements Delivered

- ✅ CORE-01: Application runs without errors
- ✅ CORE-02: All CRUD operations work
- ✅ CORE-03: CSV import functions correctly
- ✅ AUTH-01: User authentication (login/logout) functionality
- ✅ AUTH-02: User roles (Admin, Power User, User)
- ✅ AUTH-03: Permission checks based on roles
- ✅ AUTH-04: User menu in UI

### Archived Artifacts

- `.planning/ROADMAP.md` → `.planning/archive/v1.0/ROADMAP.md`
- `.planning/v1.0-MILESTONE-AUDIT.md` → `.planning/archive/v1.0/v1.0-MILESTONE-AUDIT.md`
- Phases 04-06 → `.planning/archive/v1.0/phases/`

### Git Tag

`v1.0`

---

## v1.1 - Storyboard Display ✅ Complete

**Status:** ✅ Complete  
**Date:** 2026-03-12  
**Progress:** 100%

### Overview

Visual storyboard viewing with grid layouts and image upload capability.

### Phases Included

- **Phase 07:** Storyboard Display - Grid views + image upload for Episode/Sequence storyboards

### Accomplishments

- Episode storyboard view showing sequences as visual cards
- Sequence storyboard view showing shots as visual cards  
- Optional image upload per shot
- Image display in storyboard grids
- Responsive grid layouts

### Requirements Delivered

- ✅ STORY-01: Storyboard grid display at Episode level
- ✅ STORY-02: Storyboard grid display at Sequence level
- ✅ STORY-03: Optional image upload per shot
- ✅ STORY-04: Image display in storyboard grids

---

## v1.2 - Enhanced Features (In Progress)

**Status:** 🔄 In Progress  
**Started:** 2026-03-12  
**Goal:** Add features to improve usability

### Overview

Building on the foundation of v1.0 and v1.1, this milestone adds search, filtering, export capabilities, and improves user onboarding.

### Phases Included

- **Phase 08:** Search functionality across all models (Series, Episodes, Sequences, Shots, Characters, Props)
- **Phase 09:** Filtering and sorting improvements (including character sorting by series)
- **Phase 10:** Export to JSON and CSV formats
- **Phase 11:** User onboarding and registration (default user, self-registration)

### Requirements

- FEAT-01: Search functionality across all models
- FEAT-02: Better filtering and sorting
- FEAT-03: Export to common formats (JSON, CSV)

---

*Last updated: 2026-03-12*
