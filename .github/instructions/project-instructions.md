## Project Overview
This is a Vue 3 project using Composition API with TypeScript, Vuex for state management, and Vue Router for navigation.

## Technology Stack
- Vuex (state management)
- Tailwind CSS / CSS Modules
- Axios (HTTP client)
- .NET 8 (backend API)
- Entity Framework Core (ORM)
- Azure SQL Database

### File Structure
```plaintext
docs/ # Documentation files
  api/ # API documentation
  architecture/ # Architectural decisions and diagrams
  design/ # Design documents and mockups
  user-guides/ # User manuals and guides
  developer-guides/ # Developer documentation
infra/
  config/ # Configuration files
  scripts/ # Deployment and setup scripts
  migrations/ # Database migrations
  seeds/ # Seed data for development
ops/ # Operations and maintenance scripts
  monitoring/ # Monitoring scripts and configurations
  logging/ # Logging configurations and scripts
  backups/ # Backup scripts and configurations
public/ # Public assets
  images/ # Images and icons
  fonts/ # Custom fonts
src/
 components/ # Core business logic and entities
 css/ # Global styles and CSS files
  themes/ # Theme-specific styles
 router/ # Application routing
  routes/ # Route definitions
  guards/ # Route guards for authentication and authorization
  middleware/ # Middleware functions for routes
 services/ # Use cases and application logic
 store/ # data storage
 tests/
  unit/ # Unit tests 
  integration/ # Integration tests 
  functional/ # End-to-end tests
 utility/ # Utility functions and helpers
  formatters/ # Formatters for data presentation
  constants/ # Application constants
  types/ # Type definitions and interfaces
  mixins/ # Vue mixins for reusable logic
  plugins/ # Vue plugins for extending functionality
 views/ # Application views and pages
```