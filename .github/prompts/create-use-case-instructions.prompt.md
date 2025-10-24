---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "create"]
description: Generates a Markdown authoring guide for creating use cases with a standard structure and Mermaid diagram guidance
prompt_metadata:
  id: create-use-case-instructions
  title: Generate Use Case Authoring Instructions (Markdown)
  owner: johnmillerATcodemag-com
  repository: zeus.academia.3
  version: 1.0.0
  created: 2025-10-14
  updated: 2025-10-14
  output_path: .github/instructions/create-use-case.instructions.md
  category: documentation
  tags: [use-cases, documentation, authoring-guide, mermaid, prompt-generation]
  output_format: markdown
---

# Generate Use Case Authoring Instructions (Markdown)

You are an expert technical writer. Produce a single Markdown instruction file that teaches contributors how to author use cases in this repository, following a standard format and including Mermaid diagram guidance.

## Output requirements

- Create or overwrite the file at `.github/instructions/create-use-case.instructions.md`.
- Output only the final `.github/instructions/create-use-case.instructions.md` content as Markdown. Do not include any additional commentary, wrapper text, or code fences around the whole file.
- The instruction file must be self-contained, readable, and render correctly in Markdown preview.

## Audience and scope

- Audience: Repository contributors authoring use cases.
- Scope: Provide a copy-paste template, field-by-field guidance, Mermaid diagram guidance (flowchart and sequence), one concise example use case, a checklist, file naming conventions, and common pitfalls.

## Structure of the generated instruction file

The generated `.md` file must follow this outline and headings:

1. Title: "Use Case Authoring Instructions"
2. Introduction
3. Standard Use Case Template (copy-paste ready)
4. Field-by-field Guidance
5. Mermaid Diagram Guidance
6. Example Use Case (concise but realistic)
7. Authoring Checklist
8. Naming and File Conventions
9. Tips and Common Pitfalls

## Standard Use Case Template (to include verbatim in the output)

Provide this template as a fenced Markdown block for users to copy:

```
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
- See Mermaid diagram below.
```

## Field-by-field Guidance (what to write)

- Title: Use an action-oriented phrase that states the outcome (e.g., "Enroll Student in Course").
- Primary Actor: The role initiating the use case (not a specific person).
- Supporting Actors: Roles that assist or are consulted.
- Stakeholders and Interests: Optional—list those affected and what they care about.
- Goal: One crisp sentence; measurable when possible.
- Scope: Name the system or bounded context; avoid enterprise-wide scopes.
- Level:
  - User-goal for end-to-end value.
  - Subfunction for smaller reusable behaviors.
  - Summary for high-level aggregates.
- Preconditions: Facts that must already be true (no implied actions).
- Triggers: The event that starts the scenario (external or time-based).
- Main Success Scenario:
  - 7–12 numbered steps is typical.
  - Each step should be an observable result in present tense, attributed to Actor/System.
  - Avoid UI specifics unless essential to behavior.
- Alternate/Exception Flows:
  - Reference where they branch (e.g., "after step 3").
  - State conditions clearly; specify rejoin step or termination.
- Postconditions:
  - Success guarantees: must hold on success.
  - Minimal guarantees: must hold regardless of success.
- Business Rules: Reference IDs if you have a catalog; otherwise brief descriptions.
- Non-Functional Notes: Only those directly impacting this use case.
- Open Issues: Facts unknown, decisions pending—keep short.

## Mermaid Diagram Guidance

Include one Mermaid diagram per use case that communicates the main flow.

Preferred types:

- UML Use Case Diagram (flowchart style) showing Actor-to-Use Case relationships.
- Sequence Diagram illustrating the Main Success Scenario steps.

Place the diagram under the "Diagram" section using a fenced code block with language `mermaid`.

Example flowchart:

```mermaid
flowchart TD
  A[Actor initiates request] --> B{Preconditions met?}
  B -- Yes --> C[System validates input]
  C --> D[Perform main action]
  D --> E{Alternate condition?}
  E -- No --> F[Persist result]
  E -- Yes --> A1[Handle alternate flow]
  A1 --> F
  F --> G[Return success response]
  B -- No --> X[Abort with explanation]
```

Example sequence diagram:

```mermaid
sequenceDiagram
  autonumber
  participant Actor
  participant UI
  participant Service
  participant DB

  Actor->>UI: Submit request
  UI->>Service: Validate and process
  Service->>DB: Read/Write data
  DB-->>Service: Result
  Service-->>UI: Outcome
  UI-->>Actor: Confirmation
```

Optional Mermaid init (if supported):

```mermaid
%%{init: {"theme": "neutral"}}%%
```

## Example Use Case

Provide a short, realistic example filled in using the template. Choose a generic case like "Reset User Password" unless domain-specific knowledge is required. Include 6–9 main steps, 1–2 alternate flows, and one Mermaid diagram (either flowchart or sequence).

## Authoring Checklist

- Title states outcome and actor.
- Goal is one sentence, unambiguous.
- Scope and Level are set appropriately.
- Preconditions and Trigger are explicit.
- Main Success Scenario is numbered, observable, and avoids UI trivia.
- Alternates reference branch/rejoin points.
- Postconditions include success and minimal guarantees.
- Business rules referenced or briefly stated.
- Mermaid diagram included and readable.
- No open issues left unresolved, or they’re listed in "Open Issues".

## Naming and File Conventions

- File name: `use-case-<kebab-case-title>.md` (e.g., `use-case-reset-user-password.md`).
- Store use case files under `Model/use-cases/`.
- One use case per file.
- Place diagrams inline as Mermaid code blocks within the file.
- Keep lines under ~120 characters where feasible.

## Tips and Common Pitfalls

- Prefer user goals over UI flows; describe intent, not clicks.
- Avoid hidden system behavior—make side effects explicit.
- Keep alternates focused; don’t duplicate main steps—reference them.
- If a step is conditional, state the condition first.
- Update related business rules when the use case changes.

## Acceptance criteria for the generated instruction file

- Contains the template, field guidance, diagram guidance, example, and checklist as specified.
- Is self-contained and immediately actionable for authors.
- Renders correctly as Markdown without external assets.
- Uses clear headings matching the structure above.

## Deliverable

Generate the complete `.github/instructions/create-use-case.instructions.md` file with:

### Required AI Provenance Metadata (YAML Front Matter)

The file MUST begin with the following YAML front matter fields per `.github/instructions/ai-assisted-output.instructions.md`:

```yaml
---
ai_generated: true
model: "<provider>/<model-name>@<version>" # e.g., "openai/gpt-4o@2024-11-20" or "anthropic/claude-3.5-sonnet@2024-10-22"
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
applyTo: "Model/use-cases/*.md"
---
```

**Important**: Use the underlying AI model (e.g., `"openai/gpt-4o@2024-11-20"`), not the interface (e.g., "github/copilot").

### Content Requirements

Following the metadata, output only the final `.github/instructions/create-use-case.instructions.md` content as Markdown. Do not include any additional commentary, wrapper text, or code fences around the whole file.
