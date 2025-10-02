## Vue API Documentation Guidelines

### JSDoc Standards for Vue Components

```typescript
/**
 * User profile component that displays user information
 * @component
 * @example
 * <UserProfile :user="currentUser" @update="handleUserUpdate" />
 */
export default defineComponent({
  name: "UserProfile",
  props: {
    /**
     * User object containing profile information
     * @type {User}
     */
    user: {
      type: Object as PropType<User>,
      required: true,
    },
  },
  emits: {
    /**
     * Emitted when user information is updated
     * @event update
     * @param {User} user - Updated user object
     */
    update: (user: User) => true,
  },
});
```

### API Service Documentation

```typescript
/**
 * Service for managing user operations
 * @service UserService
 */
export class UserService {
  /**
   * Retrieves a user by ID
   * @param {string} id - User identifier
   * @returns {Promise<User>} User object
   * @throws {UserNotFoundException} When user is not found
   * @example
   * const user = await UserService.getUser('123');
   */
  static async getUser(id: string): Promise<User> {
    // Implementation
  }

  /**
   * Updates user information
   * @param {string} id - User identifier
   * @param {Partial<User>} updates - Fields to update
   * @returns {Promise<User>} Updated user object
   * @throws {ValidationException} When updates are invalid
   */
  static async updateUser(id: string, updates: Partial<User>): Promise<User> {
    // Implementation
  }
}
```

### Type Documentation

```typescript
/**
 * User interface representing a system user
 * @interface User
 */
export interface User {
  /** Unique identifier for the user */
  id: string;
  /** User's first name */
  firstName: string;
  /** User's last name */
  lastName: string;
  /** User's email address */
  email: string;
  /** Date when user joined the system */
  joinedDate: Date;
  /** Whether the user account is active */
  isActive: boolean;
}

/**
 * API response wrapper for user operations
 * @interface ApiResponse
 * @template T - Type of the response data
 */
export interface ApiResponse<T> {
  /** Response data */
  data: T;
  /** Success status */
  success: boolean;
  /** Error message if any */
  message?: string;
  /** Additional metadata */
  metadata?: Record<string, any>;
}
```

### Composable Documentation

```typescript
/**
 * Composable for managing user state and operations
 * @composable useUser
 * @returns {Object} User management methods and state
 */
export function useUser() {
  const user = ref<User | null>(null);
  const loading = ref(false);
  const error = ref<string | null>(null);

  /**
   * Fetches user data
   * @param {string} id - User ID to fetch
   */
  const fetchUser = async (id: string): Promise<void> => {
    // Implementation
  };

  /**
   * Updates user information
   * @param {Partial<User>} updates - User fields to update
   */
  const updateUser = async (updates: Partial<User>): Promise<void> => {
    // Implementation
  };

  return {
    user: readonly(user),
    loading: readonly(loading),
    error: readonly(error),
    fetchUser,
    updateUser,
  };
}
```

### Store Documentation

```typescript
/**
 * User store for managing user state across the application
 * @store useUserStore
 */
export const useUserStore = defineStore("user", {
  state: (): UserState => ({
    currentUser: null,
    users: [],
    loading: false,
    error: null,
  }),

  getters: {
    /**
     * Gets the current authenticated user
     * @returns {User | null} Current user or null if not authenticated
     */
    getCurrentUser: (state): User | null => state.currentUser,

    /**
     * Gets all active users
     * @returns {User[]} Array of active users
     */
    getActiveUsers: (state): User[] => state.users.filter((user) => user.isActive),
  },

  actions: {
    /**
     * Authenticates a user
     * @param {LoginCredentials} credentials - User login credentials
     * @returns {Promise<User>} Authenticated user
     * @throws {AuthenticationException} When credentials are invalid
     */
    async login(credentials: LoginCredentials): Promise<User> {
      // Implementation
    },
  },
});
```

### Component Event Documentation

```typescript
/**
 * Event emitted when user data changes
 * @event userUpdate
 * @param {User} user - Updated user object
 * @param {string[]} changedFields - Array of field names that changed
 */

/**
 * Event emitted when user action is completed
 * @event actionComplete
 * @param {string} action - Action that was completed
 * @param {boolean} success - Whether the action was successful
 * @param {string} [message] - Optional success/error message
 */
```
