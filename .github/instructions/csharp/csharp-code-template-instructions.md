## Code Templates

### Controller Template
```csharp
[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
public class UsersController : ControllerBase
{
    private readonly IMediator _mediator;
    private readonly ILogger<UsersController> _logger;

    public UsersController(IMediator mediator, ILogger<UsersController> logger)
    {
        _mediator = mediator ?? throw new ArgumentNullException(nameof(mediator));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    /// <summary>
    /// Gets a user by their unique identifier
    /// </summary>
    /// <param name="id">The user's unique identifier</param>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns>The user details</returns>
    [HttpGet("{id:guid}")]
    [ProducesResponseType(typeof(UserResponse), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    public async Task<ActionResult<UserResponse>> GetUserAsync(
        Guid id, 
        CancellationToken cancellationToken = default)
    {
        try
        {
            _logger.LogInformation("Getting user with ID: {UserId}", id);
            
            var query = new GetUserQuery(id);
            var result = await _mediator.Send(query, cancellationToken);
            
            return Ok(result);
        }
        catch (UserNotFoundException ex)
        {
            _logger.LogWarning("User not found: {UserId}", id);
            return NotFound($"User with ID {id} not found");
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while getting user: {UserId}", id);
            return StatusCode(StatusCodes.Status500InternalServerError, 
                "An error occurred while processing your request");
        }
    }
}

### Service Interface Template

```csharp
public interface IUserService
{
    Task<UserDto> GetUserByIdAsync(Guid id, CancellationToken cancellationToken = default);
    Task<IEnumerable<UserDto>> GetUsersAsync(UserFilterDto filter, CancellationToken cancellationToken = default);
    Task<UserDto> CreateUserAsync(CreateUserDto createUserDto, CancellationToken cancellationToken = default);
    Task<UserDto> UpdateUserAsync(Guid id, UpdateUserDto updateUserDto, CancellationToken cancellationToken = default);
    Task<bool> DeleteUserAsync(Guid id, CancellationToken cancellationToken = default);
}
```

### Service Implementation Template

```csharp
public class UserService : IUserService
{
    private readonly IUserRepository _userRepository;
    private readonly IMapper _mapper;
    private readonly ILogger<UserService> _logger;

    public UserService(
        IUserRepository userRepository,
        IMapper mapper,
        ILogger<UserService> logger)
    {
        _userRepository = userRepository ?? throw new ArgumentNullException(nameof(userRepository));
        _mapper = mapper ?? throw new ArgumentNullException(nameof(mapper));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    public async Task<UserDto> GetUserByIdAsync(Guid id, CancellationToken cancellationToken = default)
    {
        try
        {
            _logger.LogInformation("Retrieving user with ID: {UserId}", id);
            
            var user = await _userRepository.GetByIdAsync(id, cancellationToken);
            if (user == null)
            {
                throw new UserNotFoundException($"User with ID {id} not found");
            }

            var userDto = _mapper.Map<UserDto>(user);
            
            _logger.LogInformation("Successfully retrieved user: {UserId}", id);
            return userDto;
        }
        catch (UserNotFoundException)
        {
            _logger.LogWarning("User not found: {UserId}", id);
            throw;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while retrieving user: {UserId}", id);
            throw new ServiceException("An error occurred while retrieving the user", ex);
        }
    }
}
```

### Entity Template
```csharp
public class User : BaseEntity
{
    public string FirstName { get; private set; } = string.Empty;
    public string LastName { get; private set; } = string.Empty;
    public string Email { get; private set; } = string.Empty;
    public DateTime DateOfBirth { get; private set; }
    public bool IsActive { get; private set; } = true;
    
    // Private constructor for EF Core
    private User() { }
    
    public User(string firstName, string lastName, string email, DateTime dateOfBirth)
    {
        FirstName = Guard.Against.NullOrWhiteSpace(firstName, nameof(firstName));
        LastName = Guard.Against.NullOrWhiteSpace(lastName, nameof(lastName));
        Email = Guard.Against.NullOrWhiteSpace(email, nameof(email));
        DateOfBirth = Guard.Against.OutOfRange(dateOfBirth, nameof(dateOfBirth), 
            DateTime.Now.AddYears(-120), DateTime.Now.AddYears(-13));
    }
    
    public void UpdateEmail(string email)
    {
        Email = Guard.Against.NullOrWhiteSpace(email, nameof(email));
        // Add domain event if needed
        AddDomainEvent(new UserEmailUpdatedEvent(Id, email));
    }
    
    public void Deactivate()
    {
        IsActive = false;
        AddDomainEvent(new UserDeactivatedEvent(Id));
    }
}
```

### DTO Template
```csharp
public record UserDto
{
    public Guid Id { get; init; }
    public string FirstName { get; init; } = string.Empty;
    public string LastName { get; init; } = string.Empty;
    public string Email { get; init; } = string.Empty;
    public DateTime DateOfBirth { get; init; }
    public bool IsActive { get; init; }
    public DateTime CreatedAt { get; init; }
    public DateTime? UpdatedAt { get; init; }
}

public record CreateUserDto
{
    public string FirstName { get; init; } = string.Empty;
    public string LastName { get; init; } = string.Empty;
    public string Email { get; init; } = string.Empty;
    public DateTime DateOfBirth { get; init; }
}

public record UpdateUserDto
{
    public string FirstName { get; init; } = string.Empty;
    public string LastName { get; init; } = string.Empty;
    public string Email { get; init; } = string.Empty;
    public DateTime DateOfBirth { get; init; }
}
```

### Repository Interface Template
```csharp
public interface IUserRepository : IRepository<User>
{
    Task<User?> GetByEmailAsync(string email, CancellationToken cancellationToken = default);
    Task<IEnumerable<User>> GetActiveUsersAsync(CancellationToken cancellationToken = default);
    Task<IEnumerable<User>> SearchUsersAsync(string searchTerm, CancellationToken cancellationToken = default);
    Task<bool> ExistsByEmailAsync(string email, CancellationToken cancellationToken = default);
}

public interface IRepository<T> where T : BaseEntity
{
    Task<T?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default);
    Task<IEnumerable<T>> GetAllAsync(CancellationToken cancellationToken = default);
    Task<T> AddAsync(T entity, CancellationToken cancellationToken = default);
    Task<T> UpdateAsync(T entity, CancellationToken cancellationToken = default);
    Task<bool> DeleteAsync(Guid id, CancellationToken cancellationToken = default);
    Task<bool> ExistsAsync(Guid id, CancellationToken cancellationToken = default);
}
```

### Exception Handling Template
```csharp
public class UserNotFoundException : NotFoundException
{
    public UserNotFoundException(string message) : base(message) { }
    public UserNotFoundException(string message, Exception innerException) : base(message, innerException) { }
}

public class ServiceException : Exception
{
    public ServiceException(string message) : base(message) { }
    public ServiceException(string message, Exception innerException) : base(message, innerException) { }
}

public abstract class NotFoundException : Exception
{
    protected NotFoundException(string message) : base(message) { }
    protected NotFoundException(string message, Exception innerException) : base(message, innerException) { }
}
```

