import { expect, test } from "@playwright/test";
import { readFileSync } from "node:fs";

// Le PIN de test est lu dans .env.local (jamais écrit en dur dans le dépôt).
function testPin(): string {
  const env = readFileSync(".env.local", "utf8");
  const match = env.match(/^APP_PIN=(.+)$/m);
  if (!match) throw new Error("APP_PIN manquant dans .env.local");
  return match[1].trim();
}

async function submitPin(page: import("@playwright/test").Page, pin: string) {
  await page.goto("/login/");
  await page.getByLabel("Code PIN").fill(pin);
  await page.getByRole("button", { name: "Entrer" }).click();
}

async function login(page: import("@playwright/test").Page, pin: string) {
  await submitPin(page, pin);
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
}

test("une page protégée redirige vers la connexion, en mémorisant la destination", async ({ page }) => {
  await page.goto("/courses/folo/ensembles");
  await expect(page).toHaveURL(/\/login\/\?next=%2Fcourses%2Ffolo%2Fensembles%2F/);
  await expect(page.getByRole("heading", { name: "Révisions" })).toBeVisible();
});

test("un mauvais PIN est refusé", async ({ page }) => {
  await submitPin(page, "0000");
  await expect(page.locator(".login-error")).toHaveText("Code PIN incorrect.");
  await expect(page).toHaveURL(/\/login/);
});

test("le bon PIN ouvre une session d'une heure, en cookie HttpOnly", async ({ page, context }) => {
  await login(page, testPin());
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
  await expect(page.getByText("Logical Formalism (FOLO)")).toBeVisible();
  await expect(page.getByText("Probabilités et statistiques (PBS)")).toBeVisible();
  const session = (await context.cookies()).find((c) => c.name === "revisions_session");
  expect(session).toBeDefined();
  expect(session!.httpOnly).toBe(true);
  expect(session!.sameSite).toBe("Lax");
  const lifetime = session!.expires - Date.now() / 1000;
  expect(lifetime).toBeGreaterThan(3500);
  expect(lifetime).toBeLessThanOrEqual(3600);
  await expect(page.getByText(/Session : (60|59) min/)).toBeVisible();
});

test("après connexion, on revient sur la page demandée", async ({ page }) => {
  await page.goto("/courses/folo/ensembles");
  await page.getByLabel("Code PIN").fill(testPin());
  await page.getByRole("button", { name: "Entrer" }).click();
  await expect(page).toHaveURL(/\/courses\/folo\/ensembles\/$/);
  await expect(page.getByRole("heading", { name: "Ch3 — Théorie des ensembles" })).toBeVisible();
});

test("un jeton falsifié est rejeté", async ({ page, context }) => {
  await context.addCookies([
    { name: "revisions_session", value: "eyJhbGciOiJIUzI1NiJ9.eyJzY29wZSI6InJldmlzaW9ucyJ9.ZmFrZQ", url: "http://localhost:3218" },
  ]);
  await page.goto("/");
  await expect(page).toHaveURL(/\/login/);
});

test("la déconnexion ferme la session", async ({ page }) => {
  await login(page, testPin());
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
  await page.getByRole("button", { name: "Déconnexion" }).click();
  await expect(page).toHaveURL(/\/login/);
  await page.goto("/courses/folo/guide");
  await expect(page).toHaveURL(/\/login/);
});

test("un chapitre s'affiche avec ses formules et ses quiz fonctionnent", async ({ page }) => {
  await login(page, testPin());
  await page.goto("/courses/folo/objets-et-implication");
  await expect(page.locator(".katex").first()).toBeVisible();
  const quiz = page.locator('[data-item="ch1-implication"]');
  await quiz.scrollIntoViewIfNeeded();
  const rows = quiz.locator(".tf-row");
  const answers = [true, true, false, true, false];
  for (let i = 0; i < answers.length; i++) {
    await rows.nth(i).getByRole("button", { name: answers[i] ? "Vrai" : "Faux" }).click();
  }
  await quiz.getByRole("button", { name: "Valider" }).click();
  await expect(quiz.locator(".item-badge")).toHaveText("5/5");
});

test("le contenu des cours n'est pas servi sans session", async ({ request }) => {
  const response = await request.get("/courses/folo/projet-python/", { maxRedirects: 0 });
  expect(response.status()).toBe(307);
  expect(response.headers()["location"]).toContain("/login");
  const worker = await request.get("/pyodide-worker.js", { maxRedirects: 0 });
  expect(worker.status()).toBe(307);
});

test("aucun texte de cours dans les fichiers JavaScript publics (servis sans PIN)", async () => {
  const { readdirSync, readFileSync: read, statSync } = await import("node:fs");
  const { join } = await import("node:path");
  const files: string[] = [];
  const walk = (dir: string) => {
    for (const name of readdirSync(dir)) {
      const full = join(dir, name);
      if (statSync(full).isDirectory()) walk(full);
      else files.push(full);
    }
  };
  walk(".next/static");
  const phrases = ["catalogue spécial", "Voir la correction", "is_transitive_fast_enough", "Logical Formalism", "loi exponentielle"];
  for (const file of files) {
    const text = read(file, "utf8");
    for (const phrase of phrases) expect(text.includes(phrase), `${phrase} trouvé dans ${file}`).toBe(false);
  }
  expect(files.length).toBeGreaterThan(5);
});
