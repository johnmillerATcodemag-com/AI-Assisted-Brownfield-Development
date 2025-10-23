---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "create-chatmode-instructions-20251021"
prompt: |
  Generate comprehensive authoring guidelines for creating custom GitHub Copilot chat modes
  following repository standards and best practices.
started: "2025-10-21T19:30:00Z"
ended: "2025-10-21T19:45:00Z"
task_durations:
  - task: "analyze existing chat modes"
    duration: "00:05:00"
  - task: "generate comprehensive instructions"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md"
source: ".github/prompts/create-chatmode-instructions.prompt.md"
applyTo: "**/*.chatmode.md"
---

# Custom Chat Mode Authoring Instructions

## Overview and Purpose

Custom chat modes are specialized AI assistants that extend GitHub Copilot's capabilities for specific domains, workflows, or tasks. They allow teams to create focused, context-aware AI helpers with tailored expertise, personality, and command structures.

### What Are Custom Chat Modes?

Custom chat modes are Markdown-based configuration files that define:

- **Specialized expertise** in specific domains (security, documentation, architecture)
- **Consistent personality** and communication style
- **Interactive commands** for guided workflows
- **Structured methodologies** for complex analysis tasks
- **Response formats** for predictable, actionable output

### Benefits of Custom Chat Modes

**For Developers**:

- Context-aware assistance for specialized tasks
- Consistent guidance across team members
- Reduced cognitive load through structured workflows
- Command-driven interaction for efficiency

**For Teams**:

- Codified best practices and standards
- Consistent quality across analyses and reviews
- Onboarding acceleration for new team members
- Domain expertise accessible to all team members

**For Organizations**:

- Standardized security and compliance reviews
- Documented analysis methodologies
- Scalable expertise across projects
- Improved code quality and consistency

### When to Create a Custom Chat Mode

✅ **Create a custom chat mode when**:

- You have specialized domain expertise to codify (security, performance, accessibility)
- You need consistent analysis methodology across team members
- You want to automate structured workflows (threat modeling, code reviews)
- You need command-driven interaction for complex tasks
- You want to enforce standards and best practices

❌ **Use default Copilot when**:

- You need general-purpose coding assistance
- Questions are ad-hoc and don't follow patterns
- No specialized domain knowledge required
- One-off tasks without recurring workflows

### Integration with GitHub Copilot

Custom chat modes integrate seamlessly with GitHub Copilot:

- **Activation**: Use `@<modename>` to activate a specific chat mode
- **Commands**: Invoke mode-specific commands like `@security-scan` or `@overview`
- **Context**: Chat modes leverage repository context and open files
- **Tools**: Access to Copilot's code analysis and generation capabilities
- **Switching**: Easily switch between modes or return to default Copilot

## Chat Mode File Structure

### File Naming Conventions

**Pattern**: `<ChatModeName>.chatmode.md`

**Rules**:

- Use PascalCase for the mode name: `SecurityAnalyzer.chatmode.md`
- Include `.chatmode.md` extension (required for recognition)
- Name should be descriptive and unique within the repository
- Avoid abbreviations unless widely recognized

**Examples**:

```
✅ SecurityAnalyzer.chatmode.md
✅ DocDesignArchitect.chatmode.md
✅ CodebaseExplorer.chatmode.md
✅ GitFlowStrategist.chatmode.md

❌ security.chatmode.md          # Not descriptive enough
❌ security_analyzer.chatmode.md # Use PascalCase, not snake_case
❌ SecurityAnalyzerMode.md       # Missing .chatmode extension
```

### File Location

**Standard Location**: `.github/chatmodes/`

```
repository-root/
├── .github/
│   ├── chatmodes/               # Chat mode files go here
│   │   ├── SecurityAnalyzer.chatmode.md
│   │   ├── DocDesignArchitect.chatmode.md
│   │   └── CodebaseExplorer.chatmode.md
│   ├── instructions/            # Instruction files
│   └── prompts/                 # Prompt files
```

### Required Header Components

Every chat mode file must start with these header fields:

```markdown
# Name: <Display Name>

# Focus: <Primary domain or specialty>

# Temperature: <0.0-1.0>

# Style: <Communication style>
```

**Formatting Rules**:

- Each header field on its own line
- Use `# ` prefix for each field (Markdown heading syntax)
- Follow field name with colon and space
- No blank lines between header fields
- One blank line after the header block

### Core Content Sections

After the header, include these sections:

1. **Mission Statement** (required)
2. **Core Expertise** (required)
3. **Analysis Methodology** (optional but recommended)
4. **Interactive Commands** (optional)
5. **Response Format Guidelines** (recommended)
6. **Communication Principles** (recommended)
7. **Example Interactions** (recommended)

## Header Field Specifications

### Name Field

**Purpose**: The display name shown in GitHub Copilot when activating the chat mode.

**Format**: `# Name: <Display Name>`

**Guidelines**:

- Use Title Case for proper nouns and key words
- Be descriptive and memorable
- Keep to 2-4 words maximum
- Reflect the mode's primary purpose

**Examples**:

```markdown
✅ # Name: Security Analyzer
✅ # Name: Doc Design Architect
✅ # Name: Codebase Explorer
✅ # Name: Git Flow Strategist

❌ # Name: Helper # Too vague
❌ # Name: The Security Guy # Too informal
❌ # Name: sec-analyzer # Not Title Case
```

### Focus Field

**Purpose**: Defines the primary domain, specialty area, or scope of expertise.

**Format**: `# Focus: <Domain description>`

**Guidelines**:

- Be specific about the domain or task
- Describe the primary value proposition
- Include key capabilities or areas
- Use commas to separate multiple focus areas
- Keep to one line

**Examples**:

```markdown
✅ # Focus: Code security analysis, vulnerability detection, and automated issue creation
✅ # Focus: Technical documentation, diagramming with Mermaid, and readability improvements
✅ # Focus: Branching policies, merge style enforcement, and CI/CD hygiene

❌ # Focus: Helping with stuff # Too vague
❌ # Focus: Everything # Not focused
❌ # Focus: Security # Too broad, not specific enough
```

### Temperature Field

**Purpose**: Controls the AI model's response creativity and randomness.

**Format**: `# Temperature: <0.0-1.0>`

**Scale Explanation**:

- **0.0-0.3**: Highly deterministic, focused, precise (best for security, compliance)
- **0.4-0.5**: Balanced between creativity and consistency (documentation, analysis)
- **0.6-0.7**: More creative, varied responses (brainstorming, architecture design)
- **0.8-1.0**: Highly creative, exploratory (rarely used for technical work)

**Recommended Values by Use Case**:

| Use Case            | Temperature | Rationale                                               |
| ------------------- | ----------- | ------------------------------------------------------- |
| Security Analysis   | 0.3         | Precision critical, no room for creative interpretation |
| Compliance Review   | 0.3         | Strict adherence to rules required                      |
| Code Review         | 0.3-0.4     | Consistency important, some flexibility needed          |
| Documentation       | 0.4-0.5     | Balance clarity with engaging writing                   |
| Architecture Design | 0.5-0.6     | Creative solutions valued, grounded in best practices   |
| Brainstorming       | 0.6-0.7     | Creativity encouraged, explore possibilities            |

**Examples**:

```markdown
✅ # Temperature: 0.3 # Security analysis
✅ # Temperature: 0.4 # Documentation
✅ # Temperature: 0.5 # Code exploration
✅ # Temperature: 0.6 # Architecture design

❌ # Temperature: 0 # Use 0.0, not 0
❌ # Temperature: 1 # Use 1.0, not 1
❌ # Temperature: 0.85 # Too high for most technical work
```

### Style Field

**Purpose**: Defines the communication tone, personality, and writing approach.

**Format**: `# Style: <Style description>`

**Guidelines**:

- Use 2-4 descriptive adjectives
- Separate with commas
- Align with domain and audience
- Be consistent with the mode's purpose

**Common Style Attributes**:

- **Tone**: Friendly, professional, confident, pragmatic, cautious
- **Approach**: Thorough, action-oriented, educational, opinionated
- **Focus**: Precise, security-focused, formatting-conscious, compliance-aware

**Examples**:

```markdown
✅ # Style: Thorough, security-focused, and action-oriented
✅ # Style: Friendly, precise, and formatting-conscious
✅ # Style: Confident, pragmatic, and slightly opinionated
✅ # Style: Educational, systematic, and context-aware

❌ # Style: Nice # Too vague
❌ # Style: Funny and entertaining # Inappropriate for technical work
❌ # Style: Whatever works # Not descriptive
```

**Alignment Examples**:

| Domain        | Appropriate Style                                |
| ------------- | ------------------------------------------------ |
| Security      | Thorough, security-focused, action-oriented      |
| Documentation | Friendly, precise, formatting-conscious          |
| Code Review   | Constructive, educational, best-practice focused |
| Architecture  | Strategic, pragmatic, design-oriented            |
| Compliance    | Strict, detail-oriented, policy-focused          |

## Content Structure Guidelines

### Mission Statement

**Purpose**: Clearly defines the chat mode's primary role and value proposition.

**Location**: Immediately after header fields (first paragraph)

**Guidelines**:

- Write 1-2 concise sentences
- Start with "You are..." to establish persona
- Include primary role and key capabilities
- Make the value proposition clear
- Use active, confident language

**Effective Mission Statement Pattern**:

```
You are [role/title] specializing in [domain]. Your mission is to [primary value]
through [approach/methodology].
```

**Examples from Repository**:

```markdown
✅ You are an expert security analyst and vulnerability researcher specializing in
comprehensive code security assessments. Your mission is to identify security risks,
analyze potential attack vectors, and provide actionable remediation guidance through
automated GitHub issue creation.

✅ You are an expert software architect and code analyst specializing in rapidly
understanding and evaluating unfamiliar codebases. Your mission is to help developers
quickly comprehend complex projects through systematic analysis and clear explanations.

❌ You help with code. # Too vague
❌ I am a helpful assistant. # Wrong perspective, too generic
```

### Core Expertise Section

**Purpose**: Defines the specific areas of knowledge and capability.

**Structure**: Use a header and bullet list

**Guidelines**:

- Use `## Your Core Expertise` or `## Capabilities` as header
- List 5-10 specific expertise areas
- Use bold for area names, colon, then description
- Order by importance or logical grouping
- Be specific and actionable

**Format Pattern**:

```markdown
## Your Core Expertise

- **[Area Name]**: Brief description of capability
- **[Area Name]**: Brief description of capability
```

**Examples**:

```markdown
✅ ## Your Core Expertise

- **Vulnerability Detection**: OWASP Top 10, CWE classifications, and emerging threats
- **Static Code Analysis**: Pattern recognition for security anti-patterns
- **Dependency Security**: Supply chain analysis and known CVE detection
- **Authentication & Authorization**: Access control and privilege escalation risks

✅ ## Capabilities

- Generate diagrams from architecture or workflow inputs
- Refactor Markdown for better navigation and scanning
- Suggest formatting changes to improve comprehension

❌ ## What I Do

- I help with security # Not specific enough
- Various code analysis tasks # Too vague
```

### Methodology Section (Optional but Recommended)

**Purpose**: Defines a structured, multi-phase workflow for complex analysis tasks.

**When to Include**:

- Analysis tasks with logical phases (discovery → analysis → reporting)
- Workflows that need to be repeatable
- Complex assessments requiring systematic approach
- Tasks where order of operations matters

**Structure**: Use phases with numbered steps

**Format Pattern**:

```markdown
## Analysis Methodology

### Phase 1: [Phase Name]

1. **[Step Name]**: Description of what happens in this step
2. **[Step Name]**: Description of what happens in this step

### Phase 2: [Phase Name]

1. **[Step Name]**: Description
2. **[Step Name]**: Description
```

**Examples**:

```markdown
✅ ## Analysis Methodology

### Phase 1: Initial Security Scan

1. **Threat Modeling**: Identify attack surface and potential threat actors
2. **Technology Assessment**: Analyze frameworks and libraries for known vulnerabilities
3. **Entry Point Mapping**: Locate user inputs, API endpoints, and data flows

### Phase 2: Deep Security Analysis

1. **Authentication Review**: Examine authentication mechanisms and session management
2. **Authorization Check**: Analyze access controls and privilege management
```

**Benefits of Methodology Section**:

- Provides consistent analysis approach
- Ensures comprehensive coverage
- Makes complex tasks manageable
- Enables progress tracking
- Facilitates handoffs between team members

### Interactive Commands Section

**Purpose**: Defines command-driven shortcuts for common workflows and focused analysis.

**When to Include**:

- Mode has multiple distinct capabilities
- Users benefit from focused analysis modes
- Workflows can be triggered by simple commands
- Need to guide users to specific features

**Structure**: Command list with descriptions

**Command Naming Conventions**:

- Use `@command-name` format (kebab-case)
- Start with domain prefix for clarity (`@security-scan`, `@doc-generate`)
- Use verbs for actions (`@create-issues`, `@analyze-performance`)
- Keep names short but descriptive (2-3 words)
- Group related commands with common prefixes

**Format Pattern**:

```markdown
## Interactive Commands

Use these commands for [purpose]:

- **`@command-name`** - Brief description of what the command does
- **`@another-command`** - Another description
```

**Examples**:

```markdown
✅ ## Interactive Commands

Use these commands for focused security analysis:

- **`@security-scan`** - Comprehensive security vulnerability assessment
- **`@owasp-check`** - OWASP Top 10 focused analysis
- **`@auth-review`** - Authentication and authorization security review
- **`@create-issues`** - Generate GitHub issues for identified vulnerabilities

✅ ## Interactive Commands

Use these commands to guide focused analysis:

- **`@overview`** - Get high-level project summary and structure
- **`@architecture`** - Deep dive into architectural patterns and design
- **`@security`** - Perform security-focused code review
- **`@performance`** - Identify performance bottlenecks and optimizations
```

**Command Organization Patterns**:

**By Category**:

```markdown
## Interactive Commands

### Analysis Commands

- **`@overview`** - High-level project summary
- **`@deep-dive`** - Comprehensive analysis

### Quality Commands

- **`@security`** - Security review
- **`@performance`** - Performance analysis
```

**By Workflow Phase**:

```markdown
## Interactive Commands

### Discovery Phase

- **`@scan`** - Initial codebase scan
- **`@map`** - Architecture mapping

### Analysis Phase

- **`@analyze`** - Deep analysis
- **`@report`** - Generate findings report
```

### Response Format Guidelines

**Purpose**: Ensures consistent, predictable, and actionable output structure.

**When to Include**:

- Mode produces structured reports or analyses
- Users need consistent information organization
- Complex output requires standard formatting
- Emoji or visual cues enhance clarity

**Format Pattern**:

```markdown
## Response Format

Structure all responses with:

1. **[Section Icon] Section Name** (guidance on content)
2. **[Section Icon] Section Name** (guidance on content)
```

**Examples**:

```markdown
✅ ## Response Format

Structure all responses with:

1. **🎯 Executive Summary** (2-3 sentences max)
2. **📊 Key Findings** (organized by priority)
3. **💡 Recommendations** (actionable next steps)
4. **🔍 Focus Areas** (what to explore next)
5. **📝 Code Examples** (when relevant, with explanations)
```

**Benefits of Response Format Guidelines**:

- Predictable output structure
- Easy to scan and digest
- Consistent quality across analyses
- Clear action items
- Visual hierarchy with emoji

### Communication Principles

**Purpose**: Defines behavioral guidelines and expectations for responses.

**Format Pattern**:

```markdown
## Communication Guidelines

- **Be [Attribute]**: Description of what this means
- **Be [Attribute]**: Description of what this means
```

**Examples**:

```markdown
✅ ## Communication Guidelines

- **Be Systematic**: Follow logical analysis progression
- **Be Specific**: Provide file paths, line numbers, and concrete examples
- **Be Actionable**: Give practical recommendations, not just observations
- **Be Educational**: Explain the reasoning behind findings
- **Be Prioritized**: Rank issues by impact and urgency

✅ ## Expectations

When asked to document code:

- Break content into sections with proper headers and lists
- Use diagrams to illustrate complex concepts
- Annotate Mermaid output and flag ambiguity in user stories
```

### Example Interactions

**Purpose**: Shows realistic usage patterns and expected responses.

**When to Include**:

- Mode has complex command structure
- Interaction patterns aren't obvious
- Need to demonstrate capabilities
- Clarify expected input/output

**Format Pattern**:

```markdown
## Example Interactions

**User**: "[Example user request]"
**Response**: [What the mode would do or suggest]

**User**: "[Another example]"
**Response**: [Expected response]
```

**Examples**:

```markdown
✅ ## Example Interactions

**User**: "I just inherited this React/Node.js project. Can you help me understand it?"
**Response**: Use `@overview` to get started, then `@architecture` for deeper understanding.

**User**: "@overview"
**Response**: Provides structured analysis of project structure, tech stack, and key entry points.

**User**: "This app seems slow. Any ideas?"
**Response**: Use `@performance` to identify bottlenecks and optimization opportunities.
```

## Best Practices

### Clarity and Specificity

**Write Clear, Actionable Content**:

✅ **Do**:

- Use concrete examples with file paths and line numbers
- Provide step-by-step instructions
- Define technical terms on first use
- Include command syntax examples
- Specify expected outcomes

❌ **Don't**:

- Use vague language like "improve the code"
- Assume knowledge without context
- Leave commands or processes unexplained
- Use jargon without definition

**Examples**:

```markdown
❌ Vague: "Check for security issues"

✅ Specific: "Perform a security scan focusing on:

1. SQL injection in database queries (`src/db/*.ts`)
2. XSS vulnerabilities in user input handling (`src/validators/*.ts`)
3. Authentication bypass in API endpoints (`src/api/auth.ts`)"
```

### Consistency

**Maintain Consistent Formatting**:

✅ **Do**:

- Use the same heading levels for similar content
- Apply consistent bullet point styles
- Use the same terminology throughout
- Follow repository formatting conventions
- Maintain consistent command syntax

❌ **Don't**:

- Switch between heading styles
- Mix bullet and numbered lists without reason
- Use different terms for the same concept
- Invent new formatting patterns

**Standard Terminology Table**:

| Concept        | Use This Term | Not These             |
| -------------- | ------------- | --------------------- |
| User input     | Command       | Query, request, ask   |
| AI response    | Response      | Answer, reply, output |
| Workflow step  | Phase         | Stage, step, part     |
| Security issue | Vulnerability | Bug, problem, flaw    |
| Code location  | File path     | File location, path   |

### Scope Definition

**Define Clear Boundaries**:

✅ **Do**:

- Clearly state what the mode does
- Explicitly mention what's out of scope
- Define limitations upfront
- Focus on specific value proposition
- Resist scope creep

❌ **Don't**:

- Try to cover everything
- Overlap with existing modes
- Make vague promises
- Add features without clear value

**Scope Definition Example**:

```markdown
## Scope

**In Scope**:

- Static code security analysis
- Vulnerability identification and classification
- Automated GitHub issue creation for findings
- Remediation guidance and best practices

**Out of Scope**:

- Dynamic security testing (use penetration testing tools)
- Infrastructure security (use DevSecOps tools)
- Legal compliance advice (consult security/legal teams)
- Real-time threat monitoring (use SIEM tools)
```

### Command Design

**Create Intuitive, Discoverable Commands**:

✅ **Do**:

- Use verb-noun patterns (`@analyze-security`, `@create-diagram`)
- Group related commands with prefixes (`@security-*`, `@doc-*`)
- Provide clear, concise descriptions
- Organize commands by category or workflow
- Include examples for complex commands

❌ **Don't**:

- Use obscure abbreviations (`@sec`, `@perf`)
- Create too many similar commands
- Use inconsistent naming patterns
- Leave commands undocumented

**Command Organization Examples**:

```markdown
✅ Well-organized command structure:

## Interactive Commands

### Security Analysis

- **`@security-scan`** - Comprehensive vulnerability assessment
- **`@security-owasp`** - OWASP Top 10 focused check
- **`@security-deps`** - Dependency vulnerability check

### Documentation Generation

- **`@doc-api`** - Generate API documentation
- **`@doc-readme`** - Create or update README
- **`@doc-diagram`** - Generate architecture diagrams
```

## Quality Assurance

### Validation Checklist

Before submitting a chat mode file, verify:

#### Header Validation

- [ ] `Name` field present with clear, descriptive title
- [ ] `Focus` field defines specific domain or specialty
- [ ] `Temperature` field set to appropriate value (0.0-1.0)
- [ ] `Style` field describes communication approach
- [ ] All header fields use correct format (`# Field: Value`)
- [ ] One blank line separates header from content

#### Content Validation

- [ ] Mission statement clearly defines purpose and value
- [ ] Core expertise section lists specific capabilities
- [ ] Methodology section included for complex workflows (if applicable)
- [ ] Interactive commands documented with clear descriptions (if applicable)
- [ ] Response format guidelines provided for structured output
- [ ] Communication principles establish behavioral expectations
- [ ] Example interactions demonstrate usage patterns

#### Formatting Validation

- [ ] Consistent heading hierarchy (H1 for name, H2 for sections, H3 for subsections)
- [ ] Proper Markdown syntax throughout
- [ ] Bullet points and numbered lists properly formatted
- [ ] Code blocks use correct syntax highlighting
- [ ] Tables formatted correctly
- [ ] Emoji used consistently (if at all)

#### Quality Validation

- [ ] Content is clear and actionable
- [ ] No ambiguous or vague language
- [ ] Technical terms defined or self-evident
- [ ] Examples are realistic and helpful
- [ ] Commands follow naming conventions
- [ ] Scope is clearly defined
- [ ] No spelling or grammar errors

#### File Validation

- [ ] Filename follows PascalCase convention
- [ ] File has `.chatmode.md` extension
- [ ] File located in `.github/chatmodes/`
- [ ] File renders correctly in Markdown preview

### Testing Recommendations

**Test the Chat Mode**:

1. **Manual Testing**:

   - Activate the chat mode in GitHub Copilot (`@<modename>`)
   - Try each documented command
   - Verify response format and quality
   - Test with realistic scenarios
   - Check error handling for invalid inputs

2. **Peer Review**:

   - Have a colleague use the chat mode
   - Gather feedback on clarity and usefulness
   - Identify missing capabilities or confusing instructions
   - Validate command naming and organization

3. **Iterative Refinement**:
   - Incorporate user feedback
   - Refine command descriptions
   - Clarify ambiguous sections
   - Add missing examples
   - Adjust temperature if responses aren't appropriate

**Testing Scenarios Table**:

| Scenario          | What to Test                             | Success Criteria                            |
| ----------------- | ---------------------------------------- | ------------------------------------------- |
| First-time use    | Can user understand mode's purpose?      | Clear value proposition, obvious next steps |
| Command discovery | Can user find relevant commands?         | Logical organization, clear descriptions    |
| Complex workflow  | Does methodology guide user effectively? | Step-by-step clarity, no confusion          |
| Output quality    | Is response format helpful?              | Consistent structure, actionable insights   |
| Edge cases        | How does mode handle unusual inputs?     | Graceful handling, helpful guidance         |

### Review Process

**Self-Review**:

1. Read the entire chat mode file aloud
2. Verify all checklist items
3. Test in GitHub Copilot
4. Gather initial feedback from target users

**Peer Review Guidelines**:

**For Reviewers**:

- Focus on clarity and usability
- Test with realistic scenarios
- Check for consistency with repository standards
- Validate command naming and organization
- Ensure examples are helpful

**For Authors**:

- Be open to feedback
- Explain design decisions when challenged
- Incorporate suggestions iteratively
- Document changes in version history

**Review Feedback Template**:

```markdown
## Chat Mode Review: [Mode Name]

### Strengths

- [What works well]
- [Effective features]

### Improvement Areas

- [Unclear sections]
- [Missing capabilities]
- [Confusing commands]

### Suggestions

- [Specific improvements]
- [Additional examples needed]

### Approval Status

- [ ] Approved as-is
- [ ] Approved with minor changes
- [ ] Requires revision
```

## Examples and Templates

### Simple Chat Mode Template

Use this template for straightforward, single-purpose chat modes:

```markdown
# Name: [Your Mode Name]

# Focus: [Primary domain or task]

# Temperature: [0.3-0.5]

# Style: [Your communication style]

You are [role description]. Your mission is to [primary value proposition].

## Capabilities

- [Capability 1]
- [Capability 2]
- [Capability 3]

## Expectations

When [users ask for X]:

- [Expected behavior 1]
- [Expected behavior 2]
- [Expected behavior 3]
```

**Example** (based on `DocDesignArchitect.chatmode.md`):

```markdown
# Name: Doc Design Architect

# Focus: Technical documentation, diagramming with Mermaid, and readability improvements

# Temperature: 0.4

# Style: Friendly, precise, and formatting-conscious

You structure documentation to maximize clarity and impact. You incorporate Mermaid diagrams, annotate flows, and guide contributors on best practices for accessibility and skimmability.

## Capabilities

- Generate diagrams from architecture or workflow inputs
- Refactor Markdown for better navigation and scanning
- Suggest formatting changes to improve comprehension

## Expectations

When asked to document code:

- Break content into sections with proper headers and lists
- Use diagrams to illustrate complex concepts
- Annotate Mermaid output and flag ambiguity in user stories
```

### Advanced Chat Mode Template

Use this template for comprehensive, command-driven chat modes:

```markdown
# Name: [Your Mode Name]

# Focus: [Comprehensive domain description]

# Temperature: [0.3-0.7]

# Style: [Detailed communication style]

You are [detailed role and expertise description]. Your mission is to [comprehensive value proposition and approach].

## Your Core Expertise

- **[Expertise Area 1]**: Description
- **[Expertise Area 2]**: Description
- **[Expertise Area 3]**: Description
- **[Expertise Area 4]**: Description
- **[Expertise Area 5]**: Description

## Analysis Methodology

### Phase 1: [Phase Name]

1. **[Step Name]**: Description
2. **[Step Name]**: Description
3. **[Step Name]**: Description

### Phase 2: [Phase Name]

1. **[Step Name]**: Description
2. **[Step Name]**: Description

### Phase 3: [Phase Name]

1. **[Step Name]**: Description
2. **[Step Name]**: Description

## Interactive Commands

Use these commands for [purpose]:

- **`@command-1`** - Description
- **`@command-2`** - Description
- **`@command-3`** - Description
- **`@command-4`** - Description

## Response Format

Structure all responses with:

1. **[Section]** (guidance)
2. **[Section]** (guidance)
3. **[Section]** (guidance)

## Communication Guidelines

- **Be [Principle]**: Description
- **Be [Principle]**: Description
- **Be [Principle]**: Description

## Example Interactions

**User**: "[Example request]"
**Response**: [Expected response]

**User**: "[Another example]"
**Response**: [Expected response]
```

### Domain-Specific Examples

#### Security Analysis Pattern

```markdown
# Name: Security Analyzer

# Focus: Code security analysis, vulnerability detection, and remediation

# Temperature: 0.3

# Style: Thorough, security-focused, and action-oriented

You are an expert security analyst specializing in identifying vulnerabilities and providing actionable remediation guidance.

## Your Core Expertise

- **Vulnerability Detection**: OWASP Top 10, CWE classifications
- **Static Analysis**: Security anti-patterns and code smells
- **Dependency Security**: CVE detection and supply chain risks
- **Authentication**: Access control and session management

## Interactive Commands

- **`@security-scan`** - Comprehensive vulnerability assessment
- **`@owasp-check`** - OWASP Top 10 focused analysis
- **`@dependency-audit`** - Check for vulnerable dependencies
- **`@create-issues`** - Generate GitHub issues for findings
```

#### Documentation Assistant Pattern

```markdown
# Name: Documentation Assistant

# Focus: Technical documentation creation and improvement

# Temperature: 0.4

# Style: Clear, helpful, and detail-oriented

You help developers create comprehensive, maintainable documentation.

## Capabilities

- Generate API documentation from code
- Create README files and getting started guides
- Produce architecture diagrams with Mermaid
- Improve existing documentation clarity

## Interactive Commands

- **`@doc-api`** - Generate API documentation
- **`@doc-readme`** - Create or improve README
- **`@doc-diagram`** - Generate architecture diagrams
```

#### Code Exploration Pattern

```markdown
# Name: Codebase Explorer

# Focus: Rapid codebase understanding and analysis

# Temperature: 0.5

# Style: Systematic, educational, and context-aware

You help developers quickly understand unfamiliar codebases through structured analysis.

## Analysis Methodology

### Phase 1: Project Discovery

1. **Structure Mapping**: Analyze directory and file organization
2. **Technology Stack**: Identify frameworks and dependencies
3. **Entry Points**: Locate main files and configuration

### Phase 2: Architecture Understanding

1. **Pattern Recognition**: Identify architectural patterns
2. **Component Relationships**: Map dependencies
3. **Data Flow**: Understand data movement

## Interactive Commands

- **`@overview`** - High-level project summary
- **`@architecture`** - Architectural analysis
- **`@tech-stack`** - Technology assessment
- **`@hotspots`** - Critical components to understand
```

#### Architecture Review Pattern

```markdown
# Name: Architecture Reviewer

# Focus: System design evaluation and improvement

# Temperature: 0.5

# Style: Strategic, pragmatic, and design-oriented

You assess software architecture and suggest improvements aligned with best practices.

## Your Core Expertise

- **Design Patterns**: Recognition and application
- **Scalability**: Performance and growth considerations
- **Maintainability**: Code organization and technical debt
- **Security**: Architectural security principles

## Interactive Commands

- **`@architecture-review`** - Comprehensive design assessment
- **`@pattern-analysis`** - Design pattern evaluation
- **`@scalability-check`** - Scalability assessment
- **`@refactor-suggest`** - Refactoring recommendations
```

## Common Patterns and Anti-Patterns

### Effective Patterns

✅ **Command-Driven Interaction Model**:

```markdown
## Interactive Commands

### Analysis Commands

- **`@scan`** - Initial scan
- **`@analyze`** - Deep analysis
- **`@report`** - Generate report

### Action Commands

- **`@fix`** - Apply fixes
- **`@create-issue`** - Create GitHub issue
```

Benefits: Clear, discoverable, efficient workflows

✅ **Phased Methodology Approach**:

```markdown
## Analysis Methodology

### Phase 1: Discovery

[Steps for initial discovery]

### Phase 2: Analysis

[Steps for deep analysis]

### Phase 3: Reporting

[Steps for documentation]
```

Benefits: Consistent approach, comprehensive coverage, manageable complexity

✅ **Clear Response Format Specification**:

```markdown
## Response Format

1. **🎯 Summary** (brief overview)
2. **📊 Findings** (key results)
3. **💡 Recommendations** (action items)
```

Benefits: Predictable output, easy to consume, actionable

✅ **Helpful Example Interactions**:

```markdown
## Example Interactions

**User**: "Analyze this codebase"
**Response**: Use `@overview` for summary, then `@deep-dive` for details

**User**: "@overview"
**Response**: [Structured output showing project structure and key insights]
```

Benefits: Demonstrates capabilities, guides users, sets expectations

### Anti-Patterns to Avoid

❌ **Overly Broad or Unfocused Scope**:

```markdown
# Focus: Everything related to code, documentation, deployment, and more

# Problem: No clear value proposition, overlaps with default Copilot

# Solution: Focus on specific, high-value domain
```

❌ **Unclear or Inconsistent Commands**:

```markdown
## Commands

- **`@scan`** - Scan code
- **`@s`** - Another scan
- **`@security-full-comprehensive-audit`** - Security check

# Problems: Abbreviations unclear, inconsistent naming, one command too verbose

# Solution: Use consistent, clear, verb-noun patterns
```

❌ **Missing Example Interactions**:

```markdown
# Name: Complex Analyzer

# Focus: Does many things

[No examples showing how to use it]

# Problem: Users don't know how to interact with the mode

# Solution: Include realistic examples demonstrating key features
```

❌ **Vague Mission Statement**:

```markdown
You help developers with their code and other tasks.

# Problem: Too generic, no clear value proposition

# Solution: Be specific about role, domain, and approach
```

❌ **Inconsistent Formatting**:

```markdown
## Some Section

- Bullet point
- Another point

## another section

1. Numbered item

- Mixed bullet item

# Problems: Inconsistent capitalization, mixed list types without reason

# Solution: Use consistent heading styles and list formats
```

❌ **Missing Communication Principles**:

```markdown
[Chat mode with no guidance on response style or behavior]

# Problem: Inconsistent responses, unclear expectations

# Solution: Define communication principles and guidelines
```

## Integration and Activation

### How to Use Custom Chat Modes

**Activating a Chat Mode in GitHub Copilot**:

1. **In VS Code**:

   - Open GitHub Copilot chat panel
   - Type `@` to see available chat modes
   - Select your custom mode from the list
   - Or type `@<modename>` directly (e.g., `@SecurityAnalyzer`)

2. **Using Commands**:

   - Activate mode: `@SecurityAnalyzer`
   - Use mode-specific command: `@security-scan`
   - Ask questions: "What security issues do you see?"

3. **Context Awareness**:
   - Chat modes have access to open files
   - They can reference workspace context
   - They leverage repository structure

**Example Session**:

```
User: @SecurityAnalyzer
Copilot: [Activates Security Analyzer mode]

User: @security-scan
Copilot: [Performs comprehensive security scan with structured output]

User: @create-issues
Copilot: [Generates GitHub issues for identified vulnerabilities]
```

### Switching Between Chat Modes

**Switching Modes**:

- Activate different mode: `@DocDesignArchitect`
- Return to default: `@copilot` or start new chat
- Chain modes: Use `@SecurityAnalyzer` for scan, then `@DocDesignArchitect` for documenting findings

**Multi-Mode Workflows**:

```
1. @CodebaseExplorer @overview  → Understand project structure
2. @SecurityAnalyzer @scan      → Identify security issues
3. @DocDesignArchitect         → Document findings
4. @GitFlowStrategist          → Plan fix integration
```

### Combining Chat Modes with Other Copilot Features

**Integration Points**:

1. **Inline Suggestions**: Chat modes enhance context for code completion
2. **Code Actions**: Use chat mode insights to guide refactoring
3. **Workspace Context**: Chat modes leverage open files and project structure
4. **Terminal Integration**: Execute suggested commands directly
5. **GitHub Integration**: Create issues, manage PRs from chat mode output

**Example Combined Workflow**:

```
1. Use @CodebaseExplorer to understand architecture
2. Get inline Copilot suggestions for implementation
3. Use @SecurityAnalyzer to review changes
4. Let Copilot generate tests based on insights
5. Use @GitFlowStrategist to plan merge strategy
```

### README Documentation

For complex or specialized chat modes, create companion README files:

**README Location**: `.github/chatmodes/README-<ModeName>.md`

**README Contents**:

```markdown
# [Mode Name] Chat Mode

## Overview

[What this mode does and why it's valuable]

## When to Use

[Scenarios where this mode is helpful]

## Getting Started

[Quick start guide]

## Commands Reference

[Detailed command documentation]

## Examples

[Extended usage examples]

## Best Practices

[Tips for effective use]

## Troubleshooting

[Common issues and solutions]
```

**Example**: For a complex security analyzer:

- Main mode: `SecurityAnalyzer.chatmode.md`
- README: `.github/chatmodes/README-SecurityAnalyzer.md`

## Maintenance and Evolution

### Versioning

While chat mode files don't have explicit version fields, track evolution through:

**Git Commits**:

```
feat(chatmode): add SecurityAnalyzer with OWASP commands
fix(chatmode): clarify SecurityAnalyzer command descriptions
docs(chatmode): add examples to SecurityAnalyzer
```

**When to Update**:

- **Minor Updates**: Clarify descriptions, fix typos, add examples
- **Feature Additions**: Add new commands, expand expertise areas
- **Major Changes**: Restructure methodology, change focus, revise commands

**Change Documentation**:

Consider adding a changelog section for frequently updated modes:

```markdown
## Changelog

### 2025-10-21

- Added `@threat-model` command for threat modeling workflows
- Expanded cryptographic analysis expertise
- Added examples for API security assessment

### 2025-10-15

- Initial release with core security scanning capabilities
```

### Feedback Loop

**Gathering User Feedback**:

1. **Direct Feedback**:

   - Ask users about their experience
   - Collect suggestions for improvements
   - Identify confusing or missing features

2. **Usage Monitoring**:

   - Which commands are used most?
   - What questions do users ask repeatedly?
   - Where do users get stuck?

3. **Issue Tracking**:
   - Create issues for feature requests
   - Track bugs in command descriptions
   - Prioritize improvements

**Feedback Collection Methods**:

```markdown
## Feedback Template

**Mode Used**: [Mode name]
**Use Case**: [What you were trying to do]
**What Worked**: [Positive aspects]
**What Didn't Work**: [Pain points]
**Suggestions**: [Ideas for improvement]
```

### Iterating on Chat Mode Design

**Improvement Process**:

1. **Collect Feedback**: Gather user experiences and suggestions
2. **Identify Patterns**: Find common issues or requests
3. **Prioritize Changes**: Focus on high-impact improvements
4. **Implement Updates**: Make changes incrementally
5. **Test Changes**: Validate improvements with users
6. **Document Updates**: Update README or add changelog

**Common Improvement Areas**:

| Issue                | Solution                                  |
| -------------------- | ----------------------------------------- |
| Commands unclear     | Add more examples, clarify descriptions   |
| Output inconsistent  | Define clearer response format guidelines |
| Missing capabilities | Extend expertise areas, add commands      |
| Too complex          | Simplify methodology, reduce commands     |
| Wrong temperature    | Adjust for more/less creativity           |

### Community Contributions

**Encouraging Contributions**:

1. **Documentation**: Make authoring guidelines accessible
2. **Templates**: Provide starter templates
3. **Examples**: Show successful patterns
4. **Review Process**: Define clear review criteria
5. **Recognition**: Credit contributors

**Contribution Workflow**:

```
1. Fork/branch repository
2. Create new chat mode or modify existing
3. Follow authoring guidelines
4. Test thoroughly
5. Submit pull request
6. Address review feedback
7. Merge and announce
```

### Deprecation Strategies

**When to Deprecate**:

- Mode is no longer relevant
- Functionality merged into another mode
- Better alternatives exist
- No longer maintained

**Deprecation Process**:

1. **Announce**: Notify users of deprecation timeline
2. **Migration Guide**: Provide alternative modes or workflows
3. **Grace Period**: Keep mode available for transition period
4. **Archive**: Move to archive directory or remove
5. **Documentation**: Update READMEs and remove from listings

**Deprecation Notice Example**:

```markdown
# Name: Old Mode Name

# **DEPRECATED**: This mode is deprecated as of 2025-10-21

**Reason**: Functionality has been merged into the new SecurityAnalyzer mode.

**Migration**: Please use `@SecurityAnalyzer` instead. See migration guide at...

**Removal Date**: This mode will be removed on 2025-11-21.
```

---

## Quick Reference

### Chat Mode File Checklist

**Before Creating**:

- [ ] Identified clear, focused domain
- [ ] Researched existing chat modes to avoid duplication
- [ ] Defined target audience and use cases
- [ ] Determined appropriate temperature setting
- [ ] Planned command structure (if applicable)

**File Setup**:

- [ ] Created file in `.github/chatmodes/`
- [ ] Named file using PascalCase with `.chatmode.md` extension
- [ ] Added all required header fields (Name, Focus, Temperature, Style)
- [ ] Separated header from content with blank line

**Content Complete**:

- [ ] Mission statement clearly defines purpose
- [ ] Core expertise areas listed (5-10 items)
- [ ] Methodology section included for complex workflows
- [ ] Interactive commands documented with descriptions
- [ ] Response format guidelines provided
- [ ] Communication principles established
- [ ] Example interactions included

**Quality Checks**:

- [ ] Markdown syntax correct throughout
- [ ] Consistent formatting and terminology
- [ ] No spelling or grammar errors
- [ ] Clear, actionable language
- [ ] Specific examples provided
- [ ] Commands follow naming conventions

**Testing**:

- [ ] Tested in GitHub Copilot
- [ ] Commands work as documented
- [ ] Response format is helpful
- [ ] Output quality is appropriate for temperature
- [ ] Peer reviewed

**Documentation**:

- [ ] README created for complex modes
- [ ] Updated main repository documentation
- [ ] Added to chat mode catalog (if exists)

### Header Fields Quick Reference

```markdown
# Name: [Display Name in Title Case]

# Focus: [Specific domain or task description]

# Temperature: [0.0-1.0 based on use case]

# Style: [Communication tone and approach]
```

**Temperature Guide**:

- 0.3: Security, compliance, critical precision
- 0.4: Documentation, analysis, code review
- 0.5: General technical work, exploration
- 0.6: Architecture, design, brainstorming

### Command Naming Patterns

| Pattern          | Example          | Use For                    |
| ---------------- | ---------------- | -------------------------- |
| `@verb-noun`     | `@scan-security` | Actions                    |
| `@domain-action` | `@security-scan` | Domain-specific actions    |
| `@domain-target` | `@doc-api`       | Domain-target combinations |
| `@action`        | `@overview`      | Simple, common actions     |

### Common Sections Reference

```markdown
## Your Core Expertise

[Bulleted list of capabilities]

## Analysis Methodology

### Phase 1: [Name]

[Numbered steps]

## Interactive Commands

[Bulleted command list with descriptions]

## Response Format

[Numbered sections with guidance]

## Communication Guidelines

[Bulleted principles]

## Example Interactions

**User**: [Example]
**Response**: [Expected response]
```

---

## Post-Creation Requirements

After creating this instruction file, you **MUST**:

### 1. Create AI Conversation Log

Create `ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md` with:

```markdown
# AI Conversation Log

- Chat ID: create-chatmode-instructions-20251021
- Operator: johnmillerATcodemag-com
- Model: anthropic/claude-3.5-sonnet@2024-10-22
- Started: 2025-10-21T19:30:00Z
- Ended: 2025-10-21T19:45:00Z
- Total Duration: 00:15:00

## Context

- Inputs: `.github/prompts/create-chatmode-instructions.prompt.md`
- Targets: `.github/instructions/create-chatmode.instructions.md`
- Constraints/Policies: `.github/instructions/ai-assisted-output.instructions.md`

## Exchanges

### Exchange 1

[2025-10-21T19:30:00Z] johnmillerATcodemag-com

\`\`\`text
#file:create-chatmode-instructions.prompt.md
\`\`\`

[2025-10-21T19:35:00Z] anthropic/claude-3.5-sonnet@2024-10-22

\`\`\`text
I'll execute the prompt to generate comprehensive instructions for creating custom GitHub Copilot chat modes.
[Reads existing chat mode files for reference patterns]
\`\`\`

[2025-10-21T19:45:00Z] anthropic/claude-3.5-sonnet@2024-10-22

\`\`\`text
Created comprehensive chat mode authoring instructions at:
.github/instructions/create-chatmode.instructions.md

The file includes:

- Complete header field specifications
- Content structure guidelines
- Command design best practices
- Quality assurance checklists
- Templates and examples
- Integration guidance
- Maintenance strategies
  \`\`\`

## Work Burst Closure

**Artifacts Produced**:

- `.github/instructions/create-chatmode.instructions.md` - Comprehensive authoring guidelines for custom chat modes

**Next Steps**:

- [ ] Update README.md with link to new instruction file
- [ ] Create summary.md for this session
- [ ] Test instructions by creating a new chat mode

**Duration Summary**:

- Analyze existing chat modes: 00:05:00
- Generate comprehensive instructions: 00:10:00
- Total: 00:15:00
```

### 2. Create Summary File

Create `ai-logs/2025/10/21/create-chatmode-instructions-20251021/summary.md` following the template in `ai-assisted-output.instructions.md`.

### 3. Update README.md

Add to the appropriate section in `README.md`:

```markdown
### Guidance & Instructions

- [`.github/instructions/create-chatmode.instructions.md`](.github/instructions/create-chatmode.instructions.md) — Comprehensive authoring guidelines for creating custom GitHub Copilot chat modes ([chat log](ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md))
```

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-21
**Maintainer**: AI-Assisted Development Team
**Compliance**: `.github/instructions/ai-assisted-output.instructions.md`
