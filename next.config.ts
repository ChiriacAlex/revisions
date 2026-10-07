import type { NextConfig } from "next";

// Site 100 % statique (GitHub Pages) : `next build` produit le dossier out/.
// Sur GitHub Pages, le site vit sous /<nom-du-dépôt> : PAGES_BASE_PATH est fourni par le workflow.
const basePath = process.env.PAGES_BASE_PATH ?? "";

const nextConfig: NextConfig = {
  output: "export",
  basePath,
  trailingSlash: true,
  images: { unoptimized: true },
  env: { NEXT_PUBLIC_BASE_PATH: basePath },
};

export default nextConfig;
