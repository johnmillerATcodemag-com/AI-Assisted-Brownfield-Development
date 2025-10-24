---
description: "Analyze the codebase for security concerns and generate GitHub-issue-ready findings with severity and remediation"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Security Audit — Findings to GitHub Issues

Looking at the current #codebase, what are security concerns? Create GitHub issues from your findings.

## Objective

Perform a read-only security review of the repository, identify concrete risks with evidence, map them to standards (OWASP/CWE), and produce ready-to-post GitHub issue drafts including remediation steps and severity.

## Inputs

- Source code and configs across the repository
- Signals: secrets in code, insecure deps, unsafe APIs, missing validations, weak crypto, authz gaps, misconfigurations, CI/CD exposures

## Scope and exclusions

- Exclude: `.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, binaries
- Static analysis only; do not run commands or alter files

## Checks (non-exhaustive)

- Secrets and credentials: hardcoded keys/tokens, `.env` handling, `.gitignore` gaps
- Dependency risk: known-vulnerable packages by name/version hints; presence of lockfiles and audit scripts
- Injection: unsanitized input into queries/commands/templates; improper parameterization
- XSS/templating: unescaped user input rendered to UI; DOM sinks
- AuthN/AuthZ: missing checks, insecure session/token handling, CSRF protections
- Crypto: unsafe algorithms/modes, missing salting/IVs, homegrown crypto
- Transport/security headers: missing HTTPS/HSTS, CSP, X-Frame-Options, etc. (where applicable)
- Logging/observability: sensitive data in logs, lack of error boundaries, PII leakage
- Configuration: default creds, permissive CORS, debug flags in prod configs

## Steps

1. Discover security-relevant files

   - App configs, env samples, auth/crypto modules, DB access, HTTP clients/servers, CI/CD workflows

2. Scan for issues and collect evidence

   - Record concrete file paths and line ranges; minimize speculation

3. Classify and map

   - Assign Severity (Critical/High/Medium/Low), likely Impact, and map to OWASP Top 10 and/or CWE where applicable

4. Create issue drafts

   - For each finding, prepare an issue with title, description (evidence, impact), remediation steps, references, severity labels, and suggested assignees/area labels (if discoverable)

5. Summarize and durations
   - Executive summary and time breakdown per step and total

## Output format (Markdown)

### Executive summary

- 2–3 sentences on overall security posture and top risks

### Findings

Provide a table. One row per finding.

| ID      | Category         | File:Lines            | Severity | Impact                                  | OWASP/CWE   | Brief remediation                      |
| ------- | ---------------- | --------------------- | -------- | --------------------------------------- | ----------- | -------------------------------------- |
| SEC-001 | Hardcoded secret | `src/config.ts:18-26` | High     | Key leakage enables unauthorized access | A02/CWE-798 | Move secrets to vault/env; rotate keys |

### GitHub issue drafts

Provide a section per finding with an issue-ready body.

#### [SEC-001] Hardcoded secret in src/config.ts

- Severity: High
- Category: Secrets management
- Affected: `src/config.ts:18-26`
- Standards: OWASP A02 (Cryptographic Failures), CWE-798 (Use of Hard-coded Credentials)

Description:

- Evidence of a hardcoded API key/token in the repository which can leak via version control and artifact logs.

Impact:

- Exposure enables unauthorized access to dependent services and data.

Remediation:

- Remove the secret from source control; use environment variables or a secret manager.
- Rotate the compromised secret.
- Add a pre-commit/CI secret scan to prevent regressions.

References:

- https://owasp.org/Top10/A02_2021-Cryptographic_Failures/
- https://cwe.mitre.org/data/definitions/798.html

Labels:

- security, severity:high, area:config

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

- Evidence-driven; include file:line references
- No external calls or code changes
- Keep remediations actionable and minimal to start
