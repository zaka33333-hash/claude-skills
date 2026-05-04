---
name: deprecation-and-migration
description: Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when deciding whether to maintain or sunset existing code. Covers Strangler, Adapter, and Feature Flag migration patterns.
---

# Deprecation and Migration

## Overview

Code is a liability, not an asset. Every line has ongoing maintenance cost -- bugs to fix, dependencies to update, security patches to apply, and new engineers to onboard. Deprecation is the discipline of removing code that no longer earns its keep, and migration is the process of moving users safely from old to new.

## When to Use

- Replacing an old system, API, or library with a new one
- Sunsetting a feature no longer needed
- Consolidating duplicate implementations
- Removing dead code that nobody owns but everybody depends on
- Planning the lifecycle of a new system (deprecation planning starts at design time)
- Deciding whether to maintain a legacy system or invest in migration

## Core Principles

### Code Is a Liability

Every line needs tests, documentation, security patches, dependency updates, and mental overhead. The value of code is the functionality it provides, not the code itself. When the same functionality can be provided with less complexity, the old code should go.

### Hyrum's Law Makes Removal Hard

With enough users, every observable behavior becomes depended on -- including bugs and timing quirks. This is why deprecation requires active migration, not just announcement.

### Deprecation Planning Starts at Design Time

When building something new, ask: "How would we remove this in 3 years?" Systems designed with clean interfaces and minimal surface area are easier to deprecate.

## The Deprecation Decision

Before deprecating anything, answer:

```
1. Does this system still provide unique value?
2. How many users/consumers depend on it?
3. Does a replacement exist?
4. What is the migration cost for each consumer?
5. What is the ongoing maintenance cost of NOT deprecating?
```

## Compulsory vs Advisory Deprecation

| Type | When to Use | Mechanism |
|------|-------------|-----------|
| **Advisory** | Migration is optional, old system is stable | Warnings, documentation, nudges. Users migrate on their own timeline. |
| **Compulsory** | Old system has security issues, blocks progress, or maintenance cost is unsustainable | Hard deadline. Must provide migration tooling. |

**Default to advisory.** Use compulsory only when maintenance cost or risk justifies forcing migration.

## The Migration Process

### Step 1: Build the Replacement

Do not deprecate without a working alternative. The replacement must:
- Cover all critical use cases of the old system
- Have documentation and migration guides
- Be proven in production (not just "theoretically better")

### Step 2: Announce and Document

```markdown
## Deprecation Notice: OldService

**Status:** Deprecated as of 2025-03-01
**Replacement:** NewService (see migration guide below)
**Removal date:** Advisory -- no hard deadline yet
**Reason:** OldService requires manual scaling and lacks observability.

### Migration Guide
1. Replace import statement (see examples below)
2. Update configuration
3. Run the migration verification script
```

### Step 3: Migrate Incrementally

Migrate consumers one at a time, not all at once. For each consumer:
1. Identify all touchpoints with the deprecated system
2. Update to use the replacement
3. Verify behavior matches (tests, integration checks)
4. Remove references to the old system
5. Confirm no regressions

**The Churn Rule:** If you own the infrastructure being deprecated, you are responsible for migrating your users -- or providing backward-compatible updates. Don't announce deprecation and leave users to figure it out.

### Step 4: Remove the Old System

Only after all consumers have migrated:
1. Verify zero active usage (metrics, logs, dependency analysis)
2. Remove the code, tests, documentation, and configuration
3. Remove the deprecation notices
4. Celebrate -- removing code is an achievement

## Migration Patterns

### Strangler Pattern

Run old and new systems in parallel. Route traffic incrementally from old to new.

```
Phase 1: New handles 0%, old handles 100%
Phase 2: New handles 10% (canary)
Phase 3: New handles 50%
Phase 4: New handles 100%, old idle
Phase 5: Remove old system
```

### Adapter Pattern

Create an adapter that translates calls from the old interface to the new implementation. Consumers keep using the old interface while you migrate the backend.

### Feature Flag Migration

Use feature flags to switch consumers from old to new system one at a time.

## Zombie Code

Zombie code is code that nobody owns but everybody depends on. Signs:
- No commits in 6+ months but active consumers exist
- No assigned maintainer
- Failing tests that nobody fixes
- Dependencies with known vulnerabilities nobody updates

**Response:** Either assign an owner and maintain it properly, or deprecate with a concrete migration plan. Zombie code cannot stay in limbo.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "It still works, why remove it?" | Maintenance cost grows silently. |
| "Someone might need it later" | If needed later, it can be rebuilt cheaper than maintaining it. |
| "The migration is too expensive" | Compare migration cost to ongoing maintenance cost over 2-3 years. |
| "Users will migrate on their own" | They won't. Provide tooling, documentation, and incentives. |

## Red Flags

- Deprecated systems with no replacement available
- Deprecation announcements with no migration tooling
- "Soft" deprecation that has been advisory for years with no progress
- Zombie code with no owner and active consumers
- New features added to a deprecated system

## Verification

After completing a deprecation:

- [ ] Replacement is production-proven and covers all critical use cases
- [ ] Migration guide exists with concrete steps and examples
- [ ] All active consumers have been migrated (verified by metrics/logs)
- [ ] Old code, tests, documentation, and configuration are fully removed
- [ ] No references to the deprecated system remain in the codebase
- [ ] Deprecation notices are removed
