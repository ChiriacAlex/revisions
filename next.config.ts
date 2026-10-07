import type { NextConfig } from "next";

// Serveur Node autonome (output: "standalone") lancé dans Docker sur la machine d'Alex.
// Toutes les pages dépendent de la session (cookie) : rendu dynamique, protégé par le PIN.
const nextConfig: NextConfig = {
  output: "standalone",
  // Les liens relatifs des cours (« ../primitives/ ») supposent des URL terminées par « / ».
  trailingSlash: true,
  poweredByHeader: false,
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Robots-Tag", value: "noindex, nofollow" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "same-origin" },
          { key: "X-Frame-Options", value: "DENY" },
        ],
      },
    ];
  },
};

export default nextConfig;
