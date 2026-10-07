import { defineConfig } from "@playwright/test";

// Tests de bout en bout contre un build de production (port 3218) : ils n'affectent pas le serveur de dev.
export default defineConfig({
  testDir: "tests/e2e",
  timeout: 60_000,
  fullyParallel: false,
  workers: 1,
  // Utilise le Google Chrome installé (pas de téléchargement de navigateur de test).
  use: { baseURL: "http://localhost:3218", trace: "retain-on-failure", channel: "chrome", headless: true },
  webServer: {
    command: "npm run build && npx next start --port 3218",
    url: "http://localhost:3218/login",
    reuseExistingServer: false,
    timeout: 400_000,
  },
});
