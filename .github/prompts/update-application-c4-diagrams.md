---
mode: agent
model: Auto (copilot)
tools: ["search", "edit", "create"]
description: "Update application documentation to include current-state details and Mermaid C4 diagrams"

# This frontmatter supports the create-issue workflow parser
# title/labels/assignees/milestone are optional; edit as needed after creation
# You can run the workflow with this file via the "Create Issue From Prompt" action
# and leave Title/Body blank to use these values.

title: "Docs: Update application overview with Mermaid C4 diagrams"
labels:
  - documentation
  - architecture
  - diagram
assignees: []
milestone: ""
---

Please update the application documentation to include current-state details and Mermaid C4 diagrams.

Scope

- Audit current repository to reflect the application's present state (features, services, workflows)
- Update README.md (or create /docs/overview.md if preferred) with:
  - Executive summary of the system
  - Technology stack and high-level architecture
  - Clear build/run instructions if missing
- Add Mermaid C4 diagrams (as code blocks), at minimum:
  - C4 Context diagram (C1)
  - C4 Container diagram (C2)
  - (Optional) C4 Component diagram (C3) for the most critical service/module

Acceptance Criteria

- README.md (or docs/overview.md) contains:
  - Accurate description of current app state
  - At least one Mermaid code block for C1 and C2
  - Links to any deeper documentation or diagrams
- Diagrams render correctly in supported viewers (e.g., GitHub Mermaid support)
- Any assumptions or unknowns are clearly called out with TODOs or questions

References

- Use Mermaid C4 syntax patterns; example stubs below for convenience.

Examples (stubs to customize)

```mermaid
%% C4 Context (C1)
C4Context
    title System Context
    Person(user, "End User")
    System(system, "Target System", "High-level purpose")
    System_Ext(dep, "External Dependency", "What it does")

    Rel(user, system, "Uses")
    Rel(system, dep, "Calls")
```

```mermaid
%% C4 Container (C2)
C4Container
    title System Container Diagram
    Person(user, "End User")
    System_Boundary(system, "Target System") {
      Container(web, "Web App", "Framework", "Primary UI")
      Container(api, "API", "Runtime", "Business logic")
      ContainerDb(db, "Database", "DB Type", "Data store")
    }

    Rel(user, web, "Browses")
    Rel(web, api, "REST/GraphQL")
    Rel(api, db, "Queries")
```

Notes

- If the repo contains multiple services, include per-service sections and repeat C2 as needed.
- Keep diagrams small and focused; link to deeper C3/C4 as the architecture evolves.
