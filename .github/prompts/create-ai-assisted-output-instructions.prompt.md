---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "create"]
description: Generates repository guidelines for AI-assisted outputs, including provenance metadata requirements and an AI chat logging workflow
prompt_metadata:
  id: create-ai-assisted-output-instructions
  title: Generate AI-Assisted Output Instructions (Markdown)
  owner: johnmillerATcodemag-com
  repository: zeus.academia.3
  version: 1.0.0
  created: 2025-10-14
  updated: 2025-10-14
  output_path: .github/instructions/ai-assisted-output.instructions.md
  category: documentation
  tags: [ai, provenance, logging, governance]
  output_format: markdown
---

# Generate AI-Assisted Output Instructions (Markdown)

You are an expert technical writer. Create a clear, actionable instruction file (Markdown) that contributors must follow whenever they generate AI-assisted output for this repository.

## Output requirements

- Create or overwrite the file at: `.github/instructions/ai-assisted-output.instructions.md`.
- Format strictly as Markdown with headings and lists.
- Include a short introduction on why provenance and logging matter.
- Provide a table of contents matching the current structure (include all top-level headings, including "Overview").
- Include a "Before You Start (Mandatory)" section that emphasizes automatic Copilot chat management with specific implementation details for Copilot.
- In the AI chat logging workflow, emphasize Copilot-integrated chat management as the preferred approach with automatic scaffolding.
- Update the conversation.md template to include a "Context" section (Inputs, Targets, Constraints) and require listing "Artifacts produced" and "Next steps" when closing a work burst.
- Explicitly forbid sidecar `.meta.md` files for Markdown (or other formats that support embedded front matter); require embedded YAML for those.
- Add a "PR and Commit Checklist (Mandatory)" section with checkboxes.
- Add "GitHub Copilot Implementation Requirements" section with technical specifications including TypeScript interfaces, error handling, and integration points.
- Include "Non-Compliance and Remediation" section.
- Ensure consistent terminology: use "chat ID" in prose and `chat_id` in metadata/front matter; do not use "session" or "session-id" in paths or labels. All examples and paths should standardize on `<chat-id>`.
- Include an "Enforcement (CI)" subsection with a minimal GitHub Actions example (or clear steps) that blocks PRs when AI artifacts are missing `ai_log` or when the referenced log path does not exist. Add a note about bash compatibility and alternatives for Windows/other platforms. Clarify that the example validates Markdown files and suggest extending to other file types.
- State the sidecar prohibition once in a canonical "Metadata placement policy" section and use brief cross-references with inline context (e.g., "For non-embeddable formats, use sidecar files - see Metadata placement policy") to balance brevity with clarity.

## Audience

- Contributors generating or curating AI-assisted content (code, docs, diagrams, tests, data).

## Scope

- Define what metadata must be captured with each AI-assisted artifact.
- Define the logging workflow for conversational context and outputs.
- Provide a template and a quality checklist.
- Require updating the top-level README.md with a brief entry whenever this process generates a new file (what it is, where it lives, and a one-line purpose), including a link to the new artifact.
- Provide enforcement patterns that make session scaffolding a prerequisite and block PRs until ai-logs linkage exists.
- Include specific "Before You Start" requirements that emphasize automatic chat management, context-aware logging, and artifact protection.
- Address bootstrap scenarios: how the policy applies to legacy artifacts created before adoption, and whether policy/instruction files themselves require AI provenance metadata when manually authored.

## Required provenance metadata (for every AI-assisted artifact)

Authors must attach or embed the following metadata near the top of the artifact or in an adjacent `.meta.md` file with the same basename:

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

If the artifact cannot embed front matter, create a sidecar file named `<artifact>.meta.md` with the above content.

**Note**: In YAML front matter, use the boolean value `true` for `ai_generated` rather than the string "Yes". The list above shows conceptual fields; adapt the format to match YAML conventions when embedding.

## Before You Start (Mandatory) Section Requirements

The "Before You Start" section should emphasize automatic Copilot chat management and include:

**⚠️ AUTOMATIC CHAT MANAGEMENT**: GitHub Copilot should automatically manage AI chats and their provenance:

1. **New Chat = New Context**: Each new Copilot chat automatically creates a unique chat ID
2. **Context-Aware Logging**: The chat conversation IS the provenance log
3. **No Manual Setup Required**: Chat scaffolding happens automatically when artifacts are created
4. **Artifact Protection**: No AI-generated artifacts should be created without an active chat context

**For Copilot Implementation**:

- Generate chat ID at chat start: `<chat-id>` or `<timestamp-based-uuid>`
- Use chat conversation as the primary conversation log
- Auto-create `ai-logs/yyyy/mm/dd/<chat-id>/` structure when first artifact is generated
- Embed chat reference in all generated artifact metadata
- Prevent artifact creation if chat context is unavailable

## Standard Metadata Front Matter

**Copilot Auto-Generated Front Matter**:
GitHub Copilot should automatically embed this YAML front matter in all generated artifacts:

```yaml
---
ai_generated: true
model: "<auto-detected-model>"
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
# Auto-generated by GitHub Copilot Chat
---
```

For other file formats, adapt this structure using appropriate comment syntax.

## AI chat logging workflow

All AI chat transcripts and key outputs must be saved under `ai-logs/` in a date- and session-structured layout.

- Base folder: `ai-logs/`
- Structure: `ai-logs/yyyy/mm/dd/<chat-id>/`
- Required files per chat:
  - `conversation.md` — Full prompt/response transcript with timestamps
  - `summary.md` — Chat summary (goals, key decisions, outcomes)
  - `artifacts/` — Generated files not committed elsewhere

### Copilot-Integrated Chat Management

**Preferred Approach: Copilot Chat Context**:

When using GitHub Copilot, chat management should be automatic and context-aware:

**Copilot Chat Behavior**:

```yaml
# Copilot should automatically handle:
chat_id: "<copilot-chat-id>"
chat_start: "<chat-initialization-timestamp>"
conversation_log: "<entire-chat-transcript>"
auto_scaffolding: true # Create ai-logs structure on first artifact
artifact_protection: true # Prevent creation without chat context
```

**Implementation Requirements for Copilot**:

- **Chat ID**: Use Copilot's chat ID directly as the identifier
- **Automatic Scaffolding**: Create `ai-logs/yyyy/mm/dd/<chat-id>/` when first artifact is generated
- **Conversation Logging**: Export chat transcript to `conversation.md` automatically
- **Artifact Metadata**: Auto-populate chat ID reference in all generated files
- **Context Validation**: Block artifact creation if chat context is lost

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

[<timestamp>] USER

```text
<prompt text>
```

[<timestamp>] AI

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

## Provenance template for non-Markdown artifacts

When front matter isn’t applicable (e.g., images, binaries), create a sidecar: `<basename>.meta.md`.

```markdown
# AI-Assisted Artifact Metadata

- Artifact: <relative path>
- AI-Generated: Yes
- Model: <provider>/<model>@<version>
- Operator: <name>
- Prompt: |
  <exact prompt>
- Started: <ISO8601>
- Ended: <ISO8601>
- Task Durations:
  - <task>: <hh:mm:ss>
- Total Duration: <hh:mm:ss>
- Source Conversation Log: <relative path>

Note: Do not create sidecars for Markdown (or other formats that support embedded front matter); embed YAML front matter instead.
```

````

## Capturing task durations

- Record the start and end timestamps for each significant task (e.g., drafting, refactor, diagram generation, test updates).
- Compute each task duration and the overall total.
- If multiple tools are used, list each tool’s portion or note parallel execution.

## Placement and naming

- Place `ai-assisted-output.instructions.md` in `.github/instructions`.
- Place logs in `ai-logs/yyyy/mm/dd/<chat-id>/`.
- Prefer lowercase for artifact filenames; include context (e.g., `uc-001-enrollment-diagram.md`).
- **Notable artifacts** (documentation, architecture diagrams, major code modules, or any output intended for long-term reference) require README.md updates. When creating any new AI-assisted notable artifact, add a short bullet to the project `README.md` that links to the artifact and states its purpose. If a section like "AI-Assisted Artifacts" exists, add to it; otherwise, create one.
- Where appropriate, include a link from the README entry to the corresponding `ai_log` (chat folder) to improve traceability.
- Temporary or intermediate artifacts (e.g., draft notes, exploration scripts) do not require README entries but must still include full provenance metadata.

## Example Implementation

Provide a brief filled example showing a Markdown file with front matter, and a matching `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` header.

**Example Markdown file with front matter**:

```markdown
---
ai_generated: true
model: "openai/gpt-4@2024-05-13"
operator: "john-doe"
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
---

# User Registration Flow Diagram

This document describes the complete user registration process...
```

**Matching conversation log header**:

```markdown
# AI Conversation Log

- Chat ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
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

Note: Use "Chat ID:" (capitalized) in conversation log field labels, and "chat ID" (lowercase) in running prose.

## Quality Checklist

Before committing AI-assisted content, verify:

- [ ] **AI-Generated flag** set to `true`
- [ ] **Model information** includes provider, model name, and version
- [ ] **Operator identification** with full name or username
- [ ] **Exact prompt text** captured verbatim
- [ ] **Timestamps** present for start and end times
- [ ] **Task durations** recorded and total calculated
- [ ] **Conversation log** saved under `ai-logs/` structure
- [ ] **chat reference** included in artifact metadata
- [ ] **No sensitive data** exposed in prompts or outputs
- [ ] **Naming conventions** followed for files and paths
- [ ] **README.md updated** for new notable artifacts
- [ ] **Session scaffolded** before artifact creation
- [ ] **Embedded metadata** used for Markdown (no sidecar files)

## PR and Commit Checklist (Mandatory)

Before submitting pull requests containing AI-assisted content:

- [ ] **Chat log verified**: Confirm `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` exists
- [ ] **Artifact metadata complete**: Each artifact includes `ai_log` reference
- [ ] **README.md updated**: New artifacts documented with links and descriptions
- [ ] **No orphaned artifacts**: All AI-generated content traces back to a logged chat
- [ ] **Metadata format correct**: Embedded YAML for supported formats, sidecars only for binaries
- [ ] **Sensitive data check**: No credentials, keys, or private information in logs

Note: For detailed technical requirements on automatic chat management and metadata injection, see the "GitHub Copilot Implementation Requirements" section.

## GitHub Copilot Implementation Requirements

**For Copilot Integration**: This section defines the expected behavior for GitHub Copilot to automatically handle AI chat management and provenance tracking.

### Chat Lifecycle Management

**Chat Initialization**:

```typescript
interface CopilotChat {
  chatId: string; // Copilot's native chat identifier (serves as chat ID)
  startTimestamp: string; // ISO8601 format
  userId: string; // GitHub username or configured operator
  model: string; // Underlying AI model (e.g., "openai/gpt-4o@2024-11-20" or "anthropic/claude-3.5-sonnet@2024-10-22")
  conversationHistory: ChatMessage[];
  artifactsCreated: string[]; // Paths to generated files
}

type ChatMessage = {
  role: "user" | "assistant";
  content: string;
  timestamp: string; // ISO8601
};
```

**Automatic Behaviors**:

1. **Chat Identity**: Use Copilot's chat ID as the identifier (no separate ID needed)
2. **Context Persistence**: Maintain chat context throughout conversation lifecycle
3. **Lazy Scaffolding**: Create `ai-logs/yyyy/mm/dd/<chat-id>/` structure only when first artifact is generated
4. **Conversation Export**: Auto-save chat transcript to `conversation.md` on artifact creation
5. **Metadata Injection**: Automatically embed chat ID as chat reference in all generated files
6. **Artifact Protection**: Refuse to create files without active chat context

### File Generation Workflow

**Pre-Generation Checks**:

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

**Artifact Creation Process**:

1. **Validate Chat**: Ensure active chat exists
2. **Create Logs**: Scaffold `ai-logs` structure if first artifact (using chat ID)
3. **Generate Content**: Create the requested file/content
4. **Inject Metadata**: Add front matter with chat ID as chat reference
5. **Update Logs**: Export current conversation to `conversation.md`
6. **Track Artifacts**: Add file path to chat's artifact list

### Error Handling

**No Active Chat**:

```
❌ Cannot create AI-generated artifacts without an active chat.
💡 Please start a new Copilot chat or continue an existing conversation to generate files.
```

**Chat Context Lost**:

```
⚠️ Chat chat context appears to be lost.
🔄 Attempting to restore session or create new one...
```

**File Creation Blocked**:

```
🚫 Artifact creation blocked: Missing chat provenance
📋 This ensures all AI-generated content maintains proper audit trails
```

### Integration Points

**VS Code Extension**:

- Hook into chat lifecycle events
- Monitor file creation operations
- Inject metadata during file generation
- Maintain session state across editor restarts

**API Requirements**:

- Access to chat identifiers
- Ability to intercept file creation
- Conversation history export capabilities
- User/operator identification methods

### Chat ID Clarification

**Single Identifier Approach**: In the Copilot-integrated workflow, we use **only one identifier**:

- **Chat ID = Chat ID**: Copilot's native chat identifier serves as the chat ID
- **No Dual IDs**: We don't need separate `chat_session_id` and `session_id` fields
- **Simplified Metadata**: All artifacts reference the same chat ID consistently
- **Unified Logging**: The `ai-logs/yyyy/mm/dd/<chat-id>/` structure uses the chat ID directly

**Why This Design**:

- **Eliminates Confusion**: No need to map between chat IDs and chat IDs
- **Reduces Complexity**: One identifier to track throughout the entire workflow
- **Natural Alignment**: The chat conversation IS the session, so they should share the same ID
- **Simpler Implementation**: Fewer fields to populate and maintain

This approach eliminates manual chat management while ensuring 100% provenance coverage for AI-generated artifacts.

### Enforcement (CI)

Include a minimal CI enforcement pattern to block PRs until provenance is complete. For example, a GitHub Actions job that fails when:

- Any changed Markdown file contains `ai_generated: true` but is missing `ai_log` or `chat_id` in front matter
- The `ai_log` path does not exist relative to the repository

Provide either a YAML snippet or clear validation steps so teams can adopt this quickly.

**Important**: Add a note after the YAML example stating: "This example uses bash and is compatible with Linux/macOS runners. For Windows runners, adapt the script to PowerShell or use WSL. For non-GitHub CI systems, apply equivalent logic in your platform's scripting language."

Also clarify that:

- The provided example validates Markdown files with YAML front matter as a starting point
- Teams should extend the workflow to validate other file types (Python, JavaScript, etc.) using appropriate parsers for comment-based metadata
- README updates are typically verified during PR review rather than automated CI checks, though teams may extend the CI script to detect new AI-generated files and verify corresponding README entries if desired

## Non-Compliance and Remediation

- If missing logs or references, scaffold `ai-logs/` with `yyyy/mm/dd/<chat-id>/`, add front matter `ai_log` and `chat_id`, update README (and optionally link back to the session), then re-request review.
- For orphaned artifacts, create or reconstruct `conversation.md` from available history and update artifacts to reference it.
- For incomplete metadata, add missing required fields, timestamps, and task durations; verify operator and model details.

## Deliverable

Generate the complete `.github/instructions/ai-assisted-output.instructions.md` file with:

### Required AI Provenance Metadata (YAML Front Matter)

The file MUST begin with the following YAML front matter fields per `.github/instructions/ai-assisted-output.instructions.md`:

```yaml
---
ai_generated: true
model: "<provider>/<model-name>@<version>"  # e.g., "openai/gpt-4o@2024-11-20" or "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<operator-username>"
chat_id: "<chat-identifier>"
prompt: |
  <exact-prompt-text-from-this-execution>
started: "<ISO8601-timestamp>"
ended: "<ISO8601-timestamp>"
task_durations:
  - task: "<task-name>"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
---
```

**Important**: Use the underlying AI model (e.g., `"openai/gpt-4o@2024-11-20"`), not the interface (e.g., "github/copilot").

### Content Requirements

Following the metadata, include the final Markdown content for `.github/instructions/ai-assisted-output.instructions.md` with all sections and requirements specified above. Do not include commentary outside the document.
````
