---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Generates comprehensive authoring guidelines for creating custom GitHub Copilot chat modes
prompt_metadata:
  id: create-chatmode-instructions
  title: Generate Custom Chat Mode Instructions (Markdown)
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Software-Development
  version: 1.0.0
  created: 2025-10-22
  updated: 2025-10-22
  output_path: .github/instructions/create-chatmode.instructions.md
  category: documentation
  tags: [chatmode, copilot, documentation, authoring-guidelines]
  output_format: markdown
---

# Generate Custom Chat Mode Instructions

Create comprehensive guidelines for authoring custom GitHub Copilot chat modes following repository standards and best practices.

## Context

You are tasked with creating detailed instructions for authoring custom chat mode files within this repository. These instructions will serve as the definitive guide for creating consistent, high-quality chat modes that enhance GitHub Copilot's capabilities for specific domains and workflows.

Custom chat modes allow developers to create specialized AI assistants with specific expertise, personality, and command structures tailored to particular tasks like security analysis, documentation, architecture review, or code exploration.

**CRITICAL**: All AI-generated artifacts in this repository MUST comply with `.github/instructions/ai-assisted-output.instructions.md`. The generated instruction file MUST include full AI provenance metadata as specified in that policy.

**Important**: Follow [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) for:

- Model format requirements (use underlying model, not interface)
- Conversation logging format (use GitHub username, not "USER")
- Post-creation requirements (update AI logs, summary, README)
- Quality checklist and common mistakes to avoid

## Target Audience

- Software developers creating specialized AI assistants
- DevOps engineers setting up workflow-specific chat modes
- Security analysts creating security-focused chat modes
- Technical writers authoring documentation chat modes
- Team leads establishing project-specific AI assistants

## Requirements

Create `.github/instructions/create-chatmode.instructions.md` with the following comprehensive structure:

### 1. Overview and Purpose

Define what custom chat modes are and why they're valuable:

- Purpose of custom chat modes
- Benefits for specialized workflows
- When to create a custom chat mode vs using default Copilot
- Integration with GitHub Copilot ecosystem

### 2. Chat Mode File Structure

Document the complete structure requirements:

#### File Naming Conventions

- File naming pattern: `<ChatModeName>.chatmode.md`
- Location: `.github/chatmodes/`
- Naming best practices (PascalCase for mode names)

#### Required Header Components

- **Name**: The display name of the chat mode
- **Focus**: Primary domain or specialty area
- **Temperature**: AI temperature setting (0.0-1.0) for response creativity
- **Style**: Communication style and personality

#### Core Content Sections

- Mission statement and purpose
- Core expertise areas
- Analysis methodology or workflow phases
- Interactive commands (if applicable)
- Response format guidelines
- Communication principles
- Example interactions

### 3. Header Field Specifications

Provide detailed guidance for each header field:

#### Name Field

- Formatting requirements (e.g., "# Name: Security Analyzer")
- Naming conventions and best practices
- Examples of effective names

#### Focus Field

- How to define clear, specific focus areas
- Examples: "Code security analysis", "Technical documentation"
- Single vs. multi-domain focus

#### Temperature Field

- Temperature scale explanation (0.0 = deterministic, 1.0 = creative)
- Recommended values by use case:
  - 0.3 for security/compliance (precision required)
  - 0.4-0.5 for documentation (balance)
  - 0.6-0.7 for brainstorming (creativity valued)
- How to choose appropriate temperature

#### Style Field

- Writing tone and personality options
- Examples: "Thorough, security-focused", "Friendly, precise"
- Alignment with domain and audience

### 4. Content Structure Guidelines

#### Mission Statement

- How to write an effective mission statement
- Length and clarity requirements
- Examples from existing chat modes

#### Core Expertise Section

- Structuring expertise areas
- Using bullet points effectively
- Categorizing capabilities

#### Methodology Section (Optional but Recommended)

- When to include methodology/phases
- How to structure multi-phase workflows
- Examples: "Phase 1: Discovery, Phase 2: Analysis"

#### Interactive Commands Section

- Command naming conventions (e.g., `@security-scan`, `@overview`)
- Command format and syntax
- Creating command reference tables
- Best practices for command descriptions

#### Response Format Guidelines

- Structuring response templates
- Using emoji and formatting for clarity
- Creating consistent response patterns

#### Communication Principles

- Defining behavioral guidelines
- Setting expectations for responses
- Alignment with domain expertise

#### Example Interactions

- Providing realistic usage examples
- Showing expected inputs and outputs
- Demonstrating command usage

### 5. Best Practices

#### Clarity and Specificity

- Writing clear, actionable content
- Avoiding ambiguity
- Using specific examples

#### Consistency

- Maintaining consistent formatting
- Using standard terminology
- Following repository conventions

#### Scope Definition

- Defining clear boundaries for the chat mode
- Avoiding scope creep
- Focusing on specific value propositions

#### Command Design

- Creating intuitive command names
- Organizing commands by category
- Providing clear command descriptions

### 6. Quality Assurance

#### Validation Checklist

- Required header fields present
- Clear mission statement
- Well-defined expertise areas
- Command syntax (if applicable)
- Example interactions included
- Proper formatting and Markdown rendering

#### Testing Recommendations

- How to test the chat mode
- Validation of command functionality
- User acceptance testing

#### Review Process

- Peer review guidelines
- Feedback incorporation
- Iteration and refinement

### 7. Examples and Templates

Provide practical examples:

#### Simple Chat Mode Template

A minimal viable chat mode with basic structure

#### Advanced Chat Mode Template

A comprehensive chat mode with commands, methodology, and examples

#### Domain-Specific Examples

- Security analysis chat mode pattern
- Documentation assistant pattern
- Code exploration pattern
- Architecture review pattern

### 8. Common Patterns and Anti-Patterns

#### Effective Patterns

- Command-driven interaction models
- Phased methodology approaches
- Clear response format specifications
- Helpful example interactions

#### Anti-Patterns to Avoid

- Overly broad or unfocused scope
- Unclear or inconsistent commands
- Missing example interactions
- Vague mission statements
- Inconsistent formatting

### 9. Integration and Activation

#### How to Use Custom Chat Modes

- Activating a chat mode in GitHub Copilot
- Switching between chat modes
- Combining chat modes with other Copilot features

#### README Documentation

- Creating README files for complex chat modes
- Documentation best practices
- Usage examples and tutorials

### 10. Maintenance and Evolution

#### Versioning

- When to update a chat mode
- Tracking changes and improvements
- Deprecation strategies

#### Feedback Loop

- Gathering user feedback
- Iterating on chat mode design
- Community contributions

## Technical Requirements

- Use clear, actionable language
- Include specific examples for each concept
- Provide copy-paste templates
- Ensure all guidance is immediately implementable
- Structure content for easy reference and navigation
- Include Markdown formatting examples

## Output Format

Create a well-structured Markdown file that:

- Renders correctly in Markdown preview
- Uses consistent formatting throughout
- Includes proper heading hierarchy
- Contains actionable checklists and templates
- Follows established documentation patterns
- Includes example chat mode files

## Quality Standards

The generated instructions must:

- Be immediately usable by chat mode authors
- Maintain consistency across the repository
- Follow established documentation patterns
- Enable efficient chat mode creation workflows
- Reduce common authoring errors
- Provide clear validation criteria
- Include real-world examples from existing chat modes

## Deliverable

Generate the complete `.github/instructions/create-chatmode.instructions.md` file with:

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
source: ".github/prompts/create-chatmode-instructions.prompt.md"
applyTo: "**/*.chatmode.md"
---
```

**Important**: Use the underlying AI model (e.g., `"openai/gpt-4o@2024-11-20"`), not the interface (e.g., "github/copilot").

### Content Requirements

Following the metadata, include:

1. Complete custom chat mode authoring instructions as specified in all requirements above
2. Comprehensive templates and examples
3. Ready for immediate use by chat mode authors throughout the repository
4. All sections, examples, templates, and checklists as detailed in the requirements
5. Reference existing chat modes in the repository:
   - `.github/chatmodes/SecurityAnalyzer.chatmode.md`
   - `.github/chatmodes/DocDesignArchitect.chatmode.md`
   - `.github/chatmodes/codebase-explorer.chatmode.md`
   - `.github/chatmodes/GitFlowStrategist.chatmode.md`

The file should be comprehensive, well-structured, and follow established documentation patterns while providing practical, actionable guidance for creating effective custom chat modes.
