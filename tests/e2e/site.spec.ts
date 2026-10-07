import { expect, test } from "@playwright/test";

test("la page d'accueil est publique et liste les trois cours", async ({ page }) => {
  await page.goto("./");
  await expect(page.getByRole("heading", { name: "Mes cours" })).toBeVisible();
  await expect(page.getByText("Logical Formalism (FOLO)")).toBeVisible();
  await expect(page.getByText("Probabilités et statistiques (PBS)")).toBeVisible();
  await expect(page.getByText("Intégration et approximation de fonctions (IGAF)")).toBeVisible();
});

test("l'erratum IGAF renvoie vers des chapitres qui existent", async ({ page, request }) => {
  await page.goto("courses/igaf/erratum/");
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

test("on navigue de l'accueil vers un chapitre (liens compatibles avec le sous-dossier)", async ({ page }) => {
  await page.goto("./");
  await page.getByText("Logical Formalism (FOLO)").click();
  await expect(page).toHaveURL(/\/revisions\/courses\/folo\/$/);
  await page.getByRole("link", { name: /Ch3 — Théorie des ensembles/ }).click();
  await expect(page.getByRole("heading", { name: "Ch3 — Théorie des ensembles" })).toBeVisible();
  await expect(page.locator(".katex").first()).toBeVisible();
});

test("un quiz se corrige dans le navigateur", async ({ page }) => {
  await page.goto("courses/folo/objets-et-implication/");
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

test("il n'y a plus de page de connexion", async ({ request }) => {
  const response = await request.get("login/");
  expect(response.status()).toBe(404);
});

test("le labo Python charge Python depuis le sous-dossier et lance les tests officiels", async ({ page }) => {
  await page.goto("courses/folo/projet-python/");
  await page.getByRole("button", { name: "▶ Lancer les tests" }).click();
  await expect(page.locator(".pylab-status").first()).toContainText("1/60 tests réussis", { timeout: 60_000 });
});
