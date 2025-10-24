---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "GITHUB_USERNAME_HERE"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of create-chatmode.instructions.md with minimal tokens
started: "2025-10-23T04:40:00Z"
ended: "2025-10-23T04:40:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
applyTo: "**/*.chatmode.md"
---

# AI Instructions: Custom Chat Mode Creation

Create specialized GitHub Copilot chat modes with domain expertise.

## File Structure

### Naming & Location
- Pattern: `<ChatModeName>.chatmode.md` (PascalCase)
- Location: `.github/chatmodes/`
- Extension: `.chatmode.md` (required)

### Required Header
```markdown
# Name: <Display Name>
# Focus: <Primary domain>
# Temperature: <0.0-1.0>
# Style: <Communication style>
```

### Core Sections
1. Mission Statement (required)
2. Core Expertise (required)
3. Analysis Methodology (optional)
4. Interactive Commands (optional)
5. Response Format (recommended)
6. Communication Principles (recommended)
7. Example Interactions (recommended)

## Header Field Specs

### Name
- Title Case, 2-4 words
- Descriptive, memorable
- Example: `# Name: Security Analyzer`

### Focus
- Specific domain description
- Key capabilities, comma-separated
- Example: `# Focus: Code security analysis, vulnerability detection, automated issue creation`

### Temperature
Scale:
- 0.0-0.3: Deterministic (security, compliance)
- 0.4-0.5: Balanced (documentation, analysis)
- 0.6-0.7: Creative (brainstorming, architecture)
- 0.8-1.0: Highly creative (rarely used)

Example: `# Temperature: 0.3`

### Style
- 2-4 descriptive adjectives
- Align with domain
- Example: `# Style: Thorough, security-focused, action-oriented`

## Content Structure

### Mission Statement
1-2 sentences defining role and value:
```markdown
You are [role] specializing in [domain]. Your mission is to [value]
through [approach].
```

### Core Expertise
5-10 specific areas:
```markdown
## Your Core Expertise
- **[Area]**: Description
- **[Area]**: Description
```

### Methodology (Optional)
Multi-phase workflow:
```markdown
## Analysis Methodology
### Phase 1: [Name]
1. **[Step]**: Description
2. **[Step]**: Description
```

### Interactive Commands (Optional)
Command shortcuts:
```markdown
## Interactive Commands
- **`@command-name`** - Description
- **`@another-command`** - Description
```

### Response Format
Output structure:
```markdown
## Response Format
1. **[Icon] Section** (guidance)
2. **[Icon] Section** (guidance)
```

### Communication Principles
Behavioral guidelines:
```markdown
## Communication Guidelines
- **Be [Attribute]**: Description
- **Be [Attribute]**: Description
```

### Example Interactions
Usage demonstrations:
```markdown
## Example Interactions
**User**: "[request]"
**Response**: [action/response]
```

## Templates

### Security Analysis
```markdown
# Name: Security Analyzer
# Focus: Code security, vulnerability detection
# Temperature: 0.3
# Style: Thorough, security-focused, action-oriented

You are an expert security analyst...

## Your Core Expertise
- **Vulnerability Detection**: OWASP Top 10, CWE
- **Static Analysis**: Security anti-patterns

## Interactive Commands
- **`@security-scan`** - Comprehensive assessment
- **`@owasp-check`** - OWASP Top 10 analysis
```

### Documentation Assistant
```markdown
# Name: Documentation Assistant
# Focus: Technical documentation, clarity
# Temperature: 0.4
# Style: Clear, helpful, detail-oriented

You help create comprehensive documentation...

## Capabilities
- Generate API docs
- Create READMEs
- Produce diagrams

## Interactive Commands
- **`@doc-api`** - API documentation
- **`@doc-readme`** - README creation
```

### Code Explorer
```markdown
# Name: Codebase Explorer
# Focus: Rapid codebase understanding
# Temperature: 0.5
# Style: Systematic, educational, context-aware

You help understand unfamiliar codebases...

## Analysis Methodology
### Phase 1: Discovery
1. **Structure Mapping**: Analyze organization
2. **Tech Stack**: Identify frameworks

## Interactive Commands
- **`@overview`** - Project summary
- **`@architecture`** - Design analysis
```

## Validation Checklist
- [ ] PascalCase filename with `.chatmode.md`
- [ ] Located in `.github/chatmodes/`
- [ ] All header fields present (Name, Focus, Temperature, Style)
- [ ] Mission statement clear
- [ ] Core expertise listed (5-10 items)
- [ ] Commands use `@kebab-case` format
- [ ] Temperature appropriate for use case
- [ ] Style aligns with domain

## Anti-Patterns
❌ Overly broad focus
❌ Unclear commands
❌ Missing examples
❌ Vague mission
❌ Inconsistent formatting
❌ Wrong temperature for task

## Quality Rules
**Be Specific**:
- ❌ "Validate input"
- ✅ "Validate email format (RFC 5322) and uniqueness"

**Be Testable**:
- ❌ "System works correctly"
- ✅ "Given valid input, returns 201 with user ID"

**Flag Ambiguities**:
```markdown
⚠️ **NEEDS CLARIFICATION**
**Current**: "Password must be secure"
**Issue**: Definition unclear
**Suggested**: "8-20 chars, uppercase, lowercase, digit, special"
```

## Command Naming
Pattern: `@verb-noun` or `@domain-action`
- Use kebab-case
- 2-3 words max
- Group with common prefixes
- Examples:
  - `@security-scan`
  - `@doc-api`
  - `@overview`

## Integration
Activate: `@<modename>`
Commands: `@security-scan`
Switch: Activate different mode
Context: Accesses open files, workspace

## Reference
See human guide for comprehensive examples and patterns.
