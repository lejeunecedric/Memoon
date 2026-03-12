---
created: 2025-03-12T00:00:00.000Z
title: Add sample data prompt to Memoon setup
area: tooling
files:
  - manage.py
  - series/management/commands/populate_70s_series.py
---

## Problem

When setting up Memoon for the first time (fresh database), users should be prompted to add sample data to explore the app's features.

## Solution

Create a Django management command that populates the database with 5 classic 1970s TV series with full production details:
1. Series, Seasons, Episodes, Sequences, Shots
2. Characters with wardrobe items
3. Camera angles, movements, backgrounds, props

Suggested series (1970s detective/kids shows):
- Charlie's Angels
- The Rockford Files
- Starsky & Hutch
- Kojak
- The Adventures of Superman (reruns were popular)
