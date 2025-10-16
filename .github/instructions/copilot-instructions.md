---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "create-prompt-instructions-2025-10-15"
prompt: |
  Consolidate all Copilot-specific instructions into a single copilot-instructions.md file
  that can be referenced from other meta-prompts, prompts, and instruction files.
started: "2025-10-15T16:00:00Z"
ended: "2025-10-15T16:15:00Z"
task_durations:
  - task: "requirements consolidation"
    duration: "00:10:00"
  - task: "file creation"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/15/create-prompt-instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*"
---

# GitHub Copilot Instructions for AI-Assisted Development

## Overview

This document provides comprehensive instructions for GitHub Copilot when working in this repository. These instructions ensure consistent, compliant, and high-quality AI-assisted outputs with proper provenance tracking.

**Scope**: All AI-assisted work in this repository must follow these instructions.

## Core Principles

### 1. Underlying Model Identification

**CRITICAL**: Always identify and use the **underlying AI model**, not the interface.

#### Model Format Requirements

- **Format**: `"<provider>/<model-name>@<version>"`
- **Examples**:
  - `"openai/gpt-4o@2024-11-20"` - GPT-4o (latest)
  - `"openai/gpt-4-turbo@2024-04-09"` - GPT-4 Turbo
  - `"openai/o1-preview@2024-09-12"` - o1-preview reasoning model
  - `"anthropic/claude-3.5-sonnet@2024-10-22"` - Claude 3.5 Sonnet
  - `"anthropic/claude-3-opus@2024-02-29"` - Claude 3 Opus
  - `"google/gemini-1.5-pro@2024-02"` - Gemini 1.5 Pro

#### What NOT to Do

❌ **WRONG**: `"github/copilot@2025-10-15"` (interface, not model)
❌ **WRONG**: `"copilot"` (too vague)
❌ **WRONG**: `"gpt-4"` (missing provider and version)

✅ **CORRECT**: `"openai/gpt-4o@2024-11-20"` (provider/model@version)

#### Interface vs Model

- **Interface**: GitHub Copilot, Cursor, Windsurf, ChatGPT, Claude.ai
- **Model**: The actual AI (GPT-4o, Claude 3.5 Sonnet, etc.)
- **Rule**: Use the model in metadata, optionally note interface in comments

```yaml
# ✅ Correct approach
model: "openai/gpt-4o@2024-11-20"  # via GitHub Copilot

# ❌ Wrong approach
model: "github/copilot@2025-10-15"
```

### 2. Conversation Log Format

**CRITICAL**: Use the operator's GitHub username, not "USER".

#### Correct Format

```markdown
### Exchange 1

[2025-10-15T14:30:00Z] johnmillerATcodemag-com

\`\`\`text
Create a new feature for...
\`\`\`

[2025-10-15T14:32:00Z] openai/gpt-4o@2024-11-20

\`\`\`text
I'll create that feature...
\`\`\`
```

#### Incorrect Format

```markdown
### Exchange 1

[2025-10-15T14:30:00Z] USER ❌ WRONG

\`\`\`text
Create a new feature for...
\`\`\`
```

### 3. New Chat = New Conversation File

**CRITICAL**: Each new AI chat session MUST create a NEW conversation log file.

#### Rules

- ✅ Each chat gets unique `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md`
- ✅ Each chat gets unique `ai-logs/yyyy/mm/dd/<chat-id>/summary.md`
- ❌ NEVER reuse or append to existing conversation files
- ❌ NEVER share conversation files across multiple chat sessions

#### Rationale

- Prevents cross-contamination between sessions
- Maintains clear provenance trail
- Enables proper context isolation
- Facilitates debugging and audit

## AI Provenance Metadata Requirements

### Required Fields (All 11)

Every AI-generated artifact MUST include:

```yaml
---
ai_generated: true # 1. Boolean flag
model: "<provider>/<model>@<version>" # 2. Underlying AI model
operator: "<github-username>" # 3. Who initiated the work
chat_id: "<unique-chat-identifier>" # 4. Chat session ID
prompt: | # 5. Exact prompt text
  <exact-prompt-text>
started: "<ISO8601-timestamp>" # 6. Start time
ended: "<ISO8601-timestamp>" # 7. End time
task_durations: # 8. Task breakdown
  - task: "<task-name>"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>" # 9. Total time
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md" # 10. Log path
source: "<source-identifier>" # 11. What created this file
---
```

### Source Field Values

The `source` field identifies what created the file:

- **User-created**: `"<github-username>"` (e.g., `"johnmillerATcodemag-com"`)
- **Prompt-generated**: `"<path-to-prompt-file>"` (e.g., `".github/prompts/create-prompt-instructions.prompt.md"`)
- **Meta-prompt-generated**: `"<path-to-meta-prompt-file>"` (e.g., `".github/prompts/meta/create-instruction-prompt.prompt.md"`)

### Optional Fields

```yaml
applyTo: "<glob-pattern>" # For instruction files - when to auto-apply
interface: "GitHub Copilot" # Optional: note the interface used
context: "<additional-context>" # Optional: extra provenance details
```

## Post-Creation Requirements

After creating or modifying ANY file, you MUST:

### 1. Update AI Conversation Log

Add to `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md`:

```markdown
**Artifacts Produced**:

- `<path-to-file>` - <Brief description>
```

### 2. Update or Create Summary

Ensure `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/summary.md` exists with:

- Session objectives
- Work completed
- Key decisions
- Artifacts produced
- Next steps
- Compliance status

**Resumability**: Summary MUST contain enough context for another developer to:

- Understand original objectives
- See what was accomplished
- Identify key decisions and rationale
- Locate all artifacts
- Resume incomplete work

### 3. Update README.md

Add appropriate entry to `README.md`:

**For meta-prompts**:

```markdown
### Meta-Prompts (Prompt Generators)

- [`.github/prompts/meta/<name>.prompt.md`](...) — <Description> ([chat log](...))
```

**For instruction files**:

```markdown
### Guidance & Instructions

- [`.github/instructions/<name>.instructions.md`](...) — <Description> ([chat log](...))
```

**For notable artifacts**:

```markdown
### Notable Artifacts

- **<Title>** ([`<path>`](...))
  - <Description>
  - Provenance: [Chat log](...)
```

## File Naming Conventions

### Instruction Files

- **Format**: `<domain>.instructions.md`
- **Examples**:
  - `create-prompt.instructions.md`
  - `api-documentation.instructions.md`
  - `test-authoring.instructions.md`

### Prompt Files

- **Format**: `<action>-<domain>.prompt.md`
- **Examples**:
  - `create-prompt-instructions.prompt.md`
  - `generate-api-docs.prompt.md`
  - `analyze-code-quality.prompt.md`

### Meta-Prompt Files

- **Location**: `.github/prompts/meta/`
- **Format**: `create-<domain>-prompt.prompt.md`
- **Examples**:
  - `create-instruction-prompt.prompt.md`
  - `create-analysis-prompt.prompt.md`

### AI Log Files

- **Structure**: `ai-logs/yyyy/mm/dd/<chat-id>/`
- **Required**: `conversation.md`, `summary.md`
- **Optional**: `artifacts/` (for files not committed elsewhere)

## Prompt File Structure

### YAML Front Matter (Required)

```yaml
---
mode: agent | chat # Execution mode
model: Auto (copilot) # Let Copilot choose
tools: ["create", "edit", "read"] # Available tools
description: <clear-description> # What the prompt does
prompt_metadata:
  id: <kebab-case-id> # Unique identifier
  title: <Title Case> # Human-readable title
  owner: <github-username> # Creator
  repository: <repo-name> # Repository
  version: <semver> # Version (e.g., 1.0.0)
  created: <YYYY-MM-DD> # Creation date
  updated: <YYYY-MM-DD> # Last update
  output_path: <path> # Where output goes
  category: <category> # Classification
  tags: [<tag1>, <tag2>] # Keywords
  output_format: markdown | json | yaml # Output format
---
```

### Markdown Content (Required)

```markdown
# <Prompt Title>

## Context

<What this prompt does and why>

**CRITICAL**: All AI-generated artifacts must comply with
`.github/instructions/ai-assisted-output.instructions.md`

## Requirements

<Specific requirements for the task>

## Deliverable

Generate `<output-path>` with:

## \`\`\`yaml

ai_generated: true
model: "<provider>/<model>@<version>"
operator: "<username>"
chat_id: "<chat-id>"
source: "<source-identifier>"

# ... all 11 required fields

---

\`\`\`

### Content

<Specific content requirements>
```

## Quality Checklist

Before completing any AI-assisted work:

- [ ] ✅ Model uses `<provider>/<model>@<version>` format (not interface)
- [ ] ✅ Operator is GitHub username (not "USER")
- [ ] ✅ Chat ID is unique to this session
- [ ] ✅ All 11 required metadata fields present
- [ ] ✅ Timestamps in ISO8601 format
- [ ] ✅ Task durations calculated
- [ ] ✅ Conversation log created/updated
- [ ] ✅ Summary file created/updated with resumability context
- [ ] ✅ README.md updated with artifact links
- [ ] ✅ New conversation file for new chat (not reused)
- [ ] ✅ Embedded YAML for Markdown (not sidecar files)
- [ ] ✅ All links use correct relative paths
- [ ] ✅ No sensitive data in logs or metadata

## Common Mistakes to Avoid

### ❌ Using Interface as Model

```yaml
model: "github/copilot@2025-10-15" # WRONG
```

**Fix**: Use underlying model

```yaml
model: "openai/gpt-4o@2024-11-20" # CORRECT
```

### ❌ Using "USER" in Conversation Logs

```markdown
[2025-10-15T14:30:00Z] USER # WRONG
```

**Fix**: Use GitHub username

```markdown
[2025-10-15T14:30:00Z] johnmillerATcodemag-com # CORRECT
```

### ❌ Reusing Conversation Files

```
ai-logs/2025/10/15/session-1/conversation.md
  (appending multiple chats here)  # WRONG
```

**Fix**: New chat = new file

```
ai-logs/2025/10/15/chat-abc123/conversation.md
ai-logs/2025/10/15/chat-def456/conversation.md  # CORRECT
```

### ❌ Incomplete Summary

```markdown
## Summary

Created some files. # WRONG - not resumable
```

**Fix**: Include complete context

```markdown
## Summary

Created prompt authoring instructions with:

- Objective: Establish prompt standards
- Deliverables: instruction file + templates
- Key Decision: Use embedded metadata (rationale: version control)
- Next: Add validation CI checks
```

## Reference Files

For complete requirements, see:

- **AI Provenance Policy**: `.github/instructions/ai-assisted-output.instructions.md`
- **Prompt Authoring**: `.github/instructions/create-prompt.instructions.md`
- **Instruction Prompt Requirements**: `.github/instructions/instruction-prompt-requirements.instructions.md`

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-15
**Maintainer**: AI-Assisted Development Team
**Compliance**: `.github/instructions/ai-assisted-output.instructions.md`
