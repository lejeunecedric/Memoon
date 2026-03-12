# Phase 4: Add dark mode - Research

**Researched:** 2025-03-12
**Domain:** CSS theming, browser theme persistence
**Confidence:** HIGH

## Summary

Dark mode implementation for Django templates requires converting hardcoded colors to CSS custom properties (variables), then overlaying a dark theme via a `[data-theme="dark"]` selector. The critical success factor is preventing the "Flash of Unstyled Content" (FOUC) by placing an inline JavaScript snippet in the `<head>` that reads localStorage before the page renders.

**Primary recommendation:** Convert base.html colors to CSS variables, add inline script for FOUC prevention, add theme toggle button, persist to localStorage.

---

## Standard Stack

### Core Approach
| Component | Technology | Purpose |
|-----------|------------|---------|
| Theming | CSS Custom Properties (variables) | Define colors once, override for dark mode |
| Toggle mechanism | `data-theme` attribute on `<html>` | Controls which theme applies |
| Persistence | localStorage | Stores user preference between visits |
| FOUC prevention | Inline `<script>` in `<head>` | Sets theme before first paint |

### Implementation Pattern

The modern approach (2025-2026) uses CSS variables exclusively:

```css
:root {
  --bg-color: #f5f5f5;
  --text-color: #333;
  --header-bg: #2c3e50;
  /* ... all colors as variables */
}

[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #e0e0e0;
  --header-bg: #1a1a2e;
  /* ... dark theme overrides */
}
```

Source: [CSS Tips - Correct Way to Toggle Dark Mode](https://redstapler.co/css-tips-correct-way-to-toggle-dark-mode/), [DEV Community - Modern Dark Mode](https://dev.to/vinay_5d249e669fb47d24e2c/stop-inverting-your-colors-the-modern-way-to-implement-dark-light-mode-4p2d)

---

## Architecture Patterns

### Pattern 1: CSS Variables with data-theme Attribute

**What:** Define all colors as CSS custom properties in `:root`, override them under `[data-theme="dark"]`

**When to use:** Any web application without a CSS framework, or when you want full control

**Structure:**
```html
<!-- base.html -->
<head>
  <!-- Inline script to prevent FOUC -->
  <script>
    (function() {
      try {
        const stored = localStorage.getItem('theme');
        const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const theme = stored ? stored : (systemDark ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', theme);
      } catch (e) {}
    })();
  </script>
  <style>
    :root {
      --bg-color: #f5f5f5;
      --text-color: #333;
      --card-bg: #ffffff;
      --header-bg: #2c3e50;
      --nav-bg: #34495e;
      --border-color: #ddd;
      --link-color: #2980b9;
      --btn-bg: #2980b9;
      --btn-hover: #3498db;
    }
    [data-theme="dark"] {
      --bg-color: #121212;
      --text-color: #e0e0e0;
      --card-bg: #1e1e1e;
      --header-bg: #1a1a2e;
      --nav-bg: #16213e;
      --border-color: #333;
      --link-color: #64b5f6;
      --btn-bg: #1976d2;
      --btn-hover: #2196f3;
    }
    body {
      background-color: var(--bg-color);
      color: var(--text-color);
    }
    .card {
      background: var(--card-bg);
    }
  </style>
</head>
<body>
  <button id="theme-toggle">Toggle Theme</button>
  <script>
    document.getElementById('theme-toggle').addEventListener('click', function() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
  </script>
</body>
```

Source: [Savvy - Add Dark Mode Toggle](https://savvy.co.il/en/blog/wordpress-development/adding-dark-theme-to-your-site/)

### Pattern 2: System Preference Detection

**What:** Respect user's OS/browser dark mode setting as default, with manual override

**When to use:** Default behavior should match system preference

**Priority chain:**
1. Check localStorage for saved preference
2. If none, check `prefers-color-scheme` media query
3. Fall back to light theme

```javascript
const stored = localStorage.getItem('theme');
const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const theme = stored ? stored : (systemDark ? 'dark' : 'light');
```

Source: [WhiteP4nth3r - Best Theme Toggle](https://whitep4nth3r.com/blog/best-light-dark-mode-theme-toggle-javascript/)

### Anti-Patterns to Avoid

- **filter: invert(100%):** Never use CSS filters to "invert" colors for dark mode. This produces unreadable results and ignores semantic color meaning.
  - Source: [DEV Community - Stop Inverting](https://dev.to/vinay_5d249e669fb47d24e2c/stop-inverting-your-colors-the-modern-way-to-implement-dark-light-mode-4p2d)

- **Loading theme JS asynchronously:** JavaScript that runs after page load causes FOUC (flash of wrong theme on every page load).
  - Source: [Nishul Dev - Dark Mode Flicker Fix](https://nishuldev.substack.com/p/how-to-fix-dark-mode-flicker-in-nextjs)

- **Using cookies instead of localStorage:** Cookies are sent with every HTTP request, unnecessary overhead for theme preference. localStorage is client-side only.
  - Source: [Savvy - Dark Mode Toggle](https://savvy.co.il/en/blog/wordpress-development/adding-dark-theme-to-your-site/)

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Theme persistence | Custom cookie/session solution | localStorage | Simpler API, no server round-trip, sufficient for this use case |
| FOUC prevention | External JS file loaded after CSS | Inline `<script>` in `<head>` | Must execute before first paint to prevent flash |
| Color management | Hardcoded colors scattered throughout CSS | CSS custom properties | Single source of truth, easy to theme |

**Key insight:** The only JS needed is ~10 lines for localStorage read/write. Everything else is CSS. Do not add libraries like Alpine.js, Vue, or React just for theme toggling.

---

## Common Pitfalls

### Pitfall 1: Flash of Unstyled Content (FOUC)

**What goes wrong:** User sees light theme for 100-200ms before dark mode applies on every page load

**Why it happens:** External JavaScript loads after the browser begins rendering. The page paints with default (light) styles, then JS executes and switches to dark.

**How to avoid:** Place inline `<script>` in `<head>` that runs synchronously BEFORE any content renders

**Warning signs:** Brief white flash when refreshing dark mode pages

**Source:** [Medium - FOUC Prevention](https://medium.com/@mohantaankit2002/building-a-dynamic-theme-switcher-in-tailwind-css-without-flash-of-unstyled-content-fouc-da8b92e0fec2)

### Pitfall 2: Hardcoded Colors Not Using Variables

**What goes wrong:** Some elements don't switch to dark mode, remain light colored

**Why it happens:** Converting some colors to variables but leaving others as hex codes. Browser uses hex directly, ignoring theme.

**How to avoid:** Audit ALL color values in base.html, convert every hardcoded color to a CSS variable

**Warning signs:** Headers are dark, but cards or buttons remain light in dark mode

### Pitfall 3: No System Preference Detection

**What goes wrong:** Dark mode users must manually enable dark mode every visit

**Why it happens:** Not checking `prefers-color-scheme` media query, always defaulting to light

**How to avoid:** Use the priority chain (localStorage > system > default)

### Pitfall 4: localStorage Access Errors

**What goes wrong:** Theme breaks in private/incognito mode or when cookies are blocked

**Why it happens:** localStorage can throw security errors in certain browser configurations

**How to avoid:** Wrap localStorage access in try-catch:
```javascript
try {
  localStorage.setItem('theme', 'dark');
} catch (e) {}
```

Source: [WhiteP4nth3r - Theme Toggle Code](https://whitep4nth3r.com/blog/best-light-dark-mode-theme-toggle-javascript/)

---

## Code Examples

### Converting Existing Inline CSS to Variables

Original (base.html):
```css
body {
  color: #333;
  background-color: #f5f5f5;
}
header {
  background-color: #2c3e50;
}
.card {
  background: white;
}
```

Converted to CSS variables:
```css
:root {
  --bg-color: #f5f5f5;
  --text-color: #333;
  --card-bg: #ffffff;
  --header-bg: #2c3e50;
}
[data-theme="dark"] {
  --bg-color: #121212;
  --text-color: #e0e0e0;
  --card-bg: #1e1e1e;
  --header-bg: #1a1a2e;
}
body {
  color: var(--text-color);
  background-color: var(--bg-color);
}
header {
  background-color: var(--header-bg);
}
.card {
  background: var(--card-bg);
}
```

### Complete Theme Toggle Implementation

```html
<!-- In <head>, before any other content -->
<script>
  (function() {
    try {
      const stored = localStorage.getItem('theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = stored || (prefersDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    } catch (e) {
      // localStorage unavailable, use light theme
    }
  })();
</script>

<!-- Toggle button, anywhere in body -->
<button id="theme-toggle" aria-label="Toggle dark mode">
  <span id="theme-icon">🌙</span>
</button>

<script>
  const toggle = document.getElementById('theme-toggle');
  const icon = document.getElementById('theme-icon');
  
  // Update icon based on current theme
  const updateIcon = () => {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    icon.textContent = isDark ? '☀️' : '🌙';
  };
  updateIcon();
  
  toggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try {
      localStorage.setItem('theme', next);
    } catch (e) {}
    updateIcon();
  });
</script>
```

Source: [Learn End Geek - Dark Mode Tailwind](https://www.learnedgeek.com/Blog/Post/dark-mode-toggle-tailwind-localstorage)

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Separate CSS files for each theme | CSS custom properties with overrides | ~2019+ | Single stylesheet, instant switching |
| Class-based toggle (`.dark`) | `data-theme` attribute | ~2022+ | More explicit, works with CSS `light-dark()` |
| Cookies for persistence | localStorage | ~2015+ | No server overhead |
| JS toggles external CSS | Inline script prevents FOUC | Ongoing issue | Critical for user experience |
| Manual dark mode only | System preference detection | ~2019+ | Better default UX |

**Modern (2025-2026) best practice:**
- Use `color-scheme: light dark` CSS property
- Use `light-dark()` function where supported (fallback for older browsers)
- Combine with `prefers-color-scheme` for system preference

```css
:root {
  color-scheme: light dark;
  --bg-color: light-dark(#f5f5f5, #121212);
  --text-color: light-dark(#333, #e0e0e0);
}
```

Source: [DEV Community - Modern Dark Mode](https://dev.to/renekaesler/a-modern-approach-of-implementing-dark-mode-20f8)

**Note:** Browser support for `light-dark()` is good but not universal. Stick with `data-theme` attribute approach for maximum compatibility.

---

## Open Questions

1. **Should theme preference persist server-side?**
   - What we know: localStorage is sufficient for client-only theme preference
   - What's unclear: If user logs in later, should preference sync to server?
   - Recommendation: Start with localStorage only; add server sync if/when user authentication is implemented

2. **Should there be an "auto" option alongside light/dark?**
   - What we know: Auto respects system preference, light/dark are manual overrides
   - What's unclear: Whether UI complexity is worth the feature
   - Recommendation: Start with simple light/dark toggle; add auto later if requested

3. **Should theme toggle be in header or navigation?**
   - What we know: Needs to be visible on all pages
   - What's unclear: Best placement in current layout
   - Recommendation: Add to header near the nav, visible on all pages

---

## Sources

### Primary (HIGH confidence)
- [Red Stapler - CSS Tips Dark Mode](https://redstapler.co/css-tips-correct-way-to-toggle-dark-mode/) - Current best practices
- [Savvy - Dark Mode Toggle](https://savvy.co.il/en/blog/wordpress-development/adding-dark-theme-to-your-site/) - Comprehensive guide
- [WhiteP4nth3r - Best Theme Toggle](https://whitep4nth3r.com/blog/best-light-dark-mode-theme-toggle-javascript/) - Priority chain implementation

### Secondary (MEDIUM confidence)
- [DEV Community - Modern Dark Mode](https://dev.to/renekaesler/a-modern-approach-of-implementing-dark-mode-20f8) - `light-dark()` function
- [Nishul Dev - Dark Mode Flicker](https://nishuldev.substack.com/p/how-to-fix-dark-mode-flicker-in-nextjs) - FOUC explanation and fix

### Tertiary (LOW confidence)
- [Stack Overflow - Django Theme Toggle](https://stackoverflow.com/questions/69060631/how-to-allow-user-to-toggle-between-color-themes-in-a-django) - Community solutions

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - CSS variables with data-theme is the established standard
- Architecture: HIGH - Inline script for FOUC prevention is well-documented
- Pitfalls: HIGH - FOUC and hardcoded colors are well-known issues with clear solutions

**Research date:** 2025-03-12
**Valid until:** 2025-09-12 (6 months - CSS variables approach is stable)
