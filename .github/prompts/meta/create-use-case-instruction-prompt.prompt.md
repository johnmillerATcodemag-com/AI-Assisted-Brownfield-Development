---
prompt_metadata:
	id: create-use-case-instruction-prompt
	title: Meta Prompt — Create Use Case Instruction Prompt
	description: Creates a prompt that generates a Markdown authoring guide for use cases.
	owner: johnmillerATcodemag-com
	repository: zeus.academia.3
	version: 1.0.0
	created: 2025-10-14
	updated: 2025-10-14
	output_path: .github/prompts/create-use-case-instructions.prompt.md
	category: documentation
	tags: [use-cases, documentation, prompt-generation]
	output_format: markdown
---

# Meta Prompt — Create Use Case Instruction Prompt

This is prompt 0, hand-written to seed the process by creating the downstream prompt used to generate the authoring instructions. It was then updated by the instructions for creating prompts.

## Output requirements

- Create or overwrite the file at: `.github/prompts/create-use-case-instructions.prompt.md`.
- The output must conform to the Repository Prompt File Standards and include YAML `prompt_metadata`.
- The generated prompt must instruct producing `.github/instructions/create-use-case.instructions.md` and include:
  - An explicit "Output requirements" section stating to output only the final Markdown file content with no extra commentary or wrappers.
  - Audience and scope.
  - A defined outline for the instruction file, including: Title, Introduction, Standard Use Case Template (copy/paste), Field-by-field Guidance, Mermaid Diagram Guidance, Example Use Case, Authoring Checklist, Naming and File Conventions, Tips and Common Pitfalls, and Acceptance Criteria.
  - A copy/paste-ready standard use case template (fenced Markdown block).
  - Field-by-field guidance for each template section (e.g., Title, Actors, Preconditions, Triggers, Main Success Scenario, Extensions, Postconditions, Business Rules, Non-Functional Notes, Open Issues).
  - Mermaid diagram guidance with at least one flowchart example and one sequence diagram example (as `mermaid` fenced code blocks), and an optional Mermaid init snippet.
  - A brief, realistic example use case filled using the template (6–9 steps, 1–2 alternates) with one Mermaid diagram.
  - An authoring checklist and file naming conventions (kebab-case; one use case per file; diagrams inline as Mermaid code blocks).
  - Acceptance criteria that verify completeness, clarity, and correct Markdown rendering.

### Notes for the generated prompt (alignment hints)

- Use `prompt_metadata.id: create-use-case-instructions` and set `output_path: .github/instructions/create-use-case.instructions.md`.
- Title: "Generate Use Case Authoring Instructions (Markdown)".
- Ensure the instruction file is self-contained and renders correctly in Markdown preview.

## Deliverable

Output only the final `.github/prompts/create-use-case-instructions.prompt.md` content as Markdown. Do not include any additional commentary.
