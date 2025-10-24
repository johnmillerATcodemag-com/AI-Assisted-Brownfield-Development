---
description: "Analyzes instruction files in the .github/instruction folder and report any conflicts or inconsistencies"
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ['search', 'edit', 'fetch']
mode: agent
---

# Context Analysis and Conflict Detection

Please perform a comprehensive analysis of the provided context and identify any issues or inconsistencies.

Only focus on detecting conflicts, contradictions, or inconsistencies within the context.

Examine the following areas:

## 1. Conflicting Instructions

- Are there contradictory directives or requirements?
- Do any instructions override or conflict with others?
- Are there incompatible methodologies or approaches specified?

## 2. Factual Inconsistencies

- Are there contradictory statements about facts, data, or specifications?
- Do dates, numbers, or technical details conflict across different parts of the context?
- Are there inconsistent assumptions or premises?

## 3. Logical Contradictions

- Are there statements that cannot logically coexist?
- Do any conclusions contradict their supporting evidence or reasoning?
- Are there circular dependencies or impossible requirements?

## 4. Scope and Priority Conflicts

- Are there competing priorities that haven't been resolved?
- Do different sections suggest incompatible scopes of work?
- Are there resource or timeline conflicts?

## 5. Technical Incompatibilities

- Are there technology choices that conflict with each other?
- Do system requirements contradict each other?
- Are there version conflicts or dependency issues mentioned?

## 6. Communication Gaps

- Are there missing connections between related concepts?
- Do different sections use inconsistent terminology for the same concepts?
- Are there undefined references or assumptions?

## 7. Duplication and Redundancy

- Are there repeated instructions, requirements, or information across different sections?
- Do multiple sections cover the same topic without adding new value?
- Are there redundant processes, steps, or procedures that could be consolidated?
- Is the same information presented in conflicting ways in different locations?
- Are there duplicate definitions, examples, or explanations that should be unified?

## Response Format

For each issue identified, please provide:

- **Category**: Which type of conflict/issue this represents
- **Description**: Clear explanation of the conflict or inconsistency
- **Location**: Where in the context this occurs (if applicable)
- **Impact**: Potential consequences if not resolved
- **Recommendation**: Suggested approach to resolve the conflict

If no conflicts are found, please confirm that the context appears consistent and coherent, and highlight any areas that might benefit from clarification or additional detail.
