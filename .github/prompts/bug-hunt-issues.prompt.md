---
description: "Identify likely bugs via static analysis heuristics and generate GitHub-issue-ready findings with remediation"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Bug Hunt — Findings to GitHub Issues

Look at the current #codebase and find bugs. Create GitHub issues for any bugs that you find.

## Objective

Perform a read-only, static analysis to surface likely bugs with concrete evidence and produce ready-to-post GitHub issue drafts including remediation suggestions.

## Heuristics (non-exhaustive)

- Null/undefined handling mistakes, unchecked optionals
- Incorrect async/await usage, missing `await`, unhandled promise rejections
- Off-by-one and boundary errors, unsafe indexing
- Resource leaks: timers, subscriptions, file/socket handles not disposed
- Data races/concurrency issues (where applicable)
- API contract mismatches: wrong types/shape, missing fields, misused enums
- Error handling/logging gaps: swallowed errors, broad catches, missing context
- Security-adjacent bugs: input not validated where required
- UI logic pitfalls: stale state, missing dependency arrays, uncontrolled/controlled mismatches (web)

## Steps

1. Map key modules and contracts

   - Identify public APIs, core services, critical flows

2. Scan for bug heuristics

   - Record evidence with file paths and line ranges; avoid speculation

3. Validate and classify

   - Assign severity (Critical/High/Medium/Low) and impact description

4. Create GitHub issue drafts

   - Provide issue titles, descriptions (evidence, impact), remediation steps, and labels

5. Summarize and durations
   - Executive summary and time breakdown per step and total

## Output format (Markdown)

### Executive summary

- 2–3 sentences on overall bug posture and highest risks

### Findings

Provide a table. One row per finding.

| ID      | Category          | File:Lines                   | Severity | Impact                                        | Suggested fix                             |
| ------- | ----------------- | ---------------------------- | -------- | --------------------------------------------- | ----------------------------------------- |
| BUG-001 | Unhandled promise | `src/services/user.ts:72-84` | High     | User save may silently fail and corrupt state | Add missing await and catch; bubble error |

### GitHub issue drafts

Provide a section per finding with an issue-ready body.

#### [BUG-001] Unhandled promise in src/services/user.ts

- Severity: High
- Category: Async error handling
- Affected: `src/services/user.ts:72-84`

Description:

- Promise returned by service call isn’t awaited or handled; errors are swallowed.

Impact:

- Can cause silent data loss or inconsistent UI state.

Remediation:

- Add `await` and proper error handling; propagate or show user-facing error as appropriate.

Labels:

- bug, severity:high, area:services

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

- Evidence-based; include file:line references
- Conservative classification; call out uncertainty when applicable
- No external calls or edits
