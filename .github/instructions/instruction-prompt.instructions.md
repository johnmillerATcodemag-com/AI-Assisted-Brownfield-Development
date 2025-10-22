---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Create an instruction file that ensures all instruction-generating prompts
  include AI provenance requirements in their deliverable sections.
started: "2025-10-15T15:20:00Z"
ended: "2025-10-15T15:30:00Z"
task_durations:
  - task: "instruction design"
    duration: "00:08:00"
  - task: "template creation"
    duration: "00:02:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: ".github/prompts/meta/create-instruction-file-instructions.prompt.md"
applyTo: "**/*.instructions.prompt.md"
---

# Instruction Prompt Requirements

This file provides mandatory requirements for all prompt files that generate instruction files (i.e., prompts that create `*.instructions.md` files).

**Important**: Follow [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) for model format, conversation logging, and quality requirements.

## Applies To

All prompt files matching pattern: `**/*.instructions.prompt.md`

## Purpose

Ensures that all instruction-generating prompts produce compliant output files with complete AI provenance metadata as required by `.github/instructions/ai-assisted-output.instructions.md`.

## Mandatory Requirements

### 1. Context Section Must Reference AI Policy

Every instruction-generating prompt MUST include this in its Context section:

```markdown
## Context

<domain-specific context>

**CRITICAL**: All AI-generated artifacts in this repository MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`. The generated
instruction file MUST include full AI provenance metadata as specified in that policy.
```

### 2. Deliverable Section Must Include AI Provenance Template

Every instruction-generating prompt MUST include this exact structure in its Deliverable section:

```markdown
## Deliverable

Generate the complete `<output-path>` file with:

### Required AI Provenance Metadata (YAML Front Matter)

The file MUST begin with the following YAML front matter fields per
`.github/instructions/ai-assisted-output.instructions.md`:

## \`\`\`yaml

ai_generated: true
model: "<model-name-and-version>"
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
  applyTo: "<apply-to-pattern>" # Optional, based on instruction type

---

\`\`\`

### Content Requirements

Following the metadata, include:
<specific content requirements for the instruction file>
```

### 3. Required Front Matter Fields

All instruction-generating prompts should have:

```yaml
prompt_metadata:
  id: create-<domain>-instructions
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  output_format: markdown
```

## Complete Example Template

Here's a complete example of a compliant instruction-generating prompt:

```markdown
---
mode: agent
model: Auto (copilot)
tools: ["create"]
description: Generates <domain> authoring guidelines for contributors
prompt_metadata:
  id: create-<domain>-instructions
  title: Generate <Domain> Instructions (Markdown)
  owner: <author-username>
  repository: AI-Assisted-Brownfield-Development
  version: 1.0.0
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  tags: [<domain>, documentation, authoring-guidelines]
  output_format: markdown
---

# Generate <Domain> Instructions

Create comprehensive guidelines for <domain> following repository standards.

## Context

<Domain-specific context and background>

**CRITICAL**: All AI-generated artifacts in this repository MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`. The generated
instruction file MUST include full AI provenance metadata as specified in that policy.

## Target Audience

<Who will use these instructions>

## Requirements

<Detailed requirements for instruction content>

## Deliverable

Generate the complete `.github/instructions/<domain>.instructions.md` file with:

### Required AI Provenance Metadata (YAML Front Matter)

The file MUST begin with the following YAML front matter fields per
`.github/instructions/ai-assisted-output.instructions.md`:

## \`\`\`yaml

ai_generated: true
model: "<model-name-and-version>"
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
  applyTo: "<pattern>" # Optional

---

\`\`\`

### Content Requirements

Following the metadata, include:

1. Complete <domain> instructions
2. Templates and examples
3. Best practices and common pitfalls
```

## Validation Checklist

Before creating or modifying an instruction-generating prompt, verify:

- [ ] **Context references AI policy**: Includes statement about `.github/instructions/ai-assisted-output.instructions.md` compliance
- [ ] **Deliverable includes provenance template**: Shows complete YAML front matter structure with all 10 required fields
- [ ] **Output path is correct**: Points to `.github/instructions/<name>.instructions.md`
- [ ] **Category is 'documentation'**: Instruction files are documentation
- [ ] **Output format is 'markdown'**: Instruction files are Markdown
- [ ] **ID follows convention**: Uses `create-<domain>-instructions` pattern

## Common Mistakes to Avoid

❌ **Missing AI provenance section** in Deliverable

- Fix: Add complete YAML front matter template

❌ **Not referencing AI policy** in Context

- Fix: Add CRITICAL statement about compliance

❌ **Vague deliverable requirements**

- Fix: Be explicit about required metadata fields

❌ **Forgetting applyTo field** when applicable

- Fix: Include `applyTo` in template if instruction file should apply to specific patterns

## How to Create a New Instruction-Generating Prompt

### Option 1: Use the Meta-Prompt (Recommended)

Execute the meta-prompt generator:

```
Submit .github/prompts/meta/create-instruction-prompt.prompt.md
```

Provide domain information when prompted.

### Option 2: Manual Creation

1. Copy an existing instruction prompt as template
2. Update all domain-specific content
3. Ensure Context section references AI policy
4. Ensure Deliverable section includes provenance template
5. Validate against checklist above

## Enforcement

This requirement is enforced through:

1. **Documentation**: This instruction file (applies to `**/*.instructions.prompt.md`)
2. **CI Validation**: Future CI checks may validate prompt structure
3. **Code Review**: Reviewers should verify compliance before merging

## Reference Examples

Compliant instruction-generating prompts in this repository:

- `.github/prompts/prompt-file.instructions.prompt.md`
- `.github/prompts/create-ai-assisted-output-instructions.prompt.md`
- `.github/prompts/create-use-case-instructions.prompt.md`

## Questions?

For questions or clarification about these requirements, see:

- `.github/instructions/ai-assisted-output.instructions.md` - AI provenance policy
- `.github/instructions/create-prompt.instructions.md` - General prompt authoring guide

---

**Last Updated**: 2025-10-15
**Maintainer**: AI-Assisted Development Team
**Version**: 1.0.0
