import { SignJWT, jwtVerify } from "jose";

/** Durée de vie d'une session : 1 heure, après quoi le PIN est redemandé. */
export const SESSION_TTL_SECONDS = 60 * 60;
export const SESSION_COOKIE = "revisions_session";

export type SessionCheck = { valid: true; expiresAt: Date } | { valid: false };

function keyFrom(secret: string): Uint8Array {
  if (!secret || secret.length < 32) {
    throw new Error("SESSION_SECRET must be at least 32 characters long");
  }
  return new TextEncoder().encode(secret);
}

export async function createSessionToken(secret: string, now: Date = new Date()): Promise<string> {
  const key = keyFrom(secret);
  const issuedAt = Math.floor(now.getTime() / 1000);
  return new SignJWT({ scope: "revisions" })
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt(issuedAt)
    .setExpirationTime(issuedAt + SESSION_TTL_SECONDS)
    .sign(key);
}

export async function verifySessionToken(
  token: string | undefined,
  secret: string,
  now: Date = new Date(),
): Promise<SessionCheck> {
  if (!token) return { valid: false };
  try {
    const { payload } = await jwtVerify(token, keyFrom(secret), {
      algorithms: ["HS256"],
      currentDate: now,
      clockTolerance: 0,
    });
    if (payload.scope !== "revisions" || typeof payload.exp !== "number") return { valid: false };
    return { valid: true, expiresAt: new Date(payload.exp * 1000) };
  } catch {
    return { valid: false };
  }
}
