---
description: "Review .github/instructions for deviations from best practices and generate GitHub issue drafts"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Instruction Files — Best Practices Review to GitHub Issues

Analyze `.github/instructions` files and report where they no longer represent best practices. Create GitHub issues for updates.

## Inputs
Instructions (`.github/instructions/**/*` md, mdx, yml, yaml, json), signals (MUST/SHOULD, version pins, tooling refs, security/testing/coding/CI policies)

## Exclusions
Non-instruction folders, no file modifications, no external calls

## Best-practices Lenses
- **Security**: Secret management, SBOM/dependency policy, secure defaults, headers, least privilege
- **Testing**: Coverage targets, CI enforcement, flaky test policy, test types
- **Code quality**: Formatting/linters, code review guidelines, naming conventions, ADRs
- **DevEx/Tooling**: Modern toolchain versions, deprecations, recommended alternatives
- **Observability**: Logging standards, error handling, tracing/metrics guidance
- **Cloud/Infra**: Environment config patterns, IaC references

## Process
1. **Inventory**: Map files to topics, note version/tool refs
2. **Detect outdated**: Deprecated tools, weak security stances, unclear/conflicting rules, missing critical sections
3. **Propose updates**: Concrete wording/structural changes, exact file/section
4. **Create issue drafts**: Title, context, suggested update, acceptance criteria, labels
5. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
2–3 sentences summarizing gaps and urgency

### Findings table
| ID | Topic | File/Section | Finding | Impact | Suggested update |
|----|-------|--------------|---------|--------|------------------|
| INST-001 | Security | `path#Section` | Issue | High | Update details |

### GitHub issue drafts per finding
**[INST-001] Update security instructions: topic**
- Topic: Security
- File/Section: `path#Section`
- Problem: Current guidance issue
- Suggested update: New policy with examples
- Acceptance: File updated, add refs to tooling
- Labels: documentation, best-practices, security

### Sources scanned
List of instruction files/sections

### Durations
Per-step + total

## Constraints
- Evidence-based, cite exact files/sections
- Conservative suggestions, align with modern practices
- No edits/external calls
