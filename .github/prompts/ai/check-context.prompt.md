---
description: "Analyze instruction files for conflicts and inconsistencies"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ['search', 'edit', 'fetch']
mode: agent
---

# Context Analysis and Conflict Detection

Analyze provided context for conflicts, contradictions, and inconsistencies.

## Areas to Examine

1. **Conflicting Instructions**: Contradictory directives, overriding requirements, incompatible methodologies
2. **Factual Inconsistencies**: Contradictory facts/data/specs, conflicting dates/numbers/details
3. **Logical Contradictions**: Statements that can't coexist, conclusions contradicting evidence, circular deps
4. **Scope/Priority Conflicts**: Competing priorities, incompatible scopes, resource/timeline conflicts
5. **Technical Incompatibilities**: Conflicting tech choices, contradictory requirements, version/dependency conflicts
6. **Communication Gaps**: Missing connections, inconsistent terminology, undefined references
7. **Duplication/Redundancy**: Repeated instructions/info, redundant processes, conflicting presentations of same info

## Response Format per Issue
- **Category**: Conflict type
- **Description**: Clear explanation
- **Location**: Where it occurs
- **Impact**: Consequences if unresolved
- **Recommendation**: Resolution approach

If no conflicts: confirm consistency and note areas needing clarification.
