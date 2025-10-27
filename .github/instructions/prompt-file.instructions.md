---
ai_generated: true
model: "openai/gpt-4o@2024-11-20" # Corrected from "github/copilot@2025-10-15"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Generate Prompt Authoring Instructions - Create comprehensive Markdown authoring
  guidelines that help developers and prompt authors create effective, well-structured
  repository prompts following established standards.
started: "2025-10-15T14:00:00Z"
ended: "2025-10-15T14:45:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:05:00"
  - task: "content generation"
    duration: "00:35:00"
  - task: "validation and formatting"
    duration: "00:05:00"
total_duration: "00:45:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: ".github/prompts/prompt-file.instructions.prompt.md"
applyTo: "**/*.prompt.md"
---

# Prompt Authoring Instructions

This document provides comprehensive guidelines for creating effective, well-structured repository prompts that follow the Repository Prompt File Standards.

## Audience and Scope

### Target Audience

These instructions are designed for:

- **Software developers** creating repository prompts for AI-assisted workflows
- **AI prompt engineers** designing prompt templates and patterns
- **Technical writers** authoring prompt documentation
- **Contributors** to AI-assisted development workflows

### Prerequisites

Prompt authors should have:

- Basic understanding of YAML syntax and structure
- Familiarity with Markdown formatting
- Knowledge of the repository's domain and goals
- Understanding of AI-assisted development workflows

## Prompt File Structure Guide

A repository prompt file consists of two main sections:

1. **YAML Frontmatter** - Metadata and configuration
2. **Markdown Content** - The actual prompt instructions

### Complete Structure Template

```markdown
---
mode: agent|chat
model: Auto (copilot)
tools: ["create", "edit", "search"]
description: Clear, concise description of what this prompt does
prompt_metadata:
  id: unique-prompt-identifier
  title: Human-Readable Prompt Title
  owner: author-name
  repository: repository-name
  version: 1.0.0
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  output_path: path/to/output/file
  output_format: markdown|code|json|yaml
  category: prompt-category
  tags: [tag1, tag2, tag3]
---

# Prompt Title

Prompt content goes here...
```

## Field-by-Field Documentation

### Required Top-Level Fields

#### `mode`

**Purpose**: Specifies how the prompt should be executed

**Valid Values**:

- `agent` - For prompts that perform autonomous actions (file creation, editing, etc.)
- `chat` - For interactive conversational prompts

**Selection Criteria**:

- Use `agent` when the prompt will:

  - Create or modify files
  - Execute terminal commands
  - Perform automated tasks
  - Generate deliverables without user interaction

- Use `chat` when the prompt will:
  - Provide guidance or advice
  - Answer questions interactively
  - Facilitate brainstorming
  - Require ongoing user input

**Examples**:

```yaml
mode: agent  # Creates files automatically
mode: chat   # Interactive Q&A session
```

#### `model`

**Purpose**: Specifies the AI model to use for prompt execution

**Default Value**: `"anthropic/claude-3.5-sonnet@2024-10-22"`

**CRITICAL**: Always use explicit model specification for proper provenance tracking.

**Guidelines**:

- **REQUIRED**: Use explicit model format `"<provider>/<model-name>@<version>"`
- **Default for new prompts**: `"anthropic/claude-3.5-sonnet@2024-10-22"` (per `copilot-instructions.md`)
- **Why explicit format is required**: AI models cannot self-detect their identity, so "Auto (copilot)" loses provenance
- **Operators should update**: If you know the actual model being used differs from the default, update accordingly
- Can specify alternative models for specific requirements (e.g., reasoning tasks, longer context)

**Model Format Requirements**:

- Format: `"<provider>/<model-name>@<version>"`
- Examples:
  - `"openai/gpt-4o@2024-11-20"` - GPT-4o
  - `"anthropic/claude-3.5-sonnet@2024-10-22"` - Claude 3.5 Sonnet (RECOMMENDED DEFAULT)
  - `"openai/o1@2024-12-17"` - o1 reasoning model (stable)

**Examples**:

```yaml
# In a .prompt.md file - use explicit default
model: "anthropic/claude-3.5-sonnet@2024-10-22"  # Recommended default

# Alternative if you know you're using GPT-4o
model: "openai/gpt-4o@2024-11-20"

# For reasoning tasks with o1
model: "openai/o1@2024-12-17"

# ❌ WRONG - loses provenance tracking
# model: Auto (copilot)
```

**See Also**: `.github/instructions/copilot-instructions.md` § "Model Format Requirements" for complete guidance

#### `tools`

**Purpose**: Declares which tools the AI needs to accomplish the prompt's goals

**Format**: Array of tool names

**Common Tools**:

- `create` - Creating new files
- `edit` - Modifying existing files
- `search` - Searching codebase
- `read` - Reading file contents
- `run` - Running terminal commands
- `list` - Listing directories/files

**Tool Selection Methodology**:

1. **Analyze the prompt's goals**: What actions need to be performed?
2. **Identify required capabilities**: File creation? Code modification? Search?
3. **List minimal tool set**: Include only what's necessary
4. **Validate completeness**: Can all tasks be accomplished?

**Examples**:

```yaml
tools: ["create"]                    # Simple file creation
tools: ["create", "edit", "search"]  # Complex workflow
tools: ["read", "search"]            # Analysis-only prompt
```

**Validation Criteria**:

- ✅ All necessary tools are included
- ✅ No unnecessary tools are listed
- ✅ Tools align with prompt's stated goals
- ✅ Array syntax is correct

#### `description`

**Purpose**: Provides a clear, concise summary of what the prompt does

**Location**: Top-level field (NOT in prompt_metadata)

**Guidelines**:

- Write in present tense, active voice
- Be specific about the prompt's purpose
- Keep to one or two sentences
- Describe outcomes, not process
- Use action verbs

**Good Examples**:

```yaml
description: Generates comprehensive API documentation from source code comments
description: Creates unit tests for Python modules following pytest conventions
description: Analyzes security vulnerabilities in JavaScript dependencies
```

**Poor Examples**:

```yaml
description: A prompt that helps with documentation  # Too vague
description: This will create some files  # Not specific
description: Use this when you need tests  # Describes usage, not function
```

### Required prompt_metadata Fields

#### `id`

**Purpose**: Unique identifier for the prompt within the repository

**Naming Convention**: kebab-case, descriptive, unique

**Pattern**: `{domain}-{action}-{target}`

**Guidelines**:

- Use lowercase letters, numbers, and hyphens only
- Be descriptive and specific
- Ensure uniqueness across repository
- Reflect the prompt's purpose

**Examples**:

```yaml
id: api-documentation-generator
id: python-unit-test-creator
id: security-vulnerability-analyzer
id: prompt-file.instructions-prompt
```

**Anti-patterns**:

```yaml
id: prompt1              # Not descriptive
id: MyPromptFile         # Not kebab-case
id: api_doc_gen          # Use hyphens, not underscores
```

#### `title`

**Purpose**: Human-readable title displayed in listings and documentation

**Guidelines**:

- Use Title Case
- Be descriptive and clear
- Mirror the prompt's purpose
- Keep concise (5-10 words)

**Examples**:

```yaml
title: Generate API Documentation
title: Create Python Unit Tests
title: Analyze Security Vulnerabilities
title: Generate Prompt Authoring Instructions (Markdown)
```

#### `owner`

**Purpose**: Identifies the prompt's author or maintainer

**Format Options**:

- GitHub username: `github-username`
- Email-based: `name-AT-domain-com`
- Full name: `First Last`

**Guidelines**:

- Use consistent format across repository
- Make contact/attribution clear
- Update when ownership transfers

**Examples**:

```yaml
owner: johnmillerATcodemag-com
owner: jane-smith
owner: John Miller
```

#### `output_path`

**Purpose**: Specifies where the prompt's output should be saved

**Guidelines**:

- Use relative paths from repository root
- Include full filename with extension
- Create logical directory structures
- Follow repository conventions

**Common Patterns**:

```yaml
output_path: .github/instructions/feature-name.instructions.md
output_path: docs/generated/api-documentation.md
output_path: tests/unit/test_module_name.py
output_path: src/components/ComponentName.tsx
```

**Path Conventions**:

- Instructions: `.github/instructions/`
- Documentation: `docs/` or `documentation/`
- Code: Follow language conventions (`src/`, `lib/`, etc.)
- Tests: `tests/`, `test/`, or `__tests__/`

#### `output_format`

**Purpose**: Declares the format of the generated output

**Common Values**:

- `markdown` - Documentation, instructions, guides
- `code` - Source code files
- `json` - Configuration, data files
- `yaml` - Config files, metadata
- `typescript` - TypeScript source
- `python` - Python source
- `html` - Web pages, templates

**Examples**:

```yaml
output_format: markdown  # For .md files
output_format: python    # For .py files
output_format: json      # For .json files
```

#### `tags`

**Purpose**: Categorizes and enables discovery of prompts

**Format**: Array of lowercase, hyphenated strings

**Guidelines**:

- Use 3-7 relevant tags
- Include technology names
- Add functional categories
- Use consistent vocabulary

**Tag Categories**:

- **Technology**: `python`, `typescript`, `react`, `docker`
- **Function**: `testing`, `documentation`, `security`, `deployment`
- **Domain**: `api`, `database`, `frontend`, `backend`
- **Type**: `code-generation`, `analysis`, `refactoring`

**Examples**:

```yaml
tags: [prompt-engineering, documentation, authoring-guidelines, standards]
tags: [python, testing, unit-tests, pytest]
tags: [security, vulnerability-analysis, dependency-scanning]
```

### Optional prompt_metadata Fields

#### `repository`

**Purpose**: References the repository this prompt belongs to

**Format**: Repository name or full GitHub path

**Examples**:

```yaml
repository: AI-Assisted-Brownfield-Development
repository: owner/repo-name
```

#### `version`

**Purpose**: Tracks prompt evolution using semantic versioning

**Format**: `MAJOR.MINOR.PATCH`

**Versioning Guidelines**:

- **MAJOR** (1.0.0 → 2.0.0): Breaking changes, complete rewrites
- **MINOR** (1.0.0 → 1.1.0): New features, significant enhancements
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, minor improvements

**Examples**:

```yaml
version: 1.0.0  # Initial release
version: 1.2.3  # Mature, stable version
version: 2.0.0  # Major revision
```

#### `created` / `updated`

**Purpose**: Tracks prompt lifecycle dates

**Format**: `YYYY-MM-DD`

**Guidelines**:

- `created`: Set once, never changes
- `updated`: Update with each modification
- Use ISO 8601 date format
- Keep dates current

**Examples**:

```yaml
created: 2025-10-15
updated: 2025-10-15
```

#### `category`

**Purpose**: High-level classification of prompt function

**Common Categories**:

- `code-generation` - Creates source code
- `documentation` - Generates docs
- `testing` - Test creation/analysis
- `security` - Security-related tasks
- `refactoring` - Code improvement
- `analysis` - Code/system analysis
- `meta-documentation` - Documentation about documentation

**Examples**:

```yaml
category: meta-documentation
category: code-generation
category: security-analysis
```

## Best Practices Guidelines

### Metadata Structure Organization

#### Top-Level vs prompt_metadata

**Top-Level Fields** (execution configuration):

- `mode` - How the prompt runs
- `model` - Which AI model to use
- `tools` - What capabilities are needed
- `description` - What the prompt does

**prompt_metadata Fields** (informational metadata):

- Everything else (id, title, owner, version, etc.)

#### Field Ordering Convention

```yaml
# Recommended order for consistency
---
mode: agent
model: Auto (copilot)
tools: ["create", "edit"]
description: Brief description here
prompt_metadata:
  id: prompt-identifier
  title: Prompt Title
  owner: author-name
  repository: repo-name
  version: 1.0.0
  created: 2025-10-15
  updated: 2025-10-15
  output_path: path/to/output
  output_format: markdown
  category: category-name
  tags: [tag1, tag2, tag3]
---
```

#### YAML Formatting Standards

- Use 2-space indentation
- Quote string values containing special characters
- Use array notation `[item1, item2]` for short lists
- Use block notation for long lists:
  ```yaml
  tools:
    - create
    - edit
    - search
  ```
- Maintain consistent spacing
- No trailing whitespace

### Tool Selection Best Practices

#### Analysis Methodology

1. **Read the prompt content**: What tasks are described?
2. **Identify actions**: List all operations needed
3. **Map to tools**: Match actions to available tools
4. **Minimize tool set**: Remove redundant tools
5. **Validate**: Ensure all goals are achievable

#### Tool Array Construction

**Decision Tree**:

```
Will files be created? → Add "create"
Will files be modified? → Add "edit"
Need to find code/files? → Add "search"
Need to read files? → Add "read"
Need to run commands? → Add "run"
Need directory listings? → Add "list"
```

**Example Analysis**:

Prompt Goal: "Create unit tests for existing Python modules"

1. Need to find existing modules → `search`
2. Need to read module code → `read`
3. Need to create test files → `create`

Result: `tools: ["search", "read", "create"]`

#### Common Tool Combinations

```yaml
# File creation only
tools: ["create"]

# Code modification workflow
tools: ["search", "read", "edit"]

# Analysis and documentation
tools: ["search", "read", "create"]

# Complex refactoring
tools: ["search", "read", "edit", "run"]

# Deployment/build
tools: ["read", "edit", "run"]
```

### Mode Specification Guidelines

#### Selection Criteria Decision Flowchart

```
Does the prompt produce files as output?
  ├─ YES → Does it require user input during execution?
  │         ├─ NO → Use mode: agent
  │         └─ YES → Use mode: chat (guide user to create files)
  └─ NO → Is it purely conversational/advisory?
            ├─ YES → Use mode: chat
            └─ NO → Reconsider prompt design
```

#### Use Case Examples

**Agent Mode Examples**:

- Generate API documentation from code
- Create test files from specifications
- Build configuration files
- Generate migration scripts
- Create component boilerplate

**Chat Mode Examples**:

- Answer questions about best practices
- Provide architecture guidance
- Help debug issues interactively
- Explain complex code
- Brainstorm solutions

### Content Guidelines

#### Clarity and Specificity Requirements

**Be Explicit About**:

- What should be generated
- Where output should go
- What format to use
- What standards to follow
- What to include/exclude

**Example - Vague**:

```markdown
Create some tests for the code.
```

**Example - Specific**:

```markdown
Create comprehensive unit tests for all Python modules in `src/`,
following pytest conventions, with minimum 80% code coverage,
saving tests to `tests/unit/test_{module_name}.py`.
```

#### Context Provision Techniques

**Provide Context About**:

1. **Repository structure**: Where files are located
2. **Coding standards**: What conventions to follow
3. **Dependencies**: What libraries/frameworks are used
4. **Target audience**: Who will use the output
5. **Quality criteria**: How to judge success

**Context Template**:

```markdown
## Context

This repository uses [framework/language] with [dependencies].
Code follows [coding standard] conventions.
Output will be used by [audience] for [purpose].

## Environment

- Language: [language] [version]
- Framework: [framework] [version]
- Build system: [system]
- Testing framework: [framework]
```

#### Output Format Specifications

**Be Specific About**:

- File structure and organization
- Naming conventions
- Code style and formatting
- Documentation requirements
- Error handling patterns

**Example Specification**:

```markdown
## Output Format

Generate Python code that:

- Follows PEP 8 style guidelines
- Includes comprehensive docstrings (Google style)
- Uses type hints for all functions
- Implements error handling with custom exceptions
- Includes inline comments for complex logic
```

#### Version Control Considerations

**Include Guidance On**:

- Whether to update existing files or create new ones
- How to handle conflicts
- What commit messages to suggest
- Whether to create branches

**Example**:

```markdown
## Version Control

- Create new files; do not modify existing code
- Use descriptive commit message: "Add unit tests for [module]"
- Suggest branch name: feature/tests-[module-name]
```

## Quality Assurance Elements

### Validation Checklist

Use this checklist before submitting a prompt:

#### Metadata Completeness

- [ ] All required top-level fields are present (mode, model, tools, description)
- [ ] All required prompt_metadata fields are present (id, title, owner, output_path, output_format, tags)
- [ ] Description is at top-level, NOT in prompt_metadata
- [ ] Optional fields are included where appropriate
- [ ] All field values are properly formatted

#### Tool Array Accuracy

- [ ] All necessary tools are included
- [ ] No unnecessary tools are listed
- [ ] Tools align with prompt's stated goals
- [ ] Array syntax is correct

#### Description Placement

- [ ] Description is a top-level field
- [ ] Description is clear and concise
- [ ] Description accurately reflects prompt function

#### Standards Compliance

- [ ] YAML frontmatter is valid
- [ ] Field names match specifications exactly
- [ ] Values follow formatting guidelines
- [ ] File naming follows kebab-case convention

### Authoring Standards

#### File Naming Conventions

**Pattern**: `{domain}-{action}-{target}.prompt.md`

**Rules**:

- Use kebab-case (lowercase with hyphens)
- Include `.prompt.md` extension
- Be descriptive and specific
- Avoid abbreviations unless widely known

**Examples**:

```
api-documentation-generator.prompt.md
python-unit-test-creator.prompt.md
security-vulnerability-analyzer.prompt.md
prompt-file.instructions.prompt.md
```

**Anti-patterns**:

```
prompt1.md                    # Not descriptive
ApiDocGen.prompt.md          # Not kebab-case
api_doc_generator.prompt.md  # Use hyphens, not underscores
```

#### Directory Structure Requirements

**Standard Locations**:

```
repository-root/
├── .github/
│   ├── prompts/              # Prompt files go here
│   │   ├── *.prompt.md
│   └── instructions/         # Generated instructions
│       ├── *.instructions.md
├── docs/                     # User-facing documentation
└── src/                      # Source code
```

**Guidelines**:

- Store prompts in `.github/prompts/`
- Generate instructions to `.github/instructions/`
- Keep output separate from prompts
- Use subdirectories for organization if needed

#### Content Organization Patterns

**Recommended Prompt Structure**:

```markdown
---
[YAML frontmatter]
---

# [Prompt Title]

[Brief introduction to what this prompt does]

## Context

[Background information, repository structure, conventions]

## Target Audience

[Who will use the output, what they need to know]

## Requirements

[Detailed requirements for the output]

### [Requirement Category 1]

[Specific requirements]

### [Requirement Category 2]

[Specific requirements]

## Technical Requirements

[Technical specifications, constraints, dependencies]

## Output Format

[Detailed format specifications]

## Quality Standards

[Acceptance criteria, quality metrics]

## Deliverable

[Clear statement of what should be produced]
```

### Testing Recommendations

#### Prompt Execution Testing

**Test Process**:

1. Execute prompt in clean environment
2. Verify all files are created as specified
3. Check file contents match requirements
4. Validate output format and structure
5. Ensure quality standards are met

**Test Checklist**:

- [ ] Prompt executes without errors
- [ ] Output files are created in correct locations
- [ ] Output format matches specification
- [ ] Content quality meets standards
- [ ] All requirements are addressed

#### Output Validation Procedures

**Validation Steps**:

1. **Structural Validation**:

   - Files created in correct locations
   - Naming conventions followed
   - Directory structure correct

2. **Content Validation**:

   - All required sections present
   - Content is complete and accurate
   - Format specifications followed

3. **Quality Validation**:
   - Meets quality standards
   - No errors or inconsistencies
   - Appropriate level of detail

#### Markdown Rendering Verification

**Check**:

- [ ] Markdown renders correctly in preview
- [ ] Headings hierarchy is logical
- [ ] Code blocks have proper syntax highlighting
- [ ] Links are valid and functional
- [ ] Tables render properly
- [ ] Lists are formatted correctly

**Tools**:

- VS Code Markdown preview
- GitHub Markdown preview
- Markdown linters

## Acceptance Criteria

### Completeness Verification

**A complete prompt includes**:

✅ **Valid YAML Frontmatter**:

- All required fields present
- Correct field placement (description at top-level)
- Proper YAML syntax

✅ **Clear Prompt Content**:

- Well-defined objective
- Adequate context
- Specific requirements
- Clear deliverables

✅ **Appropriate Metadata**:

- Unique, descriptive ID
- Meaningful title
- Correct owner attribution
- Accurate output_path
- Relevant tags

✅ **Tool Configuration**:

- Correct mode selection
- Complete tool array
- Validated tool needs

### Clarity Assessment

**Clarity Criteria**:

✅ **Purpose is Immediately Clear**:

- Description explains what the prompt does
- Title is descriptive
- Content supports the stated purpose

✅ **Requirements are Specific**:

- No ambiguous language
- Clear acceptance criteria
- Specific output format

✅ **Context is Sufficient**:

- Enough information to execute successfully
- Relevant background provided
- Standards and conventions specified

### Standards Compliance Checklist

**YAML Frontmatter**:

- [ ] mode: agent or chat
- [ ] model: Auto (copilot) or specified
- [ ] tools: [array of tools]
- [ ] description: Clear description (TOP-LEVEL)
- [ ] prompt_metadata: Contains all required fields

**prompt_metadata Section**:

- [ ] id: unique-identifier
- [ ] title: Human Readable Title
- [ ] owner: author-name
- [ ] output_path: path/to/output
- [ ] output_format: appropriate format
- [ ] tags: [relevant, tags]

**File and Path Standards**:

- [ ] Filename uses kebab-case
- [ ] File has .prompt.md extension
- [ ] Located in .github/prompts/
- [ ] output_path follows conventions

**Content Standards**:

- [ ] Clear objective stated
- [ ] Adequate context provided
- [ ] Specific requirements listed
- [ ] Quality criteria defined
- [ ] Deliverable clearly specified

## Examples and Templates

### Complete Example: Documentation Generator

`````markdown
---
mode: agent
model: Auto (copilot)
tools: ["search", "read", "create"]
description: Generates comprehensive API documentation from TypeScript source code with JSDoc comments
prompt_metadata:
  id: typescript-api-documentation-generator
  title: Generate TypeScript API Documentation
  owner: jane-smith
  repository: enterprise-api-project
  version: 1.2.0
  created: 2025-01-15
  updated: 2025-10-15
  output_path: docs/api/api-reference.md
  output_format: markdown
  category: documentation
  tags: [typescript, api, documentation, jsdoc, code-generation]
---

# Generate TypeScript API Documentation

Create comprehensive API documentation from TypeScript source code, extracting information from JSDoc comments and type definitions.

## Context

This repository contains a TypeScript-based REST API with extensive JSDoc documentation. The codebase follows these conventions:

- **Language**: TypeScript 5.x
- **API Framework**: Express.js
- **Documentation**: JSDoc comments on all public interfaces
- **Code Location**: `src/api/` directory
- **Style**: Airbnb TypeScript style guide

## Target Audience

- API consumers (frontend developers, integration partners)
- Backend developers maintaining the API
- Technical writers updating documentation

## Requirements

### Documentation Structure

Generate documentation with the following sections:

1. **Overview**: API purpose and capabilities
2. **Authentication**: Auth methods and requirements
3. **Endpoints**: Complete endpoint reference
4. **Data Models**: Request/response schemas
5. **Error Handling**: Error codes and messages
6. **Examples**: Code examples for common operations

### Endpoint Documentation

For each endpoint, include:

- HTTP method and path
- Description and purpose
- Authentication requirements
- Request parameters (path, query, body)
- Response format and status codes
- Example request and response
- Error scenarios

### Data Model Documentation

For each model, include:

- Model name and description
- All properties with types
- Required vs optional fields
- Validation rules
- Example JSON representation

## Technical Requirements

- Extract information from JSDoc `@param`, `@returns`, `@throws` tags
- Parse TypeScript type definitions and interfaces
- Generate valid Markdown with proper formatting
- Include syntax highlighting for code examples
- Create anchor links for easy navigation

## Output Format

````markdown
# API Reference

## Overview

[Generated overview]

## Authentication

[Auth documentation]

## Endpoints

### [HTTP METHOD] /path/to/endpoint

[Description]

**Authentication**: Required/Optional

**Parameters**:

- `param1` (type): Description
- `param2` (type, optional): Description

**Request Body**:

```json
{example}
```
````
`````

`````

**Response** (200 OK):

```json
{example}
```

**Errors**:

- 400: Bad Request - [description]
- 401: Unauthorized - [description]

## Data Models

### ModelName

[Description]

**Properties**:

- `property1` (type, required): Description
- `property2` (type, optional): Description

**Example**:

```json
{example}
```

```

## Quality Standards

- Complete coverage of all public endpoints
- Accurate type information
- Runnable code examples
- Clear, professional writing
- Valid Markdown formatting

## Deliverable

A single `docs/api/api-reference.md` file containing complete API documentation, ready for publication and use by API consumers.
```

### Complete Example: Test Generator

````markdown
---
mode: agent
model: Auto (copilot)
tools: ["search", "read", "create"]
description: Creates comprehensive Jest unit tests for React components with 80%+ coverage
prompt_metadata:
  id: react-component-test-generator
  title: Generate React Component Unit Tests
  owner: johnmillerATcodemag-com
  repository: react-dashboard-app
  version: 1.0.0
  created: 2025-10-15
  updated: 2025-10-15
  output_path: src/components/__tests__/ComponentName.test.tsx
  output_format: typescript
  category: testing
  tags: [react, typescript, testing, jest, unit-tests, code-generation]
---

# Generate React Component Unit Tests

Create comprehensive Jest unit tests for React components, achieving minimum 80% code coverage with tests for props, state, events, and edge cases.

## Context

This React application uses:

- **Framework**: React 18 with TypeScript
- **Testing**: Jest + React Testing Library
- **State**: React Hooks (useState, useEffect, useContext)
- **Styling**: CSS Modules
- **Location**: Components in `src/components/`

## Target Audience

Frontend developers maintaining the React application who need reliable tests for component functionality.

## Requirements

### Test Coverage

Generate tests covering:

1. **Rendering**: Component renders without errors
2. **Props**: All prop variations and combinations
3. **State**: State changes and updates
4. **Events**: User interactions (clicks, inputs, etc.)
5. **Hooks**: useEffect dependencies and cleanup
6. **Conditional Rendering**: All conditional paths
7. **Edge Cases**: Null/undefined props, empty states
8. **Accessibility**: ARIA labels and roles

### Test Structure

Organize tests using:

```typescript
describe("ComponentName", () => {
  describe("Rendering", () => {
    it("renders without crashing", () => {});
    it("renders with required props", () => {});
  });

  describe("Props", () => {
    it("handles prop X correctly", () => {});
  });

  describe("User Interactions", () => {
    it("handles click events", () => {});
  });

  describe("Edge Cases", () => {
    it("handles null props gracefully", () => {});
  });
});
```
`````

## Technical Requirements

- Use React Testing Library queries (getByRole, getByText, etc.)
- Use userEvent for interaction testing
- Mock external dependencies and API calls
- Clean up after each test (cleanup, jest.clearAllMocks)
- Use TypeScript type definitions
- Follow AAA pattern (Arrange, Act, Assert)

## Output Format

```typescript
import React from "react";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ComponentName } from "../ComponentName";

describe("ComponentName", () => {
  describe("Rendering", () => {
    it("renders without crashing", () => {
      render(<ComponentName />);
      expect(screen.getByRole("...")).toBeInTheDocument();
    });
  });

  // Additional test groups...
});
```

## Quality Standards

- Minimum 80% code coverage
- All user-facing functionality tested
- Tests are maintainable and readable
- No false positives or flaky tests
- Tests run in under 5 seconds

## Deliverable

A complete test file at `src/components/__tests__/ComponentName.test.tsx` with comprehensive test coverage for the specified component.

````

### Common Patterns

#### Pattern: Code Generator

```yaml
mode: agent
tools: ["search", "read", "create"]
description: [What code to generate and where]
prompt_metadata:
  output_format: [language]
  category: code-generation
  tags: [language, framework, code-generation, ...]
````

#### Pattern: Documentation Generator

```yaml
mode: agent
tools: ["search", "read", "create"]
description: [What documentation to generate from what source]
prompt_metadata:
  output_format: markdown
  category: documentation
  tags: [documentation, ...]
```

#### Pattern: Analysis Tool

```yaml
mode: agent
tools: ["search", "read", "create"]
description: [What to analyze and what report to produce]
prompt_metadata:
  output_format: markdown
  category: analysis
  tags: [analysis, ...]
```

#### Pattern: Interactive Assistant

```yaml
mode: chat
tools: ["search", "read"]
description: [What guidance or assistance to provide]
prompt_metadata:
  category: guidance
  tags: [interactive, ...]
```

### Anti-patterns to Avoid

#### ❌ Description in Wrong Location

```yaml
# WRONG - description inside prompt_metadata
prompt_metadata:
  id: my-prompt
  description: Does something # ❌ Wrong location
```

```yaml
# CORRECT - description at top level
description: Does something # ✅ Correct location
prompt_metadata:
  id: my-prompt
```

#### ❌ Incomplete Tool Array

```yaml
# Prompt creates files but tools array is incomplete
description: Creates and modifies configuration files
tools: ["create"] # ❌ Missing "edit" tool
```

```yaml
# CORRECT
description: Creates and modifies configuration files
tools: ["create", "edit"] # ✅ Complete tool set
```

#### ❌ Vague Descriptions

```yaml
description: A helpful prompt # ❌ Too vague
```

```yaml
description: Generates TypeScript interfaces from JSON schemas # ✅ Specific
```

#### ❌ Wrong Mode Selection

```yaml
# Prompt that generates files uses chat mode
mode: chat # ❌ Should be agent
description: Creates unit test files
tools: ["create"]
```

```yaml
# CORRECT
mode: agent # ✅ Correct for file generation
description: Creates unit test files
tools: ["create"]
```

#### ❌ Non-unique IDs

```yaml
id: test-generator # ❌ Too generic, likely conflicts
```

```yaml
id: react-jest-unit-test-generator # ✅ Specific and unique
```

### Troubleshooting Common Issues

#### Issue: Prompt doesn't execute

**Symptoms**: Prompt fails to run or produces errors

**Diagnosis**:

- Check YAML syntax (use a YAML validator)
- Verify all required fields are present
- Ensure description is at top-level, not in prompt_metadata
- Check tool array syntax

**Solution**:

```yaml
# Use YAML validator
# Verify structure matches template
# Check for typos in field names
```

#### Issue: Wrong files are created

**Symptoms**: Output appears in unexpected locations

**Diagnosis**:

- Check output_path value
- Verify path is relative to repository root
- Ensure directory separators are correct

**Solution**:

```yaml
output_path: .github/instructions/file.md # Use forward slashes
```

#### Issue: Tools missing capabilities

**Symptoms**: Prompt cannot accomplish stated goals

**Diagnosis**:

- Review tools array
- Compare required actions to available tools
- Check for missing tools

**Solution**:

```yaml
# Add all necessary tools
tools: ["search", "read", "create", "edit"]
```

## Workflow Integration

### Creation Process

1. **Plan the Prompt**:

   - Define clear objectives
   - Identify required tools
   - Determine output format

2. **Create Prompt File**:

   - Use kebab-case filename
   - Place in `.github/prompts/`
   - Follow structure template

3. **Write Frontmatter**:

   - Add required top-level fields
   - Complete prompt_metadata section
   - Validate YAML syntax

4. **Author Content**:

   - Provide clear context
   - Specify detailed requirements
   - Define quality standards
   - State clear deliverable

5. **Validate**:
   - Run through validation checklist
   - Test YAML parsing
   - Verify completeness

### Review Procedures

**Self-Review Checklist**:

- [ ] Re-read prompt for clarity
- [ ] Verify metadata completeness
- [ ] Check YAML syntax
- [ ] Validate tool selection
- [ ] Test prompt execution
- [ ] Review generated output

**Peer Review Focus**:

- Clarity and completeness
- Standards compliance
- Tool selection appropriateness
- Output quality
- Metadata accuracy

### Maintenance Practices

**When to Update**:

- Requirements change
- Output format evolves
- Tools become available/deprecated
- Standards are updated
- Issues are discovered

**Update Process**:

1. Modify prompt content or metadata
2. Increment version number appropriately
3. Update `updated` date
4. Test changes
5. Document changes in comments or commit message

**Version Control**:

```yaml
# Initial version
version: 1.0.0
created: 2025-10-15
updated: 2025-10-15

# After bug fix
version: 1.0.1
updated: 2025-10-20

# After new feature
version: 1.1.0
updated: 2025-11-01
```

### Version Control Integration

**Commit Messages**:

```
Add prompt: [prompt-title]
Update prompt: [prompt-title] - [what changed]
Fix prompt: [prompt-title] - [what was fixed]
```

**Branch Naming**:

```
feature/prompt-[domain-action-target]
fix/prompt-[prompt-id]
docs/prompt-[prompt-id]
```

**Pull Request Template**:

```markdown
## Prompt Changes

**Prompt**: [prompt-title]
**Type**: New / Update / Fix
**Version**: [version]

### Changes Made

- [List changes]

### Testing

- [ ] Prompt executes successfully
- [ ] Output meets requirements
- [ ] Metadata is complete
- [ ] YAML is valid

### Checklist

- [ ] Follows authoring guidelines
- [ ] All required fields present
- [ ] Description at top-level
- [ ] Tools array is complete
- [ ] Version and dates updated
```

## Quick Reference

### Minimal Valid Prompt

```yaml
---
mode: agent
model: Auto (copilot)
tools: ["create"]
description: Creates a simple example file
prompt_metadata:
  id: simple-example
  title: Simple Example
  owner: author-name
  output_path: examples/example.md
  output_format: markdown
  tags: [example]
---
# Simple Example

Create a file at `examples/example.md` with "Hello, World!" content.
```

### Field Quick Reference

| Field         | Location  | Required | Format      | Example            |
| ------------- | --------- | -------- | ----------- | ------------------ |
| mode          | Top-level | ✅       | agent\|chat | agent              |
| model         | Top-level | ✅       | string      | Auto (copilot)     |
| tools         | Top-level | ✅       | array       | ["create", "edit"] |
| description   | Top-level | ✅       | string      | Generates API docs |
| id            | metadata  | ✅       | kebab-case  | api-doc-generator  |
| title         | metadata  | ✅       | Title Case  | Generate API Docs  |
| owner         | metadata  | ✅       | string      | john-smith         |
| output_path   | metadata  | ✅       | path        | docs/api.md        |
| output_format | metadata  | ✅       | string      | markdown           |
| tags          | metadata  | ✅       | array       | [api, docs]        |
| repository    | metadata  | ⭕       | string      | my-repo            |
| version       | metadata  | ⭕       | semver      | 1.0.0              |
| created       | metadata  | ⭕       | YYYY-MM-DD  | 2025-10-15         |
| updated       | metadata  | ⭕       | YYYY-MM-DD  | 2025-10-15         |
| category      | metadata  | ⭕       | string      | documentation      |

### Tool Selection Guide

| Goal                    | Tools Needed                 |
| ----------------------- | ---------------------------- |
| Create new files        | ["create"]                   |
| Modify existing files   | ["read", "edit"]             |
| Find and modify code    | ["search", "read", "edit"]   |
| Analyze codebase        | ["search", "read"]           |
| Generate docs from code | ["search", "read", "create"] |
| Run tests               | ["read", "run"]              |
| Build/deploy            | ["read", "edit", "run"]      |

---

## Post-Creation Requirements

After creating or modifying any `.prompt.md` file, follow the AI chat logging workflow as defined in [`.github/instructions/ai/ai-assisted-output.instructions.md`](ai/ai-assisted-output.instructions.md#ai-chat-logging-workflow).

### Prompt-Specific Requirements

**Update Conversation Log**:
Add to `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md`:

```markdown
**Artifacts Produced**:
- `.github/prompts/<path>/<filename>.prompt.md` - <Brief description of what the prompt does>
```

**Update README.md**:
Add entry to appropriate section based on prompt type:

- **Meta-prompts**: Add to "Meta-Prompts (Prompt Generators)" section
- **Instruction-generating prompts**: Link to generated instruction file in "Guidance & Instructions"
- **Other notable prompts**: Add to "Notable Artifacts" section

See examples in [README.md](../../README.md) for formatting.

### Verification Checklist

Before completing your work, verify:

- [ ] Prompt file created/updated with complete YAML front matter
- [ ] AI conversation log updated with new artifact entry
- [ ] README.md updated with appropriate link and description
- [ ] Chat log link points to correct `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md`
- [ ] All links are valid and use correct relative paths
- [ ] Description is clear and concise

See [complete post-creation workflow](ai/ai-assisted-output.instructions.md#ai-chat-logging-workflow) for detailed requirements and policy compliance.

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-15
**Maintainer**: AI-Assisted Development Team
**Feedback**: Submit issues or suggestions via repository issues
