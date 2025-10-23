---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "ai-vertical-slice-implementation-20251022"
prompt: |
  Create an instruction file to guide AI implementations using vertical slices -
  specifically for AI assistants when generating or refactoring code using
  vertical slice architecture patterns.
started: "2025-10-22T14:00:00Z"
ended: "2025-10-22T14:45:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:10:00"
  - task: "instruction file creation"
    duration: "00:30:00"
  - task: "review and refinement"
    duration: "00:05:00"
total_duration: "00:45:00"
ai_log: "ai-logs/2025/10/22/ai-vertical-slice-implementation-20251022/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{cs,ts,js,py,java,go,rb}"
---

# AI Assistant Instructions: Vertical Slice Implementation

## Overview

This document provides instructions for AI assistants (GitHub Copilot, ChatGPT, Claude, etc.) when implementing code using vertical slice architecture. These instructions ensure AI-generated code follows vertical slice principles consistently and correctly.

**Target Audience**: AI assistants generating or refactoring code
**Related Documentation**: See [`.github/instructions/vertical-slice-architecture.instructions.md`](.github/instructions/vertical-slice-architecture.instructions.md) for comprehensive architecture guidance

## Table of Contents

- [When to Apply These Instructions](#when-to-apply-these-instructions)
- [Pre-Implementation Analysis](#pre-implementation-analysis)
- [Feature Identification and Planning](#feature-identification-and-planning)
- [Code Generation Rules](#code-generation-rules)
- [File Structure and Naming](#file-structure-and-naming)
- [Implementation Order](#implementation-order)
- [Language-Specific Generation](#language-specific-generation)
- [Testing Generation](#testing-generation)
- [Validation and Quality Checks](#validation-and-quality-checks)
- [Common Generation Patterns](#common-generation-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Integration with Existing Code](#integration-with-existing-code)

## When to Apply These Instructions

Apply vertical slice architecture when:

1. **User explicitly requests it**: "Use vertical slices", "implement as a feature slice", "follow vertical slice architecture"
2. **New feature implementation**: User asks to add a complete feature (e.g., "add user registration")
3. **File patterns indicate it**: Existing codebase has `/Features` folder or feature-organized structure
4. **User references CQRS**: Commands/Queries, Handlers, MediatR patterns mentioned
5. **Refactoring layered code**: User wants to move from layered to feature-centric organization

**Do NOT apply when**:

- User explicitly requests layered architecture
- Working on simple scripts or utilities
- Adding to existing non-vertical-slice codebase without permission
- User asks for traditional MVC/three-tier architecture

## Pre-Implementation Analysis

Before generating any code, perform this analysis:

### 1. Identify the Feature Boundary

**Ask yourself (or clarify with user)**:

- What is the complete user capability being implemented?
- What is the smallest vertical slice that delivers value?
- Does this feature naturally group with an existing feature?

**Example Analysis**:

```
User Request: "Add ability for users to reset their password"

Feature Boundary Analysis:
✅ Good: "PasswordReset" feature
  - Includes: request reset, validate token, update password
  - Complete user capability

❌ Too Broad: "UserManagement"
  - Includes unrelated capabilities

❌ Too Narrow: "SendResetEmail"
  - Only part of the feature
```

### 2. Scan for Existing Structure

Check if the codebase already has:

- `/Features` or `/features` directory
- MediatR or mediator pattern usage
- CQRS-style commands/queries
- Existing vertical slices

**If found**: Follow the existing patterns exactly
**If not found**: Ask user: "Should I create this using vertical slice architecture?"

### 3. Identify Required Components

For each feature slice, determine what's needed:

- [ ] Command/Query object (always)
- [ ] Handler (always)
- [ ] Validator (if input validation needed)
- [ ] Result DTO (if response differs from domain model)
- [ ] Repository (if complex data access)
- [ ] Domain models (if new entities)
- [ ] API endpoint (if external entry point)
- [ ] Tests (always)

## Feature Identification and Planning

### Planning Template

Before generating code, present this plan to the user:

```markdown
## Implementation Plan: [Feature Name]

**Feature**: [Brief description]
**User Story**: As a [user], I want to [action] so that [benefit]

**Files to Create**:

1. `/Features/[FeatureName]/[Action]Command.cs` - Request object
2. `/Features/[FeatureName]/[Action]Handler.cs` - Business logic
3. `/Features/[FeatureName]/[Action]Validator.cs` - Input validation
4. `/Features/[FeatureName]/[Action]Result.cs` - Response DTO
5. `/Api/Controllers/[Feature]Controller.cs` - API endpoint (if needed)
6. `/Tests/Features/[FeatureName]/[Action]HandlerTests.cs` - Unit tests

**Dependencies**:

- Existing: [List existing services/repositories to be used]
- New: [List new dependencies to be created]

**Shared Code**:

- [Any shared interfaces or models needed]

Proceed? (y/n)
```

### Feature Naming Rules

**Feature Names** (folder names):

- PascalCase
- Singular noun or verb+noun
- Business capability focused
- Examples: `UserRegistration`, `ProductSearch`, `OrderCheckout`, `PasswordReset`

**Command/Query Names**:

- `[Verb][Entity]Command` for writes
- `[Verb][Entity]Query` for reads
- Examples: `RegisterUserCommand`, `GetUserProfileQuery`, `SearchProductsQuery`

**Handler Names**:

- `[Verb][Entity]Handler`
- Examples: `RegisterUserHandler`, `GetUserProfileHandler`

## Code Generation Rules

### Rule 1: Feature Independence

**CRITICAL**: Features must NOT directly reference other features.

```csharp
// ❌ NEVER DO THIS
using Features.UserManagement;

public class OrderCheckoutHandler
{
    private readonly UserService _userService; // Direct feature dependency
}

// ✅ ALWAYS DO THIS
using Common.Interfaces;

public class OrderCheckoutHandler
{
    private readonly IUserProvider _userProvider; // Shared interface
}
```

**Enforcement**:

- Check all `using` statements
- Flag any `using Features.[OtherFeature]`
- Suggest shared interface or domain event instead

### Rule 2: Complete Feature Encapsulation

Each feature slice must contain everything needed for that feature.

```
/Features/UserRegistration
  ✅ RegisterUserCommand.cs        - Request
  ✅ RegisterUserHandler.cs         - Logic
  ✅ RegisterUserValidator.cs       - Validation
  ✅ RegistrationResult.cs          - Response
  ✅ UserRegistrationRepository.cs  - Data access
  ❌ ../../Repositories/UserRepository.cs  - NO! Don't reference shared repos
```

### Rule 3: Thin Controllers/Endpoints

Controllers must ONLY:

- Receive HTTP request
- Map to Command/Query
- Send via mediator
- Return HTTP response

```csharp
// ✅ CORRECT: Thin controller
[ApiController]
[Route("api/users")]
public class UserRegistrationController : ControllerBase
{
    private readonly IMediator _mediator;

    [HttpPost("register")]
    public async Task<IActionResult> Register(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        var result = await _mediator.Send(command, cancellationToken);
        return result.IsSuccess ? Ok(result.Value) : BadRequest(result.Error);
    }
}

// ❌ WRONG: Business logic in controller
[HttpPost("register")]
public async Task<IActionResult> Register(RegisterRequest request)
{
    // Validation here - NO!
    if (string.IsNullOrEmpty(request.Email)) return BadRequest();

    // Database access here - NO!
    var user = await _dbContext.Users.FirstOrDefaultAsync(...);

    // Business logic here - NO!
    if (user != null) return Conflict();
}
```

### Rule 4: Handler Contains Business Logic

Handlers are the heart of vertical slices. They should:

- Orchestrate dependencies
- Implement business rules
- Handle errors
- Return results

```csharp
// ✅ CORRECT: Handler with business logic
public class RegisterUserHandler
    : IRequestHandler<RegisterUserCommand, Result<RegistrationResult>>
{
    private readonly IDbContext _dbContext;
    private readonly IPasswordHasher _passwordHasher;
    private readonly IEmailService _emailService;
    private readonly ILogger<RegisterUserHandler> _logger;

    public async Task<Result<RegistrationResult>> Handle(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        // 1. Business rule: Check if user exists
        var existingUser = await _dbContext.Users
            .FirstOrDefaultAsync(u => u.Email == command.Email, cancellationToken);

        if (existingUser != null)
            return Result<RegistrationResult>.Failure("User already exists");

        // 2. Business logic: Create user
        var user = new User
        {
            Id = Guid.NewGuid(),
            Email = command.Email,
            PasswordHash = _passwordHasher.Hash(command.Password),
            FirstName = command.FirstName,
            LastName = command.LastName,
            CreatedAt = DateTime.UtcNow
        };

        // 3. Persist
        _dbContext.Users.Add(user);
        await _dbContext.SaveChangesAsync(cancellationToken);

        // 4. Side effects
        await _emailService.SendWelcomeEmailAsync(user.Email, user.FirstName);

        // 5. Return result
        _logger.LogInformation("User {UserId} registered", user.Id);
        return Result<RegistrationResult>.Success(new RegistrationResult
        {
            UserId = user.Id,
            Email = user.Email
        });
    }
}
```

### Rule 5: Validation in Separate Validators

```csharp
// ✅ CORRECT: Separate validator
public class RegisterUserValidator : AbstractValidator<RegisterUserCommand>
{
    public RegisterUserValidator()
    {
        RuleFor(x => x.Email)
            .NotEmpty()
            .EmailAddress()
            .MaximumLength(255);

        RuleFor(x => x.Password)
            .NotEmpty()
            .MinimumLength(8)
            .Matches(@"[A-Z]").WithMessage("Must contain uppercase")
            .Matches(@"[a-z]").WithMessage("Must contain lowercase")
            .Matches(@"[0-9]").WithMessage("Must contain digit");

        RuleFor(x => x.FirstName)
            .NotEmpty()
            .MaximumLength(100);

        RuleFor(x => x.LastName)
            .NotEmpty()
            .MaximumLength(100);
    }
}

// ❌ WRONG: Validation in handler
public async Task<Result> Handle(RegisterUserCommand command)
{
    if (string.IsNullOrEmpty(command.Email)) // NO!
        return Result.Failure("Email is required");

    if (!IsValidEmail(command.Email)) // NO!
        return Result.Failure("Invalid email");
}
```

## File Structure and Naming

### Directory Structure Template

Generate files following this structure:

```
/src
  /Features
    /[FeatureName]
      - [Action]Command.cs or [Action]Query.cs
      - [Action]Handler.cs
      - [Action]Validator.cs
      - [Action]Result.cs
      - [Feature]Repository.cs (optional)
      - [Feature]Models.cs (optional)
      - [Feature]Extensions.cs (DI registration)
  /Common
    /Behaviors
    /Infrastructure
    /Primitives
    /Interfaces
  /Api
    /Controllers
  /Tests
    /Features
      /[FeatureName]
        - [Action]HandlerTests.cs
        - [Action]ValidatorTests.cs
```

### Naming Conventions Checklist

When generating files, ensure:

- [ ] Feature folder is PascalCase, singular
- [ ] Command/Query ends with `Command` or `Query`
- [ ] Handler ends with `Handler`
- [ ] Validator ends with `Validator`
- [ ] Result/DTO ends with `Result` or `Dto`
- [ ] Repository (if needed) ends with `Repository`
- [ ] Test file matches handler name + `Tests`

## Implementation Order

Generate files in this order:

### 1. Command/Query Object First

**Why**: Defines the contract and makes dependencies clear

```csharp
// Step 1: Generate this first
public record RegisterUserCommand(
    string Email,
    string Password,
    string FirstName,
    string LastName
) : IRequest<Result<RegistrationResult>>;
```

### 2. Result DTO Second

**Why**: Defines what the handler returns

```csharp
// Step 2: Generate this second
public record RegistrationResult
{
    public Guid UserId { get; init; }
    public string Email { get; init; }
    public DateTime RegisteredAt { get; init; }
}
```

### 3. Validator Third

**Why**: Defines validation rules before business logic

```csharp
// Step 3: Generate validator
public class RegisterUserValidator : AbstractValidator<RegisterUserCommand>
{
    // ... validation rules
}
```

### 4. Handler Fourth

**Why**: Now we know inputs, outputs, and validation

```csharp
// Step 4: Generate handler
public class RegisterUserHandler : IRequestHandler<RegisterUserCommand, Result<RegistrationResult>>
{
    // ... handler implementation
}
```

### 5. Controller/Endpoint Fifth

**Why**: Creates the entry point after core logic exists

```csharp
// Step 5: Generate controller
[ApiController]
[Route("api/users")]
public class UserRegistrationController : ControllerBase
{
    // ... thin controller
}
```

### 6. Tests Last

**Why**: Tests validate the completed implementation

```csharp
// Step 6: Generate tests
public class RegisterUserHandlerTests
{
    // ... test implementation
}
```

## Language-Specific Generation

### C# / .NET

**Required Packages**:

```xml
<PackageReference Include="MediatR" Version="12.0.0" />
<PackageReference Include="FluentValidation" Version="11.0.0" />
<PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.0" />
```

**Standard Patterns**:

- Use `record` for Commands/Queries/Results
- Use `IRequestHandler<TRequest, TResponse>`
- Use `AbstractValidator<T>` for validation
- Use `Result<T>` pattern for error handling
- Use async/await with `CancellationToken`

**Template**:

```csharp
// Command
public record [Action][Entity]Command(...) : IRequest<Result<[Action]Result>>;

// Handler
public class [Action][Entity]Handler
    : IRequestHandler<[Action][Entity]Command, Result<[Action]Result>>
{
    public async Task<Result<[Action]Result>> Handle(
        [Action][Entity]Command command,
        CancellationToken cancellationToken)
    {
        // Implementation
    }
}

// Validator
public class [Action][Entity]Validator : AbstractValidator<[Action][Entity]Command>
{
    public [Action][Entity]Validator()
    {
        // Rules
    }
}
```

### TypeScript / Node.js

**Required Packages**:

```json
{
  "dependencies": {
    "ts-mediator": "^1.0.0",
    "class-validator": "^0.14.0",
    "class-transformer": "^0.5.0"
  }
}
```

**Standard Patterns**:

- Use classes with decorators
- Use `IRequestHandler<TRequest, TResponse>`
- Use class-validator decorators
- Use async/await with proper error handling

**Template**:

```typescript
// Command
export class [Action][Entity]Command {
  constructor(
    public readonly email: string,
    public readonly password: string
  ) {}
}

// Handler
export class [Action][Entity]Handler
  implements IRequestHandler<[Action][Entity]Command, Result<[Action]Result>>
{
  async handle(command: [Action][Entity]Command): Promise<Result<[Action]Result>> {
    // Implementation
  }
}

// Validator (using class-validator)
export class [Action][Entity]Validator {
  @IsEmail()
  @IsNotEmpty()
  email: string;

  @IsString()
  @MinLength(8)
  password: string;
}
```

### Python

**Required Packages**:

```python
# requirements.txt
mediatr==1.0.0
pydantic==2.0.0
sqlalchemy==2.0.0
```

**Standard Patterns**:

- Use dataclasses or Pydantic models
- Use type hints throughout
- Use async/await
- Use Pydantic for validation

**Template**:

```python
# Command
from dataclasses import dataclass
from mediatr import Request

@dataclass
class [Action][Entity]Command(Request):
    email: str
    password: str
    first_name: str
    last_name: str

# Handler
from mediatr import RequestHandler

class [Action][Entity]Handler(RequestHandler[[Action][Entity]Command, Result]):
    async def handle(self, command: [Action][Entity]Command) -> Result:
        # Implementation
        pass

# Validator (using Pydantic)
from pydantic import BaseModel, EmailStr, constr

class [Action][Entity]Validator(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    first_name: str
    last_name: str
```

### Java / Spring Boot

**Required Dependencies**:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

**Standard Patterns**:

- Use records for Commands/Queries (Java 16+)
- Use `@Component` for handlers
- Use Bean Validation annotations
- Use Spring's dependency injection

**Template**:

```java
// Command
public record [Action][Entity]Command(
    @NotBlank @Email String email,
    @NotBlank @Size(min = 8) String password,
    @NotBlank String firstName,
    @NotBlank String lastName
) implements Command<Result<[Action]Result>> {}

// Handler
@Component
public class [Action][Entity]Handler
    implements CommandHandler<[Action][Entity]Command, Result<[Action]Result>> {

    @Override
    public Result<[Action]Result> handle([Action][Entity]Command command) {
        // Implementation
    }
}
```

## Testing Generation

### Test Generation Rules

When generating tests:

1. **Always generate tests with the feature**
2. **Test the handler, not the controller**
3. **Mock external dependencies**
4. **Test happy path and error cases**
5. **Use in-memory database for integration tests**

### Unit Test Template

```csharp
public class [Action][Entity]HandlerTests
{
    private readonly Mock<IDbContext> _dbContextMock;
    private readonly Mock<[Dependency]> _dependencyMock;
    private readonly [Action][Entity]Handler _handler;

    public [Action][Entity]HandlerTests()
    {
        _dbContextMock = new Mock<IDbContext>();
        _dependencyMock = new Mock<[Dependency]>();
        _handler = new [Action][Entity]Handler(
            _dbContextMock.Object,
            _dependencyMock.Object,
            Mock.Of<ILogger<[Action][Entity]Handler>>());
    }

    [Fact]
    public async Task Handle_ValidCommand_ReturnsSuccess()
    {
        // Arrange
        var command = new [Action][Entity]Command(/* test data */);

        _dbContextMock.Setup(/* setup mocks */);

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.True(result.IsSuccess);
        Assert.NotNull(result.Value);
        // More assertions
    }

    [Fact]
    public async Task Handle_[ErrorCondition]_ReturnsFailure()
    {
        // Arrange
        var command = new [Action][Entity]Command(/* test data */);

        _dbContextMock.Setup(/* setup error condition */);

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.False(result.IsSuccess);
        Assert.Contains("[expected error message]", result.Error);
    }
}
```

### Test Coverage Requirements

Generate tests for:

- [ ] Happy path (valid inputs → success)
- [ ] Invalid inputs (validation failures)
- [ ] Business rule violations (duplicate user, etc.)
- [ ] External service failures (database errors, etc.)
- [ ] Edge cases (empty collections, null handling)

## Validation and Quality Checks

### Pre-Generation Checklist

Before generating code, verify:

- [ ] Feature name follows naming conventions
- [ ] No naming conflicts with existing features
- [ ] All required dependencies are available
- [ ] Shared interfaces exist (or will be created)
- [ ] No circular dependencies

### Post-Generation Checklist

After generating all files, verify:

- [ ] No `using Features.[OtherFeature]` statements
- [ ] Handler contains business logic (not just pass-through)
- [ ] Controller is thin (only routing to mediator)
- [ ] Validator exists and is comprehensive
- [ ] Tests cover happy path and error cases
- [ ] All files follow naming conventions
- [ ] Result type is appropriate for the use case
- [ ] Cancellation tokens are used in async methods
- [ ] Logging is present for important events
- [ ] Error handling returns Result<T>, not exceptions

### Common Issues to Check

**Issue 1: Feature Dependencies**

```bash
# Check for feature dependencies
grep -r "using Features\." /Features/[YourFeature]/
```

Expected: No results (or only references to the same feature)

**Issue 2: Anemic Handlers**
Check handler line count:

- < 10 lines: Likely too thin (just pass-through)
- 10-100 lines: Good
- > 100 lines: Consider breaking up

**Issue 3: Missing Validation**
Every Command/Query should have a corresponding Validator.

**Issue 4: Missing Tests**
Every Handler should have a corresponding test file.

## Common Generation Patterns

### Pattern 1: Create New Entity

**User Request**: "Add ability to create products"

**Generation Plan**:

1. Feature: `ProductCreation`
2. Files:
   - `CreateProductCommand.cs`
   - `CreateProductHandler.cs`
   - `CreateProductValidator.cs`
   - `ProductCreationResult.cs`
   - `ProductCreationController.cs`
   - `CreateProductHandlerTests.cs`

**Key Decisions**:

- Use `CreateProduct` (not `AddProduct` or `InsertProduct`)
- Return created product ID and basic info
- Validate all required fields
- Check for duplicates (if applicable)

### Pattern 2: Retrieve Entity

**User Request**: "Get user profile by ID"

**Generation Plan**:

1. Feature: `UserProfile` (or add to existing feature)
2. Files:
   - `GetUserProfileQuery.cs`
   - `GetUserProfileHandler.cs`
   - `UserProfileDto.cs`
   - `GetUserProfileHandlerTests.cs`

**Key Decisions**:

- Use Query (not Command) - it's a read
- No validator needed (just ID)
- Return DTO, not domain entity
- Handle "not found" gracefully

### Pattern 3: Update Entity

**User Request**: "Allow users to update their profile"

**Generation Plan**:

1. Feature: `ProfileUpdate`
2. Files:
   - `UpdateProfileCommand.cs`
   - `UpdateProfileHandler.cs`
   - `UpdateProfileValidator.cs`
   - `UpdateProfileResult.cs`
   - `UpdateProfileHandlerTests.cs`

**Key Decisions**:

- Include only updatable fields in command
- Validate authorization (user can only update own profile)
- Check if entity exists before updating
- Consider optimistic concurrency

### Pattern 4: Delete Entity

**User Request**: "Delete user account"

**Generation Plan**:

1. Feature: `AccountDeletion`
2. Files:
   - `DeleteAccountCommand.cs`
   - `DeleteAccountHandler.cs`
   - `DeleteAccountValidator.cs` (optional)
   - `DeleteAccountResult.cs`
   - `DeleteAccountHandlerTests.cs`

**Key Decisions**:

- Consider soft delete vs hard delete
- Validate authorization
- Handle cascading deletes or orphaned data
- Return confirmation or deleted entity info

### Pattern 5: Search/List Entities

**User Request**: "Search products by keyword"

**Generation Plan**:

1. Feature: `ProductSearch`
2. Files:
   - `SearchProductsQuery.cs`
   - `SearchProductsHandler.cs`
   - `SearchProductsValidator.cs` (optional)
   - `ProductSearchResult.cs`
   - `SearchProductsHandlerTests.cs`

**Key Decisions**:

- Use Query (it's a read)
- Support pagination (page, pageSize)
- Return collection with metadata (total count, etc.)
- Consider caching for performance

## Anti-Patterns to Avoid

### Anti-Pattern 1: God Handler

**Problem**: Handler doing too many things

```csharp
// ❌ AVOID: 300+ line handler
public class ProcessOrderHandler
{
    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        // 50 lines of validation
        // 100 lines of business logic
        // 50 lines of database operations
        // 100 lines of email/notifications
        // Total: 300+ lines
    }
}
```

**Solution**: Break into smaller handlers or extract services

```csharp
// ✅ BETTER: Focused handler
public class ProcessOrderHandler
{
    private readonly IPaymentService _paymentService;
    private readonly IInventoryService _inventoryService;
    private readonly IOrderRepository _orderRepository;
    private readonly IPublisher _publisher;

    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        var payment = await _paymentService.ProcessAsync(command.Payment);
        if (!payment.IsSuccess) return payment;

        var inventory = await _inventoryService.ReserveAsync(command.Items);
        if (!inventory.IsSuccess) return inventory;

        var order = await _orderRepository.CreateAsync(command);

        await _publisher.Publish(new OrderCreatedEvent(order.Id));

        return Result.Success(order);
    }
}
```

### Anti-Pattern 2: Shared Repository

**Problem**: Generic repository shared across all features

```csharp
// ❌ AVOID: Generic repository
public interface IRepository<T>
{
    Task<T> GetByIdAsync(Guid id);
    Task<List<T>> GetAllAsync();
    Task AddAsync(T entity);
    Task UpdateAsync(T entity);
    Task DeleteAsync(Guid id);
}

public class OrderHandler
{
    private readonly IRepository<Order> _orderRepo; // Shared across all features
}
```

**Solution**: Feature-specific repository

```csharp
// ✅ BETTER: Feature-specific repository
public class OrderCreationRepository
{
    private readonly IDbContext _dbContext;

    public async Task<Order> CreateOrderAsync(Order order)
    {
        _dbContext.Orders.Add(order);
        await _dbContext.SaveChangesAsync();
        return order;
    }

    public async Task<bool> IsInventoryAvailableAsync(List<OrderItem> items)
    {
        // Feature-specific query
    }
}
```

### Anti-Pattern 3: Feature Dependencies

**Problem**: One feature depending on another feature

```csharp
// ❌ AVOID: Direct feature dependency
using Features.UserManagement;

public class OrderHandler
{
    private readonly UserService _userService; // From another feature!
}
```

**Solution**: Shared interface or domain events

```csharp
// ✅ BETTER: Shared interface
using Common.Interfaces;

public class OrderHandler
{
    private readonly IUserProvider _userProvider; // Shared interface
}

// Or use domain events
public class OrderHandler
{
    private readonly IPublisher _publisher;

    public async Task Handle(CreateOrderCommand command)
    {
        // ... create order ...

        await _publisher.Publish(new OrderCreatedEvent(order.Id));
    }
}
```

### Anti-Pattern 4: Anemic Handler

**Problem**: Handler with no logic, just pass-through

```csharp
// ❌ AVOID: No value added
public class GetUserHandler
{
    private readonly IUserService _userService;

    public async Task<User> Handle(GetUserQuery query)
    {
        return await _userService.GetUserAsync(query.Id); // Just forwarding!
    }
}
```

**Solution**: Either add logic or access data directly

```csharp
// ✅ BETTER: Handler with logic
public class GetUserHandler
{
    private readonly IDbContext _dbContext;

    public async Task<UserDto> Handle(GetUserQuery query)
    {
        var user = await _dbContext.Users
            .Include(u => u.Profile)
            .Include(u => u.Orders)
            .FirstOrDefaultAsync(u => u.Id == query.Id);

        if (user == null)
            return null;

        // Map to DTO
        return new UserDto
        {
            Id = user.Id,
            FullName = $"{user.FirstName} {user.LastName}",
            Email = user.Email,
            OrderCount = user.Orders.Count
        };
    }
}
```

### Anti-Pattern 5: Business Logic in Controller

**Problem**: Controller contains business logic

```csharp
// ❌ AVOID: Logic in controller
[HttpPost("register")]
public async Task<IActionResult> Register(RegisterRequest request)
{
    // Validation in controller - NO!
    if (string.IsNullOrEmpty(request.Email))
        return BadRequest("Email required");

    // Database access in controller - NO!
    var existing = await _dbContext.Users
        .FirstOrDefaultAsync(u => u.Email == request.Email);

    // Business logic in controller - NO!
    if (existing != null)
        return Conflict("User exists");

    var user = new User { /* ... */ };
    _dbContext.Users.Add(user);
    await _dbContext.SaveChangesAsync();

    return Ok(user);
}
```

**Solution**: Move everything to handler

```csharp
// ✅ BETTER: Thin controller
[HttpPost("register")]
public async Task<IActionResult> Register(
    RegisterUserCommand command,
    CancellationToken cancellationToken)
{
    var result = await _mediator.Send(command, cancellationToken);
    return result.IsSuccess ? Ok(result.Value) : BadRequest(result.Error);
}
```

## Integration with Existing Code

### Scenario 1: Adding to Existing Vertical Slice Codebase

**Steps**:

1. Analyze existing feature structure
2. Follow exact same patterns
3. Use existing shared interfaces
4. Match naming conventions
5. Add tests in same style

**Example**:

```
Existing: /Features/UserRegistration/RegisterUserCommand.cs
New:      /Features/UserAuthentication/AuthenticateUserCommand.cs
          (follow same pattern)
```

### Scenario 2: Adding Vertical Slice to Layered Codebase

**Steps**:

1. Ask user for permission to introduce vertical slices
2. Create `/Features` folder
3. Add new feature as vertical slice
4. Keep existing layered code unchanged
5. Document coexistence pattern

**Example Structure**:

```
/src
  /Features (NEW)
    /ProductSearch
  /Controllers (OLD)
    /OrderController.cs
  /Services (OLD)
    /OrderService.cs
```

### Scenario 3: Migrating Layered Code to Vertical Slices

**Steps**:

1. Identify feature to migrate
2. Create feature folder
3. Move/refactor code into feature
4. Update namespaces
5. Update DI registrations
6. Run tests
7. Remove old code

**Migration Checklist**:

- [ ] Feature folder created
- [ ] Command/Query created from request DTO
- [ ] Handler created from service method
- [ ] Validator moved or created
- [ ] Repository made feature-specific
- [ ] Controller updated to use mediator
- [ ] Tests updated
- [ ] Old code removed
- [ ] DI registrations updated

## Summary for AI Assistants

**When generating vertical slice code**:

1. ✅ **DO**:

   - Organize by feature, not layer
   - Create complete, independent slices
   - Keep handlers focused (10-100 lines)
   - Use separate validators
   - Generate comprehensive tests
   - Follow language-specific patterns
   - Keep controllers thin
   - Use Result<T> for error handling

2. ❌ **DON'T**:

   - Create dependencies between features
   - Put business logic in controllers
   - Create god handlers (300+ lines)
   - Use generic shared repositories
   - Skip validation
   - Skip tests
   - Mix features together

3. 🤔 **VERIFY**:

   - No `using Features.[OtherFeature]`
   - Handler has business logic
   - Validator exists
   - Tests cover main scenarios
   - Naming follows conventions
   - Files in correct structure

4. 💬 **COMMUNICATE**:
   - Present implementation plan before coding
   - Ask about existing patterns
   - Suggest improvements to existing code
   - Explain tradeoffs when relevant

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Maintainer**: AI-Assisted Development Team
**Related Instructions**:

- `.github/instructions/vertical-slice-architecture.instructions.md` - Comprehensive architecture guide
- `.github/instructions/ai-assisted-output.instructions.md` - AI provenance requirements
- `.github/instructions/copilot-instructions.md` - Copilot-specific guidance
