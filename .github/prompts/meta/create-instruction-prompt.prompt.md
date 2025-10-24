---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "prompt-file.instructions-2025-10-15"
prompt: |
  Create a meta-prompt generator that produces instruction-generating prompts with
  AI provenance requirements built in.
started: "2025-10-15T15:00:00Z"
ended: "2025-10-15T15:20:00Z"
task_durations:
  - task: "meta-prompt design"
    duration: "00:15:00"
  - task: "template creation"
    duration: "00:05:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
mode: chat
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: Interactive guide for creating instruction-prompt files with AI provenance requirements built-in
prompt_metadata:
  id: create-instruction-prompt-generator
  title: Interactive Instruction Prompt Generator
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Brownfield-Development
  version: 2.0.0
  created: 2025-10-15
  updated: 2025-10-15
  output_path: .github/prompts/<instruction-name>.prompt.md
  category: meta-prompt
  tags: [meta-prompt, prompt-generation, ai-provenance, standards]
  output_format: markdown
---

---

# Interactive Instruction Prompt Generator

I'll guide you through creating a new instruction-prompt file that automatically includes AI provenance requirements.

This ensures any instruction file generated will comply with our AI-assisted output standards.

**Important**: Follow [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) for model format, conversation logging, and post-creation requirements.

## Let's Get Started

**First, let's understand what you're creating:**

### Question 1: What's the domain?

What topic or area will this instruction file cover?

Examples:

- API documentation
- Test authoring
- Architecture diagrams
- Code review guidelines
- Database schema design

**Your answer:** _[waiting for response]_

---

### Question 2: What's the instruction ID?

This should be a unique identifier in kebab-case format.

Pattern: `create-<domain>-instructions`

Example: If your domain is "API documentation", the ID would be `create-api-documentation-instructions`

**Your answer:** _[waiting for response]_

---

### Question 3: Where should the instruction file be saved?

Provide the full path where the generated instruction file should be created.

Pattern: `.github/instructions/<domain>.instructions.md`

Example: `.github/instructions/api-documentation.instructions.md`

**Your answer:** _[waiting for response]_

---

### Question 4: What files should these instructions apply to? (Optional)

You can specify a glob pattern to automatically apply these instructions when working with certain files.

Examples:

- `"docs/api/**/*.md"` - All markdown files under docs/api/
- `"**/*.test.ts"` - All TypeScript test files
- `"**/*.diagram.mmd"` - All Mermaid diagram files
- `"**/*"` - All files (use sparingly)

**Your answer:** _[waiting for response, or skip if not applicable]_

---

### Question 5: What are the key requirements?

What specific content, structure, or rules should the instruction file contain?

Examples:

- Required sections (e.g., "Must include Prerequisites, Steps, Examples")
- Templates to include
- Naming conventions
- Style guidelines
- Validation criteria

**Your answer:** _[waiting for response]_

---

## Review & Confirm

Based on your answers, I'll create a prompt file with:

- **Domain:** _[your domain]_
- **Prompt ID:** _[your instruction-id]_
- **Prompt File Path:** `.github/prompts/<instruction-id>.prompt.md`
- **Generated Instruction File Path:** _[your output path]_
- **ApplyTo Pattern:** _[your pattern or "N/A"]_
- **Key Requirements:** _[your requirements]_

The generated prompt will ensure that any instruction file it creates includes:
✅ All 10 required AI provenance metadata fields
✅ Proper YAML front matter structure
✅ Embedded provenance (not sidecar files)
✅ Compliance with ai-assisted-output.instructions.md

**Does this look correct?** _[waiting for confirmation]_

---

## Deliverable

Once confirmed, I'll create the prompt file at:
`.github/prompts/<instruction-id>.prompt.md`

The prompt file will have this structure:

### YAML Front Matter

```yaml
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create"]
description: <Description based on your domain>
prompt_metadata:
  id: <your-instruction-id>
  title: Generate <Domain> Instructions
  owner: <current-user>
  repository: AI-Assisted-Brownfield-Development
  version: 1.0.0
  created: <today's-date>
  updated: <today's-date>
  output_path: <your-output-path>
  category: documentation
  tags: [instructions, <domain-tags>]
  output_format: markdown
```

````

### Content Sections

**Context Section** (Required):
```markdown
## Context
<Domain-specific context>

**CRITICAL**: All AI-generated artifacts must comply with
.github/instructions/ai-assisted-output.instructions.md
````

**Requirements Section** (Required):

- Structure and sections needed
- Templates to include
- Examples to provide
- Best practices to document
- Common pitfalls to address

**Deliverable Section** (Required - with AI Provenance Template):

```markdown
## Deliverable

Generate `<output-path>` with the following YAML front matter:

## \`\`\`yaml

ai_generated: true
model: "<provider>/<model-name>@<version>" # e.g., "openai/gpt-4o@2024-11-20" or "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<username>"
chat_id: "<chat-id>"
prompt: |
<exact-prompt-text>
started: "<ISO8601-timestamp>"
ended: "<ISO8601-timestamp>"
task_durations:

- task: "<task-name>"
  duration: "<hh:mm:ss>"
  total_duration: "<hh:mm:ss>"
  ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
  source: ".github/prompts/meta/create-instruction-prompt.prompt.md"
  applyTo: "<pattern>" # If specified

---

\`\`\`

**Important**: Use the underlying AI model (e.g., `"openai/gpt-4o@2024-11-20"`), not the interface (e.g., "github/copilot").

### Content

<Specific content requirements for the instruction file>
```

---

## Validation

Before creating the file, I'll verify:

✅ All user inputs are complete and valid
✅ File paths follow repository conventions
✅ Prompt ID uses kebab-case format
✅ ApplyTo pattern (if provided) is a valid glob
✅ YAML front matter template includes all 11 required fields
✅ Deliverable section explicitly requires AI provenance metadata
✅ Context section includes CRITICAL compliance statement

---

## Ready to Create

Once you've answered all questions and confirmed the review, I'll generate the prompt file with complete AI provenance metadata tracking built-in.

**This ensures every instruction file created by this prompt will automatically comply with our AI-assisted output standards.** 2. <Templates, examples, checklists> 3. <Any domain-specific guidance>

The file should be comprehensive, self-contained, and immediately usable.

````

## Output Format

Generate a complete prompt file at `.github/prompts/<instruction-id>.prompt.md` that:

1. ✅ Follows the structure above
2. ✅ Includes AI provenance requirements in Deliverable section
3. ✅ References `.github/instructions/ai-assisted-output.instructions.md`
4. ✅ Uses appropriate `applyTo` pattern if specified
5. ✅ Contains clear, actionable requirements
6. ✅ Specifies expected instruction file structure

## Validation Checklist

Before generating, verify:

- [ ] Instruction ID is unique and follows naming convention
- [ ] Output path is correct and follows repository structure
- [ ] Deliverable section includes complete AI provenance template
- [ ] Context section references AI-assisted output policy
- [ ] Requirements are clear and specific
- [ ] Tools array matches the task (create vs create+edit)

## Example Usage

**User Request**: "Create a prompt for generating test authoring instructions"

**Generated Prompt Would Include**:

- ID: `create-test-authoring-instructions`
- Output: `.github/instructions/test-authoring.instructions.md`
- ApplyTo: `"**/*.test.ts"` or `"**/*.test.js"`
- Deliverable section with full AI provenance template

## Quality Standards

The generated prompt must:

- Be immediately executable without modification
- Produce compliant instruction files on first run
- Include all mandatory AI provenance fields
- Reference the AI-assisted output policy
- Provide clear guidance for instruction content

## Deliverable

Generate a complete, executable prompt file that will produce instruction files with full AI provenance metadata compliance.

**File Location**: `.github/prompts/<instruction-id>.prompt.md`

**File Content**: Complete YAML front matter + markdown prompt following the structure above

---

## Post-Creation Requirements

After creating the prompt file, you **MUST** also:

### 1. Update AI Conversation Log

Add the new prompt to the **Artifacts Produced** section:

```markdown
**Artifacts Produced**:
- `.github/prompts/<instruction-id>.prompt.md` - <Brief description>
````

**Important**: In conversation.md, use the operator's GitHub username (not "USER") for all exchanges:

```markdown
### Exchange N

[<timestamp>] <operator-username>

\`\`\`text
<user's prompt>
\`\`\`

[<timestamp>] AI

\`\`\`text
<AI response>
\`\`\`
```

**Location**: `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md`

### 2. Update or Create Summary

Add or update `summary.md` with:

- Session objectives
- The new prompt file in artifacts table
- Key decisions made during creation

**Location**: `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/summary.md`

### 3. Update README.md

Add entry to appropriate section:

```markdown
### Meta-Prompts (Prompt Generators)

- [`.github/prompts/meta/<filename>.prompt.md`](.github/prompts/meta/<filename>.prompt.md) — <Description> ([chat log](ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md))
```

Or for instruction-generating prompts:

```markdown
### Guidance & Instructions

- [`.github/prompts/<filename>.prompt.md`](.github/prompts/<filename>.prompt.md) — <Description> ([chat log](ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md))
```

---

**Remember**: Follow `.github/instructions/ai-assisted-output.instructions.md` for complete provenance requirements.

```

```
