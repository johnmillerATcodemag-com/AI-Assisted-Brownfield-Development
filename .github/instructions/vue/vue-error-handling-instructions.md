### Vue Exception Template

```typescript
import { defineStore } from 'pinia';

export const useErrorStore = defineStore('error', {
  state: () => ({
    error: null as Error | null
  }),
  actions: {
    setError(error: Error) {
      this.error = error;
    },
    clearError() {
      this.error = null;
    }
  }
});
```