---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "create"]
description: Generate Markdown authoring guide for creating instruction files
prompt_metadata:
  id: create-instruction-file-instructions
  title: Generate Instruction-File Authoring Instructions
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/instruction-standards.instruction.md
  category: documentation
  tags: [instructions, documentation, authoring-guide]
  output_format: markdown
---

# Generate Instruction-File Authoring Instructions

Create Markdown guide for authoring repository instruction files consistently.

## Output
File: `.github/instructions/instruction-standards.instruction.md`
Self-contained, renders correctly in Markdown

## Structure Required:
1. Title: "Instruction File Authoring Guide"
2. Introduction (purpose, when to use)
3. Audience & Scope
4. File Placement & Naming: `.github/instructions/`, hyphenated lowercase, ends with `.instruction.md`
5. Standard Sections (overview)
6. Copy/Paste Template (complete skeleton)
7. Section-by-Section Guidance
8. Example (concise, realistic)
9. Quality Checklist
10. Versioning & Ownership
11. Security & Privacy
12. References/Glossary (optional)

## Standard Sections to Document:
- Introduction, Audience & Scope, Prerequisites
- Output Requirements, Steps/Procedure
- Examples/Samples, Templates/Snippets
- Validation/Quality Checklist
- File Placement & Naming
- Versioning & Ownership
- Security & Privacy
- References/Glossary (optional)

## Template Format:
````markdown
# Instruction File Title
## Introduction
## Audience and Scope
## Prerequisites
## Output Requirements
## Steps
## Examples
## Templates
## Validation Checklist
## File Placement
## Versioning
## Security
````

## Quality Checklist:
- All standard sections present
- Template is copy-paste ready
- Examples are realistic
- Naming conventions clear
- Validation criteria defined
