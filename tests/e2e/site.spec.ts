import { expect, test } from "@playwright/test";
import { readFileSync } from "node:fs";

// Toutes les pages sont derrière le PIN : on se connecte avant chaque test (PIN lu dans .env.local).
test.beforeEach(async ({ page }) => {
  const pin = readFileSync(".env.local", "utf8").match(/^APP_PIN=(.+)$/m)?.[1].trim() ?? "";
  await page.goto("/login/");
  await page.getByLabel("Code PIN").fill(pin);
  await page.getByRole("button", { name: "Entrer" }).click();
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
});

test("la page d'accueil liste les trois cours", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
  await expect(page.getByText("Logical Formalism (FOLO)")).toBeVisible();
  await expect(page.getByText("Probabilités et statistiques (PBS)")).toBeVisible();
  await expect(page.getByText("Intégration et approximation de fonctions (IGAF)")).toBeVisible();
});

test("l'erratum IGAF renvoie vers des chapitres qui existent", async ({ page, request }) => {
  await page.goto("/courses/igaf/erratum/");
  const hrefs = await page.locator("article a[href^='../']").evaluateAll((links) =>
    links.map((a) => (a as HTMLAnchorElement).href),
  );
  expect(hrefs.length).toBeGreaterThan(5);
  for (const href of new Set(hrefs)) {
    expect((await request.get(href)).status(), href).toBe(200);
  }
  await page.getByRole("link", { name: "Primitives", exact: true }).first().click();
  await expect(page.getByRole("heading", { name: /Ch1 — Primitives/ })).toBeVisible();
  await expect(page.locator(".katex").first()).toBeVisible();
});

test("on navigue de l'accueil vers un chapitre", async ({ page }) => {
  await page.goto("/");
  await page.getByText("Logical Formalism (FOLO)").click();
  await expect(page).toHaveURL(/\/courses\/folo\/$/);
  await page.getByRole("link", { name: /Ch3 — Théorie des ensembles/ }).click();
  await expect(page.getByRole("heading", { name: "Ch3 — Théorie des ensembles" })).toBeVisible();
  await expect(page.locator(".katex").first()).toBeVisible();
});

test("un quiz se corrige dans le navigateur", async ({ page }) => {
  await page.goto("/courses/folo/objets-et-implication/");
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

test("le labo Python charge Python et lance les tests officiels", async ({ page }) => {
  await page.goto("/courses/folo/projet-python/");
  await page.getByRole("button", { name: "▶ Lancer les tests" }).click();
  await expect(page.locator(".pylab-status").first()).toContainText("1/60 tests réussis", { timeout: 60_000 });
});
