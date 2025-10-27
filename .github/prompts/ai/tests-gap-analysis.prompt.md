---
description: "Analyze codebase and identify missing tests with prioritized recommendations"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Tests Gap Analysis

What tests are needed and missing?

## Inputs
Codebase (source + test files), signals (unit/integration/e2e tests, runners, CI steps, coverage reports, fixtures, mocks)

## Exclusions
`.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/` artifacts, binaries

## Process
1. **Discover testing setup**: Frameworks/runners (Jest, Vitest, pytest, etc.), test dirs, naming patterns, coverage config/thresholds, CI workflow steps
2. **Inventory existing tests**: Count by type (unit/integration/e2e/component/contract), critical modules/components with tests, flakiness indicators
3. **Map critical functionality**: Core domains, public APIs, services, critical UI flows, error handling paths (use naming, folders, entry points)
4. **Identify gaps/risks**: Per critical area, state if tests exist/adequate, flag untested error paths, boundaries, auth/security checks, integration seams
5. **Recommend tests**: Prioritized list with type, target, scenario outline (Given/When/Then or Arrange/Act/Assert), rationale (risk/regressions), effort (S/M/L)
6. **Coverage goals/plan**: Baseline targets (overall + critical areas), 2–3 phase plan with quick wins first
7. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
Current test posture, biggest gaps, risk level (2–3 sentences)

### Detected testing setup
Frameworks, dirs, patterns, CI steps, coverage config

### Test inventory
Counts by type, notable files/components and their tests

### Gaps/risks table
| Area/Target | Missing type | Scenario | Risk/Impact | Effort |
|-------------|--------------|----------|-------------|--------|
| auth/login | e2e | Invalid creds show error | Auth regressions | M |

### Recommended tests (prioritized)
Grouped by High/Medium/Low priority with scenario outlines

### Coverage goals and plan
Baseline targets, phased plan with milestones

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Concrete, evidence-based (file paths, components)
- Prefer small, high-signal tests early
- No network calls/code modifications
