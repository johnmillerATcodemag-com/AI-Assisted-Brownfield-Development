---
ai_generated: true
model: "openai/gpt-4o@2024-11-20"
operator: "johnmillerATcodemag-com"
chat_id: "validate-improve-instructions-2025-10-15"
prompt: |
  Create a meta-prompt that orchestrates iterative improvement of instruction files
  through generation, validation, and refinement cycles.
started: "2025-10-15T16:30:00Z"
ended: "2025-10-15T16:45:00Z"
task_durations:
  - task: "meta-prompt design"
    duration: "00:10:00"
  - task: "workflow orchestration logic"
    duration: "00:05:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md"
source: "johnmillerATcodemag-com"
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["run", "create", "edit", "search", "read"]
description: Orchestrates iterative validation and improvement of instruction files through automated generation, analysis, and refinement cycles
prompt_metadata:
  id: validate-and-improve-instructions-meta-prompt
  title: Validate and Improve Instruction Files (Iterative Meta-Prompt)
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Brownfield-Development
  version: 1.0.0
  created: 2025-10-15
  updated: 2025-10-15
  output_path: .github/instructions/
  category: meta-automation
  tags: [meta-prompt, validation, quality-assurance, iterative-improvement, governance]
  output_format: multiple
---

# Validate and Improve Instruction Files (Iterative Meta-Prompt)

This meta-prompt orchestrates an automated quality improvement workflow for instruction files through iterative generation, validation, and refinement cycles.

## Context

This repository uses AI-assisted generation for instruction files. To ensure quality and consistency, we need an automated workflow that:

1. Generates all instruction files from their source prompts
2. Analyzes them for conflicts, inconsistencies, and redundancy
3. Fixes root causes in the source prompts (not the generated files)
4. Validates improvements through re-generation
5. Iterates until issues are resolved or maximum attempts reached

**CRITICAL**: All work must comply with `.github/instructions/ai-assisted-output.instructions.md` and `.github/instructions/copilot-instructions.md`.

## Objective

Execute a complete validation and improvement cycle for all instruction-generating prompts in the repository.

## Workflow Steps

### Phase 1: Branch Creation and Setup

1. **Create Feature Branch**

   ```bash
   git checkout -b feature/validate-improve-instructions-$(date +%Y%m%d-%H%M%S)
   ```

2. **Record Initial State**
   - Count existing instruction files
   - Create baseline snapshot
   - Initialize iteration counter (max: 3)

### Phase 2: Generation Cycle

Execute the following prompts in sequence:

1. **Submit**: `.github/prompts/create-ai-assisted-output-instructions.prompt.md`

   - Generates: `.github/instructions/ai-assisted-output.instructions.md`
   - Wait for completion
   - Verify file created successfully

2. **Submit**: `.github/prompts/meta/create-instruction-file-instructions.prompt.md`

   - Generates: `.github/instructions/instruction-standards.instruction.md`
   - Wait for completion
   - Verify file created successfully

3. **Submit**: `.github/prompts/prompt-file.instructions.prompt.md`

   - Generates: `.github/instructions/create-prompt.instructions.md`
   - Wait for completion
   - Verify file created successfully

4. **Submit**: `.github/prompts/create-use-case-instructions.prompt.md`
   - Generates: `.github/instructions/create-use-case.instructions.md`
   - Wait for completion
   - Verify file created successfully

### Phase 3: Validation and Analysis

5. **Submit**: `.github/prompts/check-context.prompt.md`

   - Analyzes all instruction files in `.github/instructions/`
   - Reports conflicts, inconsistencies, redundancy, and other issues
   - Categorizes issues by severity and location
   - Wait for complete analysis

6. **Parse Analysis Results**
   - Count total issues found
   - Categorize by type:
     - Conflicting Instructions
     - Factual Inconsistencies
     - Logical Contradictions
     - Scope/Priority Conflicts
     - Technical Incompatibilities
     - Communication Gaps
     - **Duplication and Redundancy**
   - Map issues to source prompt files

### Phase 4: Root Cause Resolution

7. **For Each Issue Found**:

   **Identify Source Prompt**:

   - Determine which prompt file generated the problematic instruction
   - Map issue location to source prompt section

   **Fix Root Cause**:

   - Edit the SOURCE PROMPT FILE (not the generated instruction)
   - Address the specific issue at its origin
   - Update prompts to prevent recurrence
   - Document changes in commit message

   **Source Prompt Mapping**:

   - `ai-assisted-output.instructions.md` ← `create-ai-assisted-output-instructions.prompt.md`
   - `instruction-standards.instruction.md` ← `meta/create-instruction-file-instructions.prompt.md`
   - `create-prompt.instructions.md` ← `prompt-file.instructions.prompt.md`
   - `create-use-case.instructions.md` ← `create-use-case-instructions.prompt.md`

### Phase 5: Validation Cycle

8. **Delete Generated Instruction Files**

   ```bash
   rm .github/instructions/ai-assisted-output.instructions.md
   rm .github/instructions/instruction-standards.instruction.md
   rm .github/instructions/create-prompt.instructions.md
   rm .github/instructions/create-use-case.instructions.md
   ```

9. **Re-run Generation Cycle** (Phase 2)

   - Execute all prompts again
   - Generate fresh instruction files with fixes applied

10. **Re-run Validation** (Phase 3)
    - Submit `check-context.prompt.md` again
    - Count new issue total

### Phase 6: Iteration Decision Logic

11. **Compare Results**:

```
IF (new_issue_count > previous_issue_count):
    STATUS = "ERROR: Issues increased"
    ACTION = "STOP - Review changes manually"

ELSE IF (new_issue_count == 0):
    STATUS = "SUCCESS: All issues resolved"
    ACTION = "COMMIT and proceed to merge"

ELSE IF (new_issue_count == previous_issue_count):
    STATUS = "WARNING: No improvement"
    IF (iteration_count >= 3):
        ACTION = "STOP - Manual review needed"
    ELSE:
        ACTION = "Try alternative fixes, increment iteration, GOTO Phase 4"

ELSE IF (new_issue_count < previous_issue_count):
    STATUS = "PROGRESS: Issues reduced"
    IF (iteration_count >= 3):
        ACTION = "COMMIT with remaining issues documented"
    ELSE:
        ACTION = "Increment iteration, GOTO Phase 4"
```

### Phase 7: Completion

12. **Success Path** (0 issues):

    - Create comprehensive commit message
    - Stage all changes (prompts + generated files)
    - Commit with provenance metadata
    - Create summary report
    - Update README.md if needed

13. **Partial Success Path** (reduced issues, max iterations):

    - Document remaining issues
    - Commit improvements
    - Create GitHub issue for remaining work
    - Update README.md with status

14. **Failure Path** (increased issues or no progress):
    - Rollback to previous state
    - Create detailed issue report
    - Request manual review

## Success Criteria

- **Primary**: Zero conflicts/inconsistencies found
- **Secondary**: Issues reduced compared to baseline
- **Tertiary**: Clear documentation of remaining issues

## Output Requirements

Generate the following artifacts:

1. **Validation Report** (`validation-report-<timestamp>.md`):

   ```markdown
   # Instruction Validation Report

   **Date**: <ISO8601>
   **Branch**: feature/validate-improve-instructions-<timestamp>
   **Iterations**: <count>
   **Initial Issues**: <count>
   **Final Issues**: <count>
   **Status**: <SUCCESS|PARTIAL|FAILURE>

   ## Issues by Category

   ### Iteration 1

   - Conflicting Instructions: <count>
   - Duplication and Redundancy: <count>
   - [other categories]

   ### Iteration 2 (if applicable)

   ...

   ## Resolutions Applied

   ### Issue #1: [Title]

   - **Category**: [category]
   - **Source Prompt**: [file path]
   - **Fix Applied**: [description]
   - **Result**: [resolved/partial/unresolved]

   ## Remaining Issues

   [List any unresolved issues with recommendations]

   ## Recommendations

   [Next steps for manual review if needed]
   ```

2. **Updated Source Prompts**: All prompt files with fixes applied

3. **Generated Instruction Files**: Fresh, validated instruction files

4. **AI Conversation Log**: Complete session transcript with all iterations

5. **Summary**: Session summary with iteration details

## Quality Standards

- **Prompt Fixes**: Must address root cause, not symptoms
- **Validation**: Must re-validate after each change
- **Documentation**: Must document all iterations and decisions
- **Provenance**: Must maintain complete AI provenance for all changes

## Error Handling

- **Prompt Execution Fails**: Log error, skip to next, report at end
- **Validation Fails**: Capture error details, continue workflow
- **Git Operations Fail**: Rollback to safe state, report error
- **Iteration Limit Reached**: Document state, commit partial progress

## Rollback Strategy

If any critical error occurs:

1. Stash or commit current work in progress
2. Return to original branch
3. Create detailed error report
4. Tag commit with failure reason

## Post-Execution Requirements

After completion:

1. **Update AI Conversation Log**:

   - Document all iterations
   - Include validation results
   - Note all prompt changes

2. **Update Summary**:

   - Session objectives
   - Work completed (iterations, fixes)
   - Key decisions (which fixes worked)
   - Final status and metrics

3. **Update README.md** (if successful):
   - Link to validation report
   - Note instruction file updates
   - Reference conversation log

## Execution Command

To execute this meta-prompt:

1. Ensure working directory is clean
2. Submit this prompt file
3. Monitor progress through each phase
4. Review validation report when complete

## Technical Notes

- **Iteration Safety**: Maximum 3 iterations prevents infinite loops
- **Source Control**: Each iteration creates atomic commits for rollback
- **Parallel Execution**: Prompts execute sequentially to maintain dependencies
- **State Tracking**: Iteration state persists across validation cycles

## Expected Outcomes

**Best Case**: 0 issues after 1-2 iterations
**Typical Case**: Reduced issues after 2-3 iterations
**Worst Case**: Manual review needed with detailed issue documentation

---

**Meta-Prompt Version**: 1.0.0
**Last Updated**: 2025-10-15
**Maintainer**: AI-Assisted Development Team
**Compliance**:

- `.github/instructions/ai-assisted-output.instructions.md`
- `.github/instructions/copilot-instructions.md`
