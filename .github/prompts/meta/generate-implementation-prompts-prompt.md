# Generate Implementation Prompts for Academia System

## Objective
Create comprehensive prompt files to systematically implement the Academia System. Each prompt file should guide developers through specific implementation tasks while ensuring quality and continuity across the entire system.

## Prompt File Requirements

### Structure
Each implementation prompt file should follow this structure:
1. **Context & Overview** - Brief description of the component being implemented
2. **Prerequisites** - Dependencies and prior implementations required
3. **Implementation Tasks** - Detailed, actionable tasks with acceptance criteria
4. **Verification Steps** - Specific tests to confirm successful implementation
5. **Integration Testing** - Cumulative tests to ensure prior implementations remain functional

### Content Guidelines
- **Granularity**: Break down complex features into manageable, focused prompts
- **Clarity**: Use clear, unambiguous language with specific technical requirements
- **Completeness**: Include all necessary details (APIs, schemas, UI components, business logic)
- **Testability**: Every task must have measurable success criteria

### Implementation Task Format
For each task, include:
- **Task Description**: What needs to be implemented
- **Technical Requirements**: Specific technologies, patterns, or constraints
- **Acceptance Criteria**: Measurable outcomes that define completion
- **Code Quality Standards**: Testing, documentation, and style requirements

### Verification Framework
Each prompt must include:

#### Component-Level Verification
- Unit tests for new functionality
- Integration tests for component interactions
- Performance benchmarks where applicable
- Security validation for sensitive operations

#### Cumulative System Verification
- **Regression Testing**: Verify all previously implemented features still work
- **End-to-End Scenarios**: Test complete user workflows spanning multiple components
- **Data Integrity**: Ensure database consistency across all implementations
- **API Compatibility**: Verify all existing API contracts remain valid

## Academia System Components to Address

### Core Infrastructure
- Database schema and migrations
- Authentication and authorization system
- API gateway and routing
- Logging and monitoring

### Academic Management
- Student enrollment and profiles
- Course catalog and scheduling
- Grade management and transcripts
- Faculty management

### Administrative Functions
- User management and permissions
- Reporting and analytics
- System configuration
- Data import/export

### User Interfaces
- Student portal
- Faculty dashboard
- Administrative interface
- Mobile applications

## Prompt File Organization
Create prompts in logical implementation order:
1. **Foundation**: Database, authentication, core APIs
2. **Core Features**: Student/faculty management, courses
3. **Advanced Features**: Scheduling, grading, reporting
4. **User Interfaces**: Web and mobile applications
5. **Integration & Deployment**: System integration, deployment automation

## Quality Assurance
Each prompt should ensure:
- **Backwards Compatibility**: New implementations don't break existing features
- **Data Migration**: Handle schema changes and data preservation
- **Performance**: Maintain or improve system performance
- **Security**: Follow security best practices and compliance requirements
- **Scalability**: Consider future growth and extensibility

## Example Verification Checklist Template
```
□ All unit tests pass (>95% coverage)
□ Integration tests pass
□ API documentation updated
□ Database migrations successful
□ Previous system functionality verified
□ Performance benchmarks met
□ Security scan passed
□ Code review completed
□ Documentation updated
```

## Success Criteria
The generated prompts should result in:
- A fully functional Academia System implemented incrementally
- Each component thoroughly tested and documented
- Seamless integration between all system parts
- Maintainable, scalable, and secure codebase
- Comprehensive test coverage and documentation