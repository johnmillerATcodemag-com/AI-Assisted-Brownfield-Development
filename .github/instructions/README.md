# Development Instructions

This folder contains coding guidelines, templates, and best practices for the Zeus project.

## 📁 Folder Structure

```
instructions/
├── README.md                           # This file
├── commands-instructions.md            # Common commands and scripts
├── error-handling-instructions.md      # Global error handling guidelines
├── practices-instructions.md           # Best practices and standards
├── project-instructions.md             # Project overview and structure
├── style-instructions.md               # Code style and naming conventions
├── tools-instructions.md               # Development tools and usage
├── csharp/                            # C# specific instructions
│   ├── csharp-api-documentation-instructions.md
│   ├── csharp-azure-integration-instructions.md
│   ├── csharp-code-template-instructions.md
│   ├── csharp-error-handling-instructions.md
│   ├── csharp-style-instructions.md
│   ├── csharp-testing-instructions.md
│   └── csharp-validation-instructions.md
└── vue/                               # Vue.js specific instructions
    ├── vue-api-documentation-instructions.md
    ├── vue-azure-integration-instructions.md
    ├── vue-code-template-instructions.md
    ├── vue-error-handling-instructions.md
    ├── vue-style-instructions.md
    ├── vue-testing-instructions.md
    └── vue-validation-instructions.md
```

## 🎯 How to Use These Instructions

### For New Development

1. Start with `project-instructions.md` to understand the project structure
2. Review `practices-instructions.md` for general coding standards
3. Follow language-specific guidelines in `csharp/` or `vue/` folders
4. Use code templates as starting points for new components

### For Code Reviews

1. Check adherence to `style-instructions.md` standards
2. Verify error handling follows `error-handling-instructions.md`
3. Ensure tests are written according to testing guidelines
4. Validate Azure integration follows best practices

### For Troubleshooting

1. Check `commands-instructions.md` for common operations
2. Review `tools-instructions.md` for development setup
3. Follow debugging patterns in error handling guides

## 📚 Quick Reference

### C# Development

- **API Controllers**: Use templates in `csharp/csharp-code-template-instructions.md`
- **Services**: Follow dependency injection patterns
- **Testing**: Use xUnit with FluentAssertions
- **Validation**: Implement FluentValidation for DTOs
- **Azure**: Follow patterns in `csharp-azure-integration-instructions.md`

### Vue.js Development

- **Components**: Use Composition API with TypeScript
- **State Management**: Use Pinia stores
- **Testing**: Use Vitest and Vue Test Utils
- **Validation**: Use vee-validate v4 with Zod schemas
- **Azure**: Follow patterns in `vue-azure-integration-instructions.md`

## 🔧 Development Tools

### Required Tools

- .NET 8 SDK
- Node.js 18+ with npm/yarn
- Visual Studio Code with recommended extensions
- Azure CLI for deployment

### Recommended VS Code Extensions

- C# Dev Kit
- Vue Language Features (Volar)
- Azure Tools
- GitLens
- Prettier
- ESLint

## 📋 Code Quality Standards

### General Rules

- ✅ Write comprehensive tests (80%+ coverage)
- ✅ Use TypeScript for all new JavaScript code
- ✅ Follow SOLID principles
- ✅ Implement proper error handling
- ✅ Use async/await patterns
- ✅ Add JSDoc/XML documentation

### Performance Guidelines

- ✅ Implement caching strategies
- ✅ Use pagination for large datasets
- ✅ Optimize database queries
- ✅ Implement proper monitoring

## 🚀 Deployment

### Local Development

```bash
# Backend
dotnet run

# Frontend
npm run dev
```

### Azure Deployment

```bash
# Deploy infrastructure
az deployment group create --resource-group myRG --template-file main.bicep

# Deploy application
dotnet publish -c Release
```

## 📝 Contributing

When adding new instructions:

1. Follow the existing file naming convention
2. Include code examples with proper syntax highlighting
3. Add cross-references to related files
4. Update this README with new content
5. Test all code examples before committing

## 🔗 Related Documentation

- [Project README](../../README.md)
- [Architecture Documentation](../../docs/)
- [API Documentation](../../docs/api/)
- [Deployment Guide](../../docs/deployment/)

---

_Last updated: July 2025_
