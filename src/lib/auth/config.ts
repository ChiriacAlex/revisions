import "server-only";

export function sessionSecret(): string {
  const secret = process.env.SESSION_SECRET;
  if (!secret || secret.length < 32) {
    throw new Error("SESSION_SECRET manquant ou trop court (>= 32 caractères) — voir .env.example");
  }
  return secret;
}

export function configuredPin(): string | undefined {
  return process.env.APP_PIN || undefined;
}
