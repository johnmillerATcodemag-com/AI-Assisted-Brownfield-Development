---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Create a comprehensive prompt file that will generate detailed authoring guidelines
  for creating effective repository prompts following established standards.
started: "2025-10-15T00:00:00Z"
ended: "2025-10-15T00:15:00Z"
task_durations:
  - task: "prompt design"
    duration: "00:10:00"
  - task: "metadata configuration"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Generates comprehensive Markdown authoring guidelines for creating effective repository prompts
prompt_metadata:
  id: prompt-file.instructions-prompt
  title: Generate Prompt Authoring Instructions (Markdown)
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Brownfield-Development
  version: 1.0.0
  created: 2025-10-15
  updated: 2025-10-15
  output_path: .github/instructions/create-prompt.instructions.md
  category: meta-documentation
  tags: [prompt-engineering, documentation, authoring-guidelines, standards]
  output_format: markdown
---

# Generate Prompt Authoring Instructions

Create comprehensive Markdown authoring guidelines that help developers and prompt authors create effective, well-structured repository prompts following established standards.

## Context

You are tasked with creating detailed instructions for authoring prompt files within this repository. These instructions will serve as the definitive guide for creating consistent, high-quality prompts that follow the Repository Prompt File Standards.

**CRITICAL**: All AI-generated artifacts in this repository MUST comply with `.github/instructions/ai-assisted-output.instructions.md`. The generated instruction file MUST include full AI provenance metadata as specified in that policy.

**Important**: Follow [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) for:

- Model format requirements (use underlying model, not interface)
- Conversation logging format (use GitHub username, not "USER")
- Post-creation requirements (update AI logs, summary, README)
- Quality checklist and common mistakes to avoid

## Target Audience

- Software developers creating repository prompts
- AI prompt engineers
- Technical writers authoring prompt documentation
- Contributors to AI-assisted development workflows

## Requirements

Create `.github/instructions/create-prompt.instructions.md` with the following comprehensive structure:

### 1. Audience and Scope Definition

Define the target audience and establish skill level expectations. Explain who should use these instructions and what they should already know.

### 2. Prompt File Structure Guide

Document the complete structure requirements:

#### YAML Frontmatter Requirements

- **Top-level mandatory fields**:
  - `mode:` ('agent' for file-creating prompts, 'chat' for interactive prompts)
  - `model:` ('Auto (copilot)' if unspecified)
  - `tools:` Array of required tools (create, edit, search, etc.)
  - `description:` Clear description of what the prompt does
- **prompt_metadata section** (excluding description which is now top-level)
- Section organization standards
- Metadata validation rules

### 3. Field-by-Field Documentation

Provide detailed documentation for each field:

#### Required Top-Level Fields

- `mode`: Usage patterns and selection criteria
- `model`: Default values and alternatives
- `tools`: Tool selection methodology and validation
- `description`: Writing guidelines and examples

#### Required prompt_metadata Fields

- `id`: Naming conventions and uniqueness requirements
- `title`: Formatting standards
- `owner`: Attribution guidelines
- `output_path`: Path conventions and validation
- `output_format`: Format specifications
- `tags`: Tagging best practices

#### Optional prompt_metadata Fields

- `repository`: Repository reference standards
- `version`: Semantic versioning practices
- `created`/`updated`: Date formatting standards
- `category`: Classification system

### 4. Best Practices Guidelines

#### Metadata Structure

- Top-level vs prompt_metadata organization
- Field ordering conventions
- YAML formatting standards

#### Tool Selection

- Analysis methodology for determining required tools
- Tool array construction
- Validation criteria

#### Mode Specification

- 'agent' vs 'chat' selection criteria
- Use case examples
- Decision flowchart

#### Content Guidelines

- Clarity and specificity requirements
- Context provision techniques
- Output format specifications
- Version control considerations

### 5. Quality Assurance Elements

#### Validation Checklist

- Metadata completeness verification
- Tool array accuracy check
- Description placement validation
- Standards compliance review

#### Authoring Standards

- File naming conventions (kebab-case)
- Directory structure requirements
- Content organization patterns

#### Testing Recommendations

- Prompt execution testing
- Output validation procedures
- Markdown rendering verification

### 6. Acceptance Criteria

Define clear acceptance criteria for prompt quality:

- Completeness verification methods
- Clarity assessment techniques
- Markdown rendering validation
- Standards compliance checklist

### 7. Examples and Templates

Provide practical examples:

- Complete example prompt files
- Common patterns and templates
- Anti-patterns to avoid
- Troubleshooting common issues

### 8. Workflow Integration

Explain how prompt authoring fits into the development workflow:

- Creation process
- Review procedures
- Maintenance practices
- Version control integration

## Technical Requirements

- Use clear, actionable language
- Include specific examples for each concept
- Provide copy-paste templates where appropriate
- Ensure all guidance is immediately implementable
- Structure content for easy reference and navigation

## Output Format

Create a well-structured Markdown file that:

- Renders correctly in Markdown preview
- Uses consistent formatting throughout
- Includes proper heading hierarchy
- Contains actionable checklists and templates
- Follows established documentation patterns

## Quality Standards

The generated instructions must:

- Be immediately usable by prompt authors
- Maintain consistency across the repository
- Follow established documentation patterns
- Enable efficient prompt creation workflows
- Reduce common authoring errors
- Provide clear validation criteria

## Deliverable

Generate the complete `.github/instructions/create-prompt.instructions.md` file with:

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
source: ".github/prompts/prompt-file.instructions.prompt.md"
applyTo: "**/*.prompt.md"
---
```

**Important**: Use the underlying AI model (e.g., `"openai/gpt-4o@2024-11-20"`), not the interface (e.g., "github/copilot").

### Content Requirements

Following the metadata, include:

1. Complete prompt authoring instructions as specified in all requirements above
2. Comprehensive, self-contained content
3. Ready for immediate use by prompt authors throughout the repository
4. All sections, examples, templates, and checklists as detailed in the requirements

The file should be comprehensive, well-structured, and follow established documentation patterns.
