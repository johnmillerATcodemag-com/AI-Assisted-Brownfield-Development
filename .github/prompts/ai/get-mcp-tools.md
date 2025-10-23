---
mode: agent
model: "Auto (copilot)"
tools: ["mcp_azure", "mcp_microsoft_doc"]
description: "Visualize and explore available MCP (Model Context Protocol) server tools and capabilities"
---

# MCP Server Tools Visualization

Explore available MCP server tools and capabilities.

## Azure MCP Server
- `list_resource_groups`
- `query_cosmos_db`
- `get_app_service_logs`
- `manage_key_vault`

## Microsoft Docs MCP Server
- `search_documentation`
- `fetch_full_page`
- `search_code_samples`

## Architecture Diagrams

```mermaid
graph TD
    Root[MCP Architecture] --> Azure[Azure Server]
    Root --> Docs[MS Docs Server]
    
    Azure --> A1[list_resource_groups]
    Azure --> A2[query_cosmos_db]
    Azure --> A3[get_app_service_logs]
    Azure --> A4[manage_key_vault]
    
    Docs --> B1[search_documentation]
    Docs --> B2[fetch_full_page]
    Docs --> B3[search_code_samples]
    
    style Root fill:#333,color:#fff
    style Azure fill:#0078d4,color:#fff
    style Docs fill:#107c10,color:#fff
```
