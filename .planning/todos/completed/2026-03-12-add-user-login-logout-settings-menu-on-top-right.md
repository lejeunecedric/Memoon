---
created: 2026-03-12T00:01:52.460Z
title: Add user login/logout/settings menu on top right
area: ui
files:
  - templates/base.html
---

## Problem

The application currently lacks user authentication UI. There's no visible indication of whether a user is logged in, no way to access account settings, and no logout option. This makes it unclear which user context the app is running under and prevents users from managing their session.

## Solution

Add a user menu dropdown in the top-right corner of the navigation bar (in base.html) that includes:
- Display current username when logged in
- Settings link (for user preferences/profile)
- Logout button
- Login link when not authenticated

Follow the existing dark mode toggle styling and placement pattern. Use Django's auth context processor to check `{% if user.is_authenticated %}`.
