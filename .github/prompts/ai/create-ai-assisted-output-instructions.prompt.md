---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Generate comprehensive AI provenance and logging policy for all AI-assisted outputs
prompt_metadata:
  id: create-ai-assisted-output-instructions
  title: Generate AI-Assisted Output Policy and Logging Instructions
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/ai-assisted-output.instructions.md
  category: documentation
  tags: [ai-provenance, logging, policy, standards]
  output_format: markdown
---

# Generate AI-Assisted Output Policy

Create comprehensive policy defining required metadata, workflow, and enforcement for all AI-assisted outputs.

## Purpose
Clear provenance and reliable logging for all AI-assisted artifacts to enable audits and understand how artifacts were produced.

## Output: `.github/instructions/ai-assisted-output.instructions.md`

### Structure:
1. **Overview**: Purpose, audience (contributors, developers), scope (all AI-assisted content), terminology (chat ID, not session)
2. **Metadata Placement Policy**: 
   - Formats supporting front matter (Markdown): embed YAML at top
   - Formats not supporting (images, binaries): sidecar `<artifact>.meta.md`
   - No sidecars for Markdown
3. **Required Provenance Metadata** (10 fields):
   - `ai_generated: true` (boolean)
   - `model: "<provider>/<model-name>@<version>"` (explicit format, e.g., "openai/gpt-4o@2024-11-20")
   - `operator: "<github-username>"`
   - `chat_id: "<chat-identifier>"`
   - `prompt: |` (exact prompt text, multiline)
   - `started: "<ISO8601-timestamp>"`
   - `ended: "<ISO8601-timestamp>"`
   - `task_durations:` (array of task/duration objects)
   - `total_duration: "<hh:mm:ss>"`
   - `ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"`
4. **Chat Logging Workflow**:
   - Structure: `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/` with `conversation.md` and `summary.md`
   - Conversation format: Chat ID, operator, model, timestamps, context, exchanges, work burst closure, artifacts
   - Summary format: Overview, methodology, decisions, alternatives, edge cases, testing, validation, next steps
5. **Task Durations**: Capture per-task (analysis, design, implementation, testing) and total
6. **Placement & Naming**: Conventions for different artifact types
7. **Quality Checklist**: All 10 fields present, model explicit format, chat_id matches ai_log path, timestamps ISO8601
8. **Copilot Integration**: Model identification, chat management, file generation workflow
9. **Enforcement (CI)**: Example validation scripts (Linux/Mac, PowerShell)
10. **Non-Compliance & Remediation**: What happens if missing, how to fix

### Key Requirements:
- Model format MUST be `"<provider>/<model-name>@<version>"` (NOT "Auto (copilot)")
- Use GitHub username, not "USER"
- Each chat creates new conversation.md and summary.md
- Update README.md with link to new artifacts

### Templates to Include:
- Standard metadata front matter
- conversation.md template
- summary.md template
- CI validation scripts

## Deliverable
Complete policy with YAML front matter per its own requirements, all sections, templates, enforcement examples.
