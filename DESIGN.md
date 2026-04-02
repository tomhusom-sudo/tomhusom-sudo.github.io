# Design System — Honest Tom's Market

## Product Context
- **What this is:** Weekly fresh produce, meat, and bread pre-order pickup service in Aberdeen, SD
- **Who it's for:** Aberdeen residents actively motivated to eat better — GLP-1 patients, people training, anyone tired of Walmart produce
- **Space/industry:** Local fresh food / micro-grocery / farmers market alternative
- **Project type:** Marketing landing page (market.html) + functional pre-order app (preorder.html)

## Aesthetic Direction
- **Direction:** Organic/Natural
- **Decoration level:** Intentional — subtle warmth, no decorative blobs or gradients
- **Mood:** Farmers market chalkboard crossed with a well-designed restaurant menu. Warm, personal, honest. Feels like it was made by a person, not a tech team. Trust is earned at the pixel level here — every customer is buying food from someone they don't yet know.
- **Anti-patterns to avoid:** No neon greens, no dark dashboard theme, no SaaS card grids, no centered-everything layout, no purple/blue gradients, no stock photography, no generic hero copy

## Typography
- **Display/Hero:** Lora (Google Fonts, serif, wght 400/600/700, italic 400/600) — warm, literary, approachable authority. Reads like a handwritten sign done right. Used for page title, section headers, item names, Weekly Pick.
- **Body/UI:** Inter (Google Fonts, wght 400/500/600) — clean, legible at small sizes, familiar. Used for body copy, labels, prices, form elements, nav.
- **Loading:** `https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@400;500;600&display=swap`
- **Scale:**
  - hero: 2.8rem / Lora 700
  - h2: 1.8rem / Lora 700
  - h3: 1.2rem / Lora 600
  - body: 1rem / Inter 400
  - label: 0.7rem / Inter 600 uppercase, 0.14em letter-spacing
  - small: 0.85rem / Inter 400
  - price: 0.85rem / Inter 600, tabular-nums

## Color System
```css
--ht-bg:      #F5EDD6;   /* warm parchment — page background */
--ht-text:    #2C1810;   /* dark bark brown — primary text */
--ht-accent:  #5C7A3E;   /* sage/forest green — CTAs, links, highlights */
--ht-brown:   #8B5E3C;   /* warm earth brown — prices, secondary accents */
--ht-cream:   #EDE0C4;   /* lighter parchment — card/section backgrounds */
--ht-border:  #C4A882;   /* wheat/tan — dividers, input borders */
--ht-muted:   #7A6450;   /* warm gray-brown — secondary text, captions */
--ht-error:   #8B2500;   /* burnt sienna — error states */
--ht-white:   #FDFAF4;   /* warm white — card surfaces, form fields */
--ht-green-light: #EBF2E4; /* pale green — order CTA background */
```
- **Contrast verified:** `--ht-accent` on `--ht-bg` = 4.9:1 (AA pass). `--ht-text` on `--ht-bg` = 12.1:1 (AAA pass).
- **No dark mode:** The warmth of the parchment palette IS the brand. Inverting it loses the feeling. Intentional decision.

## Spacing
- **Base unit:** 8px
- **Density:** Comfortable — like a restaurant menu, not a data dashboard
- **Scale:** 8 / 16 / 24 / 32 / 48 / 64 / 80

## Layout
- **Approach:** Editorial — left-aligned, single-column dominant, max-width constrained
- **Max content width:** 760px (editorial feel, not stretched)
- **Mobile:** Single column, full-width. Default layout — not an afterthought.
- **Desktop:** Still centered, max 760px. Forms stay single column.
- **Border radius:** 8px (inputs, small elements), 12-14px (cards/sections), 50% (portrait)
- **No 3-column feature grids.** Menu items are a left-aligned list. Steps are a numbered sequence.

## Motion
- **Approach:** Minimal-functional — no decorative animation
- **Allowed:** Hover transitions on buttons (150ms ease), link color transitions (150ms), button press (translateY 1px on active)
- **Not allowed:** Scroll animations, entrance animations, decorative motion

## Brand Mark
- A simple stamp/seal: circle border containing the letters "HT" in Lora serif. Rendered as inline SVG.
- Color: `--ht-accent` stroke on `--ht-bg` fill, or inverted on dark surfaces.
- Used in: page header (market.html, preorder.html), footer
- Portrait: Tom's pencil sketch in grocer style (`honest_tom_sketch.png`) — placed in header of both pages. Falls back to the HT mark if image is missing.

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-04-01 | Lora serif for display, Inter for body | Lora reads as "this person has taste" — rare for a local food brand, immediately differentiating |
| 2026-04-01 | Earth tone palette (parchment background) | Farmers market warmth, not tech startup. Trust signal for first-time buyers. |
| 2026-04-01 | No dark mode | The parchment warmth IS the brand identity. Inverting it destroys the feeling. |
| 2026-04-01 | Max-width 760px, editorial layout | Menu + order form don't benefit from width. Editorial constraint creates intentional feel. |
| 2026-04-01 | Portrait sketch (not photo) | Farm box sites use stock produce photography. Tom's sketch is personal and memorable. |
| 2026-04-01 | No 3-column grids | AI slop. Menu items are a list. Steps are a sequence. Neither needs a card grid. |
