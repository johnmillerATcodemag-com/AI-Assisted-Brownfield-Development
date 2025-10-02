## Vue Azure Integration Guidelines

### Azure Authentication (MSAL)

```typescript
import { PublicClientApplication } from "@azure/msal-browser";
import { createApp } from "vue";

const msalConfig = {
  auth: {
    clientId: process.env.VUE_APP_AZURE_CLIENT_ID,
    authority: `https://login.microsoftonline.com/${process.env.VUE_APP_AZURE_TENANT_ID}`,
  },
  cache: {
    cacheLocation: "localStorage",
    storeAuthStateInCookie: false,
  },
};

const msalInstance = new PublicClientApplication(msalConfig);

const app = createApp(App);
app.config.globalProperties.$msal = msalInstance;
app.mount("#app");
```

### Azure Configuration Service

```typescript
import { defineStore } from "pinia";

interface AzureConfig {
  subscriptionId: string;
  resourceGroup: string;
  keyVaultUrl: string;
  storageAccount: string;
  appInsightsKey: string;
}

export const useAzureConfigStore = defineStore("azureConfig", {
  state: (): { config: AzureConfig | null } => ({
    config: null,
  }),

  actions: {
    async loadConfig() {
      try {
        // Load from environment variables in production
        // or from Azure App Configuration in development
        this.config = {
          subscriptionId: process.env.VUE_APP_AZURE_SUBSCRIPTION_ID || "",
          resourceGroup: process.env.VUE_APP_AZURE_RESOURCE_GROUP || "",
          keyVaultUrl: process.env.VUE_APP_AZURE_KEYVAULT_URL || "",
          storageAccount: process.env.VUE_APP_AZURE_STORAGE_ACCOUNT || "",
          appInsightsKey: process.env.VUE_APP_AZURE_APP_INSIGHTS_KEY || "",
        };
      } catch (error) {
        console.error("Failed to load Azure configuration:", error);
        throw error;
      }
    },
  },
});
```

### Azure Application Insights Integration

```typescript
import { ApplicationInsights } from "@microsoft/applicationinsights-web";

class AzureInsightsService {
  private appInsights: ApplicationInsights;

  constructor(instrumentationKey: string) {
    this.appInsights = new ApplicationInsights({
      config: {
        instrumentationKey,
        enableAutoRouteTracking: true,
        autoTrackPageVisitTime: true,
      },
    });
    this.appInsights.loadAppInsights();
  }

  trackEvent(name: string, properties?: Record<string, any>) {
    this.appInsights.trackEvent({ name, properties });
  }

  trackException(exception: Error, properties?: Record<string, any>) {
    this.appInsights.trackException({ exception, properties });
  }

  trackPageView(name: string, url?: string) {
    this.appInsights.trackPageView({ name, uri: url });
  }

  trackMetric(name: string, average: number, properties?: Record<string, any>) {
    this.appInsights.trackMetric({ name, average }, properties);
  }

  setUserId(userId: string) {
    this.appInsights.setAuthenticatedUserContext(userId);
  }

  clearUser() {
    this.appInsights.clearAuthenticatedUserContext();
  }
}

export const azureInsights = new AzureInsightsService(process.env.VUE_APP_AZURE_APP_INSIGHTS_KEY || "");
```

### Azure Storage Integration

```typescript
import { BlobServiceClient } from "@azure/storage-blob";

class AzureStorageService {
  private blobServiceClient: BlobServiceClient;

  constructor(connectionString: string) {
    this.blobServiceClient = BlobServiceClient.fromConnectionString(connectionString);
  }

  async uploadFile(containerName: string, fileName: string, file: File): Promise<string> {
    try {
      const containerClient = this.blobServiceClient.getContainerClient(containerName);
      const blobClient = containerClient.getBlobClient(fileName);
      const blockBlobClient = blobClient.getBlockBlobClient();

      await blockBlobClient.uploadBrowserData(file, {
        blobHTTPHeaders: {
          blobContentType: file.type,
        },
      });

      return blobClient.url;
    } catch (error) {
      console.error("Failed to upload file:", error);
      throw error;
    }
  }

  async downloadFile(containerName: string, fileName: string): Promise<Blob> {
    try {
      const containerClient = this.blobServiceClient.getContainerClient(containerName);
      const blobClient = containerClient.getBlobClient(fileName);
      const response = await blobClient.download();

      if (!response.blobBody) {
        throw new Error("No blob body returned");
      }

      return response.blobBody;
    } catch (error) {
      console.error("Failed to download file:", error);
      throw error;
    }
  }

  async deleteFile(containerName: string, fileName: string): Promise<void> {
    try {
      const containerClient = this.blobServiceClient.getContainerClient(containerName);
      const blobClient = containerClient.getBlobClient(fileName);
      await blobClient.delete();
    } catch (error) {
      console.error("Failed to delete file:", error);
      throw error;
    }
  }
}

export const azureStorage = new AzureStorageService(process.env.VUE_APP_AZURE_STORAGE_CONNECTION_STRING || "");
```
