## Vue Validation Guidelines

### Vee-Validate v4 Schema Validation

```typescript
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/zod";
import * as z from "zod";

const validationSchema = toTypedSchema(
  z.object({
    firstName: z.string().min(1, "First name is required").max(50, "First name must not exceed 50 characters"),
    lastName: z.string().min(1, "Last name is required").max(50, "Last name must not exceed 50 characters"),
    email: z.string().email("Invalid email format").max(100, "Email must not exceed 100 characters"),
    dateOfBirth: z.date().refine((date) => {
      const age = new Date().getFullYear() - date.getFullYear();
      return age >= 13 && age <= 120;
    }, "Age must be between 13 and 120 years"),
    password: z
      .string()
      .min(8, "Password must be at least 8 characters")
      .regex(/[A-Z]/, "Password must contain at least one uppercase letter")
      .regex(/[a-z]/, "Password must contain at least one lowercase letter")
      .regex(/[0-9]/, "Password must contain at least one number"),
  })
);

export default defineComponent({
  setup() {
    const { handleSubmit, errors, values } = useForm({
      validationSchema,
    });

    const onSubmit = handleSubmit((values) => {
      console.log("Form submitted:", values);
    });

    return {
      onSubmit,
      errors,
      values,
    };
  },
});
```

### Individual Field Validation

```typescript
import { useField } from "vee-validate";
import { computed } from "vue";

export default defineComponent({
  setup() {
    const { value: email, errorMessage: emailError } = useField("email", (value: string) => {
      if (!value) return "Email is required";
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) return "Invalid email format";
      return true;
    });

    const { value: password, errorMessage: passwordError } = useField("password", (value: string) => {
      if (!value) return "Password is required";
      if (value.length < 8) return "Password must be at least 8 characters";
      if (!/[A-Z]/.test(value)) return "Password must contain at least one uppercase letter";
      if (!/[a-z]/.test(value)) return "Password must contain at least one lowercase letter";
      if (!/[0-9]/.test(value)) return "Password must contain at least one number";
      return true;
    });

    return {
      email,
      emailError,
      password,
      passwordError,
    };
  },
});
```

### Custom Validation Rules

```typescript
import { defineRule, configure } from "vee-validate";
import { required, email, min, max } from "@vee-validate/rules";

// Import built-in rules
defineRule("required", required);
defineRule("email", email);
defineRule("min", min);
defineRule("max", max);

// Custom rule for age validation
defineRule("validAge", (value: string) => {
  const dateOfBirth = new Date(value);
  const age = new Date().getFullYear() - dateOfBirth.getFullYear();
  if (age < 13 || age > 120) {
    return "Age must be between 13 and 120 years";
  }
  return true;
});

// Custom rule for password strength
defineRule("strongPassword", (value: string) => {
  if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/.test(value)) {
    return "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character";
  }
  return true;
});

// Configure global error message generation
configure({
  generateMessage: (ctx) => {
    const messages = {
      required: `The ${ctx.field} field is required.`,
      email: `The ${ctx.field} field must be a valid email.`,
      min: `The ${ctx.field} field must be at least ${ctx.rule.params[0]} characters.`,
      max: `The ${ctx.field} field must not exceed ${ctx.rule.params[0]} characters.`,
    };
    return messages[ctx.rule.name] || `The ${ctx.field} field is invalid.`;
  },
});
```
