---
description: "Analyze current codebase and identify missing tests, with prioritized recommendations and coverage targets"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Tests Gap Analysis

Looking at the current #codebase, what tests are needed and missing?

## Objective

Perform a read-only audit of the repository to:

- Inventory existing tests by type and coverage signals
- Identify critical functionalities and surfaces with missing or insufficient tests
- Recommend concrete test cases with priorities and example scaffolds
- Propose realistic coverage goals and a stepwise plan to get there

## Inputs

- Codebase: all source files and test files in the repository
- Signals: presence of unit/integration/e2e tests, test runners, CI steps, coverage reports, fixtures, mocks

## Scope and exclusions

- Exclude: `.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/` artifacts (read only), binaries
- Do not modify files or run commands; static analysis only

## Steps

1. Discover testing setup
   - Detect test frameworks/runners (e.g., Jest, Vitest, Mocha, pytest, JUnit, MSTest, xUnit, Playwright/Cypress)
   - Identify test directories and naming patterns
   - Find any coverage configuration and thresholds
   - Locate CI workflow steps for tests

2. Inventory existing tests
   - Count tests by type: unit, integration, e2e, component, contract
   - List critical modules/components with their existing tests
   - Note flakiness indicators (e.g., retries, skipped tests)

3. Map critical functionality
   - Identify core domains, public APIs, services, critical UI flows, and error handling paths
   - Use naming, folder structure, and entry points to infer importance

4. Identify gaps and risks
   - For each critical area, state whether tests exist and if they’re adequate
   - Flag untested error paths, boundary conditions, auth/security checks, and integration seams

5. Recommend tests
   - Provide a prioritized list of missing tests, each with:
     - Type (unit/integration/e2e/component/contract)
     - Target (file/module/flow)
     - Scenario outline (Given/When/Then or Arrange/Act/Assert)
     - Rationale (risk covered, regressions prevented)
     - Est. effort (S/M/L)

6. Coverage goals and plan
   - Suggest baseline coverage targets (overall and by critical areas)
   - Propose a 2–3 phase plan to reach targets with quick wins first

7. Summarize and report durations
   - Provide an executive summary and time breakdown per step and total

## Output format (Markdown)

### Executive summary
- Current test posture, biggest gaps, and risk level in 2–3 sentences

### Detected testing setup
- Frameworks/runners, directories, patterns, CI steps, coverage config

### Test inventory
- Counts by type; notable files/components and their tests

### Gaps and risks
Provide a table. One row per gap.

| Area/Target | Missing test type | Scenario summary | Risk/Impact | Effort |
|---|---|---|---|---|
| auth/login flow | e2e | Invalid credentials show error and no session set | Prevents auth regressions | M |

### Recommended tests (prioritized)
- Bullet list grouped by High/Medium/Low priority with brief scenario outlines

### Coverage goals and plan
- Baseline targets and phased plan with milestones

### Sources scanned
- Key files and directories consulted

### Durations
- Step 1: <duration>
- Step 2: <duration>
- Step 3: <duration>
- Step 4: <duration>
- Step 5: <duration>
- Step 6: <duration>
- Step 7: <duration>
- Total: <duration>

## Constraints

- Be concrete and evidence-based (file paths, components, modules)
- Prefer small, high-signal tests early; avoid speculative test cases
- No network calls or code modifications
