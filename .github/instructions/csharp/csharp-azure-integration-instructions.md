## Azure Integration Guidelines

### Configuration for Azure Services
```csharp
public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddAzureServices(this IServiceCollection services, IConfiguration configuration)
    {
        // Azure Key Vault
        services.AddAzureKeyVault(configuration);
        
        // Azure Application Insights
        services.AddApplicationInsightsTelemetry(configuration["ApplicationInsights:ConnectionString"]);
        
        // Azure SQL Database
        services.AddDbContext<ApplicationDbContext>(options =>
            options.UseSqlServer(configuration.GetConnectionString("DefaultConnection")));
        
        // Azure Blob Storage
        services.AddSingleton(x =>
        {
            var connectionString = configuration.GetConnectionString("AzureBlobStorage");
            return new BlobServiceClient(connectionString);
        });
        
        return services;
    }
}
```

### Azure Key Vault Integration
```csharp
public static class KeyVaultExtensions
{
    public static IServiceCollection AddAzureKeyVault(this IServiceCollection services, IConfiguration configuration)
    {
        var keyVaultUrl = configuration["KeyVault:Url"];
        if (!string.IsNullOrEmpty(keyVaultUrl))
        {
            var credential = new DefaultAzureCredential();
            services.AddSingleton<SecretClient>(provider => 
                new SecretClient(new Uri(keyVaultUrl), credential));
        }
        
        return services;
    }
}
```

