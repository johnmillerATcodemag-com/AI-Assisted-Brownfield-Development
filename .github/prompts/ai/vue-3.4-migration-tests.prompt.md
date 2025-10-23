---
description: "Identify tests needed to verify successful Vue 3.4 migration"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["search", "edit", "fetch"]
mode: agent
---

# Vue 3.4 Migration — Tests Needed

What tests are needed/missing to verify successful Vue 3.4 migration?

## Assumptions
- Focus on Vue app(s). If no Vue found, state and recommend.
- Prefer behavior-focused tests over brittle snapshots.

## Inputs
Frontend code (Vue SFCs, composables, router/store, entry), existing tests (unit/component/e2e), runner configs, CI steps

## Exclusions
`.git/`, `node_modules/`, `dist/`, `build/`, `.cache/`, binaries

## Migration Risk Checklist
1. **Component behavior**: Composition vs Options API interop, `setup()` side effects, props/emits/`v-model`, slots (scoped API), Teleport, Suspense fallbacks
2. **Reactivity/state**: Ref/reactive unwrapping, watch/watchEffect cleanup, store (Pinia vs Vuex migrations)
3. **Routing**: Router v4 routes, nested routes, guards (beforeEach/resolve), dynamic params, query/params, nav failures
4. **Directives/templates**: Custom directives API changes, `v-if`/`v-for` order, template parsing
5. **Lifecycle**: Unmount vs destroy hooks, `beforeUnmount`/`unmounted` (cleanup resource leaks)
6. **Build/tooling**: Vite vs webpack, HMR behavior, SSR compatibility (if applicable)
7. **Third-party libs**: Plugin compatibility (Vue 3 versions), deprecated APIs

## Process
1. **Detect Vue version/stack**: Package.json, build config, existing tests. If no Vue, stop.
2. **Inventory tests**: Unit/component/e2e counts, coverage, frameworks (Vitest, Jest, Playwright)
3. **Identify critical flows**: Key features/components/pages, error handling, auth/routing
4. **Map gaps**: Per risk category, list untested scenarios (file/component ref)
5. **Recommend tests**: Prioritized (High/Medium/Low), type, target, scenario, rationale, effort (S/M/L)
6. **Plan**: Phase 1 (pre-migration baseline), Phase 2 (migration validation), Phase 3 (regression suite)
7. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
Vue version detected, test posture, migration-critical gaps (2–3 sentences)

### Current setup
Vue version, test frameworks, existing test count by type

### Critical flows
Key features/components requiring validation

### Migration-specific gaps table
| Risk category | Target | Scenario | Why critical | Effort |
|---------------|--------|----------|--------------|--------|
| Reactivity | `Component.vue` | Ref unwrap in computed | Breaking change | S |

### Recommended tests (prioritized)
Grouped High/Medium/Low with scenario outlines

### Test plan
Phase 1 (baseline), Phase 2 (validation), Phase 3 (regression)

### Durations
Per-step + total

## Constraints
- Evidence-based (file/component refs)
- No file modifications/commands
