---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create", "edit"]
description: Create prompt that generates Markdown authoring guidelines for effective repository prompts
prompt_metadata:
  id: prompt-file.instructions-prompt
  title: Meta Prompt — Generate Prompt Authoring Instructions
  owner: johnmillerATcodemag-com
  output_path: .github/prompts/prompt-file.instructions.prompt.md
  category: meta-documentation
  tags: [meta-prompts, documentation, prompt-engineering]
  output_format: markdown
---

# Meta Prompt — Generate Prompt Authoring Instructions

Create prompt for generating Markdown guidelines to help create effective, well-structured repository prompts.

## Output Target
`.github/prompts/prompt-file.instructions.prompt.md` → creates → `.github/instructions/create-prompt.instructions.md`

## Generated Prompt Must Include:

### Required Metadata (YAML Frontmatter)
- Top-level: `mode` (agent|chat), `model` (Auto or specific), `tools` (array), `description`
- `prompt_metadata`: `id: prompt-file.instructions-prompt`, `output_path`, title, version, tags, category

### Content Structure
1. **Audience & Scope**: Developers, prompt authors, skill expectations
2. **Prompt File Structure**: YAML frontmatter (mode, model, tools, description at top-level + prompt_metadata), organization standards
3. **Field-by-Field Docs**: 
   - Top-level required: mode (agent for files), model (Auto default), tools (array), description (NOT in metadata)
   - prompt_metadata: id, title, owner, output_path, output_format, tags
   - Validation rules, examples
4. **Best Practices**: Metadata structure, tool selection methodology, mode specification, clarity/specificity
5. **Quality Assurance**: Validation checklist, authoring standards, testing
6. **Examples & Templates**: Code generator, docs generator, interactive assistant, domain-specific
7. **Common Patterns**: Effective patterns, anti-patterns
8. **Troubleshooting**: Common issues, solutions
9. **Quick Reference**: Minimal valid prompt, field reference, tool selection guide

### Key Requirements to Enforce
- Description at TOP-LEVEL (not in prompt_metadata)
- Tools array complete and minimal
- Mode: agent (file ops) or chat (interactive)
- Naming: kebab-case, unique IDs
- YAML syntax valid

## Deliverable
Complete prompt that generates comprehensive prompt authoring instructions following all standards.
