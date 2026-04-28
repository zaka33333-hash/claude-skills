---
name: doc-coauthoring
description: >
  Collaboratively writes documentation, proposals, technical specs, decision documents, and any
  structured long-form content through a guided 3-stage process. Trigger when the user wants help
  writing a document, creating a proposal, drafting a spec, writing a report, or building any
  structured written content. Also triggers for "help me write", "draft a document", "create a
  proposal", "write a brief", or when the user has complex information they need organized into
  a professional document.
keywords:
  - document
  - writing
  - proposal
  - spec
  - report
  - brief
  - draft
  - coauthoring
  - documentation
---

# Doc Co-Authoring Skill

You guide collaborative document creation through three stages: context gathering, building, and validation. The goal is documents that genuinely work for their readers — not just documents that look complete.

---

## When to Offer the Structured Workflow

When the user mentions writing documentation, a proposal, a spec, a decision doc, or any structured content, offer the guided workflow:

> "I can guide you through a structured process that produces much stronger documents — context gathering, section-by-section building, and reader testing. Want to use that approach, or prefer to work freeform?"

Always respect their choice. If they want freeform, help them directly. If they want the structure, proceed with the 3 stages below.

---

## Stage 1 — Context Gathering

**Goal**: Close all knowledge gaps before writing a single word.

### Meta Questions (ask first)
1. What type of document is this? (proposal, spec, guide, report, brief, etc.)
2. Who is the primary audience? What do they already know?
3. What should the reader DO or DECIDE after reading this?
4. What format does it need to be in? (length, structure, tone, formality)

### Info Dump
Ask the user to share everything relevant:
> "Tell me everything you know about this topic — background, context, constraints, decisions already made, things that are uncertain. Don't organize it, just dump it all."

### Clarifying Questions
After the info dump, ask targeted questions about:
- Edge cases and exceptions
- Trade-offs and decisions not yet made
- Constraints (technical, legal, organizational)
- What's explicitly NOT in scope

Do not proceed to Stage 2 until you can answer: "Do I understand this topic well enough to write about it accurately?"

---

## Stage 2 — Section-by-Section Building

**Goal**: Build the document one section at a time through a repeatable refinement cycle.

### Opening Move
Create a document scaffold — the full outline with section titles and 1-sentence descriptions of what each section will contain. Show this to the user and confirm before writing.

### Per-Section Cycle (repeat for each section)
1. **Clarifying questions** — anything still unclear for THIS section
2. **Brainstorm** — generate 5–20 options for how to frame or present the content (the more options, the better the final pick)
3. **Curate** — narrow to the best 1–3 approaches and explain why
4. **Draft** — write the section
5. **Refine** — revise based on feedback before moving to the next section

### Section Order Strategy
Start with the hardest sections — the ones with the most unknowns or greatest complexity. Once those are solid, the easier sections flow naturally from them.

### Document-Level Principles
- Maintain a running draft throughout (in an artifact or file)
- Each section should connect logically to the next — no orphaned content
- Headers should be descriptive, not generic ("Why we chose PostgreSQL" not "Database Decision")
- Use tables, lists, and callouts to break up dense text

---

## Stage 3 — Reader Testing

**Goal**: Verify the document works for someone who wasn't part of writing it.

### Predict Reader Questions
Before testing, list 5–10 questions a fresh reader would likely have:
- "What does X mean here?"
- "Why was this decision made?"
- "What should I do if Y happens?"

### Test Methods
**Option A (if subagents available)**: Spawn a fresh Claude instance and have it read the document, then report: areas of confusion, missing context, ambiguous statements, and assumed knowledge not explained.

**Option B (manual)**: Ask the user to read the document fresh, pretending they wrote none of it.

### Iteration
Fix every issue surfaced by reader testing. Then test again if significant changes were made.

### Final Check
Before declaring the document complete, the user must personally read the whole thing once. No exceptions.

---

## Document Types Reference

| Type | Key sections | Tone |
|------|-------------|------|
| Technical spec | Overview, requirements, architecture, decisions, open questions | Precise, technical |
| Business proposal | Problem, solution, benefits, costs, timeline, risks | Persuasive, professional |
| Decision doc | Context, options considered, recommendation, rationale | Clear, decisive |
| How-to guide | Prerequisites, steps, expected outcomes, troubleshooting | Instructional, clear |
| Status report | Summary, progress, blockers, next steps | Concise, factual |
| Distributor brief | Company intro, product range, terms, next steps | Professional, compelling |
