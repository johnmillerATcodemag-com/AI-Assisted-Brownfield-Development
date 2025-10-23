---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<GITHUB_USERNAME>"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of instruction-prompt.instructions.md with minimal tokens
started: "2025-10-23T04:38:00Z"
ended: "2025-10-23T04:38:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
applyTo: "**/*.instructions.prompt.md"
---

# AI Instructions: Instruction Prompt Requirements

Requirements for prompts that generate `*.instructions.md` files.

## Applies To
Pattern: `**/*.instructions.prompt.md`

## Mandatory Requirements

### 1. Context Section
Must include AI policy reference:

```markdown
## Context
<domain-specific context>

**CRITICAL**: All AI-generated artifacts MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`. Generated
instruction file MUST include full AI provenance metadata.
```

### 2. Deliverable Section
Must include AI provenance template:

```markdown
## Deliverable

Generate `.github/instructions/<domain>.instructions.md` with:

### Required AI Provenance Metadata (YAML Front Matter)

```yaml
ai_generated: true
model: "<model-name-and-version>"
operator: "<operator-username>"
chat_id: "<chat-identifier>"
prompt: |
  <exact-prompt-text>
started: "<ISO8601-timestamp>"
ended: "<ISO8601-timestamp>"
task_durations:
  - task: "<task-name>"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
applyTo: "<pattern>" # Optional
---
\```

### Content Requirements
<specific requirements>
\```

### 3. Required Front Matter

```yaml
prompt_metadata:
  id: create-<domain>-instructions
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  output_format: markdown
```

## Complete Template

```markdown
---
mode: agent
model: Auto (copilot)
tools: ["create"]
description: Generates <domain> authoring guidelines
prompt_metadata:
  id: create-<domain>-instructions
  title: Generate <Domain> Instructions
  owner: <author-username>
  version: 1.0.0
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  output_format: markdown
---

# Generate <Domain> Instructions

## Context
<domain-context>

**CRITICAL**: All AI-generated artifacts MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`.

## Deliverable
[Include provenance template from above]
```

## Validation Checklist
- [ ] Context references AI policy
- [ ] Deliverable includes provenance template with all 10 fields
- [ ] Output path points to `.github/instructions/<name>.instructions.md`
- [ ] Category is 'documentation'
- [ ] Output format is 'markdown'
- [ ] ID follows `create-<domain>-instructions` pattern

## Common Mistakes
❌ Missing AI provenance section → Add complete YAML template
❌ Not referencing AI policy → Add CRITICAL statement
❌ Vague deliverable → Be explicit about metadata fields
❌ Forgetting applyTo field → Include when applicable

## Creation Options

**Option 1**: Use meta-prompt
```
Submit .github/prompts/meta/create-instruction-prompt.prompt.md
```

**Option 2**: Manual
1. Copy existing instruction prompt
2. Update domain-specific content
3. Ensure Context references AI policy
4. Ensure Deliverable includes provenance template
5. Validate against checklist

## Reference
See `.github/instructions/ai-assisted-output.instructions.md` for complete provenance requirements.
