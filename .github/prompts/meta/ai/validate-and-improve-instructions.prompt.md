---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["run", "create", "edit", "search", "read"]
description: Orchestrate iterative validation and improvement of instruction files through automated cycles
prompt_metadata:
  id: validate-and-improve-instructions-meta-prompt
  title: Validate and Improve Instruction Files (Iterative)
  owner: johnmillerATcodemag-com
  output_path: .github/instructions/
  category: meta-automation
  tags: [meta-prompt, validation, quality-assurance, iterative-improvement]
  output_format: multiple
---

# Validate and Improve Instruction Files

Automate quality improvement workflow for instruction files through iterative generation, validation, refinement.

## Context
Ensure quality/consistency through automated workflow:
1. Generate all instruction files from source prompts
2. Analyze for conflicts, inconsistencies, redundancy
3. Fix root causes in source prompts (not generated files)
4. Validate improvements via re-generation
5. Iterate until resolved or max attempts (3)

Must comply with `.github/instructions/ai-assisted-output.instructions.md` and `copilot-instructions.md`.

## Workflow Steps

### Phase 1: Branch Creation
```bash
git checkout -b feature/validate-improve-instructions-$(date +%Y%m%d-%H%M%S)
```
Record initial state (file count, baseline), initialize iteration counter (max: 3)

### Phase 2: Generation Cycle
Execute prompts in sequence:
1. `.github/prompts/create-ai-assisted-output-instructions.prompt.md` → `ai-assisted-output.instructions.md`
2. `.github/prompts/meta/create-instruction-file-instructions.prompt.md` → `instruction-standards.instruction.md`
3. `.github/prompts/prompt-file.instructions.prompt.md` → `create-prompt.instructions.md`
4. `.github/prompts/create-use-case-instructions.prompt.md` → `create-use-case.instructions.md`

Wait for completion, verify each created successfully.

### Phase 3: Validation & Analysis
Submit `.github/prompts/check-context.prompt.md` targeting `.github/instructions/`
Analyze output for:
- Conflicting instructions
- Factual inconsistencies
- Logical contradictions
- Scope/priority conflicts
- Duplication/redundancy
- Communication gaps

### Phase 4: Root Cause Analysis
If issues found:
- Categorize by severity (Critical/High/Medium/Low)
- Trace to source prompts
- Document specific conflicts
- Propose prompt fixes (NOT instruction fixes)

### Phase 5: Iterative Improvement
For each issue:
1. Edit source prompt to address root cause
2. Re-run affected prompts
3. Re-validate
4. Track improvements
5. Repeat if needed (max 3 iterations)

### Phase 6: Finalization
- Commit all changes with detailed message
- Create/update PR with validation summary
- Document remaining issues (if any)
- Tag for review

## Output Format
Report per iteration:
- Issues found (count by severity)
- Prompts modified
- Files re-generated
- Improvements validated
- Remaining issues

Final report:
- Initial vs final state
- All modifications made
- Validation results
- Recommendations for remaining issues

## Constraints
- Max 3 iterations
- Fix prompts, not generated files
- Preserve functionality while improving quality
- Document all changes
