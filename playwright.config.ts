import { defineConfig } from "@playwright/test";

// Tests de bout en bout sur le site statique, servi sous /revisions exactement comme sur GitHub Pages.
export default defineConfig({
  testDir: "tests/e2e",
  timeout: 90_000,
  fullyParallel: false,
  workers: 1,
  // Utilise le Google Chrome installé (pas de téléchargement de navigateur de test).
  use: { baseURL: "http://localhost:3218/revisions/", trace: "retain-on-failure", channel: "chrome", headless: true },
  webServer: {
    command:
      "PAGES_BASE_PATH=/revisions npm run build && rm -rf .e2e && mkdir -p .e2e && cp -R out .e2e/revisions && python3 -m http.server 3218 -d .e2e",
    url: "http://localhost:3218/revisions/",
    reuseExistingServer: false,
    timeout: 400_000,
  },
});
