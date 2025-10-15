---
mode: 'agent'
model: 'claude-sonnet-4'
tools: ['githubRepo', 'codebase']
description: 'Generate comprehensive instruction files for a CQRS-based System with clear architectural patterns and implementation guidelines.'
---
# System - Instruction Generation Prompt

## AI Generation Directives

### Your Task
You are to generate comprehensive instruction files that will guide developers in implementing a CQRS-based System that enforces and implements the business requirements defined in the `Models` folder. Each file must be complete, actionable, and production-ready.

**Entity Requirements:**
- All system entities must be derived from the conceptual model defined in the `Models` folder
- Only entities explicitly defined in the conceptual model should be included
- Entity relationships and behaviors must align with the conceptual model specifications
- Domain terminology should match the conceptual model glossary
- Use cases from the `Models` folder should guide functional requirements

### Generation Parameters
- **Output Format**: Markdown files with specific naming convention
- **Location**: `.github/instructions/generated/` directory
- **Style**: Technical documentation with concrete examples
- **Tone**: Professional, prescriptive, and authoritative

### Files to Generate

Create these exact files with the specified focus:

1. **project-overview.instructions.md**
   - Describe the System domain based on the conceptual model in the `Models` folder
   - Define core entities and relationships from the conceptual model
   - State key business invariants from the business requirements
   - Provide high-level architecture overview

2. **sdlc-process.instructions.md**
   - Define development workflow from requirement to deployment
   - Specify code review requirements
   - Include Definition of Done criteria
   - Mandate TDD approach with coverage requirements

3. **git-workflow.instructions.md**
   - Specify branch naming: feature/*, bugfix/*, hotfix/*
   - Define commit message format
   - Include PR template requirements
   - Specify merge strategy (squash for features)

4. **cqrs-implementation.instructions.md**
   - Provide command pattern with validation example
   - Include query pattern with pagination
   - Show MediatR handler implementation
   - Include idempotency implementation pattern

5. **architecture-design.instructions.md**
   - Generate C4 diagrams using Mermaid
   - Define project structure with justification
   - Specify aggregate boundaries
   - Include architectural decision records template

6. **azure-infrastructure.instructions.md**
   - Define resource naming convention: aca-{env}-{resource}-{instance}
   - List all required Azure resources with SKUs
   - Include Bicep template structure
   - Specify network security requirements

7. **configuration-management.instructions.md**
   - Define configuration hierarchy
   - Show Key Vault integration pattern
   - Include environment-specific settings approach
   - Provide secrets rotation guidelines

8. **testing-requirements.instructions.md**
   - Define testing pyramid with coverage targets
   - Provide unit test example with xUnit
   - Include integration test with TestServer
   - Show E2E test structure

9. **documentation-guidelines.instructions.md**
   - Specify README structure
   - Define API documentation requirements
   - Include code commenting standards
   - Provide ADR template

10. **monitoring-observability.instructions.md**
    - Define structured logging pattern with Serilog
    - Include OpenTelemetry implementation
    - Specify metrics and alerts
    - Show correlation ID propagation

11. **security-compliance.instructions.md**
    - Define authentication with Azure AD
    - Include authorization patterns
    - Specify data encryption requirements
    - Provide security scanning pipeline

12. **deployment-operations.instructions.md**
    - Define CI/CD pipeline stages
    - Include blue-green deployment pattern
    - Specify rollback procedures
    - Provide health check implementation
    - Include deployment progress tracking and reporting

13. **ai-code-governance.instructions.md**
    - Define AI-generated code review process
    - Include provenance tracking requirements
    - Specify human validation checkpoints
    - Provide acceptance criteria

14. **database-migrations.instructions.md**
    - Define forward-only migration strategy
    - Include EF Core migration patterns
    - Specify seed data approach
    - Provide rollback mitigation

15. **vertical-slice-implementation.instructions.md**
    - Provide feature identification and slice definition criteria
    - Include development order strategy (simple to complex)
    - Show complete vertical slice example from API to database
    - Include feature folder organization pattern
    - Show cross-cutting concern integration
    - Specify slice boundaries and dependencies
    - Show example application structure with multiple slices
    - Specify slice criteria: independently deployable, testable end-to-end, valuable to users, 1-2 week completion
    - Include integration with showcase practices for stakeholder demonstrations

16. **progress-showcase.instructions.md**
    - Define software implementation showcasing principles and benefits
    - Explain showcasing working features throughout development vs waiting for completion
    - Include demo environment setup and management
    - Specify feature showcase requirements and cadence
    - Provide stakeholder communication templates and presentation guidelines
    - Include showcase preparation checklists and scripts
    - Define audience-specific demonstration approaches
    - Show integration with development workflow and vertical slices
    - Include feedback collection and incorporation processes
    - Provide troubleshooting guidelines for live demonstrations
    - Include progress tracking and reporting methods aligned with showcases

17. **domain-glossary.instructions.md**
    - Define all domain terms from the conceptual model in the `Models` folder
    - Include CQRS terminology
    - Specify technical acronyms
    - Provide context examples using conceptual model entities

### Content Requirements for Each File

When generating each file, ensure you:

1. **Start with this structure**:
   ```markdown
   # [Clear Title]

   ## Purpose
   [One paragraph explaining why this document exists]

   ## Scope
   This document covers:
   - [Specific item 1]
   - [Specific item 2]

   This document does not cover:
   - [Out of scope item 1]
   - [Out of scope item 2]

   ## Prerequisites
   - [Required knowledge/tools]
   ```

2. **Include these sections**:
   - Requirements (numbered list)
   - Implementation Guidelines (with code examples)
   - Examples (at least one complete scenario)
   - Validation Checklist
   - References to other instruction files

3. **For code examples**:
   - Use only the System Entities defined in the conceptual model in the `Models` folder
   - Reference entities by their exact names from the conceptual model
   - Align implementations with use cases defined in the `Models` folder
   - Show complete vertical slice implementations when applicable
   - Include feature-based organization examples
   - Show the complete implementation
   - Include error handling
   - Add unit test example
   - Ensure examples are domain-agnostic and reusable

4. **Technical specifications to embed**:
   - .NET 8.0 LTS with C# 12
   - Azure SQL Database
   - ASP.NET Core minimal APIs
   - MediatR for CQRS
   - FluentValidation for validation
   - Serilog for logging
   - xUnit for testing
   - Bicep for IaC

5. **Quality standards to enforce**:
   - `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`
   - `<AnalysisMode>All</AnalysisMode>`
   - Nullable reference types enabled
   - 85% unit test coverage minimum
   - All public APIs must have integration tests

6. **Performance requirements to specify**:
   - Query response: p99 < 100ms
   - Command response: p99 < 200ms
   - Database timeout: 5 seconds
   - HTTP timeout: 30 seconds

### Validation Requirements

Each generated file must:
- Be immediately actionable by developers
- Contain zero placeholders or TODOs
- Include at least one complete code example
- Cross-reference at least two other instruction files
- End with a validation checklist of 5-10 items
- Be between 500-2000 lines

### Output Instructions

1. Generate all files in sequence
2. Maintain consistent terminology throughout
3. Ensure each file stands alone but references others
4. Include file path comment at the start of each file
5. Do not include any commentary between files
6. Do not ask for clarification - make reasonable decisions
7. Complete all files even if response length is long

Begin generation now.
