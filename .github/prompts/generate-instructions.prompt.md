---
description: "Analyzes codebase and generates comprehensive instruction files following GitHub Copilot format"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ['search', 'edit', 'fetch']
mode: agent
---

# Generate Project Instruction Files

You are an expert software architect and documentation specialist. Your task is to analyze the current codebase and generate comprehensive instruction files following the GitHub Copilot Instruction File Format.

**IMPORTANT**: Only create NEW instruction files that do not already exist. Never modify or overwrite existing files.

## Analysis Phase

First, analyze the codebase to identify:

1. **Project Structure and Technologies**

   - Primary programming languages used
   - Frameworks and libraries detected
   - Architecture patterns observed
   - Database technologies
   - Cloud platforms (Azure, AWS, GCP)
   - Frontend technologies (React, Vue, Angular, etc.)
   - Backend technologies (.NET, Node.js, Python, Java, etc.)

2. **Existing Patterns and Conventions**

   - Naming conventions currently used
   - Code organization patterns
   - Error handling approaches
   - Testing strategies
   - Documentation styles

3. **Technology Stack Assessment**
   - Version information for major dependencies
   - Integration patterns between technologies
   - Security implementations
   - Performance optimization patterns

## Instruction File Generation

Generate instruction files in the `.github/instructions` directory with the following structure:

### General Instructions (Root Level)

#### 1. README.md

```markdown
---
applyTo: "**"
---

# Development Instructions

Comprehensive coding guidelines, templates, and best practices for this project.

## AI Assistant Integration

[Include AI-specific guidance]

## Project Overview

[Technology stack and architecture summary]

## Quick Reference

[Language and framework specific quick guides]
```

#### 2. project-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "project structure"
  - "architecture overview"
  - "technology stack"
---

# Project Structure and Architecture Instructions

## AI Assistant Guidelines

- Follow established project structure when creating new files
- Use specified technology stack consistently (versions defined below)
- Maintain separation of concerns based on architecture
- Reference technology-specific instruction files for detailed naming conventions and patterns
- Consider cross-technology integration patterns when making suggestions

## Project Overview

[Detected project details and architecture summary]

## Technology Stack (Authoritative Reference)

**IMPORTANT**: This section serves as the single source of truth for all technology versions used in this project. All other instruction files reference these versions.

### Frontend Technologies

[List frontend technologies with specific versions]

### Backend Technologies

[List backend technologies with specific versions]

### Build and Testing

[List build tools and testing frameworks with versions]

### Cloud and DevOps

[List cloud services and DevOps tools with versions]

## File Structure

[Analyze and document the project structure with clear organization principles]

## Architecture Patterns

### Cross-Technology Integration

[Document integration patterns between different technologies]

### API Communication

[Define standards for communication between frontend and backend]

### Configuration Management

[Define how configuration is managed across different environments and technologies]

## Integration Considerations

### Data Flow

[Document how data flows between different technology layers]

### Authentication and Authorization

[Define unified auth patterns across all technologies]

### Error Handling Integration

[High-level error handling strategy - see error-handling-instructions.md for details]

## Quick Reference

For detailed implementation guidance, see:

- **Style Guidelines**: style-instructions.md
- **Error Handling**: error-handling-instructions.md
- **Testing Strategy**: testing-instructions.md
- **Best Practices**: practices-instructions.md
- **Technology-Specific**: Refer to subdirectories (vue/, csharp/, azure/, etc.)

Note: For technology-specific naming conventions, coding patterns, and detailed implementation guidelines, refer to the appropriate technology-specific instruction files in their respective subdirectories.
```

#### 3. practices-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "best practices"
  - "performance guidelines"
  - "security practices"
  - "code quality"
---

# Development Best Practices

## AI Assistant Guidelines

- Always suggest async/await patterns for I/O operations across all technology layers
- Include comprehensive error handling and logging in all code suggestions (see error-handling-instructions.md)
- Recommend appropriate security practices for web applications
- Reference specific testing coverage standards (defined in testing-instructions.md)
- Focus on cross-technology best practices and architectural patterns
- Consider performance implications for both client-side and server-side code

## Cross-Technology Best Practices

### Performance Guidelines

[Include performance patterns that apply across the technology stack]

### Security Best Practices

[Include security practices for client-side, server-side, and infrastructure]

### Code Quality Standards

[Include consistency patterns across all technologies]

### Development Workflow Best Practices

[Include version control, CI/CD, and monitoring practices]

## Technology Integration Patterns

### API Design Standards

[Define consistent API patterns between frontend and backend]

### Configuration Management

[Define configuration practices across environments - references project-instructions.md technology stack]

### Dependency Management

[Define how to manage dependencies across different technologies]

## See Also

- **Technology Stack**: project-instructions.md (authoritative version information)
- **Error Handling**: error-handling-instructions.md (detailed error handling implementation)
- **Testing Standards**: testing-instructions.md (specific coverage targets and strategies)
- **Code Organization**: style-instructions.md (project-level file organization)
- **Technology-Specific**: Refer to subdirectories for detailed coding standards

Note: This file focuses on high-level, cross-technology best practices. For detailed coding standards, naming conventions, and framework-specific patterns, refer to the appropriate technology-specific instruction files.
```

#### 4. error-handling-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "error handling strategy"
  - "logging architecture"
  - "error reporting"
---

# Error Handling Strategy and Logging

## AI Assistant Guidelines

- Implement consistent error handling patterns across all technology layers
- Include correlation ID generation for cross-service operations and API calls
- Suggest appropriate HTTP status codes for API responses
- Recommend structured logging with meaningful context for distributed systems
- Focus on error handling integration between different technology layers
- Consider user experience when handling errors in frontend components

## Cross-Technology Error Handling Architecture

### Error Classification

[Define error types across all technology layers]

### API Error Response Standards

[Define consistent error response formats - must align with backend API patterns]

### HTTP Status Code Guidelines

[Define standard status codes used across the application]

### Logging Architecture

#### Structured Logging Standards

[Define logging format used across all technologies]

#### Log Levels and Usage

[Define when to use each log level across all technologies]

#### Correlation and Tracing

[Define how to implement distributed tracing across technology boundaries]

### Error Recovery Strategies

[Define automatic and user-initiated recovery patterns]

### Monitoring and Alerting

[Define monitoring strategies that work across all technologies]

## Integration with Other Instructions

This error handling strategy integrates with:

- **Technology Stack**: Uses logging frameworks defined in project-instructions.md
- **Testing Strategy**: Error scenarios covered in testing-instructions.md
- **Security Practices**: Error handling security considerations in practices-instructions.md
- **Technology-Specific**: Detailed exception handling in technology-specific instruction files

## See Also

- **Project Architecture**: project-instructions.md (technology stack and integration patterns)
- **Best Practices**: practices-instructions.md (defensive programming and graceful degradation)
- **Testing Strategy**: testing-instructions.md (error condition testing)
- **Technology-Specific Error Handling**:
  - Frontend: vue/ or react/ subdirectories
  - Backend: csharp/, nodejs/, or python/ subdirectories
  - Infrastructure: azure/, aws/, or gcp/ subdirectories

Note: This file defines the overall error handling architecture. For language-specific exception handling patterns, framework-specific error boundaries, and detailed implementation examples, refer to the appropriate technology-specific instruction files.
```

#### 5. style-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "code style"
  - "project naming"
  - "file organization"
---

# Project-Level Style and Organization

## AI Assistant Guidelines

- Follow project-level file and directory naming conventions
- Maintain consistency with existing project structure
- Use meaningful, descriptive names for files and directories
- Apply appropriate organization patterns based on project architecture
- **Technology-specific conventions override general conventions** - refer to technology-specific files for detailed guidance

## Naming Convention Precedence Rules

**IMPORTANT**: When naming conventions conflict, follow this hierarchy:

1. **Technology-Specific Instructions** (highest priority)

   - Framework-specific patterns (e.g., Vue.js component naming)
   - Language conventions (e.g., C# PascalCase for classes)
   - Platform requirements (e.g., Azure resource naming)

2. **Project-Level Conventions** (medium priority)

   - Cross-technology consistency patterns
   - Project-specific organizational patterns

3. **General Guidelines** (lowest priority)
   - Industry standards and common practices

## Project-Level File Organization

### Directory Structure Standards

[Define high-level directory organization that works across all technologies]

### Cross-Technology File Naming

[Define naming patterns that need to be consistent across different technologies]

### Configuration and Documentation Files

[Define naming for configuration files, documentation, and infrastructure files]

## File Organization Patterns

### Feature-Based vs. Technology-Based Organization

[Define when to organize by feature vs. by technology]

### Shared Resources and Assets

[Define organization for shared files, images, configurations]

### Build and Deployment Artifacts

[Define organization for build outputs and deployment files]

## Integration with Technology-Specific Guidelines

This file provides project-level organization. For detailed naming conventions:

- **Frontend Components**: vue/, react/, or angular/ subdirectories
- **Backend Code**: csharp/, nodejs/, python/, or java/ subdirectories
- **Database**: sql/, mongodb/, or redis/ subdirectories
- **Infrastructure**: azure/, aws/, or gcp/ subdirectories
- **Configuration**: Refer to technology-specific files for config file naming

## Conflict Resolution

When technology conventions conflict:

1. Consult technology-specific instruction files first
2. Maintain consistency within each technology domain
3. Use project-level conventions only for cross-technology files
4. Document exceptions and rationale in relevant instruction files

## See Also

- **Project Structure**: project-instructions.md (overall architecture and organization principles)
- **Technology Stack**: project-instructions.md (authoritative technology list)
- **Technology-Specific Style**: Refer to subdirectories for detailed coding standards and naming conventions

Note: This file focuses on project-level file and directory organization. For detailed naming conventions, coding standards, and formatting rules specific to each technology, refer to the appropriate technology-specific instruction files.
```

#### 6. testing-instructions.md

```markdown
---
applyTo: "**"
triggers:
  - "testing strategy"
  - "test architecture"
  - "integration testing"
---

# Testing Strategy and Architecture

## AI Assistant Guidelines

- Follow established testing pyramid principles across all technology layers
- Implement proper test isolation and setup/teardown patterns for all testing frameworks
- Focus on integration testing between different technology layers
- Include both positive and negative test scenarios at the system level
- Consider end-to-end testing scenarios that span the entire application stack
- **Use consistent coverage standards**: 80%+ for critical business logic (authoritative standard)

## Cross-Technology Testing Architecture

### Testing Pyramid Implementation

#### Coverage Standards (Authoritative)

- **Unit Tests**: 80%+ coverage for critical business logic
- **Integration Tests**: Focus on critical integration points and workflows
- **End-to-End Tests**: Complete user journeys across the application
- **Performance Tests**: Load and stress testing of complete system

### Technology-Specific Testing Integration

#### Testing Framework Coordination

[Define how different testing frameworks work together]

#### Test Data Management Strategy

[Define unified test data approach across all technologies]

#### Test Environment Management

[Define consistent test environments across technology stack - references project-instructions.md]

#### CI/CD Pipeline Testing

[Define automated testing in deployment pipeline]

### Integration Testing Patterns

#### Cross-Technology Integration

[Define how to test integration between frontend, backend, and infrastructure]

#### API Integration Testing

[Define standards for testing APIs between different technology layers]

#### Database Integration Testing

[Define patterns for testing data layer integration]

#### External Service Integration Testing

[Define patterns for testing third-party service integration]

## Testing Strategy Integration

This testing strategy coordinates with:

- **Technology Stack**: Uses testing frameworks defined in project-instructions.md
- **Error Handling**: Tests error scenarios defined in error-handling-instructions.md
- **Best Practices**: Implements quality standards from practices-instructions.md
- **Technology-Specific**: Detailed testing patterns in technology-specific instruction files

## Quality Gates and Standards

### Definition of Done

[Define what constitutes complete testing for features]

### Test Review Standards

[Define code review standards for test code]

### Continuous Quality Monitoring

[Define ongoing quality monitoring across all technologies]

## See Also

- **Project Architecture**: project-instructions.md (technology stack and testing framework versions)
- **Best Practices**: practices-instructions.md (quality standards and development workflow)
- **Error Handling**: error-handling-instructions.md (error scenario testing)
- **Technology-Specific Testing**:
  - Frontend: vue/, react/, or angular/ subdirectories
  - Backend: csharp/, nodejs/, python/, or java/ subdirectories
  - Infrastructure: azure/, aws/, or gcp/ subdirectories

Note: This file defines the overall testing strategy and cross-technology integration patterns. For specific testing frameworks, unit testing patterns, mocking strategies, and detailed testing implementation guidelines, refer to the appropriate technology-specific instruction files.
```

### Technology-Specific Instructions

For each detected technology, create a subdirectory with specific instructions:

#### For .NET/C# Projects

If .NET/C# files are detected, create appropriate folders under the `.github/instructions/generated` directory:

Create `csharp/` folder with essential files:

- `csharp-style-instructions.md` (applyTo: '\*_/_.cs') - Naming conventions, coding standards, and formatting
- `csharp-testing-instructions.md` (applyTo: '\*_/_.cs') - Testing frameworks, patterns, and best practices

Optional files (create only if significant C# complexity detected):

- `csharp-api-instructions.md` (applyTo: '\*_/_.cs') - For projects with substantial API development
- `csharp-patterns-instructions.md` (applyTo: '\*_/_.cs') - For projects using advanced C# patterns

#### For Vue.js Projects

If Vue.js files are detected, create appropriate folders:

Create `vue/` folder with essential files:

- `vue-component-instructions.md` (applyTo: '\*_/_.vue') - Component patterns, naming conventions, and Vue-specific coding standards
- `vue-testing-instructions.md` (applyTo: '\*_/_.vue') - Vue testing frameworks, component testing, and best practices

Optional files (create only if significant Vue complexity detected):

- `vue-state-management-instructions.md` (applyTo: '\*_/_.vue') - For projects with complex Vuex/Pinia implementations

#### For React Projects

If React files are detected, create appropriate folders:

Create `react/` folder with:

- `react-component-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')
- `react-hooks-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')
- `react-testing-instructions.md` (applyTo: '**/\*.tsx', '**/\*.jsx')

#### For Node.js Projects

If Node.js files are detected, create appropriate folders:

Create `nodejs/` folder with:

- `nodejs-api-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')
- `nodejs-testing-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')
- `nodejs-security-instructions.md` (applyTo: '**/\*.js', '**/\*.ts')

#### For Python Projects

If Python files are detected, create appropriate folders:

Create `python/` folder with:

- `python-style-instructions.md` (applyTo: '\*_/_.py')
- `python-testing-instructions.md` (applyTo: '\*_/_.py')
- `python-api-instructions.md` (applyTo: '\*_/_.py')

#### For Database Technologies

If database files are detected, create appropriate folders:

- `sql/` for SQL Server, PostgreSQL, MySQL
- `mongodb/` for MongoDB
- `redis/` for Redis

#### For Cloud Platforms

If cloud services are detected, create appropriate folders:

- `azure/` for Azure-specific instructions
- `aws/` for AWS-specific instructions
- `gcp/` for Google Cloud-specific instructions

## Template Structure for Each Instruction File

### General Instruction File Template

```markdown
---
applyTo: "[broad file patterns or **]"
triggers:
  - "high-level trigger phrases"
  - "cross-technology keywords"
  - "architectural concepts"
---

# [Category] Instructions

## AI Assistant Guidelines

- High-level guidance that applies across multiple technologies
- Cross-technology integration considerations
- References to technology-specific files for detailed implementation
- Avoid duplicating technology-specific details (delegate to specific instruction files)

## [Category] Strategy

### Cross-Technology [Category] Patterns

[High-level patterns that work across the entire technology stack]

### Integration Points

[How this category integrates across different technologies]

### Authoritative Standards

[Single source of truth for standards referenced by multiple files - e.g., coverage targets, version numbers]

## Integration with Other Instructions

This [category] strategy integrates with:

- **Technology Stack**: [reference to project-instructions.md for versions]
- **Related Categories**: [references to other general instruction files]
- **Technology-Specific**: [references to relevant technology subdirectories]

## See Also

- **High-Level**: [references to related general instruction files]
- **Implementation Details**: [references to technology-specific instruction files]
- **Authoritative References**: [references to single source of truth files]

Note: This file focuses on [high-level category description]. For detailed [technology-specific aspects], refer to the appropriate technology-specific instruction files.
```

### Technology-Specific Instruction File Template

````markdown
---
applyTo: "[specific file patterns for this technology]"
triggers:
  - "technology-specific trigger phrases"
  - "framework keywords"
  - "implementation scenarios"
---

# [Technology] [Category] Instructions

## AI Assistant Guidelines

- Technology-specific guidance for AI assistants
- Context-aware recommendations based on the specific technology and framework
- Quality assurance rules specific to this technology
- Integration considerations with other project technologies (reference project-instructions.md for tech stack)

## [Technology] Standards

### Version Information

**Technology Version**: [Reference project-instructions.md for authoritative version - DO NOT duplicate]

### [Specific Category] Guidelines

- Detailed guidelines specific to this technology
- Code examples using the actual technology stack
- Best practices aligned with the technology's conventions
- Common patterns and anti-patterns specific to this framework

### Implementation Patterns

#### [Specific Pattern Category]

```[technology]
[Include relevant code templates with proper syntax highlighting]
```
````

#### [Another Pattern Category]

[Include practical examples based on detected patterns in the codebase]

## Integration with Project Standards

This technology implementation aligns with:

- **Project Architecture**: [reference to project-instructions.md]
- **Cross-Technology Patterns**: [reference to relevant general instruction files]
- **Related Technologies**: [reference to other technology-specific files when integration is relevant]

## Technology-Specific Considerations

### Framework-Specific Patterns

[Detailed patterns unique to this technology]

### Dependencies and Configuration

[Technology-specific configuration - reference project-instructions.md for version consistency]

### Performance and Security

[Technology-specific performance and security considerations]

## See Also

- **Project Overview**: project-instructions.md (technology stack and architecture)
- **Cross-Technology Standards**: [references to relevant general instruction files]
- **Related Technologies**: [references to other technology-specific files for integration patterns]

Note: This file provides detailed implementation guidance for [technology]. For high-level architectural patterns and cross-technology integration, refer to the general instruction files.

```

### Quality Assurance Checklist for Each File

Before creating any instruction file, verify:

1. **No Content Duplication**: Content is unique and doesn't duplicate other files
2. **Clear References**: Appropriate cross-references to related files
3. **Version Consistency**: Technology versions reference project-instructions.md
4. **Scope Boundaries**: Content stays within the file's defined scope
5. **Integration Points**: Clear guidance on how this technology integrates with others

## Special Considerations

### For Multi-Technology Projects

#### Integration Focus Areas
- Create cross-technology integration instructions in the general project instructions
- Include API communication patterns between technologies in the general project instructions
- Document data flow between different technology layers in the general project instructions
- Define unified authentication and error handling strategies across all technologies

#### Content Separation Rules
- Keep technology-specific naming conventions, coding patterns, and framework details in their respective technology-specific instruction files
- **Never duplicate** naming conventions or coding standards between general and technology-specific files
- **Never duplicate** technology version information - maintain single source of truth in project-instructions.md
- **Never duplicate** testing framework details - reference technology-specific files from general testing strategy

#### Common Duplication Pitfalls to Avoid
1. **Technology Stack Definitions**: Only define in project-instructions.md, reference elsewhere
2. **Testing Coverage Standards**: Define once in testing-instructions.md, reference elsewhere
3. **Error Response Formats**: Define API standards in error-handling-instructions.md, not in technology-specific files
4. **File Organization**: Define high-level structure in style-instructions.md, specific naming in technology files
5. **Security Practices**: Define cross-technology patterns in practices-instructions.md, specific implementations in technology files

### For Microservices Architecture

- Create service-specific instruction folders
- Include inter-service communication guidelines
- Document deployment and orchestration patterns

### For Monolithic Architecture

- Create module-specific instructions
- Include layer separation guidelines
- Document internal API patterns

## Generation Rules

### Core Principles

1. **Analyze Before Generating**: Always analyze the codebase first to understand the actual technologies and patterns used
2. **Use Detected Patterns**: Base instruction content on actually observed patterns in the codebase
3. **Preserve Existing Files**: **NEVER modify or overwrite existing files** - only create new instruction files that don't already exist
4. **Practical Examples**: Use real examples from the codebase where possible

### Content Quality and Consistency

5. **Version Consistency**:
   - Create a centralized technology stack reference that all files can reference
   - Use specific version numbers consistently across all instruction files
   - Avoid generic version references when specific versions are available
   - Maintain a single source of truth for technology versions

6. **Avoid Duplication and Redundancy**:
   - Eliminate overlapping content between instruction files
   - Keep technology stack definitions in one authoritative location (project-instructions.md)
   - Reference other instruction files instead of duplicating content
   - Maintain clear content ownership boundaries between files

7. **Clear Hierarchical Structure**:
   - General instructions provide high-level architecture and integration guidance
   - Technology-specific instructions contain detailed implementation patterns
   - Establish precedence rules: technology-specific conventions override general ones
   - Create clear delegation patterns from general to specific files

8. **Cross-Referencing and Integration**:
   - Add explicit cross-references between related instruction files
   - Include "See also" sections linking to relevant files
   - Reference technology-specific files from general instructions
   - Create navigation aids for complex instruction hierarchies

### Content Organization

9. **Separation of Concerns**:
   - **General files**: Architecture, project structure, cross-technology integration, high-level best practices
   - **Technology-specific files**: Naming conventions, coding standards, framework patterns, detailed implementation guidance
   - **Avoid content bleed**: Don't duplicate technology-specific details in general files

10. **Naming Convention Clarity**:
    - Establish clear precedence rules for conflicting naming conventions
    - Document when technology-specific conventions override general ones
    - Provide conflict resolution guidance for edge cases
    - Maintain consistency within each technology domain

11. **Testing Strategy Coherence**:
    - Define clear boundaries between general testing philosophy and specific testing implementations
    - Avoid overlapping testing guidance between general and technology-specific files
    - Create unified testing coverage standards referenced by all files

### Quality Assurance

12. **Completeness**: Cover all major aspects of development for each detected technology
13. **Maintainability**: Structure instructions for easy updates and maintenance with minimal duplication
14. **Consistency**: Ensure all generated instructions follow the same format, style, and referencing patterns

## Output Format

After analysis, provide a comprehensive summary of:

### Analysis Results
1. **Detected Technologies and Versions**: Complete technology stack with specific version numbers
2. **Existing Instruction Analysis**: Assessment of current instruction files and identified quality issues
3. **Key Patterns and Conventions**: Observed coding patterns, naming conventions, and architectural decisions
4. **Quality Issues Identified**: Duplication, version inconsistencies, missing cross-references, and hierarchical problems

### Implementation Plan
5. **Proposed Instruction File Structure**: New files to be created (excluding existing files)
6. **Content Separation Strategy**: Clear boundaries between general and technology-specific content
7. **Cross-Reference Plan**: How new files will reference each other and existing files
8. **Version Consistency Strategy**: Plan for maintaining consistent technology versions

### Quality Assurance
9. **Conflict Resolution Approach**: How naming convention conflicts and precedence will be handled
10. **Redundancy Prevention**: Specific measures to avoid content duplication
11. **Maintenance Strategy**: How the instruction system will remain maintainable and consistent

Then proceed to generate only the NEW instruction files that don't already exist, using the established format, detected technologies, and quality improvement strategies.

## Safety Requirements

**CRITICAL**: Before creating any instruction file:

1. **Check if the file already exists** in the target location
2. **Skip creation** if a file with the same name already exists
3. **Only create new files** that don't conflict with existing ones
4. **Preserve all existing content** - never modify existing instruction files

## File Conflict Resolution and Quality Assurance

### Existing File Analysis

If instruction files already exist:

1. **Preservation First**: Never modify or overwrite existing files
2. **Pattern Recognition**: Analyze existing files to understand current patterns and conventions
3. **Consistency Alignment**: Use existing files as reference for format and style consistency
4. **Gap Analysis**: Only create supplementary files that fill genuine gaps
5. **Conflict Detection**: Document any detected inconsistencies but do not modify existing files

### Content Quality Assessment

Before creating new files, assess existing instruction quality for:

#### Duplication and Redundancy Issues
- **Technology Stack Definitions**: Check if versions are defined consistently across files
- **Testing Philosophy**: Identify overlapping testing guidance between general and specific files
- **Error Handling Patterns**: Look for redundant error handling information
- **File Organization**: Check for duplicated directory structure guidance
- **Build and Deployment**: Identify overlapping CI/CD and deployment guidance

#### Hierarchical Structure Issues
- **Precedence Rules**: Ensure clear precedence between general and technology-specific instructions
- **Content Boundaries**: Verify clear separation between general architecture and specific implementation
- **Cross-References**: Check for missing links between related instruction files
- **Navigation**: Assess ease of finding relevant guidance across multiple files

#### Version and Standard Consistency Issues
- **Technology Versions**: Identify inconsistent version references across files
- **Coverage Standards**: Check for conflicting test coverage targets
- **Naming Conventions**: Identify conflicts between general and technology-specific naming rules
- **Code Quality Metrics**: Verify consistent quality standards across all files

### Quality Improvement Strategy

When creating new files:

1. **Single Source of Truth**: Establish authoritative sources for commonly referenced information
2. **Clear Delegation**: General files should reference, not duplicate, technology-specific details
3. **Comprehensive Cross-Referencing**: Include "See Also" sections with relevant file references
4. **Conflict Resolution Rules**: Document precedence rules for conflicting conventions
5. **Version Centralization**: Maintain technology versions in a single authoritative location

### Content Separation Rules

#### General Instruction Files Should Contain:
- High-level architecture and integration patterns
- Cross-technology best practices and workflows
- Project structure and organization principles
- Integration patterns between different technologies
- Authoritative technology stack definitions and versions

#### Technology-Specific Files Should Contain:
- Detailed naming conventions and coding standards
- Framework-specific patterns and implementations
- Technology-specific testing frameworks and patterns
- Language-specific error handling and logging
- Platform-specific configuration and deployment details

#### Prohibited Content Duplication:
- **Never duplicate** technology versions between general and specific files
- **Never duplicate** naming conventions between general and technology-specific files
- **Never duplicate** detailed implementation patterns in general files
- **Never duplicate** testing framework specifics in general files

### Quality Validation Checklist

Before completing instruction file generation, validate:

#### Content Quality
- [ ] No duplicated technology stack definitions (only in project-instructions.md)
- [ ] No duplicated naming conventions between general and technology-specific files
- [ ] No duplicated testing framework details between general and specific files
- [ ] No duplicated error handling implementation details
- [ ] All version references point to project-instructions.md as authoritative source

#### Structural Quality
- [ ] Clear precedence rules documented for conflicting conventions
- [ ] Comprehensive cross-references between related files
- [ ] "See Also" sections in all files with relevant references
- [ ] Clear content boundaries between general and technology-specific guidance
- [ ] Integration points clearly documented for multi-technology interactions

#### Consistency Quality
- [ ] Consistent file naming and structure across all instruction files
- [ ] Consistent section organization and markdown formatting
- [ ] Consistent trigger phrase patterns and applyTo specifications
- [ ] Consistent AI Assistant Guidelines format and content type
- [ ] Consistent reference patterns between files

#### Completeness Quality
- [ ] All detected technologies have appropriate instruction files
- [ ] All major development aspects covered without gaps
- [ ] Integration patterns documented for each technology combination
- [ ] Quality standards clearly defined and consistently referenced
- [ ] Maintenance and update procedures considered

Remember: The goal is to create a coherent, non-redundant instruction system that provides clear guidance without duplication, ensures version consistency, maintains clear hierarchical relationships between general and technology-specific instructions, and eliminates the quality issues identified in the context analysis.
```
