---
ai_generated: true
model: "openai/gpt-4o@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "create-marp-slides-instructions-<timestamp>"
prompt: |
  Create instructions and templates for producing Marp slide files for this
  repository. Slides must be placed in Slides/individual-slides and every
  generated slide file must include AI provenance metadata that conforms to
  `.github/instructions/ai-assisted-output.instructions.md` and follow
  Copilot guidance in `.github/instructions/copilot-instructions.md`.
started: "<auto>"
ended: "<auto>"
task_durations:
  - task: "authoring"
    duration: "00:00:00"
total_duration: "00:00:00"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/create-marp-slides-instructions-<timestamp>/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "Slides/individual-slides/**"
---

# Create Marp Slides Instructions

Purpose: guidance, templates and required metadata for creating Marp (Markdown) slides
for this repository. Generated slides should be placed under `Slides/individual-slides`.

These instructions ensure every AI-assisted slide file includes the required
provenance metadata defined in `.github/instructions/ai-assisted-output.instructions.md`
and follows the Copilot-specific rules in `.github/instructions/copilot-instructions.md`.

## Where to put slides

- All Marp slide files must be created in: `Slides/individual-slides/`
- Filenames should be lowercase and kebab-case, e.g. `intro-to-aiasd.md`.

## Required front matter (template)

Every generated Marp Markdown slide file MUST start with embedded YAML front matter
that includes the AI provenance metadata. Use the template below and fill in the
values exactly as produced by the chat that generated the file.

```yaml
---
ai_generated: true
model: "<provider>/<model-name>@<version>"
operator: "<github-username>"
chat_id: "<chat-id>"
prompt: |
  <exact prompt text used to generate this slide file>
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

Notes:

- `ai_generated` must be boolean true.
- `model` must identify the underlying AI model in the format `provider/model@version`.
- `operator` must be the GitHub username (not the literal `USER`).
- `chat_id` and `ai_log` must point to the conversation log created for the chat that produced the file.
- Do not use sidecar `.meta.md` files for Markdown: embed YAML front matter.

## Marp slide skeleton (example)

After the front matter, add Marp directives and slide content. Minimal example:

```markdown
---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "john-doe"
chat_id: "a1b2c3d4"
prompt: |
  Draft a 5-slide introduction to the AI-Assisted Software Development course.
started: "2025-10-15T14:30:00Z"
ended: "2025-10-15T14:35:00Z"
task_durations:
  - task: "draft"
    duration: "00:03:00"
total_duration: "00:03:00"
ai_log: "ai-logs/2025/10/15/a1b2c3d4/conversation.md"
source: "johnmillerATcodemag-com"
---

<!-- slide: data-background-color="#ffffff" -->

# AI-Assisted Software Development

Welcome to the course. Use Marp features (--- for new slide) below.

---

## Slide 2: Goals

- Understand provenance
- Learn tools and patterns

---

<!-- Additional slides -->
```

## Authoring rules and checklist

Before committing or generating slides, ensure:

- [ ] The file is created under `Slides/individual-slides/`.
- [ ] YAML front matter includes all required fields from the template above.
- [ ] `ai_log` path exists in the repository under `ai-logs/` and contains `conversation.md` for the chat.
- [ ] `operator` is a GitHub username.
- [ ] Prompt is captured verbatim in the `prompt` field.
- [ ] Timestamps use ISO8601.
- [ ] README.md updated with an entry for notable AI-generated slides where applicable.

## Copilot-specific guidance

Follow the rules in `.github/instructions/copilot-instructions.md` when generating
slides via Copilot (model identification, chat scoping, new conversation file per chat,
and operator naming). In particular:

- Use the underlying model name in `model` (do not use `github/copilot`).
- Each new chat must create a new `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` and `summary.md`.
- Do not create AI-generated artifacts without an active chat context.

## README update requirement

When creating a notable slide deck or single slide intended for long-term use,
add a one-line bullet in the repo `README.md` under a `Guidance & Instructions` or
`Notable Artifacts` section that links to the slide file and the corresponding
`ai_log` chat folder.

Example README entry:

- **AIASD Intro Slides** (`Slides/individual-slides/aiasd-intro.md`) — 5-slide intro to the course. Provenance: `ai-logs/2025/10/15/<chat-id>/`.

## Examples and templates

Include common patterns or helper snippets here (e.g., slide with speaker notes,
code block slides, image inclusion). Keep examples short and focused.

## CI and enforcement suggestions (optional)

Teams may add a CI job to verify front matter on changed Markdown files. The
existing `.github/instructions/ai-assisted-output.instructions.md` contains a
Linux/Mac example; adapt it for PowerShell or the project's CI runner to enforce
that files with `ai_generated: true` include `chat_id` and `ai_log` and that
the referenced `ai_log` path exists.

## Next steps

- If you'd like, I can add a sample slide file in `Slides/individual-slides/` and
  a small PowerShell-based CI validation script to this repo.
