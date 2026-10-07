"use server";

import { cookies, headers } from "next/headers";
import { redirect } from "next/navigation";
import { createAttemptLimiter, isPinCorrect } from "@/lib/auth/pin";
import { SESSION_COOKIE, SESSION_TTL_SECONDS, createSessionToken } from "@/lib/auth/session";
import { configuredPin, sessionSecret } from "@/lib/auth/config";
import { safeNextPath } from "@/lib/auth/redirect";

const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });

export type LoginState = { error?: string };

async function clientKey(): Promise<string> {
  const h = await headers();
  return h.get("x-forwarded-for")?.split(",")[0]?.trim() || h.get("x-real-ip") || "local";
}

export async function login(_prev: LoginState, formData: FormData): Promise<LoginState> {
  const key = await clientKey();
  const wait = limiter.retryAfterMs(key);
  if (wait > 0) {
    return { error: `Trop d'essais. Réessaie dans ${Math.ceil(wait / 60_000)} min.` };
  }

  const pin = String(formData.get("pin") ?? "");
  if (!isPinCorrect(pin, configuredPin())) {
    limiter.registerFailure(key);
    await new Promise((resolve) => setTimeout(resolve, 600));
    return { error: "Code PIN incorrect." };
  }

  limiter.reset(key);
  const token = await createSessionToken(sessionSecret());
  (await cookies()).set(SESSION_COOKIE, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: SESSION_TTL_SECONDS,
  });
  redirect(safeNextPath(formData.get("next")));
}
