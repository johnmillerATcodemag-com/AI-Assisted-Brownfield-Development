---
title: "Generate Project Instruction Files"
description: "Intelligently analyzes codebase and generates comprehensive, technology-specific instruction files following GitHub Copilot format"
author: "AI Assistant"
tags:
  [
    "instructions",
    "documentation",
    "best-practices",
    "code-generation",
    "architecture",
    "ai-guidance",
  ]
version: "2.0.0"
triggers:
  - "generate instructions"
  - "create instruction files"
  - "analyze codebase for instructions"
  - "setup project guidance"
  - "create coding guidelines"
  - "generate tech docs"
  - "create ai guidance"
  - "setup development standards"
  - "analyze project structure"
  - "create technology templates"
appliesTo:
  - "**"
  - ".github/instructions/**"
  - "**/*.md"
  - "**/README.md"
  - "**/package.json"
  - "**/*.csproj"
  - "**/*.sln"
requirements:
  - "Read-only access to codebase"
  - "File system access for creating new files"
  - "Understanding of multiple programming languages and frameworks"
outputs:
  - "Comprehensive instruction file structure"
  - "Technology-specific guidance files"
  - "AI assistant integration guidelines"
---

# Generate Project Instruction Files

You are an expert software architect and documentation specialist. Your task is to analyze the current codebase and generate comprehensive instruction files following the GitHub Copilot Instruction File Format.

**IMPORTANT**: Only create NEW instruction files that do not already exist. Never modify or overwrite existing files.

## Analysis Phase

First, analyze the codebase to identify:

1. **Project Structure and Technologies**

   - Primary programming languages used
   - Frameworks and libraries detected
   - Architecture patterns observed
   - Database technologies
   - Cloud platforms (Azure, AWS, GCP)
   - Frontend technologies (React, Vue, Angular, etc.)
   - Backend technologies (.NET, Node.js, Python, Java, etc.)

2. **Existing Patterns and Conventions**

   - Naming conventions currently used
   - Code organization patterns
   - Error handling approaches
   - Testing strategies
   - Documentation styles

3. **Technology Stack Assessment**
   - Version information for major dependencies
   - Integration patterns between technologies
   - Security implementations
   - Performance optimization patterns

## Instruction File Generation

Generate instruction files in the `.github/instructions/` directory with the following structure:

### General Instructions (Root Level)

Create these files in `.github/instructions/`:

#### 1. README.md

```markdown
---
applyTo: "**"
---

# Development Instructions

Comprehensive coding guidelines, templates, and best practices for this project.

## AI Assistant Integration

[Include AI-specific guidance]

## Project Overview

[Technology stack and architecture summary]

## Quick Reference

[Language and framework specific quick guides]
```

#### 2. project-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "project structure"
  - "architecture overview"
  - "technology stack"
---

# Project Structure and Architecture Instructions

## AI Assistant Guidelines

- Follow established project structure when creating new files
- Use specified technology stack consistently
- Maintain separation of concerns based on architecture
- Apply proper naming conventions for each technology

## Project Overview

[Detected project details]

## Technology Stack

[List all detected technologies with versions]

## File Structure

[Analyze and document the project structure]
```

#### 3. practices-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "best practices"
  - "coding standards"
  - "performance guidelines"
  - "security practices"
---

# Development Best Practices

## AI Assistant Guidelines

- Always suggest async/await patterns for I/O operations
- Include error handling and logging in all code suggestions
- Recommend appropriate security practices
- Include testing examples with generated code

[Include technology-specific best practices based on detected stack]
```

#### 4. error-handling-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "error handling"
  - "exception management"
  - "logging patterns"
---

# Error Handling Instructions

## AI Assistant Guidelines

- Always wrap async operations in try-catch blocks
- Include correlation ID generation for new operations
- Suggest appropriate HTTP status codes for API responses
- Recommend structured logging with meaningful context

[Include language-specific error handling patterns]
```

#### 5. style-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "code style"
  - "naming conventions"
  - "formatting rules"
---

# Code Style and Naming Conventions

## AI Assistant Guidelines

- Apply appropriate naming convention based on language and context
- Maintain consistency with existing codebase patterns
- Use meaningful, descriptive names
- Follow language-specific conventions

[Include detected naming patterns and style guidelines]
```

#### 6. testing-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "testing guidelines"
  - "unit tests"
  - "test patterns"
---

# Testing Instructions

## AI Assistant Guidelines

- Write comprehensive tests for all business logic
- Use appropriate testing frameworks for each technology
- Include both positive and negative test cases
- Aim for meaningful test coverage

[Include technology-specific testing frameworks and patterns]
```

### Technology-Specific Instructions

For each detected technology, create a subdirectory with specific instructions:

#### For .NET/C# Projects

Create `csharp/` folder with:

- `csharp-style-instructions.md` (applyTo: '\*_/_.cs')
- `csharp-api-documentation-instructions.md` (applyTo: '\*_/_.cs')
- `csharp-testing-instructions.md` (applyTo: '\*_/_.cs')
- `csharp-error-handling-instructions.md` (applyTo: '\*_/_.cs')
- `csharp-validation-instructions.md` (applyTo: '\*_/_.cs')
- `csharp-code-template-instructions.md` (applyTo: '\*_/_.cs')

#### For Vue.js Projects

Create `vue/` folder with:

- `vue-style-instructions.md` (applyTo: '\*_/_.vue')
- `vue-component-instructions.md` (applyTo: '\*_/_.vue')
- `vue-testing-instructions.md` (applyTo: '\*_/_.vue')
- `vue-state-management-instructions.md` (applyTo: '\*_/_.vue')

#### For React Projects

Create `react/` folder with:

- `react-component-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')
- `react-hooks-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')
- `react-testing-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')

#### For Node.js Projects

Create `nodejs/` folder with:

- `nodejs-api-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')
- `nodejs-testing-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')
- `nodejs-security-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')

#### For Python Projects

Create `python/` folder with:

- `python-style-instructions.md` (applyTo: '\*_/_.py')
- `python-testing-instructions.md` (applyTo: '\*_/_.py')
- `python-api-instructions.md` (applyTo: '\*_/_.py')

#### For Database Technologies

If database files are detected, create appropriate folders:

- `sql/` for SQL Server, PostgreSQL, MySQL
- `mongodb/` for MongoDB
- `redis/` for Redis

#### For Cloud Platforms

If cloud services are detected:

- `azure/` for Azure-specific instructions
- `aws/` for AWS-specific instructions
- `gcp/` for Google Cloud-specific instructions

## Template Structure for Each Instruction File

```markdown
---
applyTo: "[specific file patterns]"
triggers:
  - "relevant trigger phrases"
  - "technology keywords"
  - "specific scenarios"
---

# [Technology] [Category] Instructions

## AI Assistant Guidelines

- Technology-specific guidance for AI assistants
- Context-aware recommendations based on the technology
- Quality assurance rules specific to this technology
- Integration considerations with other project technologies

## [Technology] Standards

### [Specific Category] Guidelines

- Detailed guidelines specific to this technology
- Code examples using the actual technology stack
- Best practices aligned with the technology's conventions
- Common patterns and anti-patterns

### Code Templates

[Include relevant code templates]

### Examples

[Include practical examples based on detected patterns]

## Integration Considerations

- How this technology integrates with others in the project
- Dependencies and configuration requirements
- Performance and security considerations
```

## Special Considerations

### For Multi-Technology Projects

- Create cross-technology integration instructions
- Include API communication patterns between technologies
- Document data flow between different technology layers

### For Microservices Architecture

- Create service-specific instruction folders
- Include inter-service communication guidelines
- Document deployment and orchestration patterns

### For Monolithic Architecture

- Create module-specific instructions
- Include layer separation guidelines
- Document internal API patterns

## Generation Rules

1. **Analyze Before Generating**: Always analyze the codebase first to understand the actual technologies and patterns used
2. **Use Detected Patterns**: Base instruction content on actually observed patterns in the codebase
3. **Technology Versions**: Include specific version information for major dependencies
4. **Practical Examples**: Use real examples from the codebase where possible
5. **Consistency**: Ensure all generated instructions follow the same format and style
6. **Completeness**: Cover all major aspects of development for each detected technology
7. **Maintainability**: Structure instructions for easy updates and maintenance
8. **Preserve Existing Files**: **NEVER modify or overwrite existing files** - only create new instruction files that don't already exist

## Output Format

After analysis, provide a summary of:

1. Detected technologies and versions
2. Proposed instruction file structure
3. Key patterns and conventions identified
4. Recommended instruction priorities

Then proceed to generate the instruction files using the established format and detected technologies.

## Safety Requirements

**CRITICAL**: Before creating any instruction file:

1. **Check if the file already exists** in the target location
2. **Skip creation** if a file with the same name already exists
3. **Only create new files** that don't conflict with existing ones
4. **Preserve all existing content** - never modify existing instruction files

## File Conflict Resolution

If instruction files already exist:

- Analyze existing files to understand current patterns
- Use existing files as reference for consistency
- Only create supplementary files that fill gaps
- Document any detected inconsistencies but do not modify existing files

Remember: The goal is to create NEW instruction files that will help AI assistants generate consistent, high-quality code that follows the project's established patterns and best practices, while preserving all existing documentation and instructions.
