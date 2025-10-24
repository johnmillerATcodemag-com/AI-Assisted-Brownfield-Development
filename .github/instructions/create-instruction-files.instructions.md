---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "create-instruction-guide-20251023"
prompt: |
  create an instruction file to guide the creation of new instruction fiules
started: "2025-10-23T10:00:00Z"
ended: "2025-10-23T10:15:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:05:00"
  - task: "instruction file creation"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/23/create-instruction-guide-20251023/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.instructions.md"
---

# Creating New Instruction Files

## Overview

This document provides comprehensive guidance for creating new instruction files in the repository. Instruction files (`.instructions.md`) provide guidance for specific domains, processes, or tools to ensure consistency and quality.

**Target Audience**: Developers, AI assistants, and contributors creating guidance documentation

**Related Documentation**:

- [AI-Assisted Output Instructions](.github/instructions/ai-assisted-output.instructions.md)
- [Copilot Instructions](.github/instructions/copilot-instructions.md)
- [Instruction Prompt Requirements](.github/instructions/ai/instruction-prompt.instructions.md)

## Table of Contents

- [When to Create Instruction Files](#when-to-create-instruction-files)
- [File Structure Requirements](#file-structure-requirements)
- [Content Guidelines](#content-guidelines)
- [Creation Process](#creation-process)
- [Quality Standards](#quality-standards)
- [Common Patterns](#common-patterns)
- [AI-Specific Considerations](#ai-specific-considerations)
- [Integration Requirements](#integration-requirements)
- [Validation Checklist](#validation-checklist)
- [Common Mistakes](#common-mistakes)
- [Examples](#examples)

## When to Create Instruction Files

Create instruction files when you need to:

- **Standardize processes**: Define consistent approaches for common tasks
- **Guide AI behavior**: Provide specific instructions for AI assistants
- **Document best practices**: Capture proven approaches for reuse
- **Ensure compliance**: Define requirements for specific domains
- **Reduce ambiguity**: Clarify expectations for complex activities

### Examples of Good Instruction Files

- `code-review.instructions.md` - Guidelines for conducting code reviews
- `api-documentation.instructions.md` - Standards for documenting APIs
- `vertical-slice-architecture.instructions.md` - Implementing architectural patterns
- `ai-assisted-output.instructions.md` - AI provenance requirements

## File Structure Requirements

### 1. Location and Naming

**Standard Location**: `.github/instructions/`
**AI-Optimized Location**: `.github/instructions/ai/` (for token-optimized versions)

**Naming Convention**: `<domain>.instructions.md`

**Examples**:

- `testing.instructions.md`
- `deployment.instructions.md`
- `code-style.instructions.md`
- `security-review.instructions.md`

### 2. Required YAML Front Matter

All instruction files MUST include complete AI provenance metadata:

```yaml
---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "unique-chat-identifier"
prompt: |
  Original prompt text that created this file
started: "2025-10-23T10:00:00Z"
ended: "2025-10-23T10:15:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:05:00"
  - task: "content creation"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/23/chat-id/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{ext}" # Optional: when to auto-apply
---
```

**Field Requirements**:

- `ai_generated`: Always `true` for AI-created files
- `model`: Use `provider/model@version` format (e.g., `"anthropic/claude-3.5-sonnet@2024-10-22"`)
- `operator`: GitHub username (e.g., `"johnmillerATcodemag-com"`)
- `chat_id`: Unique identifier for the conversation
- `prompt`: Exact prompt text that initiated creation
- `started`/`ended`: ISO8601 timestamps
- `task_durations`: Breakdown of work activities
- `total_duration`: Sum of all task durations
- `ai_log`: Path to conversation log
- `source`: What created this file (username or prompt file path)
- `applyTo`: Optional glob pattern for when to apply instructions

### 3. Required Content Structure

```markdown
# [Title]

## Overview

Brief description of what this instruction file covers and its purpose.

**Target Audience**: Who should use these instructions
**Scope**: What domains/activities these instructions apply to

**Related Documentation**:

- [Link to related instruction file](path)
- [Link to another related file](path)

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)
- [Quality Checklist](#quality-checklist)

## [Main Sections]

### Clear, actionable guidance organized by topic

## Quality Checklist

- [ ] Requirement 1 met
- [ ] Requirement 2 met
- [ ] All standards followed

## Examples

Concrete examples demonstrating the instructions.
```

## Content Guidelines

### 1. Writing Principles

**Be Specific and Actionable**:

- ✅ "Use semantic commit messages following conventional commits format"
- ❌ "Write good commit messages"

**Provide Examples**:

```markdown
**Example**: Semantic Commit Message
```

feat(auth): add OAuth2 integration

Implement OAuth2 authentication flow with Google provider

- Add OAuth2 configuration
- Create authentication middleware
- Update user model with external ID

Closes #123

```

```

**Use Clear Structure**:

- Start with overview and context
- Organize content logically
- Include quality checklist
- Provide concrete examples

### 2. Content Organization

**Standard Sections**:

1. **Overview** - Purpose, audience, scope
2. **Requirements** - What must be done
3. **Guidelines** - How to do it well
4. **Examples** - Concrete demonstrations
5. **Quality Checklist** - Validation criteria
6. **Common Mistakes** - What to avoid
7. **References** - Related documentation

### 3. Target Audience Considerations

**For Human Developers**:

- Provide rationale and context
- Include learning resources
- Explain trade-offs and decisions
- Use educational tone

**For AI Assistants**:

- Use imperative commands
- Provide explicit rules
- Include validation checklists
- Use structured formats (YAML, JSON)
- Minimize explanatory prose

## Creation Process

### Method 1: Using Meta-Prompt (Recommended)

1. **Submit Meta-Prompt**: Use `.github/prompts/meta/create-instruction-prompt.prompt.md`
2. **Specify Domain**: Clearly define the instruction domain
3. **Review Generated Prompt**: Ensure it meets requirements
4. **Execute Prompt**: Run the generated prompt to create instructions
5. **Validate Output**: Check against quality criteria

### Method 2: Manual Creation

1. **Plan Content**: Define scope, audience, and key requirements
2. **Create File**: Use naming convention in correct location
3. **Add Metadata**: Include complete AI provenance front matter
4. **Write Content**: Follow content guidelines and structure
5. **Review**: Validate against quality checklist
6. **Update Documentation**: Add to README.md and related files

### Method 3: Copy and Adapt

1. **Find Similar File**: Locate existing instruction file with similar scope
2. **Copy Structure**: Use as template for new file
3. **Update Metadata**: Change all provenance fields appropriately
4. **Adapt Content**: Modify for new domain while keeping structure
5. **Validate**: Ensure all references and examples are correct

## Quality Standards

### Content Quality

- [ ] **Clear Purpose**: Instructions have well-defined scope and objectives
- [ ] **Actionable Guidance**: Specific, implementable requirements and steps
- [ ] **Complete Coverage**: All important aspects of domain are addressed
- [ ] **Consistent Structure**: Follows standard organization patterns
- [ ] **Concrete Examples**: Real examples demonstrate key concepts
- [ ] **Quality Criteria**: Measurable validation requirements provided

### Technical Quality

- [ ] **Complete Metadata**: All 11 required provenance fields present
- [ ] **Correct Format**: YAML front matter, markdown content
- [ ] **Valid Links**: All internal links work correctly
- [ ] **Proper Location**: File in correct directory with right name
- [ ] **Unique Content**: No duplicate or conflicting instructions

### Process Quality

- [ ] **Conversation Log**: AI log file created and linked
- [ ] **Summary Created**: Session summary with resumability context
- [ ] **README Updated**: New file added to appropriate section
- [ ] **Git Integration**: File committed with semantic commit message

## Common Patterns

### Pattern 1: Process Instructions

For step-by-step processes:

```markdown
## Process Overview

1. **Step 1**: [Action]

   - Requirement A
   - Requirement B

2. **Step 2**: [Action]
   - Requirement C
   - Requirement D

## Quality Gates

- [ ] Step 1 completed successfully
- [ ] Step 2 validation passed
```

### Pattern 2: Standard Templates

For creating standardized artifacts:

````markdown
## Template Structure

### Required Sections

```markdown
# [Title]

## [Section 1]

Content requirements...

## [Section 2]

Content requirements...
```
````

````

### Pattern 3: Validation Rules

For quality and compliance checking:

```markdown
## Validation Rules

### Rule 1: [Category]
- **Requirement**: Specific requirement
- **Validation**: How to check
- **Examples**: ✅ Good / ❌ Bad

### Rule 2: [Category]
- **Requirement**: Another requirement
````

## AI-Specific Considerations

### For AI-Targeted Instructions

When creating instructions specifically for AI assistants:

**Use Imperative Language**:

- ✅ "Generate code following these patterns..."
- ❌ "You might want to consider..."

**Provide Explicit Rules**:

```markdown
## Rules

1. **MUST**: Always include error handling
2. **MUST NOT**: Use deprecated APIs
3. **SHOULD**: Include comprehensive tests
```

**Include Validation Checklists**:

```markdown
## Pre-Generation Checklist

- [ ] Requirements understood
- [ ] Dependencies identified
- [ ] Architecture validated

## Post-Generation Checklist

- [ ] Code compiles
- [ ] Tests pass
- [ ] Documentation updated
```

### AI-Optimized Versions

For frequently-used AI instructions, create optimized versions:

1. **Create Standard Version**: Full instruction file for humans
2. **Create AI Version**: Token-optimized in `.github/instructions/ai/`
3. **Cross-Reference**: Link between versions
4. **Maintain Sync**: Keep both versions aligned

**Optimization Techniques**:

- Remove explanatory prose
- Use YAML/JSON schemas instead of examples
- Combine related rules
- Use shorthand notation
- Focus on actionable directives

## Integration Requirements

### 1. README Updates

Add new instruction files to appropriate README section:

```markdown
### Guidance & Instructions

- [Domain Instructions](.github/instructions/domain.instructions.md) — Description ([chat log](ai-logs/path))
```

### 2. Related File Updates

Update any related instruction files that should reference the new file.

### 3. Prompt File Creation

Consider creating a corresponding prompt file:

- `.github/prompts/apply-[domain]-instructions.prompt.md`

## Validation Checklist

Before finalizing any instruction file:

### Content Validation

- [ ] Clear purpose and scope defined
- [ ] Target audience identified
- [ ] Actionable guidance provided
- [ ] Examples demonstrate key concepts
- [ ] Quality criteria specified
- [ ] Common mistakes addressed

### Technical Validation

- [ ] Complete AI provenance metadata (all 11 fields)
- [ ] Correct file location and naming
- [ ] Valid markdown formatting
- [ ] Working internal links
- [ ] Proper YAML front matter

### Process Validation

- [ ] Conversation log created
- [ ] Summary file with resumability context
- [ ] README.md updated
- [ ] Related files updated if needed
- [ ] Semantic commit message used

### Compliance Validation

- [ ] Follows repository standards
- [ ] AI provenance requirements met
- [ ] No sensitive information exposed
- [ ] Consistent with existing instructions

## Common Mistakes to Avoid

### Content Mistakes

❌ **Vague Requirements**: "Write good code"
✅ **Specific Requirements**: "Use semantic variable names, maximum 20 characters"

❌ **Missing Examples**: Only abstract guidance
✅ **Concrete Examples**: Show actual implementations

❌ **No Validation**: No way to verify compliance
✅ **Clear Criteria**: Measurable quality gates

### Technical Mistakes

❌ **Incomplete Metadata**: Missing required provenance fields
✅ **Complete Metadata**: All 11 fields with correct values

❌ **Wrong Location**: Files in root or incorrect directory
✅ **Correct Location**: `.github/instructions/` or `.github/instructions/ai/`

❌ **Interface as Model**: `"github/copilot"`
✅ **Actual Model**: `"anthropic/claude-3.5-sonnet@2024-10-22"`

### Process Mistakes

❌ **No Documentation**: File created without updating README
✅ **Complete Documentation**: README and related files updated

❌ **Reused Chat Logs**: Appending to existing conversation files
✅ **Unique Chat Logs**: New conversation file for each session

## Examples

### Example 1: Code Review Instructions

```markdown
---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
# ... complete metadata
applyTo: "**/*.{js,ts,py,java,cs}"
---

# Code Review Instructions

## Overview

Guidelines for conducting thorough, constructive code reviews.

**Target Audience**: Developers, team leads, AI assistants
**Scope**: All code changes requiring review

## Review Criteria

### Functional Requirements

- [ ] Code implements stated requirements
- [ ] Edge cases are handled
- [ ] Error conditions are managed

### Code Quality

- [ ] Follows established coding standards
- [ ] Names are clear and semantic
- [ ] Functions have single responsibility

### Testing

- [ ] Unit tests cover new functionality
- [ ] Integration tests validate interactions
- [ ] Test names clearly describe scenarios

## Review Process

1. **Understand Context**: Read linked issues and documentation
2. **Check Functionality**: Verify requirements are met
3. **Evaluate Quality**: Apply quality criteria
4. **Test Coverage**: Ensure adequate testing
5. **Provide Feedback**: Constructive, specific comments
6. **Approve or Request Changes**: Clear decision with rationale
```

### Example 2: API Documentation Instructions

````markdown
---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
# ... complete metadata
applyTo: "**/api/**/*.{js,ts,py,java,cs}"
---

# API Documentation Instructions

## Overview

Standards for documenting REST APIs to ensure consistency and usability.

## Required Documentation

### Endpoint Documentation

- **Method and Path**: `GET /api/users/{id}`
- **Description**: What the endpoint does
- **Parameters**: Path, query, and body parameters
- **Responses**: Success and error responses with examples
- **Authentication**: Required permissions or tokens

### Example Format

````markdown
## GET /api/users/{id}

Retrieves a specific user by ID.

**Parameters**:

- `id` (path, required): User identifier (UUID)

**Responses**:

- `200 OK`: User found
- `404 Not Found`: User does not exist
- `401 Unauthorized`: Authentication required

**Example**:

```http
GET /api/users/123e4567-e89b-12d3-a456-426614174000
Authorization: Bearer {token}
```
````
````

Response:

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "name": "John Doe"
}
```

```

```

## Maintenance and Updates

### When to Update

Update instruction files when:

- Requirements change
- New best practices emerge
- Feedback identifies gaps
- Related tools or processes change
- Compliance requirements evolve

### Update Process

1. **Identify Changes**: What needs to be updated and why
2. **Update Content**: Modify instructions while preserving structure
3. **Update Metadata**: Change `ended` timestamp, add to `task_durations`
4. **Test Instructions**: Validate updated guidance works
5. **Update Documentation**: Reflect changes in README and related files

### Version Control

- Use semantic commit messages for updates
- Maintain conversation logs for significant changes
- Consider creating new AI-optimized versions when needed

## Summary

Creating effective instruction files requires:

1. **Clear Purpose**: Well-defined scope and objectives
2. **Complete Metadata**: All AI provenance requirements
3. **Actionable Content**: Specific, implementable guidance
4. **Quality Standards**: Validation criteria and examples
5. **Proper Integration**: Updated documentation and links

Follow this guide to create instruction files that provide valuable, consistent guidance for your domain while meeting all repository standards and compliance requirements.

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-23
**Maintainer**: AI-Assisted Development Team
**Related Instructions**:

- `.github/instructions/ai-assisted-output.instructions.md`
- `.github/instructions/copilot-instructions.md`
- `.github/instructions/ai/instruction-prompt.instructions.md`
