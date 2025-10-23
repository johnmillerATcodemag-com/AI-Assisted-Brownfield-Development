---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Generate comprehensive authoring guidelines for custom GitHub Copilot chat modes
prompt_metadata:
  id: create-chatmode-instructions
  title: Generate Custom Chat Mode Instructions
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/create-chatmode.instructions.md
  category: documentation
  tags: [chatmode, copilot, documentation]
  output_format: markdown
---

# Generate Custom Chat Mode Instructions

Create comprehensive guidelines for authoring custom GitHub Copilot chat modes.

## Context
Instructions for creating specialized AI assistants with specific expertise, personality, and commands.
Must comply with `.github/instructions/ai-assisted-output.instructions.md` and `copilot-instructions.md`.

## Output: `.github/instructions/create-chatmode.instructions.md`

### Structure:
1. **Overview**: Purpose, benefits, when to create vs use default, integration
2. **File Structure**:
   - Naming: `<ChatModeName>.chatmode.md` (PascalCase) in `.github/chatmodes/`
   - Header: Name, Focus, Temperature (0.0-1.0), Style
   - Sections: Mission, Core Expertise, Methodology, Commands, Response Format, Principles, Examples
3. **Header Fields**:
   - **Name**: Display name, Title Case, 2-4 words
   - **Focus**: Primary domain, specific capabilities
   - **Temperature**: 0.3 (security/compliance), 0.4-0.5 (docs/analysis), 0.6-0.7 (brainstorming)
   - **Style**: 2-4 descriptive adjectives (tone, approach, focus)
4. **Content Structure**:
   - Mission: 1-2 sentences, role + value + approach
   - Core Expertise: 5-10 specific areas (bold + description)
   - Methodology: Multi-phase workflow (if applicable)
   - Commands: `@kebab-case` format, clear descriptions
   - Response Format: Structured output template
   - Principles: Behavioral guidelines
   - Examples: Realistic usage demonstrations
5. **Best Practices**: Clarity, consistency, scope definition, intuitive commands
6. **Quality Assurance**: Validation checklist, testing, review process
7. **Examples**: Simple template, advanced template, domain-specific (security, docs, code exploration, architecture)
8. **Common Patterns**: Command-driven interaction, phased methodology, clear response format
9. **Anti-Patterns**: Overly broad scope, unclear commands, missing examples, vague mission
10. **Integration**: Activation (`@modename`), switching, combining with Copilot features
11. **Maintenance**: Versioning, feedback loop, iteration, deprecation

### Templates to Include:
- Security analyzer pattern
- Documentation assistant pattern
- Code exploration pattern
- Architecture review pattern

### Quality Checklist:
- PascalCase filename with `.chatmode.md`
- All header fields present
- Mission clear, expertise listed (5-10)
- Commands use `@kebab-case`
- Temperature appropriate
- Style aligns with domain

## Deliverable
Complete file with YAML front matter per ai-assisted-output policy, all sections, templates, checklists, examples.
