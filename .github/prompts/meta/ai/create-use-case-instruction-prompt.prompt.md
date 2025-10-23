---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create", "edit"]
description: Create prompt that generates use case authoring guidelines
prompt_metadata:
  id: create-use-case-instruction-prompt
  title: Meta Prompt — Generate Use Case Instructions
  owner: johnmillerATcodemag-com
  output_path: .github/prompts/create-use-case-instructions.prompt.md
  category: meta-documentation
  tags: [meta-prompts, use-cases, documentation]
  output_format: markdown
---

# Meta Prompt — Generate Use Case Authoring Instructions

Create prompt that generates use case authoring guidelines.

## Output Target
`.github/prompts/create-use-case-instructions.prompt.md` → creates → `.github/instructions/create-use-case.instructions.md`

## Generated Prompt Specs:

### Required Metadata
- `mode: agent`, `model: Auto (copilot)`, `tools: ["edit", "create"]`
- `description`: Generate use case authoring guide
- `prompt_metadata`: id, output_path, title, category, tags

### Content Structure
Generated instructions must include:
1. **Audience & Scope**: Contributors authoring use cases, standard format + Mermaid diagrams
2. **Standard Template** (copy-paste ready):
```markdown
# Use Case: <Title>
- Primary Actor: <Role>
- Goal: <One sentence>
- Preconditions: 1. <Condition>
- Triggers: <Event>
## Main Success Scenario
## Alternate/Exception Flows
## Postconditions
## Business Rules
## Non-Functional Notes
## Diagram
\`\`\`mermaid
flowchart TD
\`\`\`
```
3. **Field-by-field Guidance**: Purpose and examples for each template field
4. **Mermaid Diagram Guidance**: Flowchart vs sequence, when to use each, syntax
5. **Example Use Case**: Concise but realistic
6. **Authoring Checklist**: Validation criteria
7. **Naming/File Conventions**: `use-case-<kebab-case>.md` in appropriate folder
8. **Tips & Pitfalls**: Common mistakes, best practices

### Quality Standards
- Template is copy-paste ready
- Examples are realistic
- Mermaid diagrams are clear
- All standard sections explained

## Deliverable
Complete prompt that generates comprehensive use case authoring instructions.
