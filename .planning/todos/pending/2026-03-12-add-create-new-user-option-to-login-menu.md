---
created: 2026-03-12T07:09:32.876Z
title: Add create new user option to login menu
area: auth
files: []
---

## Problem

Currently, new users cannot self-register for the application. An administrator must create user accounts through the Django admin interface. This creates a bottleneck for onboarding new team members who need access to Memoon.

## Solution

Add a "Create new user" or "Sign up" link to the login menu/page that allows visitors to register themselves.

Requirements:
- Add "Create account" or "Sign up" link on the login page
- New users created through this flow should have **read-only access** by default (lowest privilege level)
- Registration form should collect:
  - Username
  - Password (with confirmation)
  - Email (optional but recommended)
- After registration, user is redirected to login page or automatically logged in
- Consider requiring admin approval for new accounts (optional enhancement)

Implementation notes:
- Use Django's built-in UserCreationForm as base
- Set default role to 'user' (read-only) in UserProfile
- May need email verification to prevent spam accounts
- Update login template to include the new link
