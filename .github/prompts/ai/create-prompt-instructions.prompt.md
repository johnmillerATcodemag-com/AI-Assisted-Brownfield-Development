---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Generate Markdown authoring guidelines for creating effective repository prompts
prompt_metadata:
  id: prompt-file.instructions-prompt
  title: Generate Prompt Authoring Instructions (Markdown)
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/create-prompt.instructions.md
  category: meta-documentation
  tags: [prompt-engineering, documentation, authoring-guidelines]
  output_format: markdown
---

# Generate Prompt Authoring Instructions

Create comprehensive Markdown guidelines for authoring repository prompts following standards.

## Context
Detailed instructions for authoring prompt files. Must comply with:
- `.github/instructions/ai-assisted-output.instructions.md` (AI provenance)
- `.github/instructions/copilot-instructions.md` (model format, logging, post-creation)

## Audience
Developers, AI prompt engineers, technical writers, contributors to AI workflows

## Requirements for `.github/instructions/create-prompt.instructions.md`:

### 1. Audience & Scope
Target audience, skill expectations

### 2. Prompt File Structure
**YAML Frontmatter**:
- Top-level: `mode` (agent|chat), `model` (Auto or specific), `tools` (array), `description`
- `prompt_metadata` section: `id`, `title`, `owner`, `output_path`, `output_format`, `tags`, etc.

### 3. Field Documentation
- **mode**: agent (file ops), chat (interactive)
- **model**: Default "Auto (copilot)" or specified
- **tools**: Selection methodology (create, edit, search, read, run, list)
- **description**: Clear, actionable (top-level, NOT in metadata)
- **id**: kebab-case, unique, descriptive (pattern: domain-action-target)
- **output_path**: Relative path from repo root
- **tags**: 3-7 relevant tags

### 4. Best Practices
- Metadata structure (top-level vs prompt_metadata)
- Tool selection (complete, minimal)
- Mode specification (file ops vs interactive)
- Content guidelines (clarity, specificity, context)

### 5. Quality Assurance
Validation checklist, authoring standards, testing

### 6. Examples & Templates
- Code generator template
- Documentation generator template
- Interactive assistant template
- Domain-specific examples

### 7. Common Patterns
Effective patterns, anti-patterns to avoid

### 8. Troubleshooting
Common issues and solutions

### 9. Quick Reference
Minimal valid prompt, field quick reference, tool selection guide

## Critical Requirements
- Description at TOP-LEVEL (not in prompt_metadata)
- All required fields present
- Tools array complete and minimal
- YAML syntax valid
- ID follows naming convention

## Deliverable
Complete `.github/instructions/create-prompt.instructions.md` with:
- YAML front matter per ai-assisted-output policy
- All sections above
- Templates and examples
- Copy-paste ready checklists
