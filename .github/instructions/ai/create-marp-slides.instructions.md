---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<github-username>"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of create-marp-slides.instructions.md with minimal tokens
started: "2025-10-23T04:37:00Z"
ended: "2025-10-23T04:37:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
applyTo: "Slides/individual-slides/**"
---

# AI Instructions: Create Marp Slides

Generate Marp slides in `Slides/individual-slides/` with required AI provenance metadata.

## File Location & Naming
- Path: `Slides/individual-slides/`
- Filename: lowercase kebab-case (e.g., `intro-to-aiasd.md`)

## Required YAML Front Matter

```yaml
---
ai_generated: true
model: "<provider>/<model-name>@<version>"
operator: "<github-username>"
chat_id: "<chat-id>"
prompt: |
  <exact prompt text>
started: "<ISO8601-timestamp>"
ended: "<ISO8601-timestamp>"
task_durations:
  - task: "draft"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
source: "<source-identifier>"
---
```

## Marp Slide Template

```markdown
---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "username"
chat_id: "unique-id"
prompt: |
  Create 5-slide intro to topic
started: "2025-10-23T14:30:00Z"
ended: "2025-10-23T14:35:00Z"
task_durations:
  - task: "draft"
    duration: "00:05:00"
total_duration: "00:05:00"
ai_log: "ai-logs/2025/10/23/unique-id/conversation.md"
source: "username"
---

# Slide Title

Content here

---

## Slide 2

- Bullet points
- More content

---
```

## Generation Rules

**Required**:
- Embed YAML front matter (no sidecar `.meta.md`)
- Use actual model name in format `provider/model@version`
- Create `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md`
- Capture exact prompt verbatim
- Use ISO8601 timestamps

**Prohibited**:
- Generic model names like "github/copilot"
- Creating slides without active chat context
- Omitting any required metadata fields

## Checklist
- [ ] File in `Slides/individual-slides/`
- [ ] All YAML fields present
- [ ] `ai_log` path exists with conversation.md
- [ ] `operator` is GitHub username
- [ ] Timestamps in ISO8601 format
- [ ] Update README.md for notable slides

## README Entry Template

```markdown
- **[Title]** (`Slides/individual-slides/[filename].md`) — [Description]. Provenance: `ai-logs/[yyyy]/[mm]/[dd]/[chat-id]/`
```

## Reference
See `.github/instructions/ai-assisted-output.instructions.md` for complete provenance requirements.
