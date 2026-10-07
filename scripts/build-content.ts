import { writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { buildContent } from "../src/lib/content/build";

async function main() {
  const root = path.resolve(__dirname, "../content");
  const started = Date.now();
  const bundle = await buildContent(root);
  const out = path.resolve(__dirname, "../src/generated/content.json");
  await mkdir(path.dirname(out), { recursive: true });
  await writeFile(out, JSON.stringify(bundle));
  const chapters = bundle.courses.reduce((n, c) => n + c.chapters.length, 0);
  console.log(
    `✔ contenu : ${bundle.courses.length} cours, ${chapters} chapitres, ${Object.keys(bundle.items).length} exercices auto-corrigés, ${Object.keys(bundle.pylabs).length} labo(s) Python — ${Date.now() - started} ms`,
  );
}

main().catch((error) => {
  console.error(`✘ contenu invalide : ${error.message}`);
  process.exit(1);
});
