---
description: "Analyze codebase and generate comprehensive instruction files following GitHub Copilot format"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ['search', 'edit', 'fetch']
mode: agent
---

# Generate Project Instruction Files

Analyze codebase and generate comprehensive instruction files.

**IMPORTANT**: Only create NEW files. Never overwrite existing.

## Analysis Phase
1. **Project Structure/Technologies**: Languages, frameworks, libraries, architecture, DB, cloud (Azure/AWS/GCP), frontend (React/Vue/Angular), backend (.NET/Node/Python/Java)
2. **Existing Patterns**: Naming, organization, error handling, testing, docs
3. **Stack Assessment**: Versions, integrations, security, performance

## Instruction Files to Generate in `.github/instructions`:

### 1. README.md
```markdown
---
applyTo: "**"
---
# Development Instructions
Coding guidelines, templates, best practices
## AI Assistant Integration
## Project Overview
## Quick Reference
```

### 2. project-instructions.md
```markdown
---
applyTo: "**"
triggers: ["project structure", "architecture overview", "technology stack"]
---
# Project Structure and Architecture
- Project overview, detected details
- Technology Stack (authoritative versions: frontend, backend, build/test, cloud/DevOps)
- File structure with organization principles
- Architecture patterns: cross-tech integration, API communication, config management
- Data flow, auth/authz, error handling
```

### 3. Technology-Specific Files
Based on detected technologies, generate:
- `<language>-instructions.md` (e.g., csharp-instructions.md, python-instructions.md)
- `<framework>-instructions.md` (e.g., react-instructions.md, dotnet-instructions.md)

Each with:
- `applyTo: "**/*.{ext}"` pattern
- AI guidelines for style, naming, patterns
- Language/framework specific conventions
- Common patterns/anti-patterns
- Testing approach
- Documentation standards

### 4. Cross-Cutting Concerns
Generate if patterns detected:
- `error-handling-instructions.md`: Unified error handling strategy
- `logging-instructions.md`: Structured logging standards
- `testing-instructions.md`: Testing philosophy and conventions
- `security-instructions.md`: Security best practices
- `api-design-instructions.md`: API conventions
- `database-instructions.md`: DB access patterns
- `configuration-instructions.md`: Config management
- `ci-cd-instructions.md`: Build/deployment

## Instruction File Template
```markdown
---
applyTo: "<pattern>"
triggers: ["<keyword1>", "<keyword2>"]
---
# <Title> Instructions
## AI Assistant Guidelines
[3-5 key directives for AI]
## <Topic> Overview
[Context and purpose]
## Conventions
### Naming
### Organization
### Patterns
## Common Patterns
[Code examples with ✅/❌]
## Anti-Patterns
[What to avoid]
## Testing
[Testing approach]
## Examples
[Real examples from codebase]
```

## Generation Process
1. **Scan existing**: List `.github/instructions/*.md`, skip existing
2. **Analyze codebase**: Detect languages, frameworks, patterns (file counts, extensions, imports)
3. **Generate priority order**:
   - README.md (overview)
   - project-instructions.md (central reference)
   - Language-specific (most used languages first)
   - Framework-specific
   - Cross-cutting concerns (if patterns detected)
4. **Per file**:
   - Extract conventions from codebase examples
   - Document detected patterns
   - Provide concrete examples
   - Include AI-specific guidance
5. **Report**: List generated files with brief summary per file

## Quality Standards
- Evidence-based (reference actual codebase patterns)
- Specific and actionable (not generic advice)
- Include code examples from codebase
- Follow GitHub Copilot instruction format
- Clear AI assistant directives
- Cross-reference related instruction files

## Output Format
List generated files with:
- Filename
- ApplyTo pattern
- Key conventions documented
- Example patterns included
- Integration points with other instructions
