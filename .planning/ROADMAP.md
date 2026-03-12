# Roadmap: Memoon

**Project:** Memoon — Content Structure Manager  
**Created:** 2025-03-11  
**Last Updated:** 2026-03-12

---

## Milestone: v1.0 - Initial Release ✅ Complete

**Date:** 2026-03-12  
**Status:** 100% Complete  
**Tag:** `v1.0`

### Phase Summary

| Phase | Name | Status |
|-------|------|--------|
| 01-03 | Foundation | ✅ Complete |
| 04 | Dark Mode | ✅ Complete |
| 05 | Props Model | ✅ Complete |
| 06 | User Authentication | ✅ Complete |

---

## Milestone: v1.1 - Storyboard Display (In Progress)

**Started:** 2026-03-12  
**Goal:** Add visual storyboard display at Episode and Sequence levels with optional image upload per shot.

## Phases

- [x] **Phase 07: Storyboard Display** - Grid views + image upload for Episode/Sequence storyboards (completed 2026-03-12)

## Phase Details

### Phase 07: Storyboard Display

**Goal:** Users can view sequences and shots as visual cards in grid layouts at Episode and Sequence levels, with optional image upload and display.

**Depends on:** Phase 06 (User Authentication)

**Requirements:** STORY-01, STORY-02, STORY-03, STORY-04

**Success Criteria** (what must be TRUE):

1. User viewing an Episode sees sequences displayed as visual cards in a responsive grid layout
2. User viewing a Sequence sees shots displayed as visual cards in a responsive grid layout
3. User can optionally upload an image file to any shot via the shot detail or edit interface
4. When a shot has an uploaded image, that image displays within the shot card in both Episode and Sequence view grids

**Plans:** 1/1 plans complete

- [ ] 07-01-PLAN.md — Add image field to Shot model + create storyboard grid views/templates

---

## Milestone: v1.2 - Enhanced Features

**Goal:** Add features to improve usability

**Requirements:**

- [ ] FEAT-01: Search functionality across all models
- [ ] FEAT-02: Better filtering and sorting
- [ ] FEAT-03: Export to common formats (JSON, CSV)

**Success Criteria:**

1. Search returns relevant results
2. Filters work on list views
3. Export produces valid files

---

## Milestone: v1.3 - Polish & Documentation

**Goal:** Improve user experience and add documentation

**Requirements:**

- [ ] POLI-01: Fix any bugs discovered
- [ ] POLI-02: Improve UI/UX
- [ ] POLI-03: Add user documentation

**Success Criteria:**

1. No critical bugs
2. UI is intuitive
3. README is complete

---

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 07 - Storyboard Display | 1/1 | Complete    | 2026-03-12 |

---

## Traceability

| Requirement | Milestone | Phase | Status |
|-------------|-----------|-------|--------|
| CORE-01 | v1.0 | Foundation | ✅ Complete |
| CORE-02 | v1.0 | Foundation | ✅ Complete |
| CORE-03 | v1.0 | Foundation | ✅ Complete |
| AUTH-01 | v1.0 | Phase 06 | ✅ Complete |
| AUTH-02 | v1.0 | Phase 06 | ✅ Complete |
| AUTH-03 | v1.0 | Phase 06 | ✅ Complete |
| AUTH-04 | v1.0 | Phase 06 | ✅ Complete |
| STORY-01 | v1.1 | Phase 07 | ⏳ Pending |
| STORY-02 | v1.1 | Phase 07 | ⏳ Pending |
| STORY-03 | v1.1 | Phase 07 | ⏳ Pending |
| STORY-04 | v1.1 | Phase 07 | ⏳ Pending |
| FEAT-01 | v1.2 | Future | ⏳ Pending |
| FEAT-02 | v1.2 | Future | ⏳ Pending |
| FEAT-03 | v1.2 | Future | ⏳ Pending |
| POLI-01 | v1.3 | Future | ⏳ Pending |
| POLI-02 | v1.3 | Future | ⏳ Pending |
| POLI-03 | v1.3 | Future | ⏳ Pending |

---

*Roadmap created: 2025-03-11*  
*Last updated: 2026-03-12 - Milestone v1.1 started*
