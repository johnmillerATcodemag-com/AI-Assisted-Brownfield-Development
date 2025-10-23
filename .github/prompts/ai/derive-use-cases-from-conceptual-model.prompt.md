---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "read", "create"]
description: Derive use cases from conceptual model by reading ORM file from Model/orm/ and generating use case files
prompt_metadata:
  id: derive-use-cases-from-academia
  title: Generate Use Cases from conceptual model (ORM rules)
  owner: johnmillerATcodemag-com
  output_path: Model/use-cases/derived-use-cases.index.md
  category: documentation
  tags: [use-cases, orm, modeling, mermaid, automation]
  output_format: markdown
---

# Generate Use Cases from conceptual model

Read business rules from conceptual ORM model, derive user-goal use cases, generate use case files.

## Prerequisites - Locate Model
1. Use `file_search` for .txt files in `Model/orm/`
2. If one file found, read complete contents
3. If none: abort with "❌ No model found in Model/orm/"
4. If multiple: abort with "❌ Multiple .txt files in Model/orm/"

## Inputs
- ORM model from `Model/orm/*.txt`
- `.github/instructions/create-use-case.instructions.md`
- `README.md`

## Output
- Index: `Model/use-cases/derived-use-cases.index.md`
- Per use case: `Model/use-cases/use-case-<kebab>.md`
- Update `README.md` "AI-Assisted Artifacts" with link

## Process
1. Parse ORM model, extract atomic rules and terms
2. Group into user-goal use cases (6–12 steps, 1–3 alternates)
3. Create files using template with Mermaid diagram
4. Build index with table (ID, Title, Goal, Filename link)
5. Update README with link and count

## Template
```
# Use Case: <Title>
- Primary Actor: <Role>
- Goal: <One sentence>
- Preconditions: 1. <Condition>
- Triggers: <Event>
## Main Success Scenario
1. <Actor> <action>.
## Alternate/Exception Flows
A1. <Condition>: 1. <Step>
## Postconditions
- Success: <Guarantees>
## Diagram
\`\`\`mermaid
flowchart TD
\`\`\`
```

## Acceptance
- Index exists with table linking all use cases
- Each file under `Model/use-cases/`, follows template, includes Mermaid
- README updated with link
