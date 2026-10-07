"use server";

import { cookies, headers } from "next/headers";
import { redirect } from "next/navigation";
import { createAttemptLimiter, isPinCorrect } from "@/lib/auth/pin";
import { SESSION_COOKIE, SESSION_TTL_SECONDS, createSessionToken } from "@/lib/auth/session";
import { configuredPin, sessionSecret } from "@/lib/auth/config";
import { safeNextPath } from "@/lib/auth/redirect";

// Par client : 5 échecs → 15 min. Global (défense en profondeur) : 30 échecs en 1 h → 1 h de blocage.
const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
const globalLimiter = createAttemptLimiter({ maxFailures: 30, lockMs: 60 * 60_000, windowMs: 60 * 60_000 });
const GLOBAL = "global";

export type LoginState = { error?: string };

async function clientKey(): Promise<string> {
  const h = await headers();
  return h.get("x-forwarded-for")?.split(",")[0]?.trim() || h.get("x-real-ip") || "local";
}

export async function login(_prev: LoginState, formData: FormData): Promise<LoginState> {
  const key = await clientKey();
  const wait = Math.max(limiter.retryAfterMs(key), globalLimiter.retryAfterMs(GLOBAL));
  if (wait > 0) {
    return { error: `Trop d'essais. Réessaie dans ${Math.ceil(wait / 60_000)} min.` };
  }

  const pin = String(formData.get("pin") ?? "");
  if (!isPinCorrect(pin, configuredPin())) {
    limiter.registerFailure(key);
    globalLimiter.registerFailure(GLOBAL);
    await new Promise((resolve) => setTimeout(resolve, 600));
    return { error: "Code PIN incorrect." };
  }

  limiter.reset(key);
  const token = await createSessionToken(sessionSecret());
  (await cookies()).set(SESSION_COOKIE, token, {
    httpOnly: true,
    // En local derrière nginx (HTTP), COOKIE_SECURE=false ; sinon HTTPS exigé en production.
    secure: process.env.COOKIE_SECURE ? process.env.COOKIE_SECURE === "true" : process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: SESSION_TTL_SECONDS,
  });
  redirect(safeNextPath(formData.get("next")));
}
