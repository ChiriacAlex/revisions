import { defineConfig } from "@playwright/test";
import { readFileSync } from "node:fs";

// Le PIN et le secret de session viennent de .env.local (jamais écrits en dur dans le dépôt).
const env = Object.fromEntries(
  readFileSync(".env.local", "utf8")
    .split("\n")
    .filter((line) => line.includes("="))
    .map((line) => [line.slice(0, line.indexOf("=")), line.slice(line.indexOf("=") + 1).trim()]),
);

// Tests de bout en bout contre le serveur de production autonome (le même que dans Docker), port 3218.
export default defineConfig({
  testDir: "tests/e2e",
  timeout: 90_000,
  fullyParallel: false,
  workers: 1,
  // Utilise le Google Chrome installé (pas de téléchargement de navigateur de test).
  use: { baseURL: "http://localhost:3218", trace: "retain-on-failure", channel: "chrome", headless: true },
  webServer: {
    command: "npm run build && npm run start",
    url: "http://localhost:3218/login/",
    reuseExistingServer: false,
    timeout: 400_000,
    env: { ...env, PORT: "3218", HOSTNAME: "127.0.0.1" },
  },
});
