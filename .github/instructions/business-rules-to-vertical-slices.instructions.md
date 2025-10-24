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
  - task: "human instruction file creation"
    duration: "00:30:00"
  - task: "review and refinement"
    duration: "00:15:00"
total_duration: "01:00:00"
ai_log: "ai-logs/2025/10/22/business-rules-vertical-slices-20251022/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{md,txt}"
---

# Business Rules to Vertical Slices: Human Guide

## Overview

This document provides comprehensive guidance for analyzing business requirements, extracting business rules and use cases, and designing features as vertical slices for implementation. This process bridges the gap between business needs and technical implementation using vertical slice architecture.

**Target Audience**: Business analysts, product owners, software architects, and development teams

**Related Documentation**:

- [Vertical Slice Architecture Instructions](.github/instructions/vertical-slice-architecture.instructions.md)
- [AI Vertical Slice Implementation](.github/instructions/ai-vertical-slice-implementation.instructions.md)

## Table of Contents

- [Overview](#overview)
- [The Analysis Process](#the-analysis-process)
- [Understanding Business Rules](#understanding-business-rules)
- [Extracting Use Cases](#extracting-use-cases)
- [Identifying Feature Boundaries](#identifying-feature-boundaries)
- [Mapping to Vertical Slices](#mapping-to-vertical-slices)
- [Prioritization and Sequencing](#prioritization-and-sequencing)
- [Documentation Templates](#documentation-templates)
- [Validation and Review](#validation-and-review)
- [Real-World Examples](#real-world-examples)
- [Common Pitfalls](#common-pitfalls)
- [Best Practices](#best-practices)

## The Analysis Process

### High-Level Workflow

```
1. Gather Requirements
   ↓
2. Extract Business Rules
   ↓
3. Identify Use Cases
   ↓
4. Define Feature Boundaries
   ↓
5. Design Vertical Slices
   ↓
6. Prioritize & Sequence
   ↓
7. Validate with Stakeholders
   ↓
8. Document for Implementation
```

### Key Principles

1. **Start with User Value**: Every vertical slice must deliver tangible user value
2. **Think End-to-End**: Each slice spans all architectural layers
3. **Minimize Dependencies**: Slices should be as independent as possible
4. **Iterate and Refine**: Analysis is iterative, not waterfall
5. **Validate Early**: Get feedback before implementation begins

## Understanding Business Rules

### What Are Business Rules?

Business rules are statements that define or constrain some aspect of the business. They are intended to assert business structure or control/influence business behavior.

**Types of Business Rules**:

1. **Structural Rules** (Facts): Define relationships and constraints

   - Example: "A customer must have an email address"
   - Example: "An order belongs to exactly one customer"

2. **Operative Rules** (Constraints): Define what must/must not happen

   - Example: "A customer cannot place an order if their account is suspended"
   - Example: "Discount codes can only be used once per customer"

3. **Derivation Rules** (Computations): Define how values are calculated

   - Example: "Order total = sum of line items + shipping - discounts"
   - Example: "Customer tier is based on total purchases in last 12 months"

4. **Action Enablers** (Triggers): Define when actions should occur
   - Example: "Send welcome email when customer registers"
   - Example: "Notify warehouse when order is confirmed"

### Extracting Business Rules

#### Technique 1: Interview Questions

Ask stakeholders:

- "What must always be true about [concept]?"
- "What are the constraints on [action]?"
- "When can [action] happen? When can't it happen?"
- "What calculations are involved in [process]?"
- "What happens automatically when [event] occurs?"

#### Technique 2: Document Analysis

Review existing documentation for:

- Modal verbs: must, should, may, cannot, shall
- Conditional statements: if...then, when...then
- Constraints: only, never, always, at least, at most
- Computations: calculated as, derived from, based on

#### Technique 3: Business Rule Template

```markdown
**Rule ID**: BR-001
**Category**: Operative Rule
**Statement**: A user cannot register with an email that is already in use
**Rationale**: Each user must have a unique identity for security and communication
**Scope**: User Registration
**Priority**: Critical
**Exceptions**: None
**Related Rules**: BR-002 (Email validation format)
```

### Business Rule Documentation

**Format Example**:

```markdown
## Business Rules: E-Commerce Order Processing

### BR-001: Order Minimum

- **Type**: Operative Rule
- **Statement**: An order must have a minimum subtotal of $10.00
- **Rationale**: Covers processing costs
- **Impact**: High (affects all orders)
- **Validation**: Check before order confirmation

### BR-002: Inventory Reservation

- **Type**: Action Enabler
- **Statement**: When an order is placed, inventory must be reserved for 15 minutes
- **Rationale**: Prevents overselling while customer completes checkout
- **Impact**: Medium
- **Trigger**: Order creation initiated

### BR-003: Order Total Calculation

- **Type**: Derivation Rule
- **Statement**: Order Total = Subtotal + Tax + Shipping - Discounts
- **Rationale**: Standardized calculation
- **Impact**: Critical
- **Components**: Subtotal, Tax Rate, Shipping Method, Applied Discounts
```

## Extracting Use Cases

### What Are Use Cases?

Use cases describe how users (actors) interact with the system to achieve specific goals. They represent functional requirements from the user's perspective.

### Use Case Structure

**Standard Template**:

```markdown
**Use Case ID**: UC-001
**Name**: Register New User Account
**Actor**: Prospective Customer
**Goal**: Create an account to make purchases
**Preconditions**: User is not already registered
**Postconditions**: User has active account and receives welcome email

**Main Flow**:

1. User navigates to registration page
2. User enters email, password, first name, last name
3. System validates email format
4. System checks email is not already registered
5. System validates password strength
6. System creates user account
7. System sends welcome email
8. System displays success message

**Alternative Flows**:

- 4a. Email already exists

  - System displays error: "Email already registered"
  - System offers password reset link

- 6a. System error during account creation
  - System logs error
  - System displays generic error message
  - System notifies support team

**Business Rules**: BR-001, BR-002, BR-003
**Priority**: High
**Complexity**: Low
```

### Use Case Identification Techniques

#### Technique 1: Actor-Goal List

List all actors and their goals:

```markdown
**Actor: Customer**

- Register for account
- Log in to account
- Browse products
- Search for products
- Add items to cart
- Apply discount code
- Complete checkout
- View order history
- Track order status
- Update profile

**Actor: Administrator**

- Manage products
- Process refunds
- View analytics
- Manage users
```

#### Technique 2: Event Storming

Identify domain events and work backwards to use cases:

```markdown
**Events**:

- UserRegistered
- UserLoggedIn
- ProductAddedToCart
- OrderPlaced
- PaymentProcessed
- OrderShipped

**Use Cases** (derived from events):

- Register User → UserRegistered
- Login User → UserLoggedIn
- Add to Cart → ProductAddedToCart
- Checkout Order → OrderPlaced
- Process Payment → PaymentProcessed
```

#### Technique 3: User Story Expansion

Expand user stories into detailed use cases:

```markdown
**User Story**:
"As a customer, I want to reset my password so that I can regain access to my account"

**Expanded Use Cases**:

1. UC-010: Request Password Reset
2. UC-011: Validate Reset Token
3. UC-012: Update Password
```

## Identifying Feature Boundaries

### What Makes a Good Feature?

A good feature for vertical slice implementation:

1. **Delivers Complete Value**: Provides end-to-end functionality
2. **Has Clear Boundaries**: Well-defined scope with minimal external dependencies
3. **Is Independently Testable**: Can be tested without other features
4. **Is Appropriately Sized**: Can be implemented in 1-5 days
5. **Aligns with Business Capabilities**: Maps to business domains

### Feature Identification Framework

#### Level 1: Business Capabilities

```markdown
**E-Commerce Platform Capabilities**:

- Identity & Access Management
- Product Catalog Management
- Shopping Experience
- Order Processing
- Payment Processing
- Fulfillment & Shipping
- Customer Service
```

#### Level 2: Features (Within Capabilities)

```markdown
**Identity & Access Management**:

- User Registration
- User Authentication
- Password Management
- Profile Management
- Session Management

**Order Processing**:

- Shopping Cart Management
- Order Checkout
- Order Confirmation
- Order Tracking
- Order History
```

#### Level 3: Feature Slices (Smallest Deployable Units)

```markdown
**Password Management Feature Slices**:

1. Request Password Reset (Slice 1)

   - Request reset via email
   - Send reset token email

2. Reset Password (Slice 2)

   - Validate reset token
   - Update password
   - Invalidate token

3. Change Password (Slice 3)
   - Validate current password
   - Update to new password
   - Send confirmation email
```

### Boundary Analysis Questions

Ask these questions to validate feature boundaries:

1. **Cohesion**: Do all parts of this feature naturally belong together?
2. **Coupling**: Can this feature be implemented without modifying other features?
3. **Completeness**: Does this feature provide complete value to the user?
4. **Size**: Can this be implemented and tested in a reasonable timeframe?
5. **Dependencies**: What shared resources or services does this need?

### Feature Boundary Patterns

**Pattern 1: CRUD Feature**

```
Feature: Product Management
- Create Product (Slice 1)
- Update Product (Slice 2)
- Delete Product (Slice 3)
- View Product Details (Slice 4)
- List Products (Slice 5)
```

**Pattern 2: Workflow Feature**

```
Feature: Order Checkout
- Initialize Checkout (Slice 1)
- Apply Shipping Method (Slice 2)
- Apply Payment Method (Slice 3)
- Review and Confirm (Slice 4)
- Process Order (Slice 5)
```

**Pattern 3: Calculation Feature**

```
Feature: Price Calculation
- Calculate Base Price (Slice 1)
- Apply Volume Discounts (Slice 2)
- Apply Promotional Discounts (Slice 3)
- Calculate Tax (Slice 4)
- Calculate Shipping (Slice 5)
```

## Mapping to Vertical Slices

### Slice Design Template

````markdown
## Feature: User Registration

### Vertical Slice: Basic Registration

**User Story**: As a prospective customer, I want to register with email and password so that I can create an account

**Business Rules**:

- BR-001: Email must be unique
- BR-002: Email must be valid format
- BR-003: Password must meet strength requirements
- BR-004: User must provide first and last name

**Use Cases**: UC-001 (Register New User Account)

**Acceptance Criteria**:

- [ ] User can enter email, password, first name, last name
- [ ] System validates email format
- [ ] System checks email uniqueness
- [ ] System validates password strength
- [ ] System creates user account
- [ ] System sends welcome email
- [ ] User receives confirmation

**Technical Components**:

- Command: RegisterUserCommand
- Handler: RegisterUserHandler
- Validator: RegisterUserValidator
- Repository: UserRegistrationRepository
- Result: RegistrationResult
- API Endpoint: POST /api/users/register

**Data Model**:

```csharp
User {
  Id: Guid
  Email: string
  PasswordHash: string
  FirstName: string
  LastName: string
  CreatedAt: DateTime
  IsActive: bool
}
```
````

**Dependencies**:

- IPasswordHasher (shared)
- IEmailService (shared)
- IDbContext (shared)

**Test Scenarios**:

- Happy path: Valid registration
- Email already exists
- Invalid email format
- Weak password
- Missing required fields
- Database error handling

````

### Slice Decomposition Strategy

**Strategy 1: Minimal Viable Slice (MVS)**

Start with the absolute minimum:
```markdown
**Slice 1 (MVS)**: Register with email and password only
- Simplest validation
- No email verification
- No welcome email
- Basic error handling

**Slice 2**: Add email verification
**Slice 3**: Add welcome email
**Slice 4**: Add comprehensive validation
**Slice 5**: Add advanced error handling
````

**Strategy 2: Happy Path First**

Implement the ideal scenario first:

```markdown
**Slice 1**: Complete happy path

- Full validation
- All features working
- Assumes everything succeeds

**Slice 2**: Add error handling
**Slice 3**: Add edge cases
**Slice 4**: Add performance optimization
```

**Strategy 3: Core + Extensions**

Build core functionality, then extend:

```markdown
**Slice 1 (Core)**: Basic user registration
**Slice 2 (Extension)**: Social media registration
**Slice 3 (Extension)**: Enterprise SSO registration
**Slice 4 (Extension)**: Two-factor authentication
```

### Dependency Management

**Identify Shared Dependencies**:

```markdown
## Shared Dependencies Analysis

**Shared Interfaces** (multiple features need):

- IEmailService: Used by Registration, PasswordReset, OrderConfirmation
- IPaymentGateway: Used by Checkout, Refunds, Subscriptions
- IUserProvider: Used by Orders, Reviews, Support

**Shared Domain Models**:

- User: Used by Authentication, Profile, Orders
- Product: Used by Catalog, Cart, Orders
- Order: Used by Checkout, Fulfillment, Customer Service

**Shared Behaviors**:

- Validation: All features need input validation
- Authorization: All features need access control
- Logging: All features need audit logging
```

## Prioritization and Sequencing

### Prioritization Framework

**Priority Matrix**:

```markdown
| Feature Slice      | Business Value | Complexity | Dependencies | Priority |
| ------------------ | -------------- | ---------- | ------------ | -------- |
| User Registration  | High           | Low        | None         | P0       |
| User Login         | High           | Low        | Registration | P0       |
| Product Browse     | High           | Medium     | None         | P0       |
| Add to Cart        | High           | Low        | Product      | P1       |
| Basic Checkout     | High           | Medium     | Cart, User   | P1       |
| Payment Processing | High           | High       | Checkout     | P1       |
| Order Confirmation | High           | Low        | Payment      | P1       |
| Password Reset     | Medium         | Medium     | User         | P2       |
| Order History      | Medium         | Low        | Orders       | P2       |
| Product Search     | Medium         | High       | Product      | P2       |
| Product Reviews    | Low            | Medium     | Product      | P3       |
```

### Sequencing Strategies

**Strategy 1: Dependency-First**

Implement in dependency order:

```
1. User Registration (no dependencies)
2. User Authentication (depends on Registration)
3. Product Catalog (no dependencies)
4. Shopping Cart (depends on Product, User)
5. Checkout (depends on Cart)
```

**Strategy 2: Walking Skeleton**

Implement minimal end-to-end first:

```
1. Basic User Registration (minimal)
2. Basic Product Display (minimal)
3. Basic Add to Cart (minimal)
4. Basic Checkout (minimal)
5. Then enhance each feature
```

**Strategy 3: Risk-First**

Tackle highest risk/uncertainty first:

```
1. Payment Gateway Integration (high risk)
2. Inventory Management (complex)
3. Tax Calculation (complicated rules)
4. Then lower-risk features
```

## Documentation Templates

### Feature Specification Template

```markdown
# Feature Specification: [Feature Name]

## Overview

**Feature ID**: F-001
**Feature Name**: User Registration
**Business Capability**: Identity & Access Management
**Owner**: [Product Owner Name]
**Status**: Approved
**Priority**: P0

## Business Context

**Problem Statement**: New users need a way to create accounts to access personalized features and make purchases.

**Business Goals**:

- Increase user base
- Enable personalized experiences
- Track user behavior
- Build customer database

**Success Metrics**:

- 80% registration completion rate
- < 2 minutes average registration time
- < 1% error rate

## Scope

**In Scope**:

- Email/password registration
- Email verification
- Welcome email
- Basic profile information

**Out of Scope** (Future):

- Social media registration
- Two-factor authentication
- Enterprise SSO

## Business Rules

- BR-001: Email must be unique
- BR-002: Password must be 8+ characters with uppercase, lowercase, and digit
- BR-003: Users must verify email within 24 hours
- BR-004: Unverified accounts are automatically deleted after 7 days

## Use Cases

- UC-001: Register New User
- UC-002: Verify Email Address
- UC-003: Resend Verification Email

## Vertical Slices

### Slice 1: Basic Registration (Week 1)

**User Story**: As a user, I want to register with email and password
**Acceptance Criteria**:

- [ ] User can submit registration form
- [ ] Email uniqueness is validated
- [ ] Password strength is validated
- [ ] Account is created
- [ ] User receives success confirmation

**Technical Design**:

- Command: RegisterUserCommand
- Handler: RegisterUserHandler
- Validator: RegisterUserValidator
- Endpoint: POST /api/users/register

### Slice 2: Email Verification (Week 2)

**User Story**: As a user, I want to verify my email address
**Acceptance Criteria**:

- [ ] Verification email is sent on registration
- [ ] User can click verification link
- [ ] Account is activated on verification
- [ ] User receives confirmation

**Technical Design**:

- Command: VerifyEmailCommand
- Handler: VerifyEmailHandler
- Endpoint: GET /api/users/verify/{token}

## Dependencies

**Technical Dependencies**:

- Email service (SendGrid/AWS SES)
- Database (User table)
- Authentication framework

**Feature Dependencies**:

- None (foundational feature)

**Dependent Features**:

- User Authentication
- User Profile
- All authenticated features

## Non-Functional Requirements

- **Performance**: Registration completes in < 500ms
- **Security**: Passwords hashed with bcrypt
- **Availability**: 99.9% uptime
- **Scalability**: Support 100 concurrent registrations

## Testing Strategy

- Unit tests for business logic
- Integration tests for database operations
- API tests for endpoints
- UI tests for registration form
- Load tests for concurrent registrations

## Rollout Plan

- **Phase 1**: Internal testing (Week 1)
- **Phase 2**: Beta users (Week 2)
- **Phase 3**: General availability (Week 3)

## Open Questions

1. Should we support international phone numbers?
2. Do we need CAPTCHA for bot prevention?
3. What's the data retention policy for unverified accounts?
```

### Slice Implementation Card

```markdown
# Implementation Card: Register User

**Slice ID**: S-001-1
**Feature**: User Registration (F-001)
**Priority**: P0
**Estimate**: 2 days
**Status**: Ready for Development

## User Story

As a prospective customer, I want to register with email and password so that I can create an account and make purchases.

## Business Rules

- BR-001: Email must be unique
- BR-002: Email must be valid format (RFC 5322)
- BR-003: Password must be 8-20 characters
- BR-004: Password must contain: uppercase, lowercase, digit
- BR-005: First and last name required (2-100 characters each)

## Acceptance Criteria

- [ ] User submits email, password, first name, last name
- [ ] System validates email format and uniqueness
- [ ] System validates password strength requirements
- [ ] System validates name requirements
- [ ] System creates user account with hashed password
- [ ] System sends welcome email
- [ ] System returns user ID and success confirmation
- [ ] All validation errors are user-friendly

## Technical Implementation

**Files to Create**:

1. `/Features/UserRegistration/RegisterUserCommand.cs`
2. `/Features/UserRegistration/RegisterUserHandler.cs`
3. `/Features/UserRegistration/RegisterUserValidator.cs`
4. `/Features/UserRegistration/RegistrationResult.cs`
5. `/Features/UserRegistration/UserRegistrationRepository.cs`
6. `/Api/Controllers/UserRegistrationController.cs`
7. `/Tests/Features/UserRegistration/RegisterUserHandlerTests.cs`

**API Endpoint**:
```

POST /api/users/register
Content-Type: application/json

Request:
{
"email": "user@example.com",
"password": "SecurePass123",
"firstName": "John",
"lastName": "Doe"
}

Response (200 OK):
{
"userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
"email": "user@example.com",
"registeredAt": "2025-10-22T16:00:00Z"
}

Response (400 Bad Request):
{
"errors": {
"email": ["Email already registered"],
"password": ["Password must contain uppercase letter"]
}
}

````

**Database Changes**:
```sql
CREATE TABLE Users (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    Email NVARCHAR(255) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(255) NOT NULL,
    FirstName NVARCHAR(100) NOT NULL,
    LastName NVARCHAR(100) NOT NULL,
    CreatedAt DATETIME2 NOT NULL,
    IsActive BIT NOT NULL DEFAULT 1
);

CREATE INDEX IX_Users_Email ON Users(Email);
````

## Dependencies

- IPasswordHasher (hash passwords with bcrypt)
- IEmailService (send welcome email)
- IDbContext (database access)
- FluentValidation (input validation)
- MediatR (command handling)

## Test Scenarios

**Happy Path**:

- Valid registration creates account and sends email

**Validation Errors**:

- Invalid email format returns error
- Email already exists returns error
- Weak password returns specific errors
- Missing fields return errors
- Names too short/long return errors

**Edge Cases**:

- Database connection failure
- Email service failure (should not block registration)
- Concurrent registration with same email

**Security**:

- Password is never returned in response
- Password is hashed before storage
- SQL injection attempts are prevented

## Definition of Done

- [ ] All files created following vertical slice structure
- [ ] Business rules implemented and validated
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests written
- [ ] API endpoint documented
- [ ] Code reviewed and approved
- [ ] Merged to main branch
- [ ] Deployed to staging environment
- [ ] QA testing passed
- [ ] Product owner acceptance

```

## Validation and Review

### Validation Checklist

**Business Validation**:
- [ ] Feature addresses stated business need
- [ ] Success metrics are measurable
- [ ] Stakeholders agree on scope
- [ ] Priority is aligned with business goals
- [ ] ROI justifies development cost

**Technical Validation**:
- [ ] Feature boundaries are clear
- [ ] Dependencies are identified
- [ ] Technical feasibility confirmed
- [ ] Architecture patterns followed
- [ ] Non-functional requirements addressed

**Completeness Validation**:
- [ ] All business rules captured
- [ ] All use cases documented
- [ ] All acceptance criteria defined
- [ ] Test scenarios identified
- [ ] Rollout plan defined

### Review Process

**Step 1: Peer Review**
- Developers review technical design
- Identify missing components
- Validate slice independence
- Confirm implementation approach

**Step 2: Business Review**
- Product owner validates business requirements
- Confirms acceptance criteria
- Approves priority and sequencing
- Validates success metrics

**Step 3: Architecture Review**
- Architect validates architectural alignment
- Reviews dependencies and coupling
- Confirms patterns and practices
- Identifies risks

**Step 4: Stakeholder Sign-Off**
- Present complete specification
- Address questions and concerns
- Obtain formal approval
- Document decisions

## Real-World Examples

### Example 1: E-Commerce Order Processing

**Business Requirements**:
- Customers need to purchase products
- System must handle payments securely
- Inventory must be managed accurately
- Customers should receive order confirmation

**Business Rules Extracted**:
- BR-010: Order minimum is $10
- BR-011: Payment must be authorized before order confirmation
- BR-012: Inventory is reserved when order is placed
- BR-013: Order total = subtotal + tax + shipping - discounts
- BR-014: Tax calculated based on shipping address
- BR-015: Free shipping on orders over $50

**Use Cases Identified**:
- UC-020: Initialize Checkout
- UC-021: Apply Shipping Method
- UC-022: Apply Discount Code
- UC-023: Submit Payment
- UC-024: Confirm Order

**Features Designed**:

**Feature 1: Shopping Cart**
- Slice 1: Add Item to Cart
- Slice 2: Update Item Quantity
- Slice 3: Remove Item from Cart
- Slice 4: View Cart Total

**Feature 2: Checkout Process**
- Slice 1: Initialize Checkout
- Slice 2: Enter Shipping Address
- Slice 3: Select Shipping Method
- Slice 4: Apply Discount Code
- Slice 5: Enter Payment Details
- Slice 6: Review and Confirm Order

**Feature 3: Order Confirmation**
- Slice 1: Process Payment
- Slice 2: Create Order Record
- Slice 3: Send Confirmation Email
- Slice 4: Display Confirmation Page

### Example 2: SaaS Subscription Management

**Business Requirements**:
- Users need to subscribe to service plans
- Support monthly and annual billing
- Allow plan upgrades/downgrades
- Handle payment failures gracefully

**Business Rules Extracted**:
- BR-030: Free trial is 14 days
- BR-031: Payment required after trial ends
- BR-032: Upgrades take effect immediately
- BR-033: Downgrades take effect at next billing cycle
- BR-034: Prorated refunds for annual subscriptions
- BR-035: Failed payments trigger 3 retry attempts

**Use Cases Identified**:
- UC-040: Start Free Trial
- UC-041: Subscribe to Plan
- UC-042: Upgrade Plan
- UC-043: Downgrade Plan
- UC-044: Cancel Subscription
- UC-045: Reactivate Subscription

**Features Designed**:

**Feature 1: Subscription Creation**
- Slice 1: Start Free Trial
- Slice 2: Select Plan
- Slice 3: Add Payment Method
- Slice 4: Confirm Subscription

**Feature 2: Plan Management**
- Slice 1: View Current Plan
- Slice 2: Upgrade to Higher Plan
- Slice 3: Downgrade to Lower Plan
- Slice 4: Cancel Subscription

**Feature 3: Billing Management**
- Slice 1: Process Recurring Payment
- Slice 2: Handle Payment Failure
- Slice 3: Apply Proration
- Slice 4: Generate Invoice

## Common Pitfalls

### Pitfall 1: Overly Broad Features

**Problem**: Feature is too large and encompasses too many capabilities

**Example**:
```

❌ Bad: "User Management" feature
Includes: registration, login, profile, password reset,
permissions, roles, account deletion, etc.

```

**Solution**: Break into smaller, focused features
```

✅ Good: Separate features

- User Registration
- User Authentication
- Profile Management
- Password Management
- Access Control

```

### Pitfall 2: Ignoring Dependencies

**Problem**: Not identifying shared dependencies upfront

**Example**:
```

Feature 1 needs IEmailService
Feature 2 needs IEmailService
Feature 3 needs IEmailService

❌ Each feature implements its own email service

```

**Solution**: Identify shared dependencies early
```

✅ Create IEmailService in /Common
All features depend on shared interface

```

### Pitfall 3: Incomplete Business Rules

**Problem**: Missing edge cases and constraints

**Example**:
```

❌ Incomplete: "Users must have unique emails"
Missing: What happens if duplicate? Case sensitivity? Whitespace handling?

```

**Solution**: Specify complete rules
```

✅ Complete:

- BR-001: Email must be unique (case-insensitive)
- BR-002: Whitespace is trimmed before validation
- BR-003: Duplicate email returns HTTP 409 with specific message
- BR-004: Deleted user emails can be reused after 90 days

```

### Pitfall 4: Technical Slicing Instead of Vertical

**Problem**: Slicing by technical layer instead of functionality

**Example**:
```

❌ Bad slicing:

- Slice 1: Create database schema
- Slice 2: Create API endpoints
- Slice 3: Create business logic
- Slice 4: Create UI

```

**Solution**: Slice vertically through all layers
```

✅ Good slicing:

- Slice 1: Basic registration (DB + API + Logic + UI)
- Slice 2: Email verification (DB + API + Logic + UI)
- Slice 3: Welcome email (DB + API + Logic + UI)

```

### Pitfall 5: No Clear Acceptance Criteria

**Problem**: Ambiguous completion criteria

**Example**:
```

❌ Vague: "User can register"
What validates? What errors handled? What response returned?

```

**Solution**: Specific, testable criteria
```

✅ Clear:

- [ ] User submits form with email, password, name
- [ ] System validates email format (RFC 5322)
- [ ] System checks email uniqueness
- [ ] System validates password strength (8+ chars, mixed case, digit)
- [ ] System creates account with hashed password
- [ ] System returns 201 Created with user ID
- [ ] System returns 400 Bad Request with validation errors

```

## Best Practices

### Practice 1: Start with Why

Always understand the business problem before designing solutions.

**Good Flow**:
```

1. Why? → Increase conversion rates
2. How? → Simplify registration process
3. What? → Email-only registration feature

```

### Practice 2: Use Story Mapping

Visualize user journeys to identify features:

```

User Journey: Purchase Product

Activities:
[Discover] → [Evaluate] → [Purchase] → [Receive] → [Review]

Features:
Browse Product Checkout Order Write
Products Details Process Tracking Review

Search Compare Payment Delivery Rate
Products Products Processing Confirmation Product

````

### Practice 3: Apply INVEST Criteria

Ensure slices are:
- **I**ndependent: Minimal dependencies
- **N**egotiable: Flexible scope
- **V**aluable: Delivers user value
- **E**stimable: Can be estimated
- **S**mall: Can be completed in 1-5 days
- **T**estable: Has clear acceptance criteria

### Practice 4: Collaborate Continuously

Include all perspectives throughout analysis:
- **Business**: Validates value and priority
- **Development**: Validates feasibility
- **QA**: Validates testability
- **UX**: Validates user experience
- **Operations**: Validates operability

### Practice 5: Document Decisions

Capture rationale for key decisions:

```markdown
## Decision Log

**Decision**: Use email-only registration (no username)
**Date**: 2025-10-22
**Participants**: Product Owner, Tech Lead, UX Designer
**Rationale**:
- Simplifies user experience
- Email already required for communication
- Industry standard practice
- Reduces cognitive load
**Alternatives Considered**:
- Username + Email (rejected: added complexity)
- Phone number (rejected: international issues)
**Impact**: Registration, Login, Password Reset features
````

### Practice 6: Iterate and Refine

Analysis is never complete on first pass:

```
Draft 1: Initial understanding
↓
Feedback: Questions and clarifications
↓
Draft 2: Refined understanding
↓
Review: Technical feasibility check
↓
Draft 3: Final specification
↓
Implementation: Discover edge cases
↓
Refinement: Update specification
```

### Practice 7: Validate with Examples

Use concrete examples to clarify requirements:

```markdown
## Example Scenarios

**Scenario 1: Successful Registration**
```

Input:

- Email: john.doe@example.com
- Password: SecurePass123
- First Name: John
- Last Name: Doe

Expected Result:

- Account created
- User ID: generated UUID
- Welcome email sent to john.doe@example.com
- Response: 201 Created with user details

```

**Scenario 2: Duplicate Email**
```

Input:

- Email: existing@example.com (already registered)
- Password: AnotherPass456
- First Name: Jane
- Last Name: Smith

Expected Result:

- Account NOT created
- Response: 409 Conflict
- Error message: "An account with this email already exists"
- Suggestion: "Try logging in or reset your password"

```

```

## Summary

### Key Takeaways

1. **Start with Business Value**: Every feature must deliver tangible user value
2. **Extract Complete Rules**: Capture all constraints, calculations, and triggers
3. **Define Clear Boundaries**: Features should be independent and focused
4. **Slice Vertically**: Each slice spans all architectural layers
5. **Prioritize Ruthlessly**: Not everything needs to be built immediately
6. **Validate Continuously**: Get feedback from all stakeholders
7. **Document Thoroughly**: Clear documentation enables successful implementation

### Success Criteria

You've done this well if:

- ✅ Business stakeholders understand and approve features
- ✅ Developers can implement without constant clarification
- ✅ Features are independently deployable
- ✅ Each slice delivers measurable value
- ✅ Dependencies are minimal and well-managed
- ✅ Acceptance criteria are clear and testable
- ✅ Team can estimate effort confidently

### Next Steps

1. Review this guide with your team
2. Select a feature to analyze using these techniques
3. Walk through the process step-by-step
4. Gather feedback and refine approach
5. Establish this as your standard practice
6. Continuously improve based on experience

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Maintainer**: AI-Assisted Development Team
**Related Instructions**:

- `.github/instructions/vertical-slice-architecture.instructions.md`
- `.github/instructions/ai-vertical-slice-implementation.instructions.md`
- `.github/instructions/ai-business-rules-to-slices.instructions.md`
