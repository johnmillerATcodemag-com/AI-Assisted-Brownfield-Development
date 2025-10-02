## Vue Testing Guidelines

### Unit Test Template

```javascript
import { mount } from "@vue/test-utils";
import MyComponent from "@/components/MyComponent.vue";

describe("MyComponent.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = mount(MyComponent, {
      props: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
```

### Integration Test Template

```typescript
import { mount } from "@vue/test-utils";
import { createPinia } from "pinia";
import { createRouter, createWebHistory } from "vue-router";
import UserProfile from "@/components/UserProfile.vue";
import { useUserStore } from "@/stores/userStore";

describe("UserProfile Integration Tests", () => {
  let pinia: ReturnType<typeof createPinia>;
  let router: ReturnType<typeof createRouter>;

  beforeEach(() => {
    pinia = createPinia();
    router = createRouter({
      history: createWebHistory(),
      routes: [{ path: "/user/:id", component: UserProfile }],
    });
  });

  it("displays user data from store", async () => {
    const wrapper = mount(UserProfile, {
      global: {
        plugins: [pinia, router],
      },
      props: {
        userId: "123",
      },
    });

    const userStore = useUserStore();
    await userStore.fetchUser("123");

    await wrapper.vm.$nextTick();
    expect(wrapper.text()).toContain("John Doe");
  });
});
```

### E2E Test Template

```typescript
import { test, expect } from "@playwright/test";

test.describe("User Management", () => {
  test("should display user profile", async ({ page }) => {
    await page.goto("/user/123");

    await expect(page.locator('[data-testid="user-name"]')).toContainText("John Doe");
    await expect(page.locator('[data-testid="user-email"]')).toContainText("john@example.com");
  });

  test("should update user profile", async ({ page }) => {
    await page.goto("/user/123");

    await page.fill('[data-testid="first-name-input"]', "Jane");
    await page.click('[data-testid="save-button"]');

    await expect(page.locator('[data-testid="success-message"]')).toBeVisible();
    await expect(page.locator('[data-testid="user-name"]')).toContainText("Jane Doe");
  });
});
```

### Pinia Store Test Template

```typescript
import { createPinia, setActivePinia } from "pinia";
import { useUserStore } from "@/stores/userStore";

describe("User Store", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
  });

  it("should set user correctly", () => {
    const store = useUserStore();
    const user = { id: "1", firstName: "John", lastName: "Doe", email: "john@example.com" };

    store.setUser(user);

    expect(store.currentUser).toEqual(user);
    expect(store.isAuthenticated).toBe(true);
  });

  it("should clear user correctly", () => {
    const store = useUserStore();
    const user = { id: "1", firstName: "John", lastName: "Doe", email: "john@example.com" };

    store.setUser(user);
    store.clearUser();

    expect(store.currentUser).toBeNull();
    expect(store.isAuthenticated).toBe(false);
  });
});
```

### Vue Router Test Template

```javascript
import { createRouter, createWebHistory } from "vue-router";
import { mount } from "@vue/test-utils";
import MyComponent from "@/components/MyComponent.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/my-route",
      component: MyComponent,
    },
  ],
});

describe("MyComponent.vue", () => {
  it("renders correctly when navigating to /my-route", async () => {
    const wrapper = mount(MyComponent, {
      global: {
        plugins: [router],
      },
    });
    await router.push("/my-route");
    await wrapper.vm.$nextTick();
    expect(wrapper.text()).toContain("My Component");
  });
});
```

### Vue Composition API Test Template

```typescript
import { mount } from "@vue/test-utils";
import { ref } from "vue";
import { useUser } from "@/composables/useUser";
import UserProfile from "@/components/UserProfile.vue";

// Mock the composable
vi.mock("@/composables/useUser");

describe("UserProfile with Composition API", () => {
  it("should display user data from composable", () => {
    const mockUser = ref({
      id: "1",
      firstName: "John",
      lastName: "Doe",
      email: "john@example.com",
    });

    vi.mocked(useUser).mockReturnValue({
      user: mockUser,
      loading: ref(false),
      error: ref(null),
      isAuthenticated: ref(true),
      fullName: ref("John Doe"),
      setUser: vi.fn(),
      clearUser: vi.fn(),
      setError: vi.fn(),
    });

    const wrapper = mount(UserProfile);

    expect(wrapper.text()).toContain("John Doe");
    expect(wrapper.text()).toContain("john@example.com");
  });
});
```

### Vue Test Utils Template

```typescript
import { DOMWrapper, mount, VueWrapper } from "@vue/test-utils";
import { ComponentPublicInstance } from "vue";
import UserForm from "@/components/UserForm.vue";

describe("UserForm", () => {
  let wrapper: VueWrapper<ComponentPublicInstance>;

  beforeEach(() => {
    wrapper = mount(UserForm, {
      props: {
        user: {
          id: "1",
          firstName: "John",
          lastName: "Doe",
          email: "john@example.com",
        },
      },
    });
  });

  afterEach(() => {
    wrapper.unmount();
  });

  it("should emit update event when form is submitted", async () => {
    const form = wrapper.find("form");
    const firstNameInput = wrapper.find('[data-testid="first-name"]');

    await firstNameInput.setValue("Jane");
    await form.trigger("submit");

    expect(wrapper.emitted("update")).toBeTruthy();
    expect(wrapper.emitted("update")[0][0]).toEqual(expect.objectContaining({ firstName: "Jane" }));
  });
});
```

### Vue Error Handling Test Template

```typescript
import { mount } from "@vue/test-utils";
import { vi } from "vitest";
import ErrorBoundary from "@/components/ErrorBoundary.vue";
import ThrowingComponent from "@/components/ThrowingComponent.vue";

describe("Error Handling", () => {
  it("should catch and display errors", async () => {
    const consoleErrorSpy = vi.spyOn(console, "error").mockImplementation(() => {});

    const wrapper = mount(ErrorBoundary, {
      slots: {
        default: ThrowingComponent,
      },
    });

    await wrapper.vm.$nextTick();

    expect(wrapper.text()).toContain("Something went wrong");
    expect(consoleErrorSpy).toHaveBeenCalled();

    consoleErrorSpy.mockRestore();
  });
});
```

### Vue Testing Best Practices

- Use `mount` for full DOM rendering and `shallowMount` for shallow rendering.
- Always clean up after tests to avoid memory leaks.
- Use `beforeEach` and `afterEach` hooks to set up and tear down test environments.
- Use `async/await` for handling asynchronous operations in tests.

### Vue Testing Rules

- Always write tests for critical components and features.
- Use descriptive test names to clarify the purpose of each test.
- Avoid testing implementation details; focus on behavior.
- Use mocks and stubs to isolate components and avoid dependencies on external services.

### Vue Testing Tools

- [Vue Test Utils](https://vue-test-utils.vuejs.org/): Official unit testing utility library for Vue.js.
- [Jest](https://jestjs.io/): A delightful JavaScript testing framework with a focus on simplicity.
- [Cypress](https://www.cypress.io/): A powerful end-to-end testing framework for web applications.
