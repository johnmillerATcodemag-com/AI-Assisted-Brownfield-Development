---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "read", "create"]
description: Derive use cases from conceptual model by automatically locating and reading the ORM model file from Model/orm/, then generating one Markdown file per use case under Model/use-cases, plus an index file
prompt_metadata:
  id: derive-use-cases-from-academia
  title: Generate Use Cases from conceptual model (ORM rules)
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Brownfield-Development
  version: 1.1.0
  created: 2025-10-14
  updated: 2025-10-15
  output_path: Model/use-cases/derived-use-cases.index.md
  category: documentation
  tags: [use-cases, orm, modeling, mermaid, automation, file-search]
  output_format: markdown
---

# Generate Use Cases from conceptual model (ORM rules)

You are an expert analyst and technical writer. Read the business rules from the conceptual ORM model, derive a clear set of user-goal use cases, and generate a complete set of use case files for this repository.

## Prerequisites - Locate Conceptual Model

**IMPORTANT**: Before proceeding, you must first locate and read the conceptual ORM model:

1. Use the `file_search` tool to find .txt files in the `Model/orm/` folder: `file_search(query="Model/orm/*.txt")`
2. If exactly one .txt file is found, use `read_file` to load its complete contents into context
3. If no .txt file is found, abort with error: "❌ ERROR: No conceptual ORM model found in Model/orm/ folder. Please ensure a .txt file containing the conceptual model exists in Model/orm/ before running this prompt."
4. If multiple .txt files are found, abort with error: "❌ ERROR: Multiple .txt files found in Model/orm/ folder. Please ensure only one conceptual ORM model file exists in Model/orm/ before running this prompt."

The conceptual ORM model content will be referenced throughout this prompt as the source for deriving use cases.

## Inputs and references

- Source rules: The conceptual ORM model loaded from `Model/orm/*.txt` in the prerequisites step
- Use case authoring guide: `.github/instructions/create-use-case.instructions.md`
- Instruction-file standards: `.github/instructions/instruction-standards.instruction.md`
- AI-assisted output policy: `.github/instructions/ai-assisted-output.instructions.md`
- Project README: `README.md`

## Output requirements

- Create or overwrite the index file at: `Model/use-cases/derived-use-cases.index.md`.
- Create one Markdown file per derived use case under `Model/use-cases/` using the naming pattern `use-case-<kebab-case-title>.md`.
- Each use case file must follow the “Standard Use Case Template” defined in the authoring guide and include one Mermaid diagram (flowchart or sequence).
- Store use case files under `Model/use-cases/` only; one use case per file.
- Update the top-level `README.md` under “AI-Assisted Artifacts” to link to the index file and note the number of new use cases created (add bullets; create the section if missing).
- Output only the final Markdown for the index file. Do not include any extra commentary outside the document.

## Process (what to do)

1. Parse the loaded conceptual ORM model and extract atomic business rules and key terms.
2. Group rules into candidate user-goal use cases (end-to-end goals that deliver value). Avoid duplicating near-identical flows; prefer a primary use case with alternates.
3. Produce a candidate list with short titles and one-line goals. Refine for clarity and scope boundaries (system vs. external actors).
4. For each approved candidate:
   - Create `Model/use-cases/use-case-<kebab>.md`.
   - Use the repository use case template and field guidance.
   - Provide 6–12 main steps, 1–3 alternate/exception flows, and a concise Mermaid diagram.
   - Use domain terms and actors consistent with the rules.
5. Build `Model/use-cases/derived-use-cases.index.md` with a table summarizing: ID (e.g., UC-001), Title, Goal (1 line), and Filename (relative link).
6. Update `README.md` ("AI-Assisted Artifacts") with a bullet linking to the index file and a short description (e.g., "Derived N use cases from conceptual model").

## File naming and conventions

- Use-case files: `Model/use-cases/use-case-<kebab-case-title>.md`.
- Title inside each file: `# Use Case: <Descriptive Title>`.
- Actors as roles (not named individuals).
- Keep lines ≲ 120 chars when practical.

## Use case template (copy/paste into each file)

````
# Use Case: <Descriptive Title>

- Primary Actor: <Role or Persona>
- Supporting Actors: <Other roles, if any>
- Stakeholders and Interests: <Optional, brief>

- Goal: <One sentence outcome>
- Scope: <System or subsystem in scope>
- Level: <User-goal | Subfunction | Summary>

- Preconditions:
  1. <Condition>
  2. <Condition>

- Triggers:
  - <Event that starts the use case>

## Main Success Scenario
1. <Actor> <action/result>.
2. <System> <response>.
3. ...
N. <Goal achieved>.

## Alternate/Exception Flows
A1. <Condition>:
   1. <Step>
   2. <Rejoin at step X or ends>.

A2. <Condition>:
   1. <Step>

## Postconditions
- Success Guarantees:
  - <What must be true on success>
- Minimal Guarantees:
  - <What remains true even on failure>

## Business Rules
- <Rule ID or description>

## Non-Functional Notes
- <Performance, security, UX, compliance, etc.>

## Open Issues
- <Questions or TBDs>

## Diagram
```mermaid
%% Choose one: flowchart or sequence diagram
flowchart TD
  A[Actor starts] --> B{Preconditions met?}
  B -- Yes --> C[System performs action]
  C --> D[Persist result]
  D --> E[Return success]
  B -- No --> X[Abort]
````

```

## Acceptance criteria

- An index file exists at `Model/use-cases/derived-use-cases.index.md` with a table of all derived use cases and links to each file.
- Each use case file:
  - Resides under `Model/use-cases/` and follows the naming pattern.
  - Conforms to the template and guidance; includes one Mermaid diagram.
  - Uses consistent domain terminology from the conceptual ORM model.
- `README.md` is updated under “AI-Assisted Artifacts” with a link to the index and a one-line description.
- No extra commentary outside the generated files.

## Deliverable

- Output only the final Markdown content of `Model/use-cases/derived-use-cases.index.md`. Create all other files as edits without printing their contents.
```
