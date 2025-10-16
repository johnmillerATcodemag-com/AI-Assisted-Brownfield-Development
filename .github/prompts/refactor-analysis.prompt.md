---
description: "Analyze the codebase to identify refactoring opportunities with evidence, impact, and a prioritized plan"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Refactoring Opportunities Analysis

Looking at the current #codebase, what needs refactoring?

## Objective

Perform a read-only analysis to surface concrete refactoring opportunities, quantify their impact, and propose an actionable, phased plan to implement them safely.

## Inputs

- Full repository (source code, tests, configs, build/CI files)
- Signals: file size, cyclomatic complexity proxies (function length, nesting), duplication patterns, deprecated APIs, TODO/FIXME tags, lint configs, CI scripts

## Scope and exclusions

- Exclude: `.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, binaries
- No code changes or command execution; static analysis only

## Heuristics and smell catalog (non-exhaustive)

- Size/complexity: long functions, large classes/modules, deep nesting, god objects
- Coupling: high fan-in/out, cross-module imports, circular dependencies, tight UI/logic coupling
- Duplication: repeated logic, copy-paste across modules, near-duplicates
- Naming/clarity: ambiguous names, mixed responsibilities, unclear boundaries
- Error handling/logging: inconsistent patterns, swallow-catch, missing context, unstructured logs
- Testing friction: untestable design, static singletons, side effects in constructors, heavy setup
- Performance pitfalls: N+1 calls, unnecessary re-renders, blocking I/O on hot paths
- Deprecated/legacy: obsolete APIs, framework version straddles, pre-migration shims
- Configuration drift: hardcoded constants, env handling scattered

## Steps

1. Inventory modules and hotspots

   - Identify largest files/functions and high-change areas (name hints, TODOs)
   - List key entry points and boundaries (API, services, UI shells, domains)

2. Detect smells

   - Scan for the smell catalog above and record evidence: file paths and relevant line ranges
   - Note dependencies that complicate refactoring (global state, hidden I/O)

3. Propose refactors

   - For each smell, provide:
     - Refactor type (extract function/module, introduce interface/adapter, dependency inversion, composition, rename, de-duplicate, move to layer, add tests first)
     - Target files/symbols
     - Expected outcome (readability, testability, reliability, performance)
     - Effort (S/M/L) and risk (Low/Med/High)

4. Prioritize and phase

   - Group into Quick wins (S, low risk), Phase 1 (enablers for tests), Phase 2 (structural), Phase 3 (nice-to-have)
   - Suggest a safety net: add or adjust tests where needed before risky moves

5. Summarize and durations
   - Executive summary, key hotspots, and per-step duration plus total

## Output format (Markdown)

### Executive summary

- 2–3 sentences on current maintainability and top refactor themes

### Hotspots inventory

- Largest/most complex modules and why they’re risky

### Findings (smells and evidence)

Provide a table. One row per finding.

| Category    | File/Target       | Evidence (file:lines)                                | Impact                     | Proposed refactor                                   | Effort | Risk |
| ----------- | ----------------- | ---------------------------------------------------- | -------------------------- | --------------------------------------------------- | ------ | ---- |
| Duplication | src/utils/date.ts | Similar logic in `src/components/Report.vue:120-170` | Bug risk, maintenance cost | Extract shared date formatting util; dedupe callers | S      | Low  |

### Refactor proposals (prioritized)

- Grouped by Quick wins, Phase 1, Phase 2, Phase 3 with brief rationale

### Safety net and test strategy

- Tests to add first to de-risk refactors (unit/integration)

### Sources scanned

- Key files and directories consulted

### Durations

- Step 1: <duration>
- Step 2: <duration>
- Step 3: <duration>
- Step 4: <duration>
- Step 5: <duration>
- Total: <duration>

## Constraints

- Evidence-based and minimal speculation; include concrete file references
- Prefer incremental, reversible refactors; avoid big-bang plans
- No code edits or network calls
