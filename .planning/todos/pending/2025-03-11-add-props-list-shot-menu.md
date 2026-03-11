---
created: 2025-03-11T23:50:00.000Z
title: Add props list in shot menu
area: ui
files:
  - templates/series/shot_detail.html
  - series/models.py
---

## Problem

Shots need to track props (physical objects/items used in the scene) similar to how characters and wardrobe are tracked. Currently there's no way to associate props with shots.

## Solution

Add a Prop model linked to shots, similar to Character/Wardrobe pattern. Display props in shot detail page.
