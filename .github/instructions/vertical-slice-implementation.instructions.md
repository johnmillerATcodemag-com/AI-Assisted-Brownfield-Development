---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "vertical-slice-instructions-20251022"
prompt: |
  Create an instruction file to guide implementations using vertical slices in software development.
started: "2025-10-22T10:00:00Z"
ended: "2025-10-22T10:45:00Z"
task_durations:
  - task: "requirements analysis"
    duration: "00:10:00"
  - task: "instruction file creation"
    duration: "00:30:00"
  - task: "review and refinement"
    duration: "00:05:00"
total_duration: "00:45:00"
ai_log: "ai-logs/2025/10/22/vertical-slice-instructions-20251022/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "**/*.{cs,ts,js,py,java,go,rb}"
---

# Vertical Slice Architecture Instructions

## Overview

This document provides comprehensive guidance for implementing vertical slice architecture in software development. Vertical slice architecture organizes code by feature rather than by technical layer, enabling teams to deliver complete functionality independently and reduce coupling between features.

**Scope**: Apply these instructions when designing, implementing, or refactoring applications using vertical slice architecture principles.

## Table of Contents

- [Core Principles](#core-principles)
- [Architecture Overview](#architecture-overview)
- [Implementation Guidelines](#implementation-guidelines)
- [Feature Organization](#feature-organization)
- [Code Structure](#code-structure)
- [Dependencies and Coupling](#dependencies-and-coupling)
- [Testing Strategy](#testing-strategy)
- [Common Patterns](#common-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Migration Strategy](#migration-strategy)
- [Technology-Specific Guidance](#technology-specific-guidance)
- [Quality Checklist](#quality-checklist)

## Core Principles

### 1. Feature-Centric Organization

**Principle**: Organize code by business feature or use case, not by technical layer.

✅ **Correct Structure**:

```
/Features
  /UserRegistration
    - RegisterUserCommand.cs
    - RegisterUserHandler.cs
    - RegisterUserValidator.cs
    - UserRegistrationRepository.cs
    - RegistrationDto.cs
  /ProductSearch
    - SearchProductsQuery.cs
    - SearchProductsHandler.cs
    - ProductSearchResult.cs
```

❌ **Incorrect Structure** (Traditional Layered):

```
/Controllers
  - UserController.cs
  - ProductController.cs
/Services
  - UserService.cs
  - ProductService.cs
/Repositories
  - UserRepository.cs
  - ProductRepository.cs
```

**Rationale**: Feature-centric organization keeps related code together, making it easier to understand, modify, and test complete features.

### 2. Vertical Independence

**Principle**: Each slice should be independently deployable, testable, and understandable.

**Requirements**:

- Minimize dependencies between slices
- Each slice contains all code needed for its feature
- Shared code only when absolutely necessary
- Clear boundaries between features
- No feature should know about another feature's internals

**Benefits**:

- Parallel development by multiple team members
- Easier to understand feature scope
- Reduced merge conflicts
- Simplified testing

### 3. Thin Shared Kernel

**Principle**: Keep shared code minimal and focused on true cross-cutting concerns.

**Allowed in Shared Kernel**:

- Infrastructure abstractions (logging, caching, database context)
- Common domain primitives (Value Objects, base entities)
- Cross-cutting behaviors (validation, authorization, error handling)
- Shared utilities (date/time helpers, formatters)
- Configuration models
- Common interfaces

**Not Allowed in Shared Kernel**:

- Feature-specific business logic
- Feature-specific data models (unless genuinely shared)
- Feature-specific validation rules
- Feature-specific repositories or services

**Warning**: Every addition to the shared kernel increases coupling. Always ask: "Do multiple features truly need this, or can it live in one feature?"

## Architecture Overview

### High-Level Structure

```
/src
  /Features                    # All feature slices
    /UserRegistration
    /UserAuthentication
    /ProductCatalog
    /OrderProcessing
  /Common                      # Thin shared kernel
    /Behaviors                 # Cross-cutting behaviors
    /Infrastructure            # Infrastructure abstractions
    /Primitives               # Domain primitives
    /Exceptions               # Common exception types
  /Api                        # Entry point (Web API, GraphQL, etc.)
  /Database                   # Database configuration & migrations
  /Tests
    /Features                 # Feature-specific tests
    /Integration             # Integration tests
```

### Request Flow

```
1. API Endpoint receives HTTP request
   ↓
2. Request mapped to Command/Query object
   ↓
3. Mediator/Router dispatches to Handler
   ↓
4. Handler executes feature logic
   ↓  (may access database, call external services, etc.)
5. Result/Response returned to caller
   ↓
6. API maps result to HTTP response
```

## Implementation Guidelines

### 1. Feature Slice Structure

Each feature slice should follow a consistent structure:

```
/Features/[FeatureName]
  - [Action]Command.cs        # Command/Query object (request)
  - [Action]Handler.cs        # Business logic handler
  - [Action]Validator.cs      # Input validation
  - [Action]Result.cs         # Response DTO
  - [Feature]Repository.cs    # Data access (if needed)
  - [Feature]Models.cs        # Feature-specific models
  - [Feature]Mapper.cs        # Mapping logic (if complex)
  - [Feature]Extensions.cs    # DI registration
```

**Example - User Registration Feature**:

```
/Features/UserRegistration
  - RegisterUserCommand.cs
  - RegisterUserHandler.cs
  - RegisterUserValidator.cs
  - RegistrationResult.cs
  - UserRegistrationRepository.cs
  - RegistrationModels.cs
  - UserRegistrationExtensions.cs
```

### 2. Command/Query Objects (Request Objects)

**Pattern**: Use CQRS-style commands and queries as feature requests.

**Command Example** (modifies state):

```csharp
public record RegisterUserCommand(
    string Email,
    string Password,
    string FirstName,
    string LastName
) : IRequest<Result<RegistrationResult>>;
```

**Query Example** (reads state):

```csharp
public record GetUserProfileQuery(
    Guid UserId
) : IRequest<Result<UserProfileDto>>;
```

**Rules**:

- Use immutable records or classes
- Include all data required for the operation
- Name clearly: `[Verb][Entity][Command|Query]`
- No business logic in command/query objects
- Validate in separate validator class
- Return `Result<T>` or similar wrapper for error handling

**Naming Conventions**:

- Commands: `CreateX`, `UpdateX`, `DeleteX`, `ProcessX`
- Queries: `GetX`, `ListX`, `SearchX`, `FindX`

### 3. Handler Implementation

**Pattern**: One handler per command/query containing complete feature logic.

```csharp
public class RegisterUserHandler
    : IRequestHandler<RegisterUserCommand, Result<RegistrationResult>>
{
    private readonly IDbContext _dbContext;
    private readonly IPasswordHasher _passwordHasher;
    private readonly IEmailService _emailService;
    private readonly ILogger<RegisterUserHandler> _logger;

    public RegisterUserHandler(
        IDbContext dbContext,
        IPasswordHasher passwordHasher,
        IEmailService emailService,
        ILogger<RegisterUserHandler> logger)
    {
        _dbContext = dbContext;
        _passwordHasher = passwordHasher;
        _emailService = emailService;
        _logger = logger;
    }

    public async Task<Result<RegistrationResult>> Handle(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        // 1. Check if user already exists
        var existingUser = await _dbContext.Users
            .FirstOrDefaultAsync(u => u.Email == command.Email, cancellationToken);

        if (existingUser != null)
            return Result<RegistrationResult>.Failure("User already exists");

        // 2. Create user entity
        var user = new User
        {
            Id = Guid.NewGuid(),
            Email = command.Email,
            PasswordHash = _passwordHasher.Hash(command.Password),
            FirstName = command.FirstName,
            LastName = command.LastName,
            CreatedAt = DateTime.UtcNow
        };

        // 3. Save to database
        _dbContext.Users.Add(user);
        await _dbContext.SaveChangesAsync(cancellationToken);

        // 4. Send welcome email (fire and forget or queue)
        await _emailService.SendWelcomeEmailAsync(user.Email, user.FirstName);

        // 5. Log success
        _logger.LogInformation("User {UserId} registered successfully", user.Id);

        // 6. Return result
        return Result<RegistrationResult>.Success(new RegistrationResult
        {
            UserId = user.Id,
            Email = user.Email
        });
    }
}
```

**Handler Rules**:

- One handler per command/query
- Contains complete feature logic
- Orchestrates dependencies (repositories, services, etc.)
- Returns strongly-typed results
- Handles errors gracefully
- Logs important events
- Uses cancellation tokens
- Keeps handlers focused (< 100 lines if possible)

### 4. Validation

**Pattern**: Use separate validator classes for input validation.

**Using FluentValidation** (recommended):

```csharp
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
            .Matches(@"[A-Z]").WithMessage("Password must contain uppercase letter")
            .Matches(@"[a-z]").WithMessage("Password must contain lowercase letter")
            .Matches(@"[0-9]").WithMessage("Password must contain digit");

        RuleFor(x => x.FirstName)
            .NotEmpty()
            .MaximumLength(100);

        RuleFor(x => x.LastName)
            .NotEmpty()
            .MaximumLength(100);
    }
}
```

**Validation Pipeline** (MediatR behavior):

```csharp
public class ValidationBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    public ValidationBehavior(IEnumerable<IValidator<TRequest>> validators)
    {
        _validators = validators;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        if (!_validators.Any())
            return await next();

        var context = new ValidationContext<TRequest>(request);

        var validationResults = await Task.WhenAll(
            _validators.Select(v => v.ValidateAsync(context, cancellationToken)));

        var failures = validationResults
            .SelectMany(r => r.Errors)
            .Where(f => f != null)
            .ToList();

        if (failures.Any())
            throw new ValidationException(failures);

        return await next();
    }
}
```

### 5. Data Access

**Pattern**: Feature-specific repositories or direct DbContext usage.

**Option 1: Feature-Specific Repository**:

```csharp
public class UserRegistrationRepository
{
    private readonly IDbContext _dbContext;

    public UserRegistrationRepository(IDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public async Task<User?> FindByEmailAsync(string email, CancellationToken ct)
    {
        return await _dbContext.Users
            .FirstOrDefaultAsync(u => u.Email == email, ct);
    }

    public async Task<User> CreateUserAsync(User user, CancellationToken ct)
    {
        _dbContext.Users.Add(user);
        await _dbContext.SaveChangesAsync(ct);
        return user;
    }
}
```

**Option 2: Direct DbContext Access** (simpler, less abstraction):

```csharp
public class RegisterUserHandler : IRequestHandler<RegisterUserCommand, Result>
{
    private readonly ApplicationDbContext _dbContext;

    public async Task<Result> Handle(RegisterUserCommand command, CancellationToken ct)
    {
        var user = await _dbContext.Users
            .FirstOrDefaultAsync(u => u.Email == command.Email, ct);

        // ... rest of handler logic
    }
}
```

**Guidelines**:

- Use repositories when data access is complex or repeated
- Use direct DbContext for simple CRUD operations
- Keep repositories feature-specific (no generic repositories)
- Consider read vs. write optimizations (CQRS)

### 6. API Endpoints

**Pattern**: Thin controllers that delegate to handlers via mediator.

```csharp
[ApiController]
[Route("api/users")]
public class UserRegistrationController : ControllerBase
{
    private readonly IMediator _mediator;

    public UserRegistrationController(IMediator mediator)
    {
        _mediator = mediator;
    }

    [HttpPost("register")]
    [ProducesResponseType(typeof(RegistrationResult), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<IActionResult> Register(
        [FromBody] RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        var result = await _mediator.Send(command, cancellationToken);

        return result.IsSuccess
            ? Ok(result.Value)
            : BadRequest(result.Error);
    }
}
```

**Minimal API Example** (.NET 6+):

```csharp
app.MapPost("/api/users/register", async (
    RegisterUserCommand command,
    IMediator mediator,
    CancellationToken cancellationToken) =>
{
    var result = await mediator.Send(command, cancellationToken);
    return result.IsSuccess
        ? Results.Ok(result.Value)
        : Results.BadRequest(result.Error);
});
```

## Feature Organization

### Identifying Feature Boundaries

**Good Feature Boundaries** (high cohesion):

- User Registration
- User Authentication
- Password Reset
- Product Search
- Shopping Cart Management
- Order Checkout
- Payment Processing

**Poor Feature Boundaries** (too granular or too broad):

- ❌ "User Management" (too broad - split into multiple features)
- ❌ "Get User By Id" (too granular - part of larger feature)
- ❌ "Database Access" (technical layer, not feature)

**Guidelines**:

1. **Follow User Stories**: Each feature should map to a user story or use case
2. **Consider Change Patterns**: Things that change together should live together
3. **Think in Capabilities**: What capability does this provide to users?
4. **Avoid Technical Boundaries**: Don't organize by "controllers" or "services"

### Feature Dependencies

**Rule**: Features should not depend on other features directly.

**Bad Example**:

```csharp
// In OrderCheckout feature
using Features.ShoppingCart; // ❌ Direct feature dependency

public class CheckoutHandler
{
    private readonly ShoppingCartService _cartService; // ❌ Depends on another feature
}
```

**Good Example**:

```csharp
// In OrderCheckout feature
using Common.Interfaces; // ✅ Depend on shared interface

public class CheckoutHandler
{
    private readonly ICartProvider _cartProvider; // ✅ Depends on abstraction
}

// Shopping cart feature implements the interface
public class CartProvider : ICartProvider { }
```

### Shared Code Management

**When to Share Code**:

1. **Infrastructure**: Database context, logging, caching
2. **Domain Primitives**: Value objects (Email, Money, etc.)
3. **Cross-Cutting Behaviors**: Validation, authorization, error handling
4. **Common DTOs**: Only if genuinely used by multiple features

**When NOT to Share Code**:

1. **Feature-Specific Logic**: Keep in the feature
2. **Premature Abstraction**: Wait until 3+ features need it
3. **Convenience Sharing**: Resist "it might be useful"

**Refactoring to Shared**:

```
1. Identify truly duplicated code across 3+ features
2. Extract to /Common with clear purpose
3. Update features to use shared code
4. Document why it's shared
```

## Code Structure

### Directory Layout Examples

**Small to Medium Application**:

```
/src
  /Features
    /UserRegistration
    /UserAuthentication
    /ProductCatalog
    /OrderManagement
  /Common
    /Behaviors
    /Infrastructure
    /Primitives
  /Api
  /Database
```

**Large Application with Modules**:

```
/src
  /Modules
    /Identity
      /Features
        /UserRegistration
        /UserAuthentication
      /Common
    /Catalog
      /Features
        /ProductManagement
        /CategoryManagement
      /Common
    /Orders
      /Features
        /OrderCheckout
        /OrderTracking
      /Common
  /Common (Global shared kernel)
  /Api
```

### File Naming Conventions

**Commands/Queries**:

- `[Verb][Entity]Command.cs` - e.g., `CreateProductCommand.cs`
- `[Verb][Entity]Query.cs` - e.g., `GetProductQuery.cs`

**Handlers**:

- `[Verb][Entity]Handler.cs` - e.g., `CreateProductHandler.cs`

**Validators**:

- `[Verb][Entity]Validator.cs` - e.g., `CreateProductValidator.cs`

**Results/DTOs**:

- `[Entity]Result.cs` or `[Entity]Dto.cs`

**Repositories**:

- `[Feature]Repository.cs` - e.g., `ProductCatalogRepository.cs`

## Dependencies and Coupling

### Dependency Injection Setup

**Feature Registration Pattern**:

```csharp
// In Features/UserRegistration/UserRegistrationExtensions.cs
public static class UserRegistrationExtensions
{
    public static IServiceCollection AddUserRegistration(
        this IServiceCollection services)
    {
        // Register handlers (usually auto-registered via MediatR)
        services.AddTransient<RegisterUserHandler>();

        // Register feature-specific dependencies
        services.AddScoped<UserRegistrationRepository>();
        services.AddScoped<IPasswordHasher, PasswordHasher>();

        // Register validators
        services.AddTransient<IValidator<RegisterUserCommand>,
            RegisterUserValidator>();

        return services;
    }
}

// In Program.cs or Startup.cs
builder.Services.AddUserRegistration();
```

**Auto-Registration with MediatR**:

```csharp
builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(Program).Assembly));
```

### Managing Cross-Feature Communication

**Problem**: Feature A needs data from Feature B.

**Solutions**:

**1. Shared Read Models** (CQRS approach):

```csharp
// Common/ReadModels/UserSummary.cs
public record UserSummary(Guid UserId, string Email, string FullName);

// Both features can query this read model
```

**2. Domain Events** (eventual consistency):

```csharp
// Common/Events/UserRegisteredEvent.cs
public record UserRegisteredEvent(Guid UserId, string Email, DateTime RegisteredAt);

// Feature A publishes event
await _publisher.PublishAsync(new UserRegisteredEvent(...));

// Feature B handles event
public class SendWelcomeEmailHandler : INotificationHandler<UserRegisteredEvent>
{
    public async Task Handle(UserRegisteredEvent notification, CancellationToken ct)
    {
        // Send welcome email
    }
}
```

**3. Mediator Queries** (synchronous, use sparingly):

```csharp
// Feature A needs user info from Feature B
var userProfile = await _mediator.Send(new GetUserProfileQuery(userId));
```

**4. Shared Interface** (best for external dependencies):

```csharp
// Common/Interfaces/IUserProvider.cs
public interface IUserProvider
{
    Task<UserInfo> GetUserAsync(Guid userId);
}

// Identity feature implements
public class UserProvider : IUserProvider { }

// Other features depend on interface
```

## Testing Strategy

### Unit Testing Handlers

```csharp
public class RegisterUserHandlerTests
{
    private readonly Mock<IDbContext> _dbContextMock;
    private readonly Mock<IPasswordHasher> _passwordHasherMock;
    private readonly Mock<IEmailService> _emailServiceMock;
    private readonly RegisterUserHandler _handler;

    public RegisterUserHandlerTests()
    {
        _dbContextMock = new Mock<IDbContext>();
        _passwordHasherMock = new Mock<IPasswordHasher>();
        _emailServiceMock = new Mock<IEmailService>();
        _handler = new RegisterUserHandler(
            _dbContextMock.Object,
            _passwordHasherMock.Object,
            _emailServiceMock.Object,
            Mock.Of<ILogger<RegisterUserHandler>>());
    }

    [Fact]
    public async Task Handle_ValidCommand_ReturnsSuccess()
    {
        // Arrange
        var command = new RegisterUserCommand(
            "test@example.com",
            "Password123!",
            "John",
            "Doe");

        _dbContextMock.Setup(x => x.Users.FirstOrDefaultAsync(
            It.IsAny<Expression<Func<User, bool>>>(),
            It.IsAny<CancellationToken>()))
            .ReturnsAsync((User?)null);

        _passwordHasherMock.Setup(x => x.Hash(It.IsAny<string>()))
            .Returns("hashed_password");

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.True(result.IsSuccess);
        Assert.NotNull(result.Value);
        Assert.Equal(command.Email, result.Value.Email);

        _dbContextMock.Verify(x => x.Users.Add(It.IsAny<User>()), Times.Once);
        _dbContextMock.Verify(x => x.SaveChangesAsync(It.IsAny<CancellationToken>()),
            Times.Once);
    }

    [Fact]
    public async Task Handle_UserAlreadyExists_ReturnsFailure()
    {
        // Arrange
        var command = new RegisterUserCommand(
            "existing@example.com",
            "Password123!",
            "John",
            "Doe");

        var existingUser = new User { Email = command.Email };
        _dbContextMock.Setup(x => x.Users.FirstOrDefaultAsync(
            It.IsAny<Expression<Func<User, bool>>>(),
            It.IsAny<CancellationToken>()))
            .ReturnsAsync(existingUser);

        // Act
        var result = await _handler.Handle(command, CancellationToken.None);

        // Assert
        Assert.False(result.IsSuccess);
        Assert.Contains("already exists", result.Error);
    }
}
```

### Integration Testing

```csharp
[Collection("Database")]
public class UserRegistrationIntegrationTests : IAsyncLifetime
{
    private readonly WebApplicationFactory<Program> _factory;
    private readonly HttpClient _client;

    public UserRegistrationIntegrationTests()
    {
        _factory = new WebApplicationFactory<Program>()
            .WithWebHostBuilder(builder =>
            {
                builder.ConfigureServices(services =>
                {
                    // Use test database
                    services.AddDbContext<ApplicationDbContext>(options =>
                        options.UseInMemoryDatabase("TestDb"));
                });
            });
        _client = _factory.CreateClient();
    }

    [Fact]
    public async Task RegisterUser_ValidData_ReturnsSuccess()
    {
        // Arrange
        var command = new RegisterUserCommand(
            "newuser@example.com",
            "Password123!",
            "John",
            "Doe");

        // Act
        var response = await _client.PostAsJsonAsync(
            "/api/users/register",
            command);

        // Assert
        response.EnsureSuccessStatusCode();
        var result = await response.Content.ReadFromJsonAsync<RegistrationResult>();
        Assert.NotNull(result);
        Assert.Equal(command.Email, result.Email);
    }

    public Task InitializeAsync() => Task.CompletedTask;

    public async Task DisposeAsync()
    {
        await _factory.DisposeAsync();
    }
}
```

### Testing Checklist

- [ ] Unit tests for each handler
- [ ] Validation tests for validators
- [ ] Integration tests for complete feature flows
- [ ] Test happy path scenarios
- [ ] Test error scenarios
- [ ] Test edge cases
- [ ] Mock external dependencies
- [ ] Use in-memory database for integration tests
- [ ] Test authorization/authentication if applicable

## Common Patterns

### Result Pattern (Error Handling)

```csharp
public class Result<T>
{
    public bool IsSuccess { get; }
    public T Value { get; }
    public string Error { get; }

    private Result(bool isSuccess, T value, string error)
    {
        IsSuccess = isSuccess;
        Value = value;
        Error = error;
    }

    public static Result<T> Success(T value) =>
        new(true, value, string.Empty);

    public static Result<T> Failure(string error) =>
        new(false, default!, error);
}
```

### Pipeline Behaviors (Cross-Cutting Concerns)

```csharp
// Logging behavior
public class LoggingBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
{
    private readonly ILogger<LoggingBehavior<TRequest, TResponse>> _logger;

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        _logger.LogInformation("Handling {RequestName}", typeof(TRequest).Name);
        var response = await next();
        _logger.LogInformation("Handled {RequestName}", typeof(TRequest).Name);
        return response;
    }
}

// Performance behavior
public class PerformanceBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
{
    private readonly ILogger<PerformanceBehavior<TRequest, TResponse>> _logger;
    private readonly Stopwatch _timer;

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        _timer.Start();
        var response = await next();
        _timer.Stop();

        var elapsedMilliseconds = _timer.ElapsedMilliseconds;
        if (elapsedMilliseconds > 500)
        {
            _logger.LogWarning(
                "Long Running Request: {RequestName} ({ElapsedMilliseconds}ms)",
                typeof(TRequest).Name,
                elapsedMilliseconds);
        }

        return response;
    }
}
```

### Domain Events

```csharp
// Event definition
public record UserRegisteredEvent(
    Guid UserId,
    string Email,
    DateTime RegisteredAt) : INotification;

// Publishing in handler
public class RegisterUserHandler
{
    private readonly IPublisher _publisher;

    public async Task<Result> Handle(RegisterUserCommand command, CancellationToken ct)
    {
        // ... create user ...

        await _publisher.Publish(
            new UserRegisteredEvent(user.Id, user.Email, DateTime.UtcNow),
            ct);

        return Result.Success();
    }
}

// Event handler in another feature
public class SendWelcomeEmailHandler
    : INotificationHandler<UserRegisteredEvent>
{
    private readonly IEmailService _emailService;

    public async Task Handle(
        UserRegisteredEvent notification,
        CancellationToken cancellationToken)
    {
        await _emailService.SendWelcomeEmailAsync(
            notification.Email,
            cancellationToken);
    }
}
```

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: God Handlers

**Problem**: Handler doing too much, becoming difficult to test and maintain.

```csharp
// BAD: 500+ line handler doing everything
public class ProcessOrderHandler
{
    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        // Validate payment
        // Check inventory
        // Create order
        // Update inventory
        // Send confirmation email
        // Update analytics
        // Generate invoice
        // Notify warehouse
        // Update customer points
        // ... 400 more lines
    }
}
```

**Solution**: Break into smaller handlers or extract logic into services.

```csharp
// GOOD: Focused handler orchestrating services
public class ProcessOrderHandler
{
    private readonly IPaymentService _paymentService;
    private readonly IInventoryService _inventoryService;
    private readonly IOrderRepository _orderRepository;

    public async Task<Result> Handle(ProcessOrderCommand command)
    {
        var paymentResult = await _paymentService.ProcessPaymentAsync(command.Payment);
        if (!paymentResult.IsSuccess) return paymentResult;

        var inventoryResult = await _inventoryService.ReserveItemsAsync(command.Items);
        if (!inventoryResult.IsSuccess) return inventoryResult;

        var order = await _orderRepository.CreateOrderAsync(command);

        await _publisher.Publish(new OrderCreatedEvent(order.Id));

        return Result.Success(order);
    }
}
```

### ❌ Anti-Pattern 2: Feature Dependencies

**Problem**: One feature directly using another feature's code.

```csharp
// BAD: Direct feature dependency
using Features.UserManagement;

public class OrderCheckoutHandler
{
    private readonly UserManagementService _userService; // ❌
}
```

**Solution**: Use shared interfaces or domain events.

```csharp
// GOOD: Depend on shared interface
using Common.Interfaces;

public class OrderCheckoutHandler
{
    private readonly IUserProvider _userProvider; // ✅
}
```

### ❌ Anti-Pattern 3: Anemic Handlers

**Problem**: Handler just passing data through, no real logic.

```csharp
// BAD: No value, just pass-through
public class GetUserHandler
{
    private readonly IUserService _userService;

    public async Task<User> Handle(GetUserQuery query)
    {
        return await _userService.GetUserAsync(query.Id); // Just forwarding
    }
}
```

**Solution**: Either add value in handler or access data directly.

```csharp
// GOOD: Handler contains logic
public class GetUserHandler
{
    private readonly IDbContext _dbContext;

    public async Task<UserDto> Handle(GetUserQuery query)
    {
        var user = await _dbContext.Users
            .Include(u => u.Profile)
            .Include(u => u.Orders)
            .FirstOrDefaultAsync(u => u.Id == query.Id);

        return user != null
            ? MapToDto(user)
            : null;
    }
}
```

### ❌ Anti-Pattern 4: Shared Repositories

**Problem**: Generic repository shared across all features.

```csharp
// BAD: Generic repository
public interface IRepository<T>
{
    Task<T> GetByIdAsync(Guid id);
    Task<List<T>> GetAllAsync();
    Task AddAsync(T entity);
    // ... etc
}
```

**Solution**: Feature-specific data access.

```csharp
// GOOD: Feature-specific repository
public class OrderCheckoutRepository
{
    public async Task<Order> CreateOrderAsync(Order order) { }
    public async Task<bool> IsInventoryAvailableAsync(List<OrderItem> items) { }
    // Only methods needed by this feature
}
```

### ❌ Anti-Pattern 5: Premature Abstraction

**Problem**: Creating shared code before it's needed.

```csharp
// BAD: Creating abstractions "just in case"
public interface IEmailSender { }
public interface ISmsSender { }
public interface INotificationSender { }
// ... when only email is currently used
```

**Solution**: Wait until 3+ features need it.

```csharp
// GOOD: Keep it simple until duplication emerges
public class OrderConfirmationHandler
{
    private readonly IEmailService _emailService; // Simple, concrete dependency
}
```

## Migration Strategy

### Migrating from Layered Architecture

**Step 1: Identify Features**

- List all use cases/user stories
- Group related endpoints
- Map to features

**Step 2: Create Feature Structure**

```
1. Create /Features folder
2. Create first feature folder
3. Move related code into feature
4. Update namespaces
5. Test thoroughly
6. Repeat for next feature
```

**Step 3: Extract One Feature at a Time**

```
Example: Migrating User Registration

Before (Layered):
/Controllers/UserController.cs (Register action)
/Services/UserService.cs (RegisterUser method)
/Repositories/UserRepository.cs (CreateUser method)
/Models/RegisterUserRequest.cs
/Validators/RegisterUserValidator.cs

After (Vertical Slice):
/Features/UserRegistration/
  - RegisterUserCommand.cs (from RegisterUserRequest)
  - RegisterUserHandler.cs (from UserService.RegisterUser)
  - RegisterUserValidator.cs (moved as-is)
  - UserRegistrationRepository.cs (from UserRepository, feature-specific)
  - RegistrationResult.cs (new)
/Api/Controllers/UserRegistrationController.cs (thin controller)
```

**Step 4: Refactor Gradually**

- Start with new features (vertical slices)
- Migrate existing features one at a time
- Keep both architectures working during transition
- Don't rush - this can take months

**Step 5: Clean Up Shared Code**

- After migration, review /Common folder
- Remove unused abstractions
- Consolidate duplicates
- Document what remains

### Coexistence Strategy

```
/src
  /Features (new vertical slices)
    /UserRegistration
    /ProductSearch
  /Controllers (old layered code)
    /OrderController.cs
  /Services (old layered code)
    /OrderService.cs
```

**Rules for Coexistence**:

1. New code goes in /Features
2. Bug fixes in old code stay in old location
3. Major refactors move to /Features
4. Gradually migrate over 6-12 months

## Technology-Specific Guidance

### .NET / C#

**Recommended Libraries**:

- **MediatR**: Request/response handling
- **FluentValidation**: Input validation
- **AutoMapper**: Object mapping (use sparingly)
- **Entity Framework Core**: Database access

**Setup Example**:

```csharp
// Program.cs
builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(Program).Assembly));

builder.Services.AddValidatorsFromAssembly(typeof(Program).Assembly);

builder.Services.AddTransient(typeof(IPipelineBehavior<,>),
    typeof(ValidationBehavior<,>));
builder.Services.AddTransient(typeof(IPipelineBehavior<,>),
    typeof(LoggingBehavior<,>));
```

### Node.js / TypeScript

**Recommended Libraries**:

- **Mediator pattern library**: `ts-mediator` or similar
- **class-validator**: Input validation
- **TypeORM** or **Prisma**: Database access

**Example Structure**:

```typescript
// features/user-registration/register-user.command.ts
export class RegisterUserCommand {
  constructor(
    public readonly email: string,
    public readonly password: string,
    public readonly firstName: string,
    public readonly lastName: string
  ) {}
}

// features/user-registration/register-user.handler.ts
export class RegisterUserHandler {
  constructor(
    private readonly dbContext: DbContext,
    private readonly passwordHasher: PasswordHasher
  ) {}

  async handle(
    command: RegisterUserCommand
  ): Promise<Result<RegistrationResult>> {
    // Handler logic
  }
}
```

### Python

**Recommended Libraries**:

- **mediatr**: Mediator pattern
- **pydantic**: Data validation
- **SQLAlchemy**: Database access

**Example Structure**:

```python
# features/user_registration/register_user_command.py
from dataclasses import dataclass
from mediatr import Request

@dataclass
class RegisterUserCommand(Request):
    email: str
    password: str
    first_name: str
    last_name: str

# features/user_registration/register_user_handler.py
from mediatr import RequestHandler

class RegisterUserHandler(RequestHandler[RegisterUserCommand, Result]):
    def __init__(self, db_context: DbContext, password_hasher: PasswordHasher):
        self.db_context = db_context
        self.password_hasher = password_hasher

    async def handle(self, command: RegisterUserCommand) -> Result:
        # Handler logic
        pass
```

### Java / Spring Boot

**Recommended Approach**:

- **Spring MediatR** or custom mediator
- **Bean Validation**: Input validation
- **Spring Data JPA**: Database access

**Example Structure**:

```java
// features/userregistration/RegisterUserCommand.java
public record RegisterUserCommand(
    String email,
    String password,
    String firstName,
    String lastName
) implements Command<Result<RegistrationResult>> {}

// features/userregistration/RegisterUserHandler.java
@Component
public class RegisterUserHandler
    implements CommandHandler<RegisterUserCommand, Result<RegistrationResult>> {

    private final UserRepository repository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public Result<RegistrationResult> handle(RegisterUserCommand command) {
        // Handler logic
    }
}
```

## Quality Checklist

### Feature Implementation Checklist

Before considering a feature complete:

- [ ] Feature organized in dedicated folder under `/Features`
- [ ] Command/Query object created with clear naming
- [ ] Handler implemented with focused logic
- [ ] Validator created for input validation
- [ ] Result/DTO defined for response
- [ ] Repository or data access implemented (if needed)
- [ ] API endpoint created (thin controller/route)
- [ ] Unit tests written for handler
- [ ] Integration tests written for complete flow
- [ ] No direct dependencies on other features
- [ ] Shared code only in `/Common` when truly needed
- [ ] Feature registered in DI container
- [ ] Error handling implemented
- [ ] Logging added for important events
- [ ] Documentation updated (if applicable)

### Code Review Checklist

When reviewing vertical slice code:

- [ ] Is the feature boundary clear and logical?
- [ ] Does the handler have a single, focused responsibility?
- [ ] Are dependencies injected (no `new` operators)?
- [ ] Is validation separated from business logic?
- [ ] Are errors handled gracefully with Result pattern?
- [ ] Is the code testable (no static dependencies)?
- [ ] Are there direct dependencies between features? (should be none)
- [ ] Is shared code justified and documented?
- [ ] Are naming conventions followed consistently?
- [ ] Is the feature independently deployable?

### Architecture Validation Checklist

Periodically review the overall architecture:

- [ ] Features are organized by business capability, not technical layer
- [ ] Shared kernel remains thin and focused
- [ ] No circular dependencies between features
- [ ] Cross-cutting concerns handled by pipeline behaviors
- [ ] Database migrations are feature-specific when possible
- [ ] API endpoints are thin and delegate to handlers
- [ ] Tests are organized by feature
- [ ] New team members can understand feature boundaries
- [ ] Features can be developed in parallel without conflicts
- [ ] Deployment can be done incrementally by feature

## Summary

Vertical slice architecture provides:

- **Faster Development**: Parallel work on independent features
- **Better Maintainability**: Related code stays together
- **Easier Testing**: Features tested in isolation
- **Reduced Coupling**: Minimal dependencies between features
- **Team Scalability**: Clear ownership boundaries

**Key Takeaways**:

1. Organize by feature, not by technical layer
2. Keep features independent and self-contained
3. Minimize shared code - only share true cross-cutting concerns
4. Use mediator pattern for request/response handling
5. Implement cross-cutting concerns via pipeline behaviors
6. Test features in isolation
7. Migrate gradually from layered architecture

**Remember**: Vertical slice architecture is about organizing code for **changeability** and **maintainability**, not just about following a pattern. Always prioritize clarity and simplicity over strict adherence to any architectural pattern.

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Maintainer**: AI-Assisted Development Team
**Related Instructions**:

- `.github/instructions/ai-assisted-output.instructions.md`
- `.github/instructions/copilot-instructions.md`
