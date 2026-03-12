---
created: 2026-03-12T08:46:06.675Z
title: Move dark mode toggle to settings menu
area: ui
files:
  - templates/base.html
---

## Problem

The dark mode toggle (🌓) currently appears directly in the header's user menu area, taking up space next to the username and login/logout buttons. This clutters the header and makes the interface feel busier than necessary. The theme setting should be in a more appropriate location like a settings/preferences menu.

## Solution

Move the dark mode toggle from the header to a proper settings menu:

1. Remove the 🌓 toggle button from the header's user-menu area in base.html
2. Create a settings page or integrate into the Django admin user preferences
3. Add theme selection to the settings as a dropdown or toggle (Light / Dark / System)
4. Keep the theme preference stored in localStorage as currently implemented
5. Consider adding a quick-access theme toggle in a user dropdown menu rather than directly in header

Alternative approaches:
- Move toggle into a user dropdown menu (collapsed by default)
- Create a dedicated settings page at /settings/ with theme as one option
- Integrate with Django admin's user profile editing

The current inline script for FOUC prevention can remain — it reads from localStorage which will still work.
