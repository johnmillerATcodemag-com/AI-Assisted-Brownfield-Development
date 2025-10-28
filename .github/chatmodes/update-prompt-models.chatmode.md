---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["edit", "read", "search"]
description: "Updates default model specification in Copilot instructions and provides interactive selection for updating existing prompt files"
prompt_metadata:
  id: update-model-defaults
  title: Update Model Defaults with Selection
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Brownfield-Development
  version: 1.1.0
  created: 2025-01-15
  updated: 2025-01-15
  output_path: multiple
  category: maintenance
  tags: [model-management, copilot-config, interactive]
  output_format: multiple
---

# Update Model Defaults Chat Mode

## Context

Updates the default model specification in Copilot instructions to Claude 4.5 and provides interactive checkbox selection for updating existing prompt files.

**CRITICAL**: All AI-generated artifacts must comply with
`.github/instructions/ai-assisted-output.instructions.md`

## Requirements

### Phase 1: Update Copilot Instructions (Auto-Execute)

1. **Read**: `.github/instructions/copilot-instructions.md`
2. **Update default model** from:
   ```yaml
   model: "anthropic/claude-3.5-sonnet@2024-10-22"
   ```
   To:
   ```yaml
   model: "anthropic/claude-3.5-sonnet@2024-10-22"
   ```

### Phase 2: Interactive File Selection

1. **Search** for all `**/*.prompt.md` files
2. **Analyze** model specifications
3. **Present checkbox interface**:

## Execution Steps

### Step 1: Update Copilot Instructions

Automatically update `.github/instructions/copilot-instructions.md`:

```yaml
- **Default Model for Prompts**: `"anthropic/claude-3.5-sonnet-4.5@2024-12-15"`
  - Latest version verified via external search
  - Use this as the default in new prompt files
```

### Step 2: Generate Interactive Selection

Present selection interface like this:

```markdown
## Prompt File Update Selection

Found X prompt files. Select which to update:

### ✅ Files Using Old Default (can be updated)
- [ ] 1. `.github/prompts/create-api-docs.prompt.md`
  - **Current**: `anthropic/claude-3.5-sonnet@2024-10-22`
  - **New**: `anthropic/claude-3.5-sonnet-4.5@2024-12-15`
  - **Description**: API documentation generator

- [ ] 2. `.github/prompts/analyze-code.prompt.md`
  - **Current**: `anthropic/claude-3.5-sonnet@2024-10-22`
  - **New**: `anthropic/claude-3.5-sonnet-4.5@2024-12-15`
  - **Description**: Code analysis and review

### ✅ Files Missing Model (can add default)
- [ ] 3. `.github/prompts/legacy-helper.prompt.md`
  - **Current**: No model specified
  - **New**: Add `anthropic/claude-3.5-sonnet-4.5@2024-12-15`
  - **Description**: Legacy utility functions

### ❌ Files with Custom Models (preserved - reference only)
- 4. `.github/prompts/openai-specific.prompt.md`
  - **Current**: `openai/gpt-4o@2024-11-20` (PRESERVED)
  - **Description**: OpenAI-specific functionality

- 5. `.github/prompts/google-gemini.prompt.md`
  - **Current**: `google/gemini-1.5-pro@2024-02` (PRESERVED)
  - **Description**: Google Gemini integration

**Selection Options**:
- Enter numbers: "1, 3, 5"
- Enter ranges: "1-3, 5"
- Enter "all" for all updateable files (1-3 in this example)
- Enter "none" to skip updates

Which files should I update?
```

### Step 3: Process Selection

Parse user input and update only selected files:

**Valid Selection Formats**:
- Numbers: `"1, 3"` or `"1,3"`
- Ranges: `"1-3"` or `"1-5"`
- Combined: `"1, 3-5, 7"`
- Keywords: `"all"`, `"none"`

**Update Logic**:
```yaml
# Only for selected files:
# Before
model: "anthropic/claude-3.5-sonnet@2024-10-22"

# After
model: "anthropic/claude-3.5-sonnet@2024-10-22"
```

### Step 4: Confirmation Summary

After updates, provide:

```markdown
## Update Summary

### ✅ Updated Files
- `.github/prompts/create-api-docs.prompt.md` - Updated model to 4.5
- `.github/prompts/legacy-helper.prompt.md` - Added model specification

### ❌ Skipped Files
- `.github/prompts/analyze-code.prompt.md` - Not selected
- `.github/prompts/openai-specific.prompt.md` - Custom model preserved

### 📊 Statistics
- Total files found: 5
- Updateable files: 3
- Selected for update: 2
- Successfully updated: 2
- Custom models preserved: 2
```

## File Categories

### ✅ Updateable (show checkboxes)
1. **Old Default**: Using `anthropic/claude-3.5-sonnet@2024-10-22`
2. **Missing Model**: No model field in front matter

### ❌ Preserved (show for reference)
1. **Custom Models**: Different providers (`openai/*`, `google/*`)
2. **Custom Versions**: Intentionally different Claude versions
3. **Newer Models**: Already using Claude 4.x or newer

### ⚠️ Special Cases (ask user)
1. **Ambiguous Versions**: Cannot determine if intentional
2. **Invalid Format**: Malformed model specifications

## Error Handling

- **File not found**: Report and continue
- **Parse errors**: Report malformed YAML, skip file
- **Invalid selection**: Ask for clarification
- **Permission errors**: Report and suggest manual update

## Quality Assurance

- [ ] ✅ Copilot instructions updated with new default
- [ ] ✅ Only selected files modified
- [ ] ✅ Custom models preserved (never overwritten)
- [ ] ✅ All updates include proper provenance metadata
- [ ] ✅ Interactive selection presented clearly
- [ ] ✅ Update summary provided
- [ ] ✅ Conversation logged completely

## Expected Deliverables

1. **Updated Copilot Instructions**: New default model
2. **Interactive Selection Interface**: Checkbox list with descriptions
3. **Updated Prompt Files**: Only user-selected files
4. **Summary Report**: What was updated vs preserved
5. **Conversation Log**: Complete interaction record

This chat mode provides full control over which prompt files to update while automatically handling the Copilot instructions update and preserving custom model configurations.
