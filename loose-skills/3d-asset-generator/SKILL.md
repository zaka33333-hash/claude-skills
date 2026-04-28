---
name: 3d-asset-generator
description: >
  Generates optimized prompts for 3D asset creation across text-to-3D, image-to-3D, and texture
  generation workflows. Creates three coordinated prompts: (1) a text-to-3D generation prompt for
  tools like Meshy, Tripo3D, or Shap-E, (2) a texture/material prompt for PBR surface generation,
  and (3) an image reference prompt to use as visual input for image-to-3D pipelines. Delivers
  prompts via an HTML page with a left-panel generator layout and one-click copy buttons with confetti.
  Trigger when the user says "3d asset", "generate 3d", "3d model prompt", "meshy prompt",
  "text to 3d", "image to 3d", "3d object", or asks for prompts to create game-ready 3D assets.
---

# 3D Asset Generator Skill

You generate a coordinated set of 3 prompts that work together to produce a high-quality 3D asset:
a text-to-3D generation prompt, a PBR texture/material prompt, and an image reference prompt for
image-to-3D pipelines.

After generating the prompts, you deliver them in an HTML page with the generator panel on the left,
tool recommendations on the right, and one-click copy buttons with confetti.

---

## The Process

### Step 1: Confirm the Asset

Ask the user what 3D object they want (if not already specified). Good 3D asset subjects include:
- Props & items: weapons, furniture, vehicles, tools, containers
- Characters & creatures: humanoids, animals, fantasy creatures, robots
- Architecture: buildings, ruins, sci-fi structures, organic environments
- Natural objects: rocks, trees, crystals, terrain features
- Hard surface: mechanical parts, tech gadgets, industrial equipment

Default to **a sci-fi combat knife** if the user doesn't specify.

Also ask (or infer from context):
- **Style**: realistic, stylized, low-poly, cartoon, sci-fi, fantasy, medieval, etc.
- **Use case**: game asset, film VFX, 3D printing, AR/VR, product visualization
- **Polygon budget**: low-poly (game-ready), mid-poly (cinematic), high-poly (sculpt)

---

### Step 2: Generate Prompt A — Text-to-3D Generation

This is the primary generation prompt for text-to-3D tools (Meshy AI, Tripo3D, Shap-E, Point·E,
CSM, Hyper3D, etc.).

**Template:**

```
PROMPT A — TEXT-TO-3D GENERATION

[OBJECT NAME], [STYLE] style. [KEY VISUAL CHARACTERISTICS in 2-3 sentences describing
shape, silhouette, proportions, and dominant materials.]

Surface details: [MATERIAL 1 — e.g., brushed steel blade with subtle scratches and edge wear],
[MATERIAL 2 — e.g., wrapped leather handle with visible stitching], [MATERIAL 3 if applicable].

[STRUCTURAL DETAILS: notable features, functional parts, decorative elements, damage/weathering
if any.]

Optimized for [USE CASE]. [POLY BUDGET] geometry. Clean topology, UV-ready, game-ready mesh.
No floating geometry. Solid, watertight base mesh. [SCALE REFERENCE if helpful, e.g., "approximately
30cm blade length"].

Isolated object, no background, no ground plane, no scene lighting rigs. Center of mass at origin.
```

**Customize for the specific object:**
- Lead with the most distinctive visual trait (not just the object name)
- Describe materials in order of visual dominance
- Mention unique silhouette features that define the object
- For characters/creatures: add "T-pose or A-pose" and anatomy notes
- For architecture: add "exterior view, modular sections clearly defined"
- Avoid vague adjectives ("cool", "awesome") — use specific physical descriptions

---

### Step 3: Generate Prompt B — Texture & Material (PBR)

This prompt guides texture generation (Meshy texture mode, Substance 3D, Stable Diffusion ControlNet,
TextureLab, DreamMat, etc.) and should work for both AI texture gen and manual painting guidance.

**Template:**

```
PROMPT B — PBR TEXTURE / MATERIAL GENERATION

Texture set for [OBJECT NAME], [STYLE] art direction.

BASE COLOR (Albedo):
[PRIMARY SURFACE: exact color description, e.g., "dark gunmetal grey #2C2C2C, slight blue
undertone, factory-painted finish with micro-scratches revealing silver metal beneath"]
[SECONDARY SURFACE: e.g., "black wrapped handle, nylon or paracord weave pattern, matte finish"]
[ACCENT ELEMENTS: e.g., "exposed cutting edge — bright silver #C0C0C0, mirror-polished along
the bevel, oxidized dark at the spine"]

ROUGHNESS MAP:
[ZONES: describe which areas are rough vs smooth, e.g., "blade flat: very smooth (roughness 0.1),
handle wrap: rough/fabric texture (roughness 0.85), edge bevel: mirror-polished (roughness 0.02)"]

METALLIC MAP:
[Which parts are metallic vs. non-metallic, metalness values 0-1 per zone]

NORMAL MAP:
[Surface detail descriptions: scratches, dents, engravings, tool marks, fabric weave, knurling,
wood grain, rust pitting, etc. — enough detail to guide normal baking or AI texture generation]

EMISSIVE (if applicable): [glowing elements, screens, energy lines, or "none"]

STYLE REFERENCE: [art direction summary, e.g., "AAA game asset, similar to The Last of Us or
Destiny 2 weapon art — functional realism, subtle wear, readable at game distance"]

Output: 2048×2048 texture set minimum. Seamless tiling where applicable. Consistent lighting
baked out of albedo — no baked shadows in base color map.
```

---

### Step 4: Generate Prompt C — Image Reference for Image-to-3D

This prompt generates a 2D reference image (using Midjourney, DALL-E 3, Stable Diffusion, etc.)
that can then be fed into image-to-3D tools (Tripo3D, CSM, Meshy Image Mode, One-2-3-45, etc.).

**Template:**

```
PROMPT C — IMAGE REFERENCE (for Image-to-3D Pipeline)

Product-shot style rendering of [OBJECT NAME], [STYLE] design aesthetic.

[OBJECT DESCRIPTION — single detailed sentence covering shape, material, and most distinctive feature]

VIEW: [3/4 angle from slightly above for most objects / front orthographic for characters /
top-down for flat objects]. Clean white background (#FFFFFF) or transparent background.
No drop shadows. No scene elements.

LIGHTING: Soft diffuse studio lighting, fill lights on both sides, no harsh directional shadows.
Light source slightly above and in front of the object. Even illumination on all surfaces —
no area of the mesh should be in deep shadow (important for clean 3D reconstruction).

RENDER QUALITY: Hyperrealistic, 8K product visualization. Surface materials clearly readable.
[MATERIAL CALLOUTS: highlight 2-3 key material surfaces explicitly, e.g., "the steel blade
has sharp specular highlights, the handle wrap shows clear textile weave detail"]

FRAMING: Object fills 70-80% of frame. Center-aligned. Portrait or square crop preferred
(1:1 or 4:5 aspect ratio for best multi-view reconstruction results).

NO: motion blur, depth of field blur, artistic bokeh, heavy post-processing, lens distortion.
CLEAN: sharp focus edge-to-edge, no atmospheric effects.

[If multiple views needed for better reconstruction]: Generate 3 views — front, 45° side,
and top-down — matching lighting and background.
```

---

### Step 5: Build and Open the HTML Prompt Page

After generating all 3 prompts, deliver them in a gorgeous HTML page with the generator panel on
the left and tool recommendations on the right.

**How to build it:**

1. Read the HTML template from `~/.claude/skills/3d-asset-generator/3d-asset-template.html`

2. Replace these placeholders with the actual content:
   - `{{OBJECT_NAME}}` — the asset name for the page title (e.g. "Sci-Fi Combat Knife")
   - `{{ASSET_TITLE}}` — heading text (e.g. "COMBAT")
   - `{{ASSET_SUBTITLE}}` — second heading word, displayed faded (e.g. "KNIFE")
   - `{{ASSET_STYLE}}` — style descriptor (e.g. "Sci-Fi • Game Asset • PBR")
   - `{{POLY_BUDGET}}` — polygon tier (e.g. "Low-poly (game-ready)" or "High-poly (cinematic)")
   - `{{USE_CASE}}` — intended use (e.g. "Game Asset", "Film VFX", "3D Printing")
   - `{{PROMPT_A}}` — the full text of Prompt A (plain text, no HTML)
   - `{{PROMPT_B}}` — the full text of Prompt B (plain text, no HTML)
   - `{{PROMPT_C}}` — the full text of Prompt C (plain text, no HTML)
   - `{{TOOLS_A}}` — comma-separated list of recommended tools for Prompt A
   - `{{TOOLS_B}}` — comma-separated list of recommended tools for Prompt B
   - `{{TOOLS_C}}` — comma-separated list of recommended tools for Prompt C

3. **Important**: When inserting prompt text, escape any `<`, `>`, and `&` characters as HTML
   entities (`&lt;`, `&gt;`, `&amp;`) so they render correctly in the browser.

4. Write the completed HTML to a file called `3d-prompts.html` in the user's current working
   directory.

5. Open the file:
   - macOS: `open 3d-prompts.html`
   - Linux: `xdg-open 3d-prompts.html`
   - Windows: `start 3d-prompts.html`

**Tool recommendations by prompt type:**

For Prompt A (text-to-3D):
- Meshy AI (meshy.ai) — best overall quality, game-ready output
- Tripo3D — fast, good topology
- Hyper3D / Rodin — high detail
- Shap-E / Point·E — open source options

For Prompt B (textures):
- Meshy Texture Mode — one-click PBR from mesh
- Adobe Substance 3D — industry standard
- DreamMat / TextureLab — AI-driven PBR
- Stable Diffusion + ControlNet depth — custom styles

For Prompt C (image-to-3D):
- Tripo3D Image Mode — best reconstruction from single image
- CSM (Common Sense Machines) — multi-view support
- One-2-3-45 — open source multi-view
- Meshy Image Mode — integrated workflow

---

### Step 6: Also Present Prompts in Chat

After building the HTML page, also present the prompts in chat as a fallback:

```
## Your 3D Asset Prompt Set: [OBJECT]

### PROMPT A — Text-to-3D Generation
[paste into Meshy AI, Tripo3D, Hyper3D, or your preferred text-to-3D tool]

{prompt A}

---

### PROMPT B — PBR Texture / Material
[paste into Meshy Texture Mode, Substance 3D, or DreamMat after generating the mesh]

{prompt B}

---

### PROMPT C — Image Reference (Image-to-3D)
[first generate the image in Midjourney/DALL-E, then feed into Tripo3D or CSM image mode]

{prompt C}

---

### Recommended Workflow
1. Generate Prompt A in Meshy or Tripo3D → download mesh (.glb / .obj)
2. Apply Prompt B textures (use Meshy texture mode or bake in Substance)
3. If text-to-3D result is weak, generate Prompt C image first, then use image-to-3D
4. Import final .glb into your game engine / scene / slicer
```

---

## Best Practices

1. **Silhouette first** — The most important thing for 3D AI generation is a distinctive, clear
   silhouette. Front-load silhouette descriptors in Prompt A.
2. **Material clarity** — Name specific materials rather than colors. "Brushed titanium" generates
   better than "grey metal".
3. **Poly budget matters** — Low-poly prompts should emphasize "clean topology", "game-ready",
   "low polygon count". High-poly prompts should emphasize "subdivision surface ready", "sculpt quality".
4. **Texture and mesh prompts are separate** — Most tools generate geometry and textures independently.
   The prompts are split for this reason.
5. **Image-to-3D beats text-to-3D for complex objects** — If Prompt A gives weak results, use
   Prompt C to generate a reference image first, then do image-to-3D reconstruction.
6. **The HTML page is the primary deliverable** — Always generate and open it automatically.

---

## Error Recovery

| Issue | Solution |
|---|---|
| Mesh topology is poor | Add "clean quad topology, no triangles except at poles, edge loops follow form" to Prompt A |
| Textures don't match mesh style | Add "match the exact material style and weathering of the reference mesh" to Prompt B |
| Image-to-3D reconstruction is incomplete | Add "multiple views: front orthographic, side orthographic, top-down, all matching lighting" to Prompt C |
| Object has missing geometry (holes) | Add "watertight mesh, manifold geometry, no open edges or holes" to Prompt A |
| Low-poly result looks too blocky | Use Prompt C image-to-3D pipeline instead — image reference gives better detail guidance |
| Textures have baked-in shadows | Add "no ambient occlusion or shadows baked into albedo map, flat unlit base color only" to Prompt B |
| HTML page doesn't open | Use `start 3d-prompts.html` (Windows), `open 3d-prompts.html` (Mac), or tell user the path |
