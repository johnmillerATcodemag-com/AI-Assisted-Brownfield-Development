# AI-Assisted Software Development

This repo was created for the 2025 Next Gen AI Conference Leveraging AI for Legacy Code Refactoring session

## Prompts

[x] #file:check-context.prompt.md apply this prompt to files in the .github/instructions folder

[x] Update the readme.md file with current state of the application. Include mermaid C4 diagrams.

[x] #codebase analyze the code and report any deviations from the instructions in the .github/instructions folder

[x] Looking at the current #codebase, what tests are need and missing?

[x] Looking at the current #codebase, what tests are need and missing in order to verify a successful migration to Vue 3.4?

[x] Looking at the current #codebase, what needs refactoring?

[x] Looking at the current #codebase, what are security concerns? Create issues from your findings.

[x] Analyze the #codebase and create github issues for any dead code you find

[x] Analyze the files in the .github/instructions folder and report where they no longer represent best practices

[ ] #codebase analyze the code and report any deviations from the instructions in the .github/instructions folder

[ ] Create tests for #file:validatorsCustom.js

[ ] Look at the current #codebase and find the bugs?

[ ] Add comprehensive error logging architecture

[ ] The two branches sonnet4 and gpt5 contain implementations of the comprehensive error logging architecture. The gpt5 implementation is in commit aafed869e3c243b758d7a89cf29f19fa70c41f8a. The sonnet4 implementation is in commit fed7e9e927e458fa95f30ef91a3bbfcb201e20ea. Review each implementation and report the pros and cons of each.

## AI-Assisted Artifacts & Provenance

This repository enforces provenance and logging for any AI-assisted outputs (code, docs, diagrams, tests, data).

### Guidance & Instructions

- [`.github/instructions/ai-assisted-output.instructions.md`](.github/instructions/ai-assisted-output.instructions.md) — How to generate AI-assisted outputs with required metadata, logging, and CI enforcement
- [`.github/instructions/copilot-instructions.md`](.github/instructions/copilot-instructions.md) — **GitHub Copilot Users Start Here** - Comprehensive Copilot-specific guidance for model format, conversation logging, and quality standards ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/create-chatmode.instructions.md`](.github/instructions/create-chatmode.instructions.md) — Comprehensive authoring guidelines for creating custom GitHub Copilot chat modes ([chat log](ai-logs/2025/10/21/create-chatmode-instructions-20251021/conversation.md))
- [`.github/instructions/create-prompt.instructions.md`](.github/instructions/create-prompt.instructions.md) — Comprehensive guidelines for authoring effective repository prompts ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))
- [`.github/instructions/instruction-prompt.instructions.md`](.github/instructions/instruction-prompt.instructions.md) — Requirements for prompts that generate instruction files ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))

### Custom GitHub Copilot Chat Modes

Custom chat modes are specialized AI assistants that extend GitHub Copilot's capabilities for specific domains and workflows. Activate with `@<modename>` in GitHub Copilot chat.

- [`.github/chatmodes/DocumentationUpdater.chatmode.md`](.github/chatmodes/DocumentationUpdater.chatmode.md) — Documentation maintenance, accuracy verification, and continuous improvement ([chat log](ai-logs/2025/10/22/create-documentation-updater-chatmode-20251022/conversation.md))
- [`.github/chatmodes/DocDesignArchitect.chatmode.md`](.github/chatmodes/DocDesignArchitect.chatmode.md) — Technical documentation, diagramming with Mermaid, and readability improvements
- [`.github/chatmodes/SecurityAnalyzer.chatmode.md`](.github/chatmodes/SecurityAnalyzer.chatmode.md) — Code security analysis, vulnerability detection, and automated issue creation
- [`.github/chatmodes/codebase-explorer.chatmode.md`](.github/chatmodes/codebase-explorer.chatmode.md) — Rapid codebase understanding and evaluation
- [`.github/chatmodes/GitFlowStrategist.chatmode.md`](.github/chatmodes/GitFlowStrategist.chatmode.md) — Branching policies, merge style enforcement, and CI/CD hygiene

### Meta-Prompts (Prompt Generators)

- [`.github/prompts/meta/create-instruction-prompt.prompt.md`](.github/prompts/meta/create-instruction-prompt.prompt.md) — Generates new instruction-generating prompts with AI provenance built-in ([chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md))

### Instruction-Generating Prompts

- [`.github/prompts/create-chatmode-instructions.prompt.md`](.github/prompts/create-chatmode-instructions.prompt.md) — Generates comprehensive authoring guidelines for creating custom GitHub Copilot chat modes

### Notable Artifacts

- **Prompt Authoring Instructions** ([`.github/instructions/create-prompt.instructions.md`](.github/instructions/create-prompt.instructions.md))

  - Comprehensive guidelines for creating effective, well-structured repository prompts
  - Generated from: [`.github/prompts/prompt-file.instructions.prompt.md`](.github/prompts/prompt-file.instructions.prompt.md)
  - Provenance: [Chat log](ai-logs/2025/10/15/prompt-file.instructions-2025-10-15/conversation.md)

- **Instruction Validation Report** ([`validation-report-20251015-212137.md`](validation-report-20251015-212137.md))
  - Comprehensive analysis of instruction file conflicts and inconsistencies
  - Identifies 7 issues (1 high, 4 medium, 3 low severity) with fixes applied to critical issues
  - Generated from: [`.github/prompts/meta/validate-and-improve-instructions.prompt.md`](.github/prompts/meta/validate-and-improve-instructions.prompt.md)
  - Status: Critical fixes applied (Option C executed - 4 issues resolved, 3 deferred for refactoring)
  - Provenance: [Chat log](ai-logs/2025/10/15/validate-improve-instructions-20251015-212137/conversation.md) | [Summary](ai-logs/2025/10/15/validate-improve-instructions-20251015-212137/summary.md)
  - Verification: [Fixes verified 2025-10-16](validation-fixes-verified-20251016.md) ([chat log](ai-logs/2025/10/16/resume-validation-fixes-20251016/conversation.md))
