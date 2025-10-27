---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create", "edit"]
description: Generate implementation prompts for systematic system development
prompt_metadata:
  id: generate-implementation-prompts
  title: Generate Implementation Prompts
  owner: johnmillerATcodemag-com
  category: meta-documentation
  tags: [meta-prompts, implementation, system-development]
  output_format: markdown
---

# Generate Implementation Prompts

Create comprehensive prompt files to systematically implement system components with quality and continuity.

## Prompt File Structure
1. **Context & Overview**: Component description
2. **Prerequisites**: Dependencies, prior implementations
3. **Implementation Tasks**: Detailed, actionable with acceptance criteria
4. **Verification Steps**: Specific tests for confirmation
5. **Integration Testing**: Cumulative tests ensuring prior functionality

## Content Guidelines
- **Granularity**: Manageable, focused prompts
- **Clarity**: Unambiguous, specific technical requirements
- **Completeness**: All details (APIs, schemas, UI, business logic)
- **Testability**: Measurable success criteria per task

## Task Format
Per task include:
- Description (what to implement)
- Technical requirements (technologies, patterns, constraints)
- Acceptance criteria (measurable outcomes)
- Code quality standards (testing, docs, style)

## Verification Framework
**Component-Level**:
- Unit tests, integration tests
- Performance benchmarks (if applicable)
- Security validation (sensitive ops)

**Cumulative System**:
- Regression testing (verify previous features)
- End-to-end scenarios (complete workflows)
- Data integrity (DB consistency)
- API compatibility (existing contracts valid)

## Components to Address
- **Core**: DB schema/migrations, auth/authz, API gateway, logging/monitoring
- **Academic**: Student enrollment/profiles, course catalog/scheduling, grades/transcripts, faculty
- **Admin**: User management/permissions, reporting/analytics, system config, data import/export
- **UI**: Student portal, faculty dashboard, admin interface, mobile apps

## Implementation Order
1. Foundation (DB, auth, core APIs)
2. Core features (student/faculty, courses)
3. Advanced (scheduling, grading, reporting)
4. UIs (web, mobile)
5. Integration & deployment

## Quality Assurance
Ensure:
- Backwards compatibility
- Data migration handling
- Performance maintenance/improvement
- Security best practices
- Scalability for future growth

## Verification Checklist Template
```
□ Unit tests pass (>95% coverage)
□ Integration tests pass
□ API docs updated
□ DB migrations successful
□ Previous functionality verified
□ Performance benchmarks met
□ Security scan passed
□ Code review completed
□ Documentation updated
```

## Success Criteria
- Fully functional system implemented incrementally
- Each component tested and documented
- Seamless integration
- Maintainable, scalable, secure codebase
- Comprehensive test coverage and docs
