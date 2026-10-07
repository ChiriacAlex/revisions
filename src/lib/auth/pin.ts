import { createHash, timingSafeEqual } from "node:crypto";

function digest(value: string): Buffer {
  return createHash("sha256").update(value, "utf8").digest();
}

/** Comparaison en temps constant : ne révèle pas combien de chiffres sont justes. */
export function isPinCorrect(input: string, expected: string | undefined): boolean {
  if (!expected) return false;
  const candidate = input.trim();
  if (!candidate) return false;
  return timingSafeEqual(digest(candidate), digest(expected));
}

type LimiterOptions = { maxFailures: number; lockMs: number };
type Entry = { failures: number; lockedUntil: number };

/**
 * Anti-bruteforce en mémoire : après `maxFailures` échecs, le client est bloqué `lockMs`.
 * Un PIN à 4 chiffres n'a que 10 000 combinaisons : sans blocage, il se devine en minutes.
 */
export function createAttemptLimiter({ maxFailures, lockMs }: LimiterOptions) {
  const entries = new Map<string, Entry>();

  function current(key: string, now: number): Entry | undefined {
    const entry = entries.get(key);
    if (entry && entry.lockedUntil !== 0 && now > entry.lockedUntil) {
      entries.delete(key);
      return undefined;
    }
    return entry;
  }

  return {
    isLocked(key: string, now: number = Date.now()): boolean {
      const entry = current(key, now);
      return !!entry && entry.lockedUntil !== 0;
    },
    retryAfterMs(key: string, now: number = Date.now()): number {
      const entry = current(key, now);
      return entry && entry.lockedUntil !== 0 ? entry.lockedUntil - now : 0;
    },
    registerFailure(key: string, now: number = Date.now()): void {
      const entry = current(key, now) ?? { failures: 0, lockedUntil: 0 };
      entry.failures += 1;
      if (entry.failures >= maxFailures) entry.lockedUntil = now + lockMs;
      entries.set(key, entry);
    },
    reset(key: string): void {
      entries.delete(key);
    },
  };
}
