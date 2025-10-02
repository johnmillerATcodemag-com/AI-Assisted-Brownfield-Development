# Code Style and Naming Conventions

## 🎯 General Principles

- **Consistency**: Follow established patterns throughout the codebase
- **Clarity**: Code should be self-documenting and easy to understand
- **Maintainability**: Write code that is easy to modify and extend
- **Performance**: Consider performance implications of style choices

## 📝 Naming Conventions

### C# Naming Conventions

- **PascalCase**: Classes, interfaces, methods, properties, enums, namespaces

  ```csharp
  public class UserService { }
  public interface IUserRepository { }
  public void GetUserById() { }
  public string FirstName { get; set; }
  ```

- **camelCase**: Private fields, local variables, method parameters

  ```csharp
  private readonly ILogger _logger;
  public void ProcessUser(string userId) { }
  ```

- **SCREAMING_SNAKE_CASE**: Constants

  ```csharp
  public const int MAX_RETRY_ATTEMPTS = 3;
  public static readonly TimeSpan DEFAULT_TIMEOUT = TimeSpan.FromSeconds(30);
  ```

- **Prefixes**:
  - Interfaces start with 'I': `IUserService`, `IRepository<T>`
  - Private fields start with underscore: `_userRepository`, `_logger`
  - Async methods end with 'Async': `GetUserAsync`, `SaveChangesAsync`

### TypeScript/JavaScript Naming Conventions

- **PascalCase**: Classes, interfaces, types, components

  ```typescript
  class UserService {}
  interface User {}
  type ApiResponse<T> = {};
  const UserProfile = defineComponent({});
  ```

- **camelCase**: Variables, functions, methods, properties

  ```typescript
  const userName = "john";
  function getUserById() {}
  const userService = new UserService();
  ```

- **SCREAMING_SNAKE_CASE**: Constants
  ```typescript
  const MAX_RETRY_ATTEMPTS = 3;
  const API_BASE_URL = "https://api.example.com";
  ```

## 📁 File Organization

### C# File Organization

- One class per file
- Namespace should match folder structure
- File name should match the primary class name
- Group related classes in the same namespace

```
src/
├── Controllers/
│   ├── UsersController.cs
│   └── AuthController.cs
├── Services/
│   ├── UserService.cs
│   └── Interfaces/
│       └── IUserService.cs
├── Models/
│   ├── User.cs
│   └── DTOs/
│       ├── UserDto.cs
│       └── CreateUserDto.cs
└── Data/
    ├── ApplicationDbContext.cs
    └── Repositories/
        ├── UserRepository.cs
        └── IUserRepository.cs
```

### Vue.js File Organization

- Components in PascalCase with descriptive names
- Composables prefixed with 'use'
- Services suffixed with 'Service'
- Types in separate files or type definition files

```
src/
├── components/
│   ├── UserProfile.vue
│   ├── UserList.vue
│   └── Library/
│       ├── BaseButton.vue
│       └── BaseInput.vue
├── composables/
│   ├── useUser.ts
│   └── useAuth.ts
├── services/
│   ├── userService.ts
│   └── authService.ts
├── types/
│   ├── user.ts
│   └── api.ts
└── stores/
    ├── userStore.ts
    └── authStore.ts
```

## 🎨 Code Formatting

### C# Formatting Rules

```csharp
// Class structure order
public class UserService : IUserService
{
    // 1. Constants
    private const int MAX_USERS = 1000;

    // 2. Private readonly fields
    private readonly IUserRepository _userRepository;
    private readonly ILogger<UserService> _logger;

    // 3. Constructor
    public UserService(IUserRepository userRepository, ILogger<UserService> logger)
    {
        _userRepository = userRepository ?? throw new ArgumentNullException(nameof(userRepository));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    // 4. Public properties
    public bool IsInitialized { get; private set; }

    // 5. Public methods
    public async Task<User> GetUserAsync(Guid id)
    {
        // Implementation
    }

    // 6. Private methods
    private void ValidateUser(User user)
    {
        // Implementation
    }
}
```

### TypeScript/Vue Formatting Rules

```typescript
// Vue component structure
<template>
  <div class="user-profile">
    <h1>{{ user.name }}</h1>
    <p>{{ user.email }}</p>
  </div>
</template>

<script setup lang="ts">
// 1. Imports
import { ref, computed, onMounted } from 'vue';
import { useUser } from '@/composables/useUser';
import type { User } from '@/types/user';

// 2. Props
interface Props {
  userId: string;
}
const props = defineProps<Props>();

// 3. Emits
interface Emits {
  (e: 'update', user: User): void;
}
const emit = defineEmits<Emits>();

// 4. Composables
const { user, loading, fetchUser } = useUser();

// 5. Reactive state
const isEditing = ref(false);

// 6. Computed properties
const displayName = computed(() => `${user.value?.firstName} ${user.value?.lastName}`);

// 7. Methods
const handleEdit = () => {
  isEditing.value = true;
};

// 8. Lifecycle hooks
onMounted(() => {
  fetchUser(props.userId);
});
</script>

<style scoped>
.user-profile {
  padding: 1rem;
  border-radius: 0.5rem;
  background-color: var(--bg-secondary);
}
</style>
```

## 📊 Code Documentation

### C# Documentation (XML Comments)

```csharp
/// <summary>
/// Retrieves a user by their unique identifier
/// </summary>
/// <param name="id">The unique identifier of the user</param>
/// <param name="cancellationToken">Token to cancel the operation</param>
/// <returns>The user if found, null otherwise</returns>
/// <exception cref="ArgumentException">Thrown when id is empty</exception>
/// <exception cref="UserNotFoundException">Thrown when user is not found</exception>
public async Task<User?> GetUserByIdAsync(Guid id, CancellationToken cancellationToken = default)
{
    if (id == Guid.Empty)
        throw new ArgumentException("User ID cannot be empty", nameof(id));

    // Implementation
}
```

### TypeScript Documentation (JSDoc)

````typescript
/**
 * Composable for managing user data and operations
 * @param initialUserId - Optional initial user ID to load
 * @returns Object containing user state and methods
 * @example
 * ```typescript
 * const { user, loading, fetchUser } = useUser('123');
 * ```
 */
export function useUser(initialUserId?: string) {
  const user = ref<User | null>(null);
  const loading = ref(false);

  /**
   * Fetches user data by ID
   * @param id - User identifier
   * @throws {Error} When user is not found
   */
  const fetchUser = async (id: string): Promise<void> => {
    // Implementation
  };

  return { user, loading, fetchUser };
}
````

## 🔧 Configuration Files

### EditorConfig (.editorconfig)

```ini
root = true

[*]
charset = utf-8
end_of_line = crlf
insert_final_newline = true
trim_trailing_whitespace = true

[*.{cs,vb}]
indent_style = space
indent_size = 4

[*.{js,ts,vue,json}]
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

### Prettier Configuration (.prettierrc)

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

### ESLint Configuration (.eslintrc.js)

```javascript
module.exports = {
  extends: ["@vue/typescript/recommended", "@vue/prettier", "@vue/prettier/@typescript-eslint"],
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
    "vue/component-name-in-template-casing": ["error", "PascalCase"],
    "vue/no-v-html": "off",
  },
};
```

## 🎯 Best Practices

### General Code Style

- ✅ Use meaningful variable and method names
- ✅ Keep methods small and focused (single responsibility)
- ✅ Use early returns to reduce nesting
- ✅ Prefer composition over inheritance
- ✅ Use dependency injection for testability
- ✅ Handle errors gracefully with proper error messages

### Performance Considerations

- ✅ Use `readonly` for collections that don't change
- ✅ Prefer `string.IsNullOrEmpty()` over `== ""` or `== null`
- ✅ Use `ConfigureAwait(false)` in library code
- ✅ Cache expensive computations
- ✅ Use lazy loading for expensive resources

### Security Guidelines

- ✅ Validate all inputs
- ✅ Use parameterized queries
- ✅ Sanitize user output
- ✅ Don't log sensitive information
- ✅ Use secure communication (HTTPS)

## 🚫 Code Smells to Avoid

### C# Anti-patterns

```csharp
// ❌ Don't use Hungarian notation
string strUserName;
int intAge;

// ✅ Use descriptive names instead
string userName;
int age;

// ❌ Don't use magic numbers
if (user.Age > 65) { /* retire */ }

// ✅ Use named constants
private const int RETIREMENT_AGE = 65;
if (user.Age > RETIREMENT_AGE) { /* retire */ }

// ❌ Don't catch and ignore exceptions
try { /* code */ } catch { }

// ✅ Handle exceptions appropriately
try
{
    /* code */
}
catch (SpecificException ex)
{
    _logger.LogError(ex, "Specific error occurred");
    throw;
}
```

### TypeScript/Vue Anti-patterns

```typescript
// ❌ Don't use 'any' type
const user: any = getUserData();

// ✅ Use proper typing
const user: User = getUserData();

// ❌ Don't mutate props directly
props.user.name = "New Name";

// ✅ Emit events to parent component
emit("update:user", { ...props.user, name: "New Name" });

// ❌ Don't use var
var userName = "john";

// ✅ Use const or let
const userName = "john";
```
