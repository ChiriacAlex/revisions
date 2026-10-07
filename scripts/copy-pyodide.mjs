// Copie le runtime Python (Pyodide) dans public/vendor/pyodide : le labo fonctionne sans CDN externe.
import { cpSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const source = dirname(require.resolve("pyodide/package.json"));
const target = join(process.cwd(), "public", "vendor", "pyodide");
const files = ["pyodide.js", "pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"];

mkdirSync(target, { recursive: true });
for (const file of files) cpSync(join(source, file), join(target, file));
console.log(`✔ pyodide copié dans public/vendor/pyodide (${files.length} fichiers)`);
