---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "create"]
description: Generate Markdown authoring guide for creating use cases with standard structure and Mermaid diagrams
prompt_metadata:
  id: create-use-case-instructions
  title: Generate Use Case Authoring Instructions (Markdown)
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/create-use-case.instructions.md
  category: documentation
  tags: [use-cases, documentation, authoring-guide, mermaid]
  output_format: markdown
---

# Generate Use Case Authoring Instructions

Create instruction file at `.github/instructions/create-use-case.instructions.md` teaching how to author use cases with standard format and Mermaid diagrams.

## Output
Single Markdown file, self-contained, renders correctly in preview.

## Structure
1. Title: "Use Case Authoring Instructions"
2. Introduction
3. Standard Template (copy-paste ready)
4. Field-by-field Guidance
5. Mermaid Diagram Guidance
6. Example Use Case (concise, realistic)
7. Authoring Checklist
8. Naming/File Conventions
9. Tips and Pitfalls

## Template (include verbatim)
```
# Use Case: <Title>
- Primary Actor: <Role>
- Supporting Actors: <Roles>
- Goal: <One sentence>
- Scope: <System>
- Level: <User-goal | Subfunction | Summary>
- Preconditions: 1. <Condition>
- Triggers: <Event>

## Main Success Scenario
1. <Actor> <action>.
2. <System> <response>.

## Alternate/Exception Flows
A1. <Condition>: 1. <Step>

## Postconditions
- Success Guarantees: <What's true>
- Minimal Guarantees: <What remains>

## Business Rules
- <Rule>

## Non-Functional Notes
- <Notes>

## Diagram
\`\`\`mermaid
flowchart TD
\`\`\`
```
