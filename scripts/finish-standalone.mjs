// `next build` (output: "standalone") ne copie ni les fichiers publics ni les assets statiques :
// on les place à côté de server.js pour que `npm start` et l'image Docker soient autonomes.
import { cpSync, existsSync } from "node:fs";

const target = ".next/standalone";
if (!existsSync(target)) throw new Error("build standalone introuvable : next.config doit avoir output: 'standalone'");
cpSync("public", `${target}/public`, { recursive: true });
cpSync(".next/static", `${target}/.next/static`, { recursive: true });
console.log("✔ standalone prêt : public/ et .next/static copiés");
