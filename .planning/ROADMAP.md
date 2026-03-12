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

## Milestone: v1.1 - Storyboard Display ✅ Complete

**Date:** 2026-03-12  
**Status:** 100% Complete  
**Tag:** `v1.1`

### Phase Summary

| Phase | Name | Status |
|-------|------|--------|
| 07 | Storyboard Display | ✅ Complete |

---

## Milestone: v1.2 - Enhanced Features (In Progress)

**Started:** 2026-03-12  
**Goal:** Add features to improve usability

## Phases

- [x] **Phase 07: Storyboard Display** - Grid views + image upload for Episode/Sequence storyboards (completed 2026-03-12)

---

## Milestone v1.1 Complete Archive

See `.planning/milestones/v1.1-storyboard-display.md`

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
| STORY-01 | v1.1 | Phase 07 | ✅ Complete |
| STORY-02 | v1.1 | Phase 07 | ✅ Complete |
| STORY-03 | v1.1 | Phase 07 | ✅ Complete |
| STORY-04 | v1.1 | Phase 07 | ✅ Complete |
| FEAT-01 | v1.2 | Future | ⏳ Pending |
| FEAT-02 | v1.2 | Future | ⏳ Pending |
| FEAT-03 | v1.2 | Future | ⏳ Pending |
| POLI-01 | v1.3 | Future | ⏳ Pending |
| POLI-02 | v1.3 | Future | ⏳ Pending |
| POLI-03 | v1.3 | Future | ⏳ Pending |

### Phase 8: Search functionality across all models

**Goal:** Users can search across Series, Seasons, Episodes, Sequences, Shots, Characters, Props, and Wardrobe Items with relevant results displayed.
**Requirements**: FEAT-01
**Depends on:** Phase 7
**Plans:** 0 plans
**Success Criteria:**
1. Global search box visible in navigation/header
2. Search returns results from all major models (Series, Episodes, Sequences, Shots, Characters, Props)
3. Results are ranked by relevance
4. Each result links to the appropriate detail page

Plans:
- [ ] TBD (run /gsd:plan-phase 8 to break down)

### Phase 9: Filtering and sorting improvements

**Goal:** [To be planned]
**Requirements**: TBD
**Depends on:** Phase 8
**Plans:** 0 plans

Plans:
- [ ] TBD (run /gsd:plan-phase 9 to break down)

### Phase 10: Export to JSON and CSV formats

**Goal:** [To be planned]
**Requirements**: TBD
**Depends on:** Phase 9
**Plans:** 0 plans

Plans:
- [ ] TBD (run /gsd:plan-phase 10 to break down)

### Phase 11: User onboarding and registration

**Goal:** [To be planned]
**Requirements**: TBD
**Depends on:** Phase 10
**Plans:** 0 plans

Plans:
- [ ] TBD (run /gsd:plan-phase 11 to break down)

---

*Roadmap created: 2025-03-11*  
*Last updated: 2026-03-12 - Milestone v1.1 complete, v1.2 started*
