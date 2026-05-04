---
name: ci-cd-and-automation
description: Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies with feature flags and staged rollouts.
---

# CI/CD and Automation

## Overview

Automate quality gates so that no change reaches production without passing tests, lint, type checking, and build. CI/CD is the enforcement mechanism for every other skill -- it catches what humans and agents miss, consistently on every single change.

**Shift Left:** Catch problems as early in the pipeline as possible. A bug caught in linting costs minutes; the same bug caught in production costs hours.

**Faster is Safer:** Smaller batches and more frequent releases reduce risk. A deployment with 3 changes is easier to debug than one with 30.

## When to Use

- Setting up a new project's CI pipeline
- Adding or modifying automated checks
- Configuring deployment pipelines
- Debugging CI failures

## The Quality Gate Pipeline

Every change goes through these gates before merge:

```
Pull Request Opened
    |
    v
LINT CHECK     (eslint, prettier)
    |
TYPE CHECK     (tsc --noEmit)
    |
UNIT TESTS     (jest/vitest)
    |
BUILD          (npm run build)
    |
INTEGRATION    (API/DB tests)
    |
E2E (optional) (Playwright/Cypress)
    |
SECURITY AUDIT (npm audit)
    |
BUNDLE SIZE    (bundlesize check)
    |
    v
  Ready for review
```

**No gate can be skipped.** If lint fails, fix lint -- do not disable the rule. If a test fails, fix the code -- do not skip the test.

## GitHub Actions Configuration

### Basic CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - name: Install dependencies
        run: npm ci
      - name: Lint
        run: npm run lint
      - name: Type check
        run: npx tsc --noEmit
      - name: Test
        run: npm test -- --coverage
      - name: Build
        run: npm run build
      - name: Security audit
        run: npm audit --audit-level=high
```

## Feature Flags

Feature flags decouple deployment from release:

```typescript
if (featureFlags.isEnabled('new-checkout-flow', { userId })) {
  return renderNewCheckout();
}
return renderLegacyCheckout();
```

**Flag lifecycle:** Create -> Enable for testing -> Canary -> Full rollout -> Remove the flag and dead code. Set a cleanup date when you create them.

## Staged Rollouts

```
PR merged to main
    |
    v
Staging deployment (auto)
    | Manual verification
    v
Production deployment
    |
    v
Monitor for errors (15-minute window)
    |
    +-- Errors detected -> Rollback
    +-- Clean -> Done
```

## Feeding CI Failures Back to Agents

```
CI fails
    |
    v
Copy the failure output
    |
    v
Feed it to the agent:
"The CI pipeline failed with this error:
[paste specific error]
Fix the issue and verify locally before pushing again."
```

## CI Optimization

When the pipeline exceeds 10 minutes:
1. Cache dependencies (actions/cache or setup-node cache option)
2. Run jobs in parallel (split lint, typecheck, test, build)
3. Only run what changed (path filters)
4. Use matrix builds to shard test suites
5. Use larger runners for CPU-heavy builds

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "CI is too slow" | Optimize the pipeline, don't skip it. |
| "This change is trivial, skip CI" | Trivial changes break builds. |
| "The test is flaky, just re-run" | Flaky tests mask real bugs. Fix the flakiness. |
| "We'll add CI later" | Projects without CI accumulate broken states. Set it up on day one. |

## Red Flags

- No CI pipeline in the project
- CI failures ignored or silenced
- Tests disabled in CI to make the pipeline pass
- Production deploys without staging verification
- No rollback mechanism
- Secrets stored in code or CI config files

## Verification

After setting up or modifying CI:

- [ ] All quality gates are present (lint, types, tests, build, audit)
- [ ] Pipeline runs on every PR and push to main
- [ ] Failures block merge (branch protection configured)
- [ ] CI results feed back into the development loop
- [ ] Secrets are stored in the secrets manager, not in code
- [ ] Deployment has a rollback mechanism
- [ ] Pipeline runs in under 10 minutes for the test suite
