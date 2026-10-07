import "server-only";
import { cache } from "react";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { SESSION_COOKIE, verifySessionToken } from "./session";
import { sessionSecret } from "./config";

/** Vérification au plus près des données : chaque page protégée l'appelle (le proxy n'est qu'un premier filtre). */
export const requireSession = cache(async (): Promise<{ expiresAt: Date }> => {
  const token = (await cookies()).get(SESSION_COOKIE)?.value;
  const check = await verifySessionToken(token, sessionSecret());
  if (!check.valid) redirect("/login");
  return { expiresAt: check.expiresAt };
});
