---
description: "Identify bugs via static analysis and generate GitHub issues with remediation"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Bug Hunt — Findings to GitHub Issues

Perform static analysis to surface bugs with evidence and create GitHub issue drafts with remediation.

## Heuristics
- Null/undefined handling, unchecked optionals
- Incorrect async/await, missing `await`, unhandled promises
- Off-by-one, boundary errors, unsafe indexing
- Resource leaks: timers, subscriptions, handles
- Data races/concurrency issues
- API contract mismatches
- Error handling gaps: swallowed errors, missing context
- Security: unvalidated input
- UI: stale state, missing deps, controlled/uncontrolled mix

## Process
1. Map key modules/APIs/flows
2. Scan for bug patterns (file:line evidence)
3. Classify (Critical/High/Medium/Low severity + impact)
4. Create GitHub issue drafts (title, evidence, impact, fix, labels)
5. Summarize + durations

## Output (Markdown)

### Executive summary
2–3 sentences on bug posture and highest risks

### Findings table
| ID | Category | File:Lines | Severity | Impact | Fix | 
|----|----------|------------|----------|--------|-----|
| BUG-001 | Unhandled promise | `file.ts:72-84` | High | Silent failure | Add await/catch |

### GitHub issue drafts per finding
**[BUG-001] Title**
- Severity: High
- Category: Type
- Affected: `file:lines`
- Description: Details
- Impact: Consequences
- Remediation: Steps
- Labels: bug, severity, area

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Evidence-based with file:line refs
- Conservative classification
- No external calls/edits
