---
name: awesome-design-md
description: Curated collection of 84+ production DESIGN.md design system specifications from top tech companies and websites (Linear, Stripe, Apple, Vercel, Supabase, Raycast, Resend, Figma, x.ai, etc.). Use when styling, redesigning, or building web UIs that need to follow real-world design languages, design tokens, color palettes, typography, spacing, and component patterns.
---

# Awesome DESIGN.md - Design Systems Library

A curated library of 84+ production-grade `DESIGN.md` documents extracted from developer-focused and world-class consumer websites.

## What is DESIGN.md?

`DESIGN.md` is a plain-text design system document that AI coding agents read to generate consistent, high-fidelity user interfaces.

| File | Who reads it | What it defines |
| :--- | :--- | :--- |
| `AGENTS.md` / `CLAUDE.md` | Coding agents | How to build the project, conventions, git flows |
| `DESIGN.md` | Design & Frontend agents | How the project should look and feel (tokens, colors, typography, layout) |

## Available Brands & Design Systems (84 Categories)

All specifications are stored in `./design-md/<brand>/DESIGN.md`.

### Developer Tools & High-Density UI
- **Linear:** `design-md/linear.app/DESIGN.md` (Subtle borders, high density, dark mode, keyboard-first, minimalist)
- **Vercel:** `design-md/vercel/DESIGN.md` (Geist typography, high contrast monochrome, razor-sharp borders)
- **Supabase:** `design-md/supabase/DESIGN.md` (Emerald green accents, dark slate backgrounds, database tooling)
- **Stripe:** `design-md/stripe/DESIGN.md` (Legendary gradients, refined typography, trust aesthetics)
- **Raycast:** `design-md/raycast/DESIGN.md` (Floating command-palette, vibrant neon accents, macOS polish)
- **Resend:** `design-md/resend/DESIGN.md` (Pure minimalism, clean black/white, elegant spacing)
- **Sentry:** `design-md/sentry/DESIGN.md` (Developer observability, diagnostics, error badges)
- **PostHog:** `design-md/posthog/DESIGN.md` (Playful dev-first, retro-modern, visual analytics)
- **Figma:** `design-md/figma/DESIGN.md` (Canvas aesthetics, collaborative UI, color versatility)
- **Cursor:** `design-md/cursor/DESIGN.md` (AI editor dark mode, code blocks, diff markers)
- **Warp:** `design-md/warp/DESIGN.md` (Modern rust terminal, command blocks, block glow)

### Consumer, Fintech & Media
- **Apple:** `design-md/apple/DESIGN.md` (San Francisco font, generous margins, frosted glass, retina fidelity)
- **Wise:** `design-md/wise/DESIGN.md` (Bold forest green, friendly financial typography, global clarity)
- **Revolut:** `design-md/revolut/DESIGN.md` (Modern fintech, neo-banking cards, vibrant graphs)
- **Airbnb:** `design-md/airbnb/DESIGN.md` (Cereal typography, warm neutrals, photo-centric grids)
- **x.ai:** `design-md/x.ai/DESIGN.md` (Deep black, technical minimalism, monospace accents)
- **Claude (Anthropic):** `design-md/claude/DESIGN.md` (Warm terracotta/coral accents, conversational typography, intellectual warmth)

## How to Apply a Design Language to a Project

1. **Inspect the Target Design System:**
   Read the corresponding file, e.g.:
   `cat design-md/linear.app/DESIGN.md`

2. **Adopt the Design Tokens:**
   Extract and copy the design tokens into the project's root `DESIGN.md` or directly into CSS / Tailwind variables:
   - Primary and background colors
   - Border radius and border colors (e.g. `rgba(255,255,255,0.08)`)
   - Font family and scale
   - Elevation and shadow styles
   - Component guidelines (buttons, cards, badges, inputs)

3. **Verify Compliance:**
   Ensure generated components do not mix conflicting design languages (e.g. don't mix Stripe colorful gradients with Linear dark high-density minimalism).
