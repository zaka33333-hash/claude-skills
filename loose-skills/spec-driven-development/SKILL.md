---
name: spec-driven-development
description: Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements are unclear, ambiguous, or only exist as a vague idea. Enforces a gated SPECIFY -> PLAN -> TASKS -> IMPLEMENT workflow.
---

# Spec-Driven Development

## Overview

Write a structured specification before writing any code. The spec is the shared source of truth — it defines what we are building, why, and how we will know it is done. Code without a spec is guessing.

## When to Use

- Starting a new project or feature
- Requirements are ambiguous or incomplete
- The change touches multiple files or modules
- You are about to make an architectural decision
- The task would take more than 30 minutes to implement

**When NOT to use:** Single-line fixes, typo corrections, or changes where requirements are unambiguous and self-contained.

## The Gated Workflow

Do not advance to the next phase until the current one is validated by the human.

```
SPECIFY -> PLAN -> TASKS -> IMPLEMENT
```

Each phase: human reviews and approves before you proceed.

### Phase 1: Specify

Start with a high-level vision. Ask the human clarifying questions until requirements are concrete.

**Surface assumptions immediately. Before writing any spec content, list what you are assuming:**

```
ASSUMPTIONS I'M MAKING:
1. This is a web application (not native mobile)
2. Authentication uses session-based cookies (not JWT)
3. The database is PostgreSQL (based on existing Prisma schema)
4. We are targeting modern browsers only (no IE11)
-> Correct me now or I'll proceed with these.
```

Do not silently fill in ambiguous requirements.

**Write a spec document covering these six core areas:**

1. **Objective** -- What are we building and why? Who is the user? What does success look like?

2. **Commands** -- Full executable commands with flags, not just tool names.

3. **Project Structure** -- Where source code lives, where tests go, where docs belong.

4. **Code Style** -- One real code snippet showing your style beats three paragraphs describing it.

5. **Testing Strategy** -- What framework, where tests live, coverage expectations.

6. **Boundaries** -- Three-tier system:
   - **Always do:** Run tests before commits, follow naming conventions, validate inputs
   - **Ask first:** Database schema changes, adding dependencies, changing CI config
   - **Never do:** Commit secrets, edit vendor directories, remove failing tests without approval

**Reframe instructions as success criteria:**

```
REQUIREMENT: "Make the dashboard faster"

REFRAMED SUCCESS CRITERIA:
- Dashboard LCP < 2.5s on 4G connection
- Initial data load completes in < 500ms
- No layout shift during load (CLS < 0.1)
-> Are these the right targets?
```

### Phase 2: Plan

With the validated spec, generate a technical implementation plan:
- Identify the major components and their dependencies
- Determine the implementation order
- Note risks and mitigation strategies
- Identify what can be built in parallel vs. sequential
- Define verification checkpoints between phases

### Phase 3: Tasks

Break the plan into discrete, implementable tasks:
- Each task completable in a single focused session
- Each task has explicit acceptance criteria
- Each task includes a verification step (test, build, manual check)
- Tasks are ordered by dependency, not perceived importance
- No task should require changing more than ~5 files

### Phase 4: Implement

Execute tasks one at a time. Use context-engineering to load the right spec sections at each step.

## Keeping the Spec Alive

The spec is a living document:
- **Update when decisions change** -- Update the spec first, then implement
- **Update when scope changes** -- Features added or cut should be reflected in the spec
- **Commit the spec** -- The spec belongs in version control alongside the code

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "This is simple, I don't need a spec" | Simple tasks don't need long specs, but they still need acceptance criteria. |
| "I'll write the spec after I code it" | That's documentation, not specification. The spec's value is forcing clarity before code. |
| "The spec will slow us down" | A 15-minute spec prevents hours of rework. |
| "Requirements will change anyway" | That's why the spec is a living document. |

## Red Flags

- Starting to write code without any written requirements
- Asking "should I just start building?" before clarifying what "done" means
- Implementing features not mentioned in any spec or task list
- Making architectural decisions without documenting them

## Verification

Before proceeding to implementation, confirm:

- [ ] The spec covers all six core areas
- [ ] The human has reviewed and approved the spec
- [ ] Success criteria are specific and testable
- [ ] Boundaries (Always/Ask First/Never) are defined
- [ ] The spec is saved to a file in the repository
