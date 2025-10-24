---
description: "Review `.github/instructions` for deviations from current best practices and generate GitHub issue drafts to update them"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Instruction Files — Best Practices Review to GitHub Issues

Analyze the files in the `.github/instructions` folder and report where they no longer represent best practices. Create GitHub issues for instruction file updates.

## Objective

Perform a read-only audit of instruction files to identify outdated guidance, gaps, or conflicts with modern best practices and produce ready-to-post issue drafts to update them.

## Inputs

- Instruction sources: `.github/instructions/**/*` (md, mdx, yml, yaml, json)
- Signals: normative language (MUST/SHOULD), version pins, tooling references, security/testing/coding/CI policies

## Scope and exclusions

- Exclude: non-instruction folders; do not modify files; no external calls

## Best-practices lenses (non-exhaustive)

- Security: secret management, SBOM/dependency policy, secure defaults, headers, least privilege
- Testing: coverage targets, CI enforcement, flaky test policy, types of tests
- Code quality: formatting/linters, code review guidelines, naming conventions, ADRs
- DevEx/Tooling: modern toolchain versions, deprecations, recommended alternatives
- Observability: logging standards, error handling, tracing/metrics guidance
- Cloud/Infra (if applicable): environment config patterns, IaC references

## Steps

1. Inventory instruction files and topics

   - Map files to topics and note version/tool references

2. Detect outdated or non-best-practice guidance

   - Find deprecated tools, weak security stances, unclear or conflicting rules, missing critical sections

3. Propose updates

   - For each issue, suggest concrete wording or structural changes and identify the exact file/section

4. Create GitHub issue drafts

   - Prepare issue bodies with title, context, suggested update, acceptance criteria, and labels

5. Summarize and durations
   - Executive summary and time breakdown per step and total

## Output format (Markdown)

### Executive summary

- 2–3 sentences summarizing gaps and urgency

### Findings

Provide a table. One row per finding.

| ID       | Topic    | File/Section                               | Finding                             | Impact | Suggested update                                  |
| -------- | -------- | ------------------------------------------ | ----------------------------------- | ------ | ------------------------------------------------- |
| INST-001 | Security | `.github/instructions/security.md#Secrets` | Recommends storing API keys in repo | High   | Mandate secret manager and pre-commit/CI scanning |

### GitHub issue drafts

Provide a section per finding with an issue-ready body.

#### [INST-001] Update security instructions: secrets management

- Topic: Security
- File/Section: `.github/instructions/security.md#Secrets`

Problem:

- Current guidance suggests storing API keys in version control, which is no longer acceptable.

Suggested update:

- Require using a secret manager (e.g., environment variables backed by vault), remove secrets from code, and add CI secret scanning.

Acceptance criteria:

- Instruction file updated with new policy and examples
- Add note referencing secret scanning in CI and local pre-commit hooks

Labels:

- documentation, best-practices, security

### Sources scanned

- List of instruction files and sections

### Durations

- Step 1: <duration>
- Step 2: <duration>
- Step 3: <duration>
- Step 4: <duration>
- Step 5: <duration>
- Total: <duration>

## Constraints

- Evidence-based; cite exact files/sections
- Conservative suggestions; align with widely-accepted modern practices
- No edits or external calls
