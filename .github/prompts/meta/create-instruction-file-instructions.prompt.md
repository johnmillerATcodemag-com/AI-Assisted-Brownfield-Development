---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "create"]
description: Generates a Markdown authoring guide for creating instruction files with recommended sections, placement, naming, and a validation checklist
prompt_metadata:
  id: create-instruction-file-instructions
  title: Generate Instruction-File Authoring Instructions (Markdown)
  owner: johnmillerATcodemag-com
  repository: zeus.academia.3
  version: 1.0.0
  created: 2025-10-14
  updated: 2025-10-14
  output_path: .github/instructions/instruction-standards.instruction.md
  category: documentation
  tags: [instructions, documentation, authoring-guide, governance, template]
  output_format: markdown
---

# Generate Instruction-File Authoring Instructions (Markdown)

You are an expert technical writer. Produce a single Markdown instruction file that guides contributors on how to create repository instruction files consistently.

## Output requirements

- Create or overwrite the file at: `.github/instructions/instruction-standards.instruction.md`.
- Output only the final `.github/instructions/instruction-standards.instruction.md` content as Markdown. Do not include any additional commentary, wrapper text, or code fences around the whole file.
- The instruction file must be self-contained, readable, and render correctly in Markdown preview.

## Audience and scope

- Audience: Contributors authoring instruction files for this repository.
- Scope: Defines standard sections, directory placement, naming conventions, a reusable template, examples, and a quality checklist for instruction files.

## Structure of the generated instruction file

The generated `.md` file must follow this outline and headings (all required unless marked optional):

1. Title: "Instruction File Authoring Guide"
2. Introduction (purpose and when to use)
3. Audience and Scope
4. File Placement and Naming Conventions
5. Standard Sections (overview)
6. Copy/Paste Template (complete skeleton)
7. Section-by-Section Guidance
8. Example (concise but realistic)
9. Quality Checklist
10. Versioning and Ownership
11. Security and Privacy
12. References / Glossary (optional)

## Directory and naming conventions (must include in the generated file)

- Folder: `.github/instructions/`.
- Filenames: hyphenated lowercase and must end with `.instruction.md`.
- One instruction file per topic.

## Standard sections to document (must include in the generated file)

- Introduction: What this instruction covers and when to use it.
- Audience and Scope: Who should use it; what’s included/excluded.
- Prerequisites: Tools, permissions, or context needed.
- Output Requirements: Exact outputs, formats, and constraints.
- Steps / Procedure: Ordered steps with sub-steps if needed.
- Examples / Samples: Minimal but complete examples.
- Templates / Snippets: Copy-paste blocks authors can reuse.
- Validation / Quality Checklist: Criteria to confirm completeness and quality.
- File Placement and Naming: Where to store and how to name files.
- Versioning and Ownership: How to update and who maintains the doc.
- Security and Privacy: Sensitive data guidelines and redaction.
- References / Glossary: Linked resources and definitions (optional).

## Copy/Paste template (to include verbatim in the output)

Provide this template as a fenced Markdown block for users to copy:

````
# Instruction File Title

## Introduction
<Brief purpose, when to use, and outcomes.>

## Audience and Scope
- Audience: <Who>
- Scope: <What’s included>
- Out of scope: <What’s not covered>

## Prerequisites
- <Tool/permission/context>

## Output Requirements
- <Exact output path(s)/formats>
- <No extra commentary/wrappers>

## Steps / Procedure
1. <Step>
2. <Step>
3. <Step>

## Examples / Samples
```example
<Short, complete example>
```
````

## Templates / Snippets

```markdown
<Reusable snippet or section>
```

## Validation / Quality Checklist

- [ ] Outputs and formats match requirements
- [ ] Steps are actionable and ordered
- [ ] Examples run or render as expected
- [ ] No secrets or sensitive data
- [ ] Naming and placement adhere to conventions

## File Placement and Naming

- Folder: `.github/instructions/`
- Filename: `<topic-name>.instruction.md`

## Versioning and Ownership

- Owner: <name/role>
- Last updated: YYYY-MM-DD
- Change policy: <how to propose changes>

## Security and Privacy

- <Redaction, secrets handling, PII guidance>

## References / Glossary

- <Links and definitions>

````

## Section-by-Section Guidance (what to write)

- Title: Be specific; reflect the topic (e.g., "CI Pipeline Instructions").
- Prerequisites: List only what’s truly required; link to setup docs.
- Output Requirements: State exact paths and formats; specify overwrite behavior.
- Steps: Use numbered steps; one action per step; include expected outcomes.
- Examples: Keep minimal and runnable/renderable where applicable.
- Templates: Provide copy-paste blocks with placeholders and short comments.
- Quality Checklist: Focus on verifiable criteria; keep it short and scannable.
- Versioning and Ownership: Name an accountable owner; require date updates.
- Security and Privacy: Avoid secrets; show redacted examples; reference policy.

## Example (concise)

Title: Linting Instructions

- Audience: Contributors
- Scope: How to run and interpret linting locally

- Output Requirements:
  - Provide a passing lint run example output excerpt

- Steps / Procedure:
  1. Install dependencies
  2. Run linter
  3. Fix reported issues and re-run

- Example:
```text
$ tool lint
✔ No issues found
````

## Quality Checklist (for authors)

- Title and purpose are clear
- Steps are ordered and testable
- Examples render/run
- Output path and format are explicit
- File lives under `.github/instructions/` and ends with `.instruction.md`

## Versioning and Ownership

- Update "Last updated" whenever the file changes
- List an owner responsible for maintenance

## Security and Privacy

- Do not include secrets, tokens, or personal data
- Redact or omit sensitive content in examples and logs

## Acceptance criteria for the generated instruction file

- Includes all sections listed above
- Uses kebab-case filename ending with `.instruction.md`
- Stored under `.github/instructions/`
- Renders correctly in Markdown preview and is self-contained
- Contains a copy-paste template and a quality checklist
