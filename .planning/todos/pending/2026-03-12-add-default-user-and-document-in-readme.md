---
created: 2026-03-12T07:07:14.822Z
title: Add default user and document in README
area: auth
files:
  - README.md
---

## Problem

New users installing Memoon for the first time need to know how to log in. Currently there's no default user created during setup, and the README doesn't document login credentials. This creates friction for first-time users who want to try the application.

## Solution

1. Create a default user during initial setup/migrations:
   - Username: "user"
   - Password: "password"
   - Role: Power User (or appropriate default)
   
2. Update README.md to document:
   - Default login credentials
   - How to access the login page
   - How to create additional users via Django admin
   
3. Consider creating a management command or data migration that creates this default user if it doesn't exist.

Implementation options:
- Add to existing data migration
- Create new management command: `python manage.py create_default_user`
- Add to setup instructions in README
