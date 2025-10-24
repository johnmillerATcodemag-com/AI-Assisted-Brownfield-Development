---
description: "Detect dead code (unused files, exports, functions) and generate GitHub-issue-ready findings with remediation"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Dead Code Analysis — Findings to GitHub Issues

Analyze the #codebase and create GitHub issues for any dead code you find.

## Objective

Perform a read-only analysis to locate dead code and produce ready-to-post GitHub issue drafts to remove or refactor it safely.

## Definitions

- Dead file: a source file with no inbound references and not an entry point
- Dead export/symbol: exported but never imported or referenced
- Dead code path: function/branch that cannot be executed given current call graph or feature flags (heuristic)

## Inputs

- All source files and configurations that define entry points (build configs, router, package.json scripts)

## Scope and exclusions

- Exclude: `.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, binaries
- Static analysis only; no file edits or command execution

## Steps

1. Identify entry points

   - Main application bootstrap files, CLI entry scripts, configuration-declared entries (e.g., package.json, bundlers)

2. Build reference map (heuristic)

   - Map imports/exports and intra-repo references (files, functions, classes)
   - Consider dynamic imports and conventional directories (e.g., `pages/`, `routes/`)

3. Detect dead code candidates

   - Files with zero inbound references and not listed as an entry point
   - Exports/symbols never referenced elsewhere
   - Obsolete feature flags/guards that are always false/true

4. Validate and collect evidence

   - Provide file paths and, when possible, symbol names and line ranges
   - Note caveats for dynamic resolution or reflection

5. Create issue drafts

   - Generate an issue per finding with title, description (evidence, rationale), suggested remediation, and labels

6. Summarize and durations
   - Executive summary and time breakdown per step and total

## Output format (Markdown)

### Executive summary

- 2–3 sentences on overall dead code footprint and cleanup impact

### Findings

Provide a table. One row per finding.

| ID       | Type        | Target                     | Evidence                        | Risk | Suggested action             |
| -------- | ----------- | -------------------------- | ------------------------------- | ---- | ---------------------------- |
| DEAD-001 | Unused file | `src/legacy/old-helper.ts` | No inbound refs; not in entries | Low  | Remove file; verify CI build |

### GitHub issue drafts

Provide a section per finding with an issue-ready body.

#### [DEAD-001] Unused file: src/legacy/old-helper.ts

- Type: Unused file
- Evidence: Not imported anywhere; not referenced by build entries
- Risk: Low (no runtime use detected); consider dynamic import caveats

Description:

- This file appears to be unused and can be removed to reduce maintenance and build time.

Acceptance Criteria:

- File is deleted and CI/build passes
- No regressions in dependent modules

Remediation:

- Remove the file and run full build/tests

Labels:

- cleanup, tech-debt, area:legacy

### Sources scanned

- Key files and directories consulted

### Durations

- Step 1: <duration>
- Step 2: <duration>
- Step 3: <duration>
- Step 4: <duration>
- Step 5: <duration>
- Step 6: <duration>
- Total: <duration>

## Constraints

- Heuristic-based and conservative; when in doubt, mark as candidate rather than definitive
- Provide evidence and caveats for dynamic loading/reflection
- No external calls or code edits
