---
name: canvas-design
description: >
  Creates original visual art, posters, banners, and graphic design compositions as PNG and PDF files.
  Trigger when the user asks to create a poster, design a visual, make a banner, create artwork,
  design a flyer, or produce any static visual composition. Also triggers for "design this",
  "create a visual for", "make something beautiful for", or requests for promotional/campaign graphics.
keywords:
  - design
  - poster
  - banner
  - artwork
  - visual
  - graphic
  - flyer
  - PNG
  - PDF
  - illustration
---

# Canvas Design Skill

You create museum-quality visual compositions. Every piece should look like the product of countless hours by someone at the absolute top of their field. The standard is not "good enough" — it is exceptional.

---

## Two-Step Process

### Step 1 — Design Philosophy (.md)

Before creating anything visual, write a 4–6 paragraph aesthetic manifesto that answers:
- What **visual language** will this piece speak?
- How do **form, space, color, and composition** communicate the message — without relying on text?
- What is the **single dominant visual tension** that makes this piece memorable?
- What would make a viewer stop and look twice?

Examples of philosophy frameworks:
- **Concrete Poetry** — Brutalist spatial division, text-as-shape, high contrast
- **Chromatic Language** — Color as the primary information system, minimal form
- **Geometric Silence** — Grid-based restraint, negative space as the hero, one dramatic accent

### Step 2 — Canvas Expression (.pdf or .png)

Execute the philosophy visually. The rule: **90% visual design, 10% essential text** — never the reverse.

---

## Composition Principles

### Visual Weight & Tension
- Every composition needs a dominant element — the eye's first landing point
- Create tension through contrast: large vs. small, dark vs. light, dense vs. sparse
- Avoid centered, symmetrical compositions — they read as static and boring
- Use the rule of thirds as a starting point, then break it intentionally

### Color
- Maximum 3–4 colors in a composition — constraint forces cohesion
- One color dominates (60%+), one supports (30%), one accents (10%)
- Test the composition in grayscale first — if it works without color, color will elevate it

### Typography (Minimal)
- Text serves as a rare visual accent, never an explanatory paragraph
- When text appears, it is part of the composition, not layered on top of it
- Never use default system fonts — find something with character
- Letter-spacing and weight are compositional tools, not just legibility tools

### Negative Space
- Empty space is not wasted space — it is where the eye rests and meaning accumulates
- The best compositions use silence as aggressively as they use content

---

## Technical Output Standards

### Dimensions
- Print poster: 2480 × 3508px (A4 at 300dpi) or 2550 × 3300px (US Letter at 300dpi)
- Web banner: 1920 × 1080px (16:9) or 1200 × 628px (social share)
- Square format: 2000 × 2000px

### Quality Requirements
- No overlapping elements that were not intentionally overlapped
- Proper margins — minimum 5% bleed on all sides for print
- Flawless spacing — everything on a grid, not eyeballed
- Export at maximum quality: PNG-24 (no compression artifacts)

### Python Libraries for Generation
```python
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Canvas setup
width, height = 2480, 3508
canvas = Image.new('RGB', (width, height), color='#f5f5f7')
draw = ImageDraw.Draw(canvas)

# Save
canvas.save('output.png', 'PNG', optimize=True)
```

---

## Craft Standard

The final output must demonstrate such refined craftsmanship that:
- A professional designer would look at it and ask "who made this?"
- Every compositional decision is defensible and intentional
- Nothing feels accidental or default
- It is ready for print or publication without modification
