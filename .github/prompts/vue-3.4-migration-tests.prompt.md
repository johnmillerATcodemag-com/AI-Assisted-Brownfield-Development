---
description: "Identify and prioritize tests needed to verify a successful migration to Vue 3.4 (components, router, store, and critical flows)"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Prompt: Vue 3.4 Migration — Tests Needed and Missing

Looking at the current #codebase, what tests are needed and missing in order to verify a successful migration to Vue 3.4?

## Objective

Perform a read-only audit to determine what tests are required to validate a Vue 3.4 migration, covering component behavior, routing, state management, reactivity, and critical user flows.

## Assumptions

- If multiple frontend stacks are detected, focus on the Vue app(s). If no Vue code is found, state that and stop early with recommendations.
- Prefer behavior-focused tests over brittle snapshots.

## Inputs

- Frontend code (Vue SFCs, composables, router/store, entry points)
- Existing tests (unit/component/e2e), test runner configs, CI steps

## Scope and exclusions

- Exclude: `.git/`, `node_modules/`, `dist/`, `build/`, `.cache/`, binaries
- No file modifications or command execution

## Migration risk checklist (what to verify with tests)

1. Component behavior and rendering

   - Composition API vs. Options API interop; `setup()` side effects
   - Props validation, `emits` contract, `v-model` usage (and `modelValue` events)
   - Slots (scoped slots API), Teleport, Suspense fallbacks

2. Reactivity and state

   - Ref/reactive unwrapping, shallow/deep reactivity edge cases
   - Watch/watchEffect correctness and cleanup
   - Store: Pinia vs. Vuex (module migrations, actions/getters behavior)

3. Routing

   - Vue Router v4 routes, nested routes, guards (beforeEach/resolve), dynamic params
   - Query/params handling and navigation failures

4. Directives and templates

   - `v-if/v-for` keying, `v-bind` modifiers, custom directives behavior

5. Async and error handling

   - Async components, error boundaries, global error handlers

6. Critical UX flows
   - Auth/login/logout, protected routes, form validation and submission, data fetching retries

## Steps

1. Detect Vue app structure

   - Identify `main.ts/js`, `App.vue`, `router`, `store`, `components`, `composables`
   - Collect existing Vue testing utilities usage (e.g., @vue/test-utils, Vitest/Jest, Cypress/Playwright)

2. Inventory existing tests

   - List component tests, router tests, store tests, and e2e flows
   - Note skipped/flaky tests and gaps around critical components/routes

3. Map migration risks to current code

   - For each risk in the checklist, map to files/modules where applicable
   - Determine presence/absence of corresponding tests

4. Recommend missing tests

   - For each gap, propose specific tests with:
     - Type: component/unit/router/store/e2e
     - Target file/component/route
     - Scenario outline (Arrange/Act/Assert)
     - Rationale and migration risk covered
     - Effort (S/M/L)

5. Prioritize and plan

   - Group as High/Medium/Low based on user impact and defect risk
   - Suggest minimal harness scaffolds if none exist (e.g., test-utils mount helpers)

6. Summarize and durations
   - Provide executive summary and per-step durations plus total

## Output format (Markdown)

### Executive summary

- 2–3 sentences on migration verification readiness and highest risks

### Detected Vue testing setup

- Test runners, @vue/test-utils usage, router/store test helpers, e2e frameworks

### Test inventory (Vue-specific)

- Component tests: list notable components covered
- Router tests: route guards, dynamic routes
- Store tests: actions/getters/mutations or Pinia stores
- E2E: critical flows

### Gaps mapped to migration risks

Provide a table. One row per gap.

| Risk area        | Target (file/component/route) | Missing test type | Scenario summary                        | Risk/Impact                     | Effort |
| ---------------- | ----------------------------- | ----------------- | --------------------------------------- | ------------------------------- | ------ |
| v-model contract | components/FormInput.vue      | component         | Emits update:modelValue on input change | prevents broken two-way binding | S      |

### Recommended tests (prioritized)

- Grouped by High/Medium/Low with brief scenario outlines and targets

### Minimal scaffolds (if needed)

- Suggest a base mount helper (plugins: router, store), and testing config pointers

### Sources scanned

- Key Vue files and directories consulted

### Durations

- Step 1: <duration>
- Step 2: <duration>
- Step 3: <duration>
- Step 4: <duration>
- Step 5: <duration>
- Step 6: <duration>
- Total: <duration>

## Constraints

- Evidence-based (file paths/components) and migration-specific
- Favor behavior tests over snapshots; minimize brittle selectors
- No network calls or edits
