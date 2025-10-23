---
description: "Audit codebase against .github/instructions and report deviations"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Codebase vs. Instructions Audit

Analyze repo and report deviations from `.github/instructions` rules.

## Inputs
- Instructions: `.github/instructions/**/*` (md, mdx, yml, yaml, json)
- Codebase: all source files (excluding build/output/deps)

## Exclusions
`.git/`, `.github/` (except instructions), `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/`, `out/`

## Process
1. **Discover**: Read instructions, extract rules (MUST, SHOULD, SHALL, REQUIRED, RECOMMENDED, MAY, OPTIONAL), assign Rule IDs
2. **Map**: Define concrete checks per rule
3. **Analyze**: Traverse files, gather evidence (file:line)
4. **Compile**: Classify deviations (Critical/High/Medium/Low), explain impact, propose fixes (S/M/L effort)
5. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
2–3 sentences on alignment, gaps, risk

### Deviations table
| Rule ID | Rule | Instruction source | Evidence | Severity | Impact | Fix | Effort |
|---------|------|-------------------|----------|----------|--------|-----|--------|
| RULE-001 | Summary | `path#Section` | `file:lines` | High | Risk | Steps | M |

### Quick wins
Small, high-impact fixes

### Larger initiatives
Medium/large efforts with milestones

### Missing/ambiguous instructions
Gaps vs. best practices, suggest updates

### Sources scanned
Instruction files + key configs

### Durations
Per-step + total

## Missing Instructions Fallback
If no instructions found:
- State clearly
- Audit using generic best practices
- Same output format + "Limitations" note
- Recommend creating initial instruction docs

## Check Examples
- **Security**: No secrets in repo, `.env` in `.gitignore`, dep audit, parameterized queries, input validation
- **Testing**: Unit/integration tests, coverage targets, test commands, CI test steps
- **CI/CD**: Workflows/pipelines, required checks, lint/format steps
- **Standards**: Linters/formatters, consistent versions, directory structure
- **Observability**: Structured logging, error handling, trace/metrics
- **Documentation**: README, contribution guidelines, ADRs

## Constraints
- Concise, specific, evidence-based
- No external calls
- Respect exclusions
