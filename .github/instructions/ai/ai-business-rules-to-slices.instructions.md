---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "business-rules-vertical-slices-20251022"
prompt: |
  Create instruction files (one for humans, one for AI) that provide guidance for
  analyzing business rules and use cases then generating features that can be
  implemented in vertical slices.
started: "2025-10-22T16:00:00Z"
ended: "2025-10-22T17:00:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:15:00"
  - task: "AI instruction file creation"
    duration: "00:30:00"
  - task: "review and refinement"
    duration: "00:15:00"
total_duration: "01:00:00"
ai_log: "ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{md,txt}"
---

# AI Assistant Instructions: Business Rules to Vertical Slices

## Overview

This document provides instructions for AI assistants when analyzing business requirements, extracting business rules, identifying use cases, and designing features as vertical slices. Follow these instructions when users ask you to analyze requirements or design features.

**Target Audience**: AI assistants (GitHub Copilot, ChatGPT, Claude, etc.)
**Related Documentation**:

- [Business Rules to Vertical Slices (Human Guide)](.github/instructions/business-rules-to-vertical-slices.instructions.md)
- [AI Vertical Slice Implementation](.github/instructions/ai-vertical-slice-implementation.instructions.md)

## Table of Contents

- [When to Apply These Instructions](#when-to-apply-these-instructions)
- [Analysis Workflow](#analysis-workflow)
- [Business Rule Extraction](#business-rule-extraction)
- [Use Case Identification](#use-case-identification)
- [Feature Boundary Definition](#feature-boundary-definition)
- [Vertical Slice Design](#vertical-slice-design)
- [Output Templates](#output-templates)
- [Validation Rules](#validation-rules)
- [Common Patterns](#common-patterns)
- [Quality Checklist](#quality-checklist)

## When to Apply These Instructions

Apply these instructions when user requests:

1. **Explicit Analysis**: "Analyze these requirements", "extract business rules", "identify use cases"
2. **Feature Design**: "Design features for...", "break down into vertical slices"
3. **Requirements Review**: "Review these requirements", "what features do I need?"
4. **Architecture Planning**: "How should I structure this feature?", "what are the slices?"

**Triggers**:

- User provides business requirements document
- User describes a business process or workflow
- User asks to design a system or feature
- User mentions "business rules", "use cases", "user stories"

**Do NOT apply** when:

- User only asks for code implementation
- User provides complete technical specifications
- User asks about existing code without new requirements

## Analysis Workflow

### Step-by-Step Process

When user provides requirements, follow this sequence:

**Step 1: Acknowledge and Clarify**

```markdown
I'll analyze these requirements to extract business rules, identify use cases,
and design vertical slices. Let me break this down:

**What I'll do**:

1. Extract business rules from your requirements
2. Identify key use cases
3. Define feature boundaries
4. Design vertical slices for implementation
5. Prioritize slices

**Questions before I begin**:

- [Ask any clarifying questions]
- [Identify ambiguities]
- [Confirm assumptions]
```

**Step 2: Extract Business Rules**

Scan requirements for:

- Modal verbs: must, should, cannot, shall, may
- Constraints: only, never, always, at least, at most
- Calculations: calculated as, based on, derived from
- Conditions: if...then, when...then
- Triggers: automatically, when [event]

**Step 3: Identify Use Cases**

Look for:

- Actor actions: "user can...", "admin should..."
- User goals: "so that", "in order to"
- Workflows: sequence of steps
- Outcomes: what happens after action

**Step 4: Define Features**

Group related use cases into features:

- Single responsibility
- Clear boundaries
- Minimal dependencies
- Deliverable value

**Step 5: Design Slices**

Break features into vertical slices:

- Each slice = complete end-to-end functionality
- Each slice spans all layers
- Each slice delivers value
- Each slice is testable

**Step 6: Present Analysis**

Present structured output (see templates below)

## Business Rule Extraction

### Extraction Rules

**Rule 1: Identify All Rule Types**

Categorize rules as you find them:

1. **Structural Rules** (Facts/Definitions)

   - Pattern: "A [entity] has/is/contains [attribute/relationship]"
   - Example: "A customer must have an email address"

2. **Operative Rules** (Constraints)

   - Pattern: "A [entity] must/cannot/should [action/condition]"
   - Example: "Users cannot register with duplicate emails"

3. **Derivation Rules** (Calculations)

   - Pattern: "[Value] is calculated as/equals [formula]"
   - Example: "Total = subtotal + tax - discounts"

4. **Action Enablers** (Triggers)
   - Pattern: "When [event], [action] happens"
   - Example: "When user registers, send welcome email"

**Rule 2: Number Each Rule**

Assign sequential IDs: BR-001, BR-002, etc.

**Rule 3: Use Standard Format**

```markdown
**BR-[ID]**: [Rule Statement]

- **Type**: [Structural|Operative|Derivation|Action Enabler]
- **Priority**: [Critical|High|Medium|Low]
- **Rationale**: [Why this rule exists]
- **Scope**: [What feature/component this applies to]
```

**Rule 4: Flag Ambiguities**

When rules are unclear, note:

```markdown
**BR-050**: ⚠️ NEEDS CLARIFICATION

- **Statement**: "Passwords must be strong"
- **Ambiguity**: What defines "strong"? Length? Complexity? Specific requirements?
- **Suggested**: "Passwords must be 8-20 characters with uppercase, lowercase, and digit"
```

### Extraction Algorithm

```
FOR each sentence/paragraph in requirements:
  IF contains modal verb (must, should, cannot):
    EXTRACT as operative rule
  ELSE IF contains calculation pattern:
    EXTRACT as derivation rule
  ELSE IF contains trigger pattern (when, automatically):
    EXTRACT as action enabler
  ELSE IF defines relationship/constraint:
    EXTRACT as structural rule

  IF rule is ambiguous:
    FLAG for clarification
    SUGGEST specific alternative
```

### Examples

**Input Requirement**:

```
"Users must register with a valid email address. Emails must be unique across
all users. The system should send a welcome email when registration is complete.
Users cannot access premium features until they verify their email."
```

**Extracted Rules**:

```markdown
**BR-001**: Users must register with a valid email address

- **Type**: Structural Rule
- **Priority**: Critical
- **Rationale**: Email is primary communication channel
- **Scope**: User Registration

**BR-002**: Email addresses must be unique across all users

- **Type**: Operative Rule
- **Priority**: Critical
- **Rationale**: Prevents duplicate accounts, ensures unique identity
- **Scope**: User Registration

**BR-003**: System automatically sends welcome email when registration completes

- **Type**: Action Enabler
- **Priority**: High
- **Rationale**: User engagement, confirm registration
- **Scope**: User Registration

**BR-004**: Users cannot access premium features until email is verified

- **Type**: Operative Rule
- **Priority**: High
- **Rationale**: Confirm user identity before granting access
- **Scope**: Email Verification, Feature Access
```

## Use Case Identification

### Identification Rules

**Rule 1: Look for Actor-Action Pairs**

Pattern: "[Actor] [verbs] [object]"

- "User registers an account" → Use Case: Register User Account
- "Admin approves refund" → Use Case: Approve Refund Request

**Rule 2: Extract from User Stories**

Pattern: "As a [actor], I want to [action] so that [benefit]"

- Extract actor, action, goal
- Convert to use case

**Rule 3: Identify Workflows**

Look for sequences:

- "First user does X, then Y, finally Z"
- Convert to primary and alternative flows

**Rule 4: Use Standard Format**

```markdown
**UC-[ID]**: [Use Case Name]

- **Actor**: [Primary actor]
- **Goal**: [What actor wants to achieve]
- **Preconditions**: [What must be true before]
- **Postconditions**: [What is true after successful completion]
- **Main Flow**: [Step-by-step happy path]
- **Alternative Flows**: [Error cases, exceptions]
- **Business Rules**: [Related BR IDs]
```

### Identification Algorithm

```
FOR each requirement statement:
  EXTRACT actor (who?)
  EXTRACT action (what?)
  EXTRACT goal (why?)

  CREATE use case:
    Name = Action + Object
    Actor = extracted actor
    Goal = extracted goal

  ANALYZE flow:
    EXTRACT main steps
    EXTRACT alternative paths
    LINK related business rules
```

### Examples

**Input Requirement**:

```
"Users should be able to reset their forgotten passwords. They enter their email,
receive a reset link, and can set a new password. The reset link expires after 1 hour."
```

**Extracted Use Cases**:

```markdown
**UC-010**: Request Password Reset

- **Actor**: User (forgot password)
- **Goal**: Initiate password reset process
- **Preconditions**: User has registered account
- **Postconditions**: Reset email sent with valid token
- **Main Flow**:
  1. User navigates to "Forgot Password" page
  2. User enters email address
  3. System validates email exists
  4. System generates reset token (1 hour expiry)
  5. System sends reset email with link
  6. System confirms email sent
- **Alternative Flows**:
  - 3a. Email not found → Display generic message (security)
  - 5a. Email service fails → Log error, notify user to try again
- **Business Rules**: BR-020, BR-021

**UC-011**: Reset Password

- **Actor**: User (with reset token)
- **Goal**: Set new password
- **Preconditions**: Valid reset token received via email
- **Postconditions**: Password updated, token invalidated
- **Main Flow**:
  1. User clicks reset link in email
  2. System validates token (not expired, not used)
  3. System displays password reset form
  4. User enters new password (twice for confirmation)
  5. System validates password strength
  6. System validates passwords match
  7. System updates password (hashed)
  8. System invalidates reset token
  9. System displays success message
- **Alternative Flows**:
  - 2a. Token expired → Display error, offer to resend
  - 2b. Token already used → Display error
  - 5a. Weak password → Display specific requirements
  - 6a. Passwords don't match → Display error
- **Business Rules**: BR-022, BR-023, BR-024
```

## Feature Boundary Definition

### Definition Rules

**Rule 1: Apply Cohesion Test**

Ask: "Do all parts of this feature naturally belong together?"

- ✅ Pass: "User Registration" (register, verify email, welcome)
- ❌ Fail: "User Management" (too broad - registration, profile, permissions, etc.)

**Rule 2: Apply Independence Test**

Ask: "Can this feature be implemented without modifying other features?"

- ✅ Pass: "Password Reset" (standalone workflow)
- ❌ Fail: "Update User Email" (if tightly coupled to multiple features)

**Rule 3: Apply Value Test**

Ask: "Does this feature deliver complete value to users?"

- ✅ Pass: "Checkout Process" (user can complete purchase)
- ❌ Fail: "Validate Credit Card" (partial feature, no user value alone)

**Rule 4: Apply Size Test**

Ask: "Can this be implemented in 1-5 days?"

- ✅ Pass: "Basic Search" (single feature)
- ❌ Fail: "Complete E-Commerce Platform" (way too large)

### Boundary Algorithm

```
FOR each group of related use cases:
  IF cohesion is HIGH AND independence is HIGH:
    CREATE feature
  ELSE IF too large:
    SPLIT into smaller features
  ELSE IF too small:
    MERGE with related feature

  VALIDATE:
    Check delivers complete value
    Check appropriate size
    Check minimal dependencies
```

### Feature Template

```markdown
**Feature**: [Feature Name]

- **ID**: F-[number]
- **Business Capability**: [High-level capability]
- **Description**: [What this feature does]
- **User Value**: [Value delivered to users]
- **Use Cases**: [UC IDs]
- **Business Rules**: [BR IDs]
- **Dependencies**: [Other features or shared services]
- **Priority**: [P0-Critical | P1-High | P2-Medium | P3-Low]
- **Complexity**: [Low | Medium | High]
```

### Examples

**Input Use Cases**:

```
UC-001: Register User
UC-002: Verify Email
UC-003: Resend Verification Email
UC-020: Request Password Reset
UC-021: Reset Password
UC-030: View Profile
UC-031: Update Profile
```

**Defined Features**:

```markdown
**Feature 1**: User Registration

- **ID**: F-001
- **Business Capability**: Identity & Access Management
- **Description**: Enable new users to create accounts
- **User Value**: Users can create accounts to access personalized features
- **Use Cases**: UC-001, UC-002, UC-003
- **Business Rules**: BR-001 through BR-010
- **Dependencies**:
  - IEmailService (shared)
  - IPasswordHasher (shared)
- **Priority**: P0-Critical (foundational feature)
- **Complexity**: Low

**Feature 2**: Password Management

- **ID**: F-002
- **Business Capability**: Identity & Access Management
- **Description**: Enable users to reset forgotten passwords
- **User Value**: Users can regain account access if password forgotten
- **Use Cases**: UC-020, UC-021
- **Business Rules**: BR-020 through BR-024
- **Dependencies**:
  - User Registration (must have account)
  - IEmailService (shared)
  - IPasswordHasher (shared)
- **Priority**: P1-High (important but not blocking)
- **Complexity**: Medium

**Feature 3**: Profile Management

- **ID**: F-003
- **Business Capability**: User Experience
- **Description**: Enable users to view and update profile information
- **User Value**: Users can personalize their account information
- **Use Cases**: UC-030, UC-031
- **Business Rules**: BR-030 through BR-035
- **Dependencies**:
  - User Registration (must have account)
  - User Authentication (must be logged in)
- **Priority**: P2-Medium (nice to have)
- **Complexity**: Low
```

## Vertical Slice Design

### Design Rules

**Rule 1: Each Slice Must Be Complete**

Include ALL layers:

- ✅ Database schema (if needed)
- ✅ Domain models
- ✅ Business logic (handler)
- ✅ Validation
- ✅ API endpoint
- ✅ Tests

**Rule 2: Each Slice Must Deliver Value**

User can do something meaningful:

- ✅ "User can register" (delivers value)
- ❌ "Create user table" (no user value)

**Rule 3: Each Slice Must Be Independent**

Can be implemented and deployed separately:

- ✅ "Basic registration" → "Email verification" → "Welcome email"
- ❌ All three must be done together

**Rule 4: Each Slice Must Be Testable**

Has clear acceptance criteria:

- ✅ "Given valid inputs, user account is created"
- ❌ "Some of registration works"

### Slice Template

```markdown
## Vertical Slice: [Slice Name]

**Slice ID**: S-[feature-id]-[number]
**Feature**: [Feature name]
**Priority**: [P0|P1|P2|P3]
**Estimate**: [1-5 days]

### User Story

As a [actor], I want to [action] so that [benefit]

### Business Rules

- BR-[ID]: [Statement]
- BR-[ID]: [Statement]

### Acceptance Criteria

- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

### Technical Components

**Files to Create**:

1. `/Features/[Feature]/[Action]Command.cs`
2. `/Features/[Feature]/[Action]Handler.cs`
3. `/Features/[Feature]/[Action]Validator.cs`
4. `/Features/[Feature]/[Action]Result.cs`
5. `/Tests/Features/[Feature]/[Action]HandlerTests.cs`

**API Endpoint**:

- Method: [POST|GET|PUT|DELETE]
- Path: `/api/[resource]/[action]`
- Request: [Schema]
- Response: [Schema]

**Database Changes** (if needed):

- [SQL or migration description]

**Dependencies**:

- [Service]: [Purpose]
- [Service]: [Purpose]

### Test Scenarios

- Happy path: [Description]
- Validation errors: [Description]
- Edge cases: [Description]
```

### Decomposition Strategy

When feature is too large, apply decomposition:

**Strategy 1: MVS (Minimal Viable Slice)**

```markdown
**Slice 1**: Absolute minimum functionality

- Simplest validation
- Basic error handling
- Core functionality only

**Slice 2**: Add comprehensive validation
**Slice 3**: Add advanced error handling
**Slice 4**: Add optional features
```

**Strategy 2: Happy Path First**

```markdown
**Slice 1**: Complete happy path (assumes everything works)
**Slice 2**: Add error handling
**Slice 3**: Add edge cases
**Slice 4**: Add performance optimization
```

**Strategy 3: Core + Extensions**

```markdown
**Slice 1 (Core)**: Essential functionality
**Slice 2-N (Extensions)**: Optional enhancements
```

### Examples

**Feature**: User Registration

**Decomposed Slices**:

````markdown
## Vertical Slice 1: Basic Registration

**Slice ID**: S-001-1
**Feature**: User Registration (F-001)
**Priority**: P0
**Estimate**: 2 days

### User Story

As a prospective customer, I want to register with email and password so that I can create an account

### Business Rules

- BR-001: Email must be unique
- BR-002: Email must be valid format (RFC 5322)
- BR-003: Password must be 8+ characters with mixed case and digit
- BR-004: First and last name required (2-100 characters)

### Acceptance Criteria

- [ ] User submits email, password, first name, last name
- [ ] System validates email format
- [ ] System checks email uniqueness
- [ ] System validates password strength
- [ ] System validates name length
- [ ] System creates account with hashed password
- [ ] System returns success with user ID
- [ ] All validation errors are clear and specific

### Technical Components

**Files to Create**:

1. `/Features/UserRegistration/RegisterUserCommand.cs`
2. `/Features/UserRegistration/RegisterUserHandler.cs`
3. `/Features/UserRegistration/RegisterUserValidator.cs`
4. `/Features/UserRegistration/RegistrationResult.cs`
5. `/Features/UserRegistration/UserRegistrationRepository.cs`
6. `/Api/Controllers/UserRegistrationController.cs`
7. `/Tests/Features/UserRegistration/RegisterUserHandlerTests.cs`

**API Endpoint**:

- Method: POST
- Path: `/api/users/register`
- Request:
  ```json
  {
    "email": "string",
    "password": "string",
    "firstName": "string",
    "lastName": "string"
  }
  ```
````

- Response (201):
  ```json
  {
    "userId": "guid",
    "email": "string",
    "registeredAt": "datetime"
  }
  ```

**Database Changes**:

```sql
CREATE TABLE Users (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    Email NVARCHAR(255) UNIQUE NOT NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(100) NOT NULL,
    LastName NVARCHAR(100) NOT NULL,
    CreatedAt DATETIME2 NOT NULL,
    IsActive BIT NOT NULL DEFAULT 1
);
```

**Dependencies**:

- IPasswordHasher: Hash passwords with bcrypt
- IDbContext: Database access
- FluentValidation: Input validation

### Test Scenarios

- Happy path: Valid data creates account
- Email exists: Returns 409 Conflict
- Invalid email: Returns 400 with specific error
- Weak password: Returns 400 with requirements
- Missing fields: Returns 400 for each missing field

---

## Vertical Slice 2: Email Verification

**Slice ID**: S-001-2
**Feature**: User Registration (F-001)
**Priority**: P0
**Estimate**: 2 days

### User Story

As a registered user, I want to verify my email address so that I can prove I own the email

### Business Rules

- BR-005: Verification email sent automatically on registration
- BR-006: Verification token expires in 24 hours
- BR-007: Users must verify email to access full features
- BR-008: Unverified accounts deleted after 7 days

### Acceptance Criteria

- [ ] Verification email sent on registration
- [ ] Email contains verification link with token
- [ ] User clicks link to verify
- [ ] Token validated (exists, not expired, not used)
- [ ] Account marked as verified
- [ ] Success page displayed
- [ ] Expired token shows error with resend option

### Technical Components

**Files to Create**:

1. `/Features/UserRegistration/VerifyEmailCommand.cs`
2. `/Features/UserRegistration/VerifyEmailHandler.cs`
3. `/Features/UserRegistration/SendVerificationEmailCommand.cs`
4. `/Features/UserRegistration/SendVerificationEmailHandler.cs`
5. `/Api/Controllers/EmailVerificationController.cs`
6. `/Tests/Features/UserRegistration/VerifyEmailHandlerTests.cs`

**API Endpoint**:

- Method: GET
- Path: `/api/users/verify/{token}`
- Response (200): Verification success
- Response (400): Invalid/expired token

**Database Changes**:

```sql
ALTER TABLE Users
ADD VerificationToken NVARCHAR(255),
    VerificationTokenExpiry DATETIME2,
    IsEmailVerified BIT NOT NULL DEFAULT 0;
```

**Dependencies**:

- IEmailService: Send verification emails
- IDbContext: Database access
- ITokenGenerator: Generate secure tokens

### Test Scenarios

- Happy path: Valid token verifies account
- Expired token: Returns error with resend option
- Already verified: Returns success message
- Invalid token: Returns error
- Token already used: Returns error

````

## Output Templates

### Complete Analysis Output

When user requests full analysis, provide:

```markdown
# Requirements Analysis: [System/Feature Name]

## Executive Summary
[2-3 paragraphs summarizing what was analyzed and key findings]

## Business Rules

### Structural Rules
**BR-001**: [Statement]
- **Priority**: [Level]
- **Rationale**: [Why]
- **Scope**: [Where applies]

[... all structural rules ...]

### Operative Rules
**BR-010**: [Statement]
- **Priority**: [Level]
- **Rationale**: [Why]
- **Scope**: [Where applies]

[... all operative rules ...]

### Derivation Rules
**BR-020**: [Statement]
- **Priority**: [Level]
- **Formula**: [Calculation]
- **Scope**: [Where applies]

[... all derivation rules ...]

### Action Enablers
**BR-030**: [Statement]
- **Priority**: [Level]
- **Trigger**: [When happens]
- **Action**: [What happens]

[... all action enablers ...]

## Use Cases

**UC-001**: [Use Case Name]
- **Actor**: [Primary actor]
- **Goal**: [What achieving]
- **Main Flow**: [Steps]
- **Alternative Flows**: [Error cases]
- **Business Rules**: [Related BR IDs]

[... all use cases ...]

## Features

**Feature 1**: [Feature Name]
- **ID**: F-001
- **Description**: [What it does]
- **User Value**: [Value delivered]
- **Use Cases**: [UC IDs]
- **Business Rules**: [BR IDs]
- **Dependencies**: [What needs]
- **Priority**: [P0-P3]
- **Complexity**: [Low|Medium|High]

[... all features ...]

## Vertical Slices

### Feature 1: [Feature Name]

#### Slice 1.1: [Slice Name]
[Complete slice specification using template]

#### Slice 1.2: [Slice Name]
[Complete slice specification using template]

[... all slices for feature 1 ...]

### Feature 2: [Feature Name]

[... all slices for feature 2 ...]

## Implementation Roadmap

**Phase 1: Foundation** (Weeks 1-2)
- S-001-1: Basic User Registration
- S-002-1: Basic User Authentication
- Priority: P0 (blocking other features)

**Phase 2: Core Features** (Weeks 3-4)
- S-001-2: Email Verification
- S-003-1: Basic Product Catalog
- Priority: P0 (critical for launch)

**Phase 3: Enhanced Features** (Weeks 5-6)
- S-004-1: Shopping Cart
- S-005-1: Checkout Process
- Priority: P1 (important)

**Phase 4: Additional Features** (Weeks 7-8)
- S-006-1: Order History
- S-007-1: Product Reviews
- Priority: P2 (nice to have)

## Open Questions

1. [Question requiring clarification]
2. [Ambiguity identified]
3. [Missing information]

## Recommendations

1. [Suggestion for improvement]
2. [Risk to consider]
3. [Optimization opportunity]
````

## Validation Rules

### Validation Checklist

Before presenting analysis, verify:

**Business Rules**:

- [ ] All rules have unique IDs
- [ ] All rules have type classification
- [ ] All rules have priority
- [ ] All ambiguous rules flagged
- [ ] All rules have clear scope

**Use Cases**:

- [ ] All use cases have unique IDs
- [ ] All use cases have actor, goal, flows
- [ ] All use cases link to business rules
- [ ] All alternative flows identified
- [ ] All preconditions/postconditions stated

**Features**:

- [ ] Each feature passes cohesion test
- [ ] Each feature passes independence test
- [ ] Each feature passes value test
- [ ] Each feature passes size test
- [ ] All dependencies identified

**Vertical Slices**:

- [ ] Each slice spans all layers
- [ ] Each slice delivers user value
- [ ] Each slice is independently testable
- [ ] Each slice has clear acceptance criteria
- [ ] Each slice lists all components

**Completeness**:

- [ ] All requirements covered
- [ ] No orphaned business rules
- [ ] No orphaned use cases
- [ ] Priority and sequencing defined
- [ ] Open questions documented

### Quality Rules

**Rule 1: Be Specific**

- ❌ "Validate input"
- ✅ "Validate email format (RFC 5322) and check uniqueness"

**Rule 2: Be Testable**

- ❌ "System should work correctly"
- ✅ "Given valid input, account is created and returns 201 with user ID"

**Rule 3: Be Complete**

- ❌ "Create user endpoint"
- ✅ "POST /api/users endpoint with request/response schemas, validation, error codes"

**Rule 4: Flag Ambiguities**

```markdown
⚠️ **NEEDS CLARIFICATION**
**Current**: "Password must be secure"
**Issue**: Definition of "secure" is ambiguous
**Suggested**: "Password must be 8-20 characters with uppercase, lowercase, digit, special character"
```

## Common Patterns

### Pattern 1: CRUD Feature

When requirements describe managing an entity:

```markdown
**Identified Pattern**: CRUD Operations

**Feature**: [Entity] Management
**Slices**:

1. Create [Entity]
2. Read [Entity]
3. Update [Entity]
4. Delete [Entity]
5. List [Entities]

**Business Rules to Extract**:

- Validation rules for entity creation
- Update authorization rules
- Delete constraints (soft vs hard delete)
- List filtering and pagination rules
```

### Pattern 2: Workflow Feature

When requirements describe a process:

```markdown
**Identified Pattern**: Multi-Step Workflow

**Feature**: [Process Name]
**Slices** (one per step):

1. Initialize [Process]
2. [Step 2]
3. [Step 3]
4. Complete [Process]

**Business Rules to Extract**:

- Step sequencing rules
- Validation at each step
- Rollback/cancellation rules
- State transition rules
```

### Pattern 3: Calculation Feature

When requirements describe computations:

```markdown
**Identified Pattern**: Calculation/Derivation

**Feature**: [Calculation Name]
**Slices** (one per calculation component):

1. Calculate Base [Value]
2. Apply [Adjustment 1]
3. Apply [Adjustment 2]
4. Calculate Final [Value]

**Business Rules to Extract**:

- Calculation formulas
- Rounding rules
- Edge case handling
- Validation of inputs
```

### Pattern 4: Authorization Feature

When requirements describe access control:

```markdown
**Identified Pattern**: Access Control

**Feature**: [Resource] Access Control
**Slices**:

1. Authenticate User
2. Authorize [Action 1]
3. Authorize [Action 2]
4. Audit Access

**Business Rules to Extract**:

- Authentication requirements
- Authorization rules per action
- Role/permission definitions
- Audit requirements
```

## Quality Checklist

### Before Presenting Analysis

**Completeness**:

- [ ] All business rules extracted from requirements
- [ ] All use cases identified
- [ ] All features defined with boundaries
- [ ] All slices designed with complete specifications
- [ ] Implementation sequence proposed

**Clarity**:

- [ ] All IDs are sequential and consistent
- [ ] All statements are specific and testable
- [ ] All ambiguities are flagged
- [ ] All technical terms are clear
- [ ] All dependencies are identified

**Consistency**:

- [ ] Naming follows patterns (BR-###, UC-###, F-###, S-###-###)
- [ ] All references link correctly (BR IDs in UC, UC IDs in Features)
- [ ] Priorities are consistent across sections
- [ ] Terminology is consistent throughout

**Actionability**:

- [ ] Each slice has clear acceptance criteria
- [ ] Each slice lists files to create
- [ ] Each slice specifies API contracts
- [ ] Each slice identifies dependencies
- [ ] Each slice includes test scenarios

### Communication Checklist

**Do**:

- ✅ Present structured output using templates
- ✅ Number all rules, use cases, features, slices
- ✅ Link related items (BR → UC → Feature → Slice)
- ✅ Flag ambiguities and ask questions
- ✅ Provide examples for clarity
- ✅ Suggest priorities and sequencing
- ✅ Include implementation estimates

**Don't**:

- ❌ Make assumptions about ambiguous requirements
- ❌ Skip validation or business rules
- ❌ Design slices that span multiple features
- ❌ Omit error handling or edge cases
- ❌ Forget to link business rules to use cases
- ❌ Provide incomplete acceptance criteria
- ❌ Design horizontal slices (by layer)

## Summary for AI Assistants

### Quick Reference

**When user provides requirements**:

1. **Extract** business rules (4 types: structural, operative, derivation, action enablers)
2. **Identify** use cases (actor, goal, flows)
3. **Define** features (cohesion, independence, value, size)
4. **Design** vertical slices (complete, valuable, independent, testable)
5. **Present** structured analysis using templates
6. **Validate** completeness and quality
7. **Communicate** clearly with IDs and links

**Key Validation Questions**:

- Does each rule have a clear, testable statement?
- Does each use case have complete flows?
- Does each feature pass the 4 tests (cohesion, independence, value, size)?
- Does each slice span all layers and deliver value?
- Are all ambiguities flagged?
- Is everything linked (BR → UC → Feature → Slice)?

**Output Structure**:

```
1. Business Rules (BR-###)
   ↓
2. Use Cases (UC-###)
   ↓
3. Features (F-###)
   ↓
4. Vertical Slices (S-###-###)
   ↓
5. Implementation Roadmap
```

**Remember**:

- Be specific (testable statements)
- Be complete (all layers, error cases)
- Be structured (use templates)
- Be questioning (flag ambiguities)
- Be helpful (suggest priorities, provide examples)

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Maintainer**: AI-Assisted Development Team
**Related Instructions**:

- `.github/instructions/business-rules-to-vertical-slices.instructions.md` - Human guide
- `.github/instructions/ai-vertical-slice-implementation.instructions.md` - Code generation
- `.github/instructions/vertical-slice-architecture.instructions.md` - Architecture guide
