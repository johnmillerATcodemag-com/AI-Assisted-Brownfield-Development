---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "github-username"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of prompt-file.instructions.md with minimal tokens
started: "2025-10-23T04:39:00Z"
ended: "2025-10-23T04:39:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
applyTo: "**/*.prompt.md"
---

# AI Instructions: Prompt File Creation

Generate repository prompts following standard structure and requirements.

## Prompt File Structure

```yaml
---
mode: agent|chat
model: "<provider>/<model-name>@<version>"
tools: ["create", "edit", "search"]
description: Clear description of prompt purpose
prompt_metadata:
  id: unique-identifier
  title: Human-Readable Title
  owner: author-name
  version: 1.0.0
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  output_path: path/to/output
  output_format: markdown|code|json|yaml
  category: category-name
  tags: [tag1, tag2, tag3]
---

# Prompt Title
[Prompt content]
```

## Field Requirements

### mode
- `agent`: Autonomous file operations, code generation
- `chat`: Interactive guidance, Q&A

### model
**REQUIRED**: Use explicit format `"<provider>/<model-name>@<version>"`
- Default: `"anthropic/claude-3.5-sonnet@2024-10-22"`
- Examples:
  - `"openai/gpt-4o@2024-11-20"`
  - `"anthropic/claude-3.5-sonnet@2024-10-22"`
  - `"openai/o1-preview@2024-09-12"`

**Prohibited**: `"Auto (copilot)"` (loses provenance)

### tools
Array of required tools:
- `create` - Create files
- `edit` - Modify files
- `search` - Search codebase
- `read` - Read files
- `run` - Execute commands
- `list` - List directories

**Rule**: Include only necessary tools

### description
**Location**: Top-level (NOT in prompt_metadata)
- Active voice, present tense
- Specific about purpose
- 1-2 sentences max
- Focus on outcomes

### prompt_metadata.id
kebab-case, descriptive, unique
Pattern: `{domain}-{action}-{target}`
Example: `api-documentation-generator`

### prompt_metadata.output_path
Relative path from repo root
Examples:
- `.github/instructions/feature.instructions.md`
- `docs/generated/api-docs.md`

### prompt_metadata.tags
3-7 relevant tags
Categories: technology, function, domain, type
Example: `[python, testing, unit-tests, pytest]`

## Common Templates

### Code Generator
```yaml
mode: agent
tools: ["search", "read", "create"]
description: [What code and where]
prompt_metadata:
  output_format: [language]
  category: code-generation
  tags: [language, framework, code-generation]
```

### Documentation Generator
```yaml
mode: agent
tools: ["search", "read", "create"]
description: [What docs from what source]
prompt_metadata:
  output_format: markdown
  category: documentation
  tags: [documentation, ...]
```

### Interactive Assistant
```yaml
mode: chat
tools: ["search", "read"]
description: [What guidance provided]
prompt_metadata:
  category: guidance
  tags: [interactive, ...]
```

## Content Structure
```markdown
# Prompt Title
[Brief introduction]

## Context
[Background, repo structure, conventions]

## Target Audience
[Who uses output, requirements]

## Requirements
[Detailed requirements by category]

## Technical Requirements
[Specifications, constraints, dependencies]

## Output Format
[Detailed format specs]

## Quality Standards
[Acceptance criteria, metrics]

## Deliverable
[Clear statement of what to produce]
```

## Validation Checklist
- [ ] All required top-level fields present (mode, model, tools, description)
- [ ] All required prompt_metadata fields present
- [ ] description at top-level (NOT in prompt_metadata)
- [ ] model uses explicit format
- [ ] tools array complete and minimal
- [ ] id follows naming convention
- [ ] output_path uses forward slashes
- [ ] YAML syntax valid

## Anti-Patterns
❌ Description in prompt_metadata (should be top-level)
❌ Incomplete tools array
❌ Vague descriptions
❌ Wrong mode selection
❌ Non-unique IDs
❌ Generic model names

## File Naming
Pattern: `{domain}-{action}-{target}.prompt.md`
- kebab-case
- Include `.prompt.md` extension
- Descriptive, specific
- No abbreviations

## Directory Structure
- Prompts: `.github/prompts/`
- Output: `.github/instructions/` or domain-specific
- Use subdirectories for organization

## Post-Creation
After creating prompt:
1. Update AI conversation log artifact section
2. Update README.md with entry and chat log link
3. Verify all links use correct relative paths

## Reference
- `.github/instructions/ai-assisted-output.instructions.md` - Provenance requirements
- `.github/instructions/copilot-instructions.md` - Copilot-specific guidance
