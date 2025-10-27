---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "ai-assisted-output-policy-2025-10-15"
prompt: |
  Create comprehensive AI provenance and logging policy for all AI-assisted
  outputs in the repository, defining required metadata, workflow, and enforcement.
started: "2025-10-15T13:00:00Z"
ended: "2025-10-15T13:45:00Z"
task_durations:
  - task: "policy design"
    duration: "00:20:00"
  - task: "workflow specification"
    duration: "00:15:00"
  - task: "template creation"
    duration: "00:10:00"
total_duration: "00:45:00"
ai_log: "ai-logs/2025/10/15/ai-assisted-output-policy-2025-10-15/conversation.md"
source: ".github/prompts/create-ai-assisted-output-instructions.prompt.md"
applyTo: "**/*"
---

# AI-Assisted Output Instructions

## Overview

This repository requires clear provenance and reliable logging for all AI-assisted outputs. Provenance and logging protect code quality, enable audits, and help teammates understand how artifacts were produced (by whom, with what model, and from which conversation). This policy defines the required metadata, logging workflow, quality gates, and Copilot integration behaviors to make provenance automatic, consistent, and verifiable.

**For GitHub Copilot Users**: See [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) for comprehensive Copilot-specific guidance including model identification, conversation format, and quality checklists.

## Table of Contents

- [Overview](#overview)
- [Audience](#audience)
- [Scope](#scope)
- [Terminology](#terminology)
- [Metadata placement policy](#metadata-placement-policy)
- [Required provenance metadata (for every AI-assisted artifact)](#required-provenance-metadata-for-every-ai-assisted-artifact)
- [Before You Start (Mandatory)](#before-you-start-mandatory)
- [Standard Metadata Front Matter](#standard-metadata-front-matter)
- [AI chat logging workflow](#ai-chat-logging-workflow)
  - [Copilot-Integrated Chat Management](#copilot-integrated-chat-management)
  - [conversation.md Template](#conversationmd-template)
  - [summary.md Template](#summarymd-template)
- [Capturing task durations](#capturing-task-durations)
- [Placement and naming](#placement-and-naming)
- [Example Implementation](#example-implementation)
- [Quality Checklist](#quality-checklist)
- [PR and Commit Checklist (Mandatory)](#pr-and-commit-checklist-mandatory)
- [GitHub Copilot Implementation Requirements](#github-copilot-implementation-requirements)
  - [Chat Lifecycle Management](#chat-lifecycle-management)
  - [File Generation Workflow](#file-generation-workflow)
  - [Error Handling](#error-handling)
  - [Integration Points](#integration-points)
  - [Chat ID Clarification](#chat-id-clarification)
- [Enforcement (CI)](#enforcement-ci)
- [Non-Compliance and Remediation](#non-compliance-and-remediation)

## Audience

Contributors generating or curating AI-assisted content (code, docs, diagrams, tests, data).

## Scope

- Define what provenance metadata must be captured with each AI-assisted artifact.
- Define the logging workflow for conversational context and outputs.
- Provide a template and a quality checklist.
- Require updating the top-level README.md with a brief entry whenever this process generates a new file (what it is, where it lives, and a one-line purpose), including a link to the new artifact.
- Provide enforcement patterns that make chat scaffolding a prerequisite and block PRs until ai-log linkage exists.
- Emphasize automatic chat management, context-aware logging, and artifact protection before any artifact is created.

## Terminology

- Use “chat ID” in prose.
- Use `chat_id` in embedded metadata/front matter.
- Do not use “session” or “session-id” in paths or labels.
- Standardize placeholder paths on `<chat-id>`.

## Metadata placement policy

- For file formats that support embedded front matter (e.g., Markdown), provenance MUST be embedded as YAML front matter at the top of the artifact.
- For formats that do not support embedded front matter (images, binaries, etc.), create a sidecar file named `<artifact>.meta.md` containing the required metadata.
- Sidecars for Markdown (or any format supporting embedded front matter) are prohibited. Use embedded YAML front matter.
- Throughout this document, references to sidecars implicitly follow this policy; see “Metadata placement policy” for the canonical rule.

## Required provenance metadata (for every AI-assisted artifact)

**🔒 CANONICAL SOURCE**: This section is the single source of truth for AI provenance metadata requirements. Other instruction files should reference this section rather than duplicating it.

Authors must attach or embed the following metadata near the top of the artifact, following the [Metadata placement policy](#metadata-placement-policy):

Conceptual fields (map to YAML when embedding):

- AI-Generated: Yes
- Model: <model name and version>
- Operator: <full name or username>
- Prompt: <exact prompt text used>
- Started: <ISO8601 timestamp>
- Ended: <ISO8601 timestamp>
- Task Durations:
  - <Task 1 label>: <duration hh:mm:ss>
  - <Task 2 label>: <duration hh:mm:ss>
- Total Duration: <duration hh:mm:ss>
- Source Conversation Log: <relative path to AI log file>

Notes:

- In YAML front matter, use `ai_generated: true` (boolean) instead of the string “Yes”.
- If the artifact cannot embed front matter, create a sidecar `<artifact>.meta.md` with the same fields (see [Metadata placement policy](#metadata-placement-policy)).

## Before You Start (Mandatory)

⚠️ AUTOMATIC CHAT MANAGEMENT: GitHub Copilot should automatically manage AI chats and their provenance.

1. New Chat = New Context: Each new Copilot chat automatically creates a unique chat ID.
2. Context-Aware Logging: The chat conversation IS the provenance log.
3. No Manual Setup Required: Chat scaffolding happens automatically when artifacts are created.
4. Artifact Protection: No AI-generated artifacts should be created without an active chat context.

For Copilot Implementation:

- Generate chat ID at chat start: `<chat-id>` or `<timestamp-based-uuid>`.
- Use the chat conversation as the primary conversation log.
- Auto-create `ai-logs/yyyy/mm/dd/<chat-id>/` structure when the first artifact is generated.
- Embed chat reference in all generated artifact metadata.
- Prevent artifact creation if chat context is unavailable.

## Standard Metadata Front Matter

Copilot Auto-Generated Front Matter (required for formats that support embedded YAML):

```yaml
---
ai_generated: true
model: "<provider>/<model-name>@<version>" # e.g., "openai/gpt-4o@2024-11-20" or "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<github-username-or-config>"
chat_id: "<copilot-chat-id>"
prompt: |
  <exact-user-prompt-from-chat>
started: "<auto-timestamp-when-generation-started>"
ended: "<auto-timestamp-when-generation-completed>"
task_durations:
  - task: "<auto-detected-task-type>"
    duration: "<calculated-duration>"
total_duration: "<total-generation-time>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<copilot-chat-id>/conversation.md"
source: "<source-identifier>" # Who/what created this file: username, prompt path, or meta-prompt path
# Auto-generated by <interface-used> powered by <underlying-model>
---
```

**Important Model Format Requirements**:

- Use the **underlying AI model** that actually generated the content, not just the interface
- Format: `"<provider>/<model-name>@<version>"`
- Examples:
  - `"openai/gpt-4o@2024-11-20"` - If using GPT-4o (via Copilot, API, or ChatGPT)
  - `"openai/gpt-4-turbo@2024-04-09"` - If using GPT-4 Turbo
  - `"openai/o1@2024-12-17"` - If using o1 reasoning model (stable)
  - `"anthropic/claude-3.5-sonnet@2024-10-22"` - If using Claude 3.5 Sonnet
  - `"anthropic/claude-3-opus@2024-02-29"` - If using Claude 3 Opus
  - `"google/gemini-1.5-pro@2024-02"` - If using Gemini Pro
- The interface (GitHub Copilot, Cursor, etc.) should be noted in comments if relevant
- If the exact model version is unknown, use best available information (e.g., `"openai/gpt-4o@unknown"`)

For other file formats, adapt the structure using appropriate comment syntax; for non-embeddable formats, see [Metadata placement policy](#metadata-placement-policy).

## AI chat logging workflow

**🔒 CANONICAL SOURCE**: This section is the single source of truth for the AI chat logging workflow and post-creation requirements. Other instruction files should reference this section rather than duplicating it.

All AI chat transcripts and key outputs must be saved under `ai-logs/` in a date- and chat-structured layout.

**CRITICAL**: Each new AI chat MUST create a NEW conversation log file. Do NOT reuse or append to existing conversation files from previous chats.

- Base folder: `ai-logs/`
- Structure: `ai-logs/yyyy/mm/dd/<chat-id>/`
- Required files per chat:
  - `conversation.md` — Full prompt/response transcript with timestamps (REQUIRED)
  - `summary.md` — Session summary: objectives, key decisions, artifacts, outcomes (REQUIRED)
  - `artifacts/` — Generated files not committed elsewhere (OPTIONAL)

### Copilot-Integrated Chat Management

Preferred Approach: Copilot Chat Context

Copilot Chat Behavior:

```yaml
# Copilot should automatically handle:
chat_id: "<copilot-chat-id>"
chat_start: "<chat-initialization-timestamp>"
conversation_log: "<entire-chat-transcript>"
auto_scaffolding: true # Create ai-logs structure on first artifact
artifact_protection: true # Prevent creation without chat context
```

Implementation Requirements for Copilot:

- Chat ID: Use Copilot’s chat ID directly as the identifier.
- Automatic Scaffolding: Create `ai-logs/yyyy/mm/dd/<chat-id>/` when the first artifact is generated.
- Conversation Logging: Export chat transcript to `conversation.md` automatically.
- Artifact Metadata: Auto-populate chat ID reference in all generated files.
- Context Validation: Block artifact creation if chat context is lost.

### conversation.md Template

````markdown
# AI Conversation Log

- Chat ID: <uuid or slug>
- Operator: <name>
- Model: <provider>/<model>@<version>
- Started: <ISO8601>
- Ended: <ISO8601>
- Total Duration: <hh:mm:ss>

## Context

- Inputs: <source files, requirements, constraints>
- Targets: <intended output files and deliverables>
- Constraints/Policies: <links to relevant guidelines or policies>

## Exchanges

### Exchange 1

[<timestamp>] <operator-username>

```text
<prompt text>
```

[<timestamp>] <provider>/<model-name>@<version>

```text
<response excerpt or full>
```

### Exchange 2

<!-- Repeat for each exchange -->

## Work Burst Closure

**Artifacts Produced**:

- `<artifact-path>` - <brief description>
- `<artifact-path>` - <brief description>

**Next Steps**:

- [ ] <action item>
- [ ] <action item>

**Duration Summary**:

- <task>: <hh:mm:ss>
- Total: <hh:mm:ss>
````

### summary.md Template

````markdown
# Session Summary: <Session Title>

**Session ID**: <chat-id>
**Date**: <YYYY-MM-DD>
**Operator**: <username>
**Model**: <provider>/<model>@<version>
**Duration**: <hh:mm:ss>

## Objective

<Clear statement of what the chat aimed to accomplish>

## Work Completed

### Primary Deliverables

1. **<Artifact Name>** (`<path>`)

   - <Description of artifact>
   - <Key features or sections>
   - <Purpose or use case>

2. **<Artifact Name>** (`<path>`)
   - <Description>

### Secondary Work

- <Supporting changes or updates>
- <Refactoring or cleanup>
- <Documentation updates>

## Key Decisions

### <Decision Title>

**Decision**: <What was decided>
**Rationale**:

- <Reason 1>
- <Reason 2>
- <Impact or benefit>

### <Decision Title>

**Decision**: <What was decided>
**Rationale**: <Why this approach was chosen>

## Artifacts Produced

| Artifact | Type   | Purpose         |
| -------- | ------ | --------------- |
| `<path>` | <type> | <brief purpose> |
| `<path>` | <type> | <brief purpose> |

## Lessons Learned

1. **<Lesson>**: <Description or insight gained>
2. **<Lesson>**: <What was discovered or learned>
3. **<Lesson>**: <Best practice identified>

## Next Steps

### Immediate

- <Action item for immediate follow-up>
- <Next task or verification needed>

### Future Enhancements

- <Potential improvement or extension>
- <Ideas for future work>

## Compliance Status

✅ <Compliance item completed>
✅ <Compliance item completed>
⚠️ <Partial compliance or known gap>
❌ <Non-compliant item requiring attention>

## Chat Metadata

```yaml
chat_id: <chat-id>
started: <ISO8601-timestamp>
ended: <ISO8601-timestamp>
total_duration: <hh:mm:ss>
operator: <username>
model: <provider>/<model>@<version>
artifacts_count: <number>
files_modified: <number>
<custom_metric>: <value>
```

---

**Summary Version**: 1.0.0
**Created**: <ISO8601-timestamp>
**Format**: Markdown
````

**Note**: The summary.md file should be created at the end of each AI-assisted chat and saved alongside conversation.md. It provides a high-level overview for quick reference without reading the full conversation transcript.

**Resumability Requirements**: The summary MUST contain sufficient context for another developer (or the same developer at a later time) to:

1. Understand the original objective and scope
2. See what was accomplished and what remains
3. Identify key decisions and their rationale
4. Locate all artifacts and understand their purposes
5. Know what files were modified and why
6. Resume work on incomplete items without re-reading the full conversation

Include enough detail that someone unfamiliar with the chat can understand the "why" behind decisions, not just the "what" of artifacts created.## Capturing task durations

- Record the start and end timestamps for each significant task (e.g., drafting, refactor, diagram generation, test updates).
- Compute each task duration and the overall total.
- If multiple tools are used, list each tool’s portion or note parallel execution.

## Placement and naming

- Place this file at `.github/instructions/ai-assisted-output.instructions.md`.
- Place logs in `ai-logs/yyyy/mm/dd/<chat-id>/`.
- Prefer lowercase for artifact filenames; include context (e.g., `uc-001-enrollment-diagram.md`).
- When creating any new AI-assisted artifact, add a short bullet to the project `README.md` that links to the artifact and states its purpose. If a section like “AI-Assisted Artifacts” exists, add to it; otherwise, create one.
- Where appropriate, include a link from the README entry to the corresponding `ai_log` (chat folder) to improve traceability.

Notable artifacts include documentation, architecture diagrams, major code modules, or any output intended for long-term reference. Temporary or intermediate artifacts (e.g., draft notes, exploration scripts) do not require README entries but must still include full provenance metadata.

## Example Implementation

Example Markdown file with front matter:

```markdown
---
ai_generated: true
model: "openai/gpt-4@2024-05-13"
operator: "john-doe"
chat_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
prompt: |
  Create a user registration flow diagram showing the complete process
  from initial signup through email verification and profile completion.
started: "2024-10-15T14:30:00Z"
ended: "2024-10-15T14:45:30Z"
task_durations:
  - task: "requirement analysis"
    duration: "00:05:00"
  - task: "diagram creation"
    duration: "00:08:15"
  - task: "review and refinement"
    duration: "00:02:15"
total_duration: "00:15:30"
ai_log: "ai-logs/2024/10/15/a1b2c3d4-e5f6-7890-abcd-ef1234567890/conversation.md"
source: "johnmillerATcodemag-com"
---

# User Registration Flow Diagram

This document describes the complete user registration process...
```

Matching conversation log header:

```markdown
# AI Conversation Log

- chat ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
- Operator: john-doe
- Model: openai/gpt-4@2024-05-13
- Started: 2024-10-15T14:30:00Z
- Ended: 2024-10-15T14:45:30Z
- Total Duration: 00:15:30

## Context

- Inputs: user-requirements.md, existing-auth-flow.md
- Targets: user-registration-flow-diagram.md
- Constraints/Policies: .github/instructions/ai-assisted-output.instructions.md
```

## Quality Checklist

Before committing AI-assisted content, verify:

- [ ] AI-Generated flag set to `true`
- [ ] Model information includes provider, model name, and version
- [ ] Operator identification with full name or username
- [ ] Exact prompt text captured verbatim
- [ ] Timestamps present for start and end times
- [ ] Task durations recorded and total calculated
- [ ] Conversation log saved under `ai-logs/` structure
- [ ] Summary file created: `ai-logs/yyyy/mm/dd/<chat-id>/summary.md`
- [ ] chat reference included in artifact metadata (`chat_id` and `ai_log`)
- [ ] No sensitive data exposed in prompts or outputs
- [ ] Naming conventions followed for files and paths
- [ ] README.md updated for new notable artifacts
- [ ] Chat scaffolding in place before artifact creation
- [ ] Embedded metadata used for Markdown (no sidecar files; see “Metadata placement policy”)

## PR and Commit Checklist (Mandatory)

Before submitting pull requests containing AI-assisted content:

- [ ] Chat log verified: `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` exists
- [ ] Chat summary verified: `ai-logs/yyyy/mm/dd/<chat-id>/summary.md` exists
- [ ] Artifact metadata complete: Each artifact includes `chat_id` and `ai_log`
- [ ] README.md updated: New artifacts documented with links and descriptions
- [ ] No orphaned artifacts: All AI-generated content traces back to a logged chat
- [ ] Metadata format correct: Embedded YAML for supported formats, sidecars only for binaries (see “Metadata placement policy”)
- [ ] Sensitive data check: No credentials, keys, or private information in logs

## GitHub Copilot Implementation Requirements

For Copilot Integration: This section defines the expected behavior for GitHub Copilot to automatically handle AI chat management and provenance tracking.

### Chat Lifecycle Management

Chat Initialization:

```typescript
interface CopilotChat {
  chatId: string; // Copilot's native chat identifier (serves as chat ID)
  startTimestamp: string; // ISO8601 format
  userId: string; // GitHub username or configured operator
  model: string; // Auto-detected model (e.g., "github/copilot@2024-10-15")
  conversationHistory: ChatMessage[];
  artifactsCreated: string[]; // Paths to generated files
}

type ChatMessage = {
  role: "user" | "assistant";
  content: string;
  timestamp: string; // ISO8601
};
```

Automatic Behaviors:

1. Chat Identity: Use Copilot’s chat ID as the identifier (no separate ID needed).
2. Context Persistence: Maintain chat context throughout conversation lifecycle.
3. Lazy Scaffolding: Create `ai-logs/yyyy/mm/dd/<chat-id>/` structure only when the first artifact is generated.
4. Conversation Export: Auto-save chat transcript to `conversation.md` on artifact creation.
5. Summary Generation: Auto-generate `summary.md` at chat end or on demand with objectives, decisions, and outcomes.
6. Metadata Injection: Automatically embed chat ID as `chat_id` and include `ai_log` in all generated files.
7. Artifact Protection: Refuse to create files without active chat context.

### File Generation Workflow

Pre-Generation Checks:

```typescript
function validateChatContext(): boolean {
  if (!currentChat?.chatId) {
    displayError("Cannot create artifacts without active chat");
    return false;
  }
  return true;
}

function displayError(message: string): void {
  // Implementation-specific: surface in VS Code notifications and logs
}
```

Artifact Creation Process:

1. Validate Chat: Ensure active chat exists.
2. Create Logs: Scaffold `ai-logs` structure if first artifact (using chat ID).
3. Generate Content: Create the requested file/content.
4. Inject Metadata: Add front matter with `chat_id` and `ai_log`.
5. Update Logs: Export current conversation to `conversation.md`.
6. Generate Summary: Create or update `summary.md` with chat overview.
7. Track Artifacts: Add the file path to the chat's artifact list.

### Error Handling

No Active Chat:

```
❌ Cannot create AI-generated artifacts without an active chat.
💡 Please start a new Copilot chat or continue an existing conversation to generate files.
```

Chat Context Lost:

```
⚠️ Chat context appears to be lost.
🔄 Attempting to restore context or create a new chat...
```

File Creation Blocked:

```
🚫 Artifact creation blocked: Missing chat provenance.
📋 This ensures all AI-generated content maintains proper audit trails.
```

### Integration Points

VS Code Extension:

- Hook into chat lifecycle events.
- Monitor file creation operations.
- Inject metadata during file generation.
- Maintain chat state across editor restarts.

API Requirements:

- Access to chat identifiers.
- Ability to intercept file creation.
- Conversation history export capabilities.
- User/operator identification methods.

### Chat ID Clarification

Single Identifier Approach: In the Copilot-integrated workflow, we use only one identifier.

- Chat ID = Copilot chat ID: Copilot’s native chat identifier serves as the chat ID.
- No Dual IDs: Do not create separate `chat_session_id` or similar.
- Simplified Metadata: All artifacts reference the same chat ID consistently (`chat_id` field).
- Unified Logging: The `ai-logs/yyyy/mm/dd/<chat-id>/` structure uses the chat ID directly.

Why This Design:

- Eliminates confusion (no mapping between multiple IDs).
- Reduces complexity (one identifier to track end-to-end).
- Natural alignment (the chat conversation is the context).
- Simpler implementation (fewer fields to populate and maintain).

## Enforcement (CI)

This repository should block PRs when provenance is incomplete. The minimal GitHub Actions job below fails when:

- Any changed Markdown file contains `ai_generated: true` but is missing `ai_log` or `chat_id` in front matter
- The `ai_log` path does not exist in the repository

Example (Linux/macOS runner using bash):

```yaml
name: Verify AI Provenance
on:
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  verify-provenance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Determine changed Markdown files
        run: |
          git fetch --no-tags --prune --depth=1 origin +refs/heads/*:refs/remotes/origin/*
          CHANGED=$(git diff --name-only --diff-filter=ACMRT "origin/${{ github.base_ref }}...HEAD" | grep -E '\\.md$' || true)
          echo "$CHANGED" > changed_md.txt

      - name: Validate front matter and ai-logs linkage
        run: |
          set -euo pipefail
          rc=0
          while IFS= read -r f; do
            [ -z "$f" ] && continue
            [ ! -f "$f" ] && continue

            # Extract YAML front matter
            awk '
              BEGIN{in=0; n=0}
              /^---[[:space:]]*$/ { n++; if (n==1) {in=1; next} else if (n==2) {in=0; exit} }
              in { print }
            ' "$f" > fm.yml || true

            # Only enforce when ai_generated: true
            if grep -qiE '^ai_generated:[[:space:]]*true[[:space:]]*$' fm.yml; then
              # Require chat_id and ai_log
              if ! grep -qE '^chat_id:' fm.yml; then
                echo "::error file=$f::Missing 'chat_id' in front matter"
                rc=1
              fi
              if ! grep -qE '^ai_log:' fm.yml; then
                echo "::error file=$f::Missing 'ai_log' in front matter"
                rc=1
              else
                # Verify the referenced ai_log path exists
                ai_log=$(awk -F':' '/^ai_log:[[:space:]]*/{sub(/^[[:space:]]*/,"",$2); print $2}' fm.yml | sed 's/^ *//; s/^"//; s/"$//')
                if [ -z "$ai_log" ] || [ ! -f "$ai_log" ]; then
                  echo "::error file=$f::ai_log path missing or not found: $ai_log"
                  rc=1
                fi
              fi
            fi
            rm -f fm.yml || true
          done < changed_md.txt
          exit $rc
```

Note: This example uses bash and is compatible with Linux/macOS runners. For Windows runners, adapt the script to PowerShell or use WSL. For non-GitHub CI systems, apply equivalent logic in your platform’s scripting language. README updates are typically verified during PR review rather than automated CI checks (teams may extend CI to detect new AI-generated files and verify corresponding README entries if desired).

## Non-Compliance and Remediation

- Missing logs or references: Scaffold `ai-logs/yyyy/mm/dd/<chat-id>/`, add front matter `ai_log` and `chat_id`, update README (optionally link back to the chat folder), then re-request review.
- Orphaned artifacts: Create or reconstruct `conversation.md` from available history and update artifacts to reference it.
- Incomplete metadata: Add missing required fields, timestamps, and task durations; verify operator and model details.
- Sidecar misuse: If a sidecar is used where embedded front matter is supported (e.g., Markdown), move the metadata into embedded YAML and remove the sidecar (see [Metadata placement policy](#metadata-placement-policy)).
