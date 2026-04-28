---
name: pptx
description: >
  Creates, reads, edits, and manipulates PowerPoint presentation files (.pptx). Trigger when the
  user asks to create a presentation, edit slides, read slide content, combine decks, or build any
  .pptx file. Also triggers for "make a presentation", "build slides", "create a deck",
  "read this PowerPoint", or "update these slides".
keywords:
  - pptx
  - powerpoint
  - presentation
  - slides
  - deck
---

# PPTX Skill

You create and edit professional PowerPoint presentations with distinctive, visually engaging design. No boring slides — every deck should look intentional and crafted.

---

## Reading Existing Presentations

### Extract Text Content
```bash
python -m markitdown presentation.pptx
```
Returns all text content as Markdown, preserving slide structure.

### Generate Visual Thumbnails
Use `thumbnail.py` to render slides as images for visual inspection.

### Access Raw Structure
Unpack the .pptx (it's a ZIP file) to inspect XML directly:
```bash
unzip presentation.pptx -d presentation_unpacked/
```

---

## Creating Presentations (PptxgenJS)

Use **PptxgenJS** for creating presentations from scratch:

```javascript
const pptx = require("pptxgenjs");
let pres = new pptx();

// Slide dimensions (widescreen)
pres.layout = "LAYOUT_WIDE"; // 13.33" x 7.5"

let slide = pres.addSlide();

// Title text
slide.addText("Main Headline", {
  x: 0.5, y: 1.5, w: 12, h: 1.5,
  fontSize: 40, bold: true, color: "1d1d1f",
  fontFace: "Arial"
});

// Body text
slide.addText("Supporting point here", {
  x: 0.5, y: 3.2, w: 8, h: 3,
  fontSize: 18, color: "86868b",
  fontFace: "Arial"
});

await pres.writeFile({ fileName: "output.pptx" });
```

---

## Design Standards (No Boring Slides)

### Color Strategy
- Pick a **topic-specific palette**: 60–70% dominant color, 1–2 supporting tones, 1 accent
- The accent appears on CTAs, highlights, and key data only
- Avoid default Microsoft blue — pick a palette that matches the brand or purpose

### Every Slide Must Have a Visual Element
- Image, chart, icon, shape, or data visualization — **no text-only slides**
- Images bleed to the edge for high-impact slides; contained with rounded corners for data slides
- Charts should have clean, minimal styling (remove gridlines, simplify legends)

### Typography Rules
- Title slides: 36–44pt, bold, tight letter-spacing
- Body text: 14–16pt — never smaller (readability at distance)
- Font pairing: Use intentional combinations (e.g., Georgia + Calibri, not two sans-serifs)
- Max 5–6 lines of text per slide — if more is needed, split into two slides

### Layout Variety — Alternate Between:
- Full-bleed image with overlaid text
- Two-column split (text left, visual right)
- Grid layout for comparing options
- Data-focused: large number/stat prominently displayed

### Spacing Rules
- 0.5" minimum margins on all sides
- 0.3–0.5" gaps between text blocks
- Consistent alignment — use slide guides

### What to NEVER Do
- No text-only slides
- No centered body text (only titles center)
- No generic Microsoft blue (`#4472C4`)
- No decorative accent lines under titles
- No 10+ bullet point lists — convert to visuals
- No clip art

---

## QA Process (Mandatory)

1. **Content check**: Read every slide — no typos, no placeholder text, no missing content
2. **Visual inspection**: Generate thumbnails and review each slide image
3. **Fix and re-verify**: Fix all issues found, then re-inspect
4. **Never declare done** without completing at least one full correction cycle

---

## Editing Existing Presentations

1. Extract content with markitdown to understand current state
2. Identify what needs changing (text, layout, design, data)
3. Use template-based approach: preserve existing slide structure, modify only what's requested
4. Validate output with visual inspection before delivering
