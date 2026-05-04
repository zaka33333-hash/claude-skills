---
name: idea-refine
description: Refines ideas iteratively. Refine ideas through structured divergent and convergent thinking. Use when someone has a rough concept that needs sharpening into an actionable proposal. Trigger phrases: "help me refine this idea", "ideate on X", "stress-test my plan".
---

# Idea Refine

Refines raw ideas into sharp, actionable concepts worth building through structured divergent and convergent thinking.

## How It Works

1. **Understand & Expand (Divergent):** Restate the idea, ask sharpening questions, generate variations.
2. **Evaluate & Converge:** Cluster ideas, stress-test them, surface hidden assumptions.
3. **Sharpen & Ship:** Produce a concrete markdown one-pager.

## Process

### Phase 1: Understand & Expand

**Goal:** Take the raw idea and open it up.

1. **Restate the idea** as a crisp "How Might We" problem statement.

2. **Ask 3-5 sharpening questions** — no more. Focus on:
   - Who is this for, specifically?
   - What does success look like?
   - What are the real constraints (time, tech, resources)?
   - What has been tried before?
   - Why now?

   Do NOT proceed until you understand who this is for and what success looks like.

3. **Generate 5-8 idea variations** using these lenses:
   - **Inversion:** "What if we did the opposite?"
   - **Constraint removal:** "What if budget/time/tech weren't factors?"
   - **Audience shift:** "What if this were for a different user?"
   - **Combination:** "What if we merged this with an adjacent idea?"
   - **Simplification:** "What's the version that's 10x simpler?"
   - **10x version:** "What would this look like at massive scale?"
   - **Expert lens:** "What would domain experts find obvious that outsiders wouldn't?"

### Phase 2: Evaluate & Converge

After the user reacts to Phase 1, shift to convergent mode:

1. **Cluster** the ideas that resonated into 2-3 distinct directions.

2. **Stress-test** each direction:
   - **User value:** Is this a painkiller or a vitamin?
   - **Feasibility:** What's the hardest part?
   - **Differentiation:** Would someone switch from their current solution?

3. **Surface hidden assumptions.** For each direction, explicitly name:
   - What you're betting is true (but haven't validated)
   - What could kill this idea
   - What you're choosing to ignore

**Be honest, not supportive.** If an idea is weak, say so with kindness. A good ideation partner is not a yes-machine.

### Phase 3: Sharpen & Ship

Produce a markdown one-pager:

```markdown
# [Idea Name]

## Problem Statement
[One-sentence "How Might We" framing]

## Recommended Direction
[The chosen direction and why -- 2-3 paragraphs max]

## Key Assumptions to Validate
- [ ] [Assumption 1 -- how to test it]
- [ ] [Assumption 2 -- how to test it]

## MVP Scope
[The minimum version that tests the core assumption. What's in, what's out.]

## Not Doing (and Why)
- [Thing 1] -- [reason]
- [Thing 2] -- [reason]

## Open Questions
- [Question that needs answering before building]
```

**The "Not Doing" list is the most valuable part.** Focus is about saying no to good ideas.

Ask the user to confirm before saving the file.

## Anti-patterns to Avoid

- Generating 20+ shallow variations instead of 5-8 considered ones
- Yes-machining weak ideas instead of pushing back
- Skipping "who is this for"
- Producing a plan without surfacing assumptions
- Producing a plan without a "Not Doing" list

## Red Flags

- No "How Might We" problem statement exists
- Skipping the sharpening questions
- No assumptions surfaced before committing to a direction
- Jumping straight to Phase 3 without running Phases 1 and 2

## Verification

After completing an ideation session:

- [ ] A clear "How Might We" problem statement exists
- [ ] The target user and success criteria are defined
- [ ] Multiple directions were explored, not just the first idea
- [ ] Hidden assumptions are explicitly listed with validation strategies
- [ ] A "Not Doing" list makes trade-offs explicit
- [ ] The output is a concrete artifact (markdown one-pager), not just conversation
