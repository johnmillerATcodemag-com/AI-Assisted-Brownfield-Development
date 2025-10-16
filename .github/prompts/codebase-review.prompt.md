---
description: "Audit codebase against .github/instructions and report evidenced deviations with severity and fixes"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Codebase vs. Instructions Audit

Analyze this repository and report any deviations from the rules and guidance defined in `.github/instructions`.

## Inputs

- Instruction sources: all files under `.github/instructions/**/*` with extensions: `md, mdx, yml, yaml, json`.
- Codebase: all source files in the repository, excluding common build/output and dependency folders.

## Scope and exclusions

- Exclude folders: `.git/`, `.github/` (except `.github/instructions/`), `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/`, `out/`.
- Read-only analysis. Do not modify files.
- Treat normative words (MUST, SHOULD, SHALL, REQUIRED, RECOMMENDED, MAY, OPTIONAL) in instruction files as rule indicators.

## Steps

1. Discover instructions

   - List and read all instruction files in `.github/instructions`.
   - If none found, see “Missing instructions fallback”.
   - Extract explicit rules, policies, and best practices across topics: coding style, security, secrets, dependencies, testing, CI, logging/observability, error handling, performance, architecture, documentation, release/versioning, branching/commits.
   - Assign each rule a stable Rule ID (file-based) and capture its source anchor (file path and heading, if available).

2. Map rules to checks

   - For each rule, define concrete, observable checks (e.g., required files present, config keys set, patterns/anti-patterns not present, linter/test coverage expectations, package scripts, CI jobs).
   - Prefer static signals and lightweight heuristics; avoid speculation.

3. Analyze the codebase

   - Traverse files (respecting exclusions) and gather evidence for each check.
   - Record file paths and, when possible, line ranges that demonstrate compliance or deviation.

4. Compile findings

   - Classify each deviation with Severity: Critical, High, Medium, Low.
   - For each, explain Impact and propose a concrete Fix with an estimated Effort (S, M, L).
   - Group fixes into Quick wins (S) and Larger initiatives (M/L).

5. Summarize and report durations
   - Provide an executive summary of overall alignment vs. deviations.
   - Report per-step durations and total duration at the end.

## Output format (Markdown)

### Executive summary

- 2–3 sentences on overall alignment, major gaps, and risk level.

### Deviations

Provide a table. One row per deviation.

| Rule ID  | Rule (summary)       | Instruction source                         | Evidence (file:lines) | Severity | Impact              | Proposed fix                                         | Effort |
| -------- | -------------------- | ------------------------------------------ | --------------------- | -------- | ------------------- | ---------------------------------------------------- | ------ |
| RULE-001 | Example rule summary | `.github/instructions/security.md#Secrets` | `src/config.ts:14-25` | High     | Secret leakage risk | Move secrets to Key Vault; load via env; rotate keys | M      |

Notes:

- “Instruction source” should include the instruction file path and section/heading if available.
- “Evidence” should reference concrete files and line ranges when possible.

### Quick wins

- Bullet list of small, high-impact fixes with links to the corresponding deviation rows.

### Larger initiatives

- Bullet list of medium/large efforts with brief milestones.

### Missing or ambiguous instructions

- List any areas where instructions are missing/ambiguous compared to common best practices; suggest specific instruction updates (file/section proposals).

### Sources scanned

- List of instruction files scanned (paths), plus any key config files in the repo that were relevant.

### Durations

- Step 1 (discover instructions): <duration>
- Step 2 (map rules to checks): <duration>
- Step 3 (analyze codebase): <duration>
- Step 4 (compile findings): <duration>
- Step 5 (summarize and report): <duration>
- Total: <duration>

## Missing instructions fallback

If `.github/instructions` does not exist or contains no files:

- Clearly state that no instruction files were found.
- Perform a lightweight general audit using widely accepted best practices for security, testing, CI, documentation, and structure.
- Output the same sections, but add a “Limitations” note explaining that findings are based on generic best practices rather than project-specific instructions.
- Recommend creating an initial set of instruction documents under `.github/instructions/` with proposed filenames and outlines (e.g., `security.md`, `testing.md`, `coding-standards.md`, `ci.md`, `observability.md`).

## Practical guidance for checks (non-exhaustive)

- Security: no secrets in repo, `.env` in `.gitignore`, dependency audit status, use of parameterized queries, input validation, secure headers, auth/crypto practices.
- Testing: presence of unit/integration tests, coverage targets if defined, test command in manifest, CI test step.
- CI/CD: presence of workflows/pipelines aligned to instructions, required checks gating PRs, lint/format steps.
- Coding standards: linters/formatters configured and enforced, consistent language versions, directory structure conventions.
- Observability: structured logging, error handling policies, trace/metrics hooks if required.
- Documentation: README completeness, contribution guidelines, ADRs if mandated.

## Constraints

- Be concise and specific; avoid speculation. Prefer concrete evidence.
- Do not run external network calls or fetch private data.
- Respect the exclusions; do not analyze binary/large artifacts.
