# Deployment Instructions

This document provides comprehensive deployment guidelines for the Zeus project.

## 🏗️ Infrastructure as Code

### Azure Bicep Templates

All infrastructure is defined using Azure Bicep templates located in the `infra/` folder.

#### Main Resources

- **Resource Group**: Container for all project resources
- **App Service Plan**: Hosting environment for web applications
- **Azure SQL Database**: Primary data storage
- **Application Insights**: Monitoring and telemetry
- **Key Vault**: Secrets management
- **Storage Account**: File storage and static assets

#### Deployment Commands

```powershell
# Deploy to development environment
az deployment group create `
  --resource-group zeus-dev-rg `
  --template-file infra/main.bicep `
  --parameters infra/main.parameters.json `
  --parameters environment=dev

# Deploy to production environment
az deployment group create `
  --resource-group zeus-prod-rg `
  --template-file infra/main.bicep `
  --parameters infra/main.parameters.json `
  --parameters environment=prod
```

## 🔧 Environment Configuration

### Environment Variables

Create the following environment variables for each environment:

#### Development (.env.development)

```bash
# Database
ConnectionStrings__DefaultConnection=Server=localhost;Database=Zeus_Dev;Trusted_Connection=true;

# Azure Services
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_SUBSCRIPTION_ID=your-subscription-id

# Application Insights
APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=your-key

# Storage
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=zeusdevstorage;AccountKey=your-key

# Frontend
VUE_APP_API_BASE_URL=https://localhost:5001/api
VUE_APP_AZURE_CLIENT_ID=your-client-id
VUE_APP_AZURE_TENANT_ID=your-tenant-id
```

#### Production (.env.production)

```bash
# Database
ConnectionStrings__DefaultConnection=Server=zeus-prod-sql.database.windows.net;Database=Zeus_Prod;Authentication=Active Directory Default;

# Azure Services (use Key Vault references)
AZURE_TENANT_ID=@Microsoft.KeyVault(SecretUri=https://zeus-prod-kv.vault.azure.net/secrets/tenant-id/)
AZURE_CLIENT_ID=@Microsoft.KeyVault(SecretUri=https://zeus-prod-kv.vault.azure.net/secrets/client-id/)

# Application Insights
APPLICATIONINSIGHTS_CONNECTION_STRING=@Microsoft.KeyVault(SecretUri=https://zeus-prod-kv.vault.azure.net/secrets/app-insights-connection/)

# Storage
AZURE_STORAGE_CONNECTION_STRING=@Microsoft.KeyVault(SecretUri=https://zeus-prod-kv.vault.azure.net/secrets/storage-connection/)

# Frontend
VUE_APP_API_BASE_URL=https://zeus-prod-api.azurewebsites.net/api
VUE_APP_AZURE_CLIENT_ID=your-prod-client-id
VUE_APP_AZURE_TENANT_ID=your-prod-tenant-id
```

## 🚀 Deployment Process

### Prerequisites

1. Azure CLI installed and authenticated
2. .NET 8 SDK installed
3. Node.js 18+ installed
4. Access to target Azure subscription

### Step 1: Infrastructure Deployment

```powershell
# Login to Azure
az login

# Set subscription
az account set --subscription "your-subscription-id"

# Create resource group
az group create --name zeus-prod-rg --location "East US"

# Deploy infrastructure
az deployment group create `
  --resource-group zeus-prod-rg `
  --template-file infra/main.bicep `
  --parameters infra/main.parameters.json `
  --parameters environment=prod
```

### Step 2: Database Migration

```powershell
# Update connection string in appsettings.json
# Run migrations
dotnet ef database update --project Zeus.csproj

# Seed initial data if needed
dotnet run --project Zeus.csproj --seed-data
```

### Step 3: Backend Deployment

```powershell
# Build and publish
dotnet publish -c Release -o ./publish

# Deploy to Azure App Service
az webapp deployment source config-zip `
  --resource-group zeus-prod-rg `
  --name zeus-prod-api `
  --src ./publish.zip
```

### Step 4: Frontend Deployment

```powershell
# Install dependencies
npm install

# Build for production
npm run build

# Deploy to Azure Static Web Apps or App Service
az staticwebapp deploy `
  --name zeus-prod-web `
  --source-location ./dist `
  --resource-group zeus-prod-rg
```

## 🔍 Health Checks

### Backend Health Endpoints

- `GET /health` - Basic health check
- `GET /health/ready` - Readiness probe
- `GET /health/live` - Liveness probe

### Frontend Health Checks

- Application loads without errors
- API connectivity test
- Authentication flow verification

## 📊 Monitoring and Logging

### Application Insights Configuration

```csharp
// Program.cs
builder.Services.AddApplicationInsightsTelemetry(options =>
{
    options.ConnectionString = builder.Configuration.GetConnectionString("ApplicationInsights");
});
```

### Custom Telemetry

```csharp
// Controller example
[HttpGet("{id}")]
public async Task<IActionResult> GetUser(Guid id)
{
    using var activity = Activity.StartActivity("GetUser");
    activity?.SetTag("user.id", id.ToString());

    try
    {
        var user = await _userService.GetUserAsync(id);
        _telemetryClient.TrackEvent("UserRetrieved", new Dictionary<string, string>
        {
            ["UserId"] = id.ToString(),
            ["UserEmail"] = user.Email
        });

        return Ok(user);
    }
    catch (Exception ex)
    {
        _telemetryClient.TrackException(ex);
        throw;
    }
}
```

## 🔒 Security Configuration

### Azure Key Vault Integration

```csharp
// Program.cs
if (builder.Environment.IsProduction())
{
    var keyVaultEndpoint = builder.Configuration["KeyVault:Endpoint"];
    builder.Configuration.AddAzureKeyVault(
        new Uri(keyVaultEndpoint),
        new DefaultAzureCredential());
}
```

### CORS Configuration

```csharp
// Program.cs
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowedOrigins", policy =>
    {
        policy.WithOrigins(
            "https://zeus-prod-web.azurestaticapps.net",
            "https://zeus-dev-web.azurestaticapps.net")
            .AllowAnyHeader()
            .AllowAnyMethod()
            .AllowCredentials();
    });
});
```

## 🏃‍♂️ CI/CD Pipeline

### GitHub Actions Workflow

```yaml
name: Deploy to Azure

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup .NET
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: 8.0.x

      - name: Run tests
        run: dotnet test --verbosity normal

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v3

      - name: Login to Azure
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Deploy Infrastructure
        run: |
          az deployment group create \
            --resource-group zeus-prod-rg \
            --template-file infra/main.bicep \
            --parameters infra/main.parameters.json

      - name: Deploy Application
        run: |
          dotnet publish -c Release -o ./publish
          az webapp deployment source config-zip \
            --resource-group zeus-prod-rg \
            --name zeus-prod-api \
            --src ./publish.zip
```

## 🧪 Testing Deployments

### Smoke Tests

```powershell
# Test API endpoints
$apiUrl = "https://zeus-prod-api.azurewebsites.net"
Invoke-RestMethod -Uri "$apiUrl/health" -Method GET

# Test database connectivity
Invoke-RestMethod -Uri "$apiUrl/health/ready" -Method GET

# Test authentication
$token = "your-test-token"
Invoke-RestMethod -Uri "$apiUrl/api/users/me" -Method GET -Headers @{Authorization="Bearer $token"}
```

### Load Testing

```powershell
# Using Azure Load Testing
az load test create \
  --name zeus-load-test \
  --resource-group zeus-prod-rg \
  --test-plan-file loadtest.yaml
```

## 🔄 Rollback Strategy

### Database Rollback

```powershell
# Rollback to previous migration
dotnet ef database update PreviousMigrationName --project Zeus.csproj
```

### Application Rollback

```powershell
# Rollback to previous deployment slot
az webapp deployment slot swap \
  --resource-group zeus-prod-rg \
  --name zeus-prod-api \
  --slot staging \
  --target-slot production \
  --action swap
```

## 📋 Deployment Checklist

### Pre-deployment

- [ ] All tests passing
- [ ] Database migration scripts reviewed
- [ ] Environment variables configured
- [ ] Secrets stored in Key Vault
- [ ] Load testing completed
- [ ] Security scan passed

### Post-deployment

- [ ] Health checks passing
- [ ] Application Insights collecting telemetry
- [ ] Database connections working
- [ ] Authentication flow verified
- [ ] Performance metrics reviewed
- [ ] Error rates monitored

## 🚨 Troubleshooting

### Common Issues

1. **Connection string not found**: Check Key Vault configuration
2. **Authentication failures**: Verify Azure AD app registration
3. **Database timeout**: Check connection pooling settings
4. **CORS errors**: Verify allowed origins configuration

### Debug Commands

```powershell
# Check application logs
az webapp log tail --resource-group zeus-prod-rg --name zeus-prod-api

# Check resource health
az resource show --resource-group zeus-prod-rg --name zeus-prod-api --resource-type Microsoft.Web/sites --query "properties.state"

# Test connectivity
Test-NetConnection zeus-prod-sql.database.windows.net -Port 1433
```

---

_For support, contact the development team or check the troubleshooting guide._
