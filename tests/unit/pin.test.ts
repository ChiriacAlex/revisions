import { describe, expect, it } from "vitest";
import { isPinCorrect, createAttemptLimiter } from "@/lib/auth/pin";

describe("isPinCorrect", () => {
  it("accepts the exact PIN", () => {
    expect(isPinCorrect("4821", "4821")).toBe(true);
  });
  it("rejects a wrong PIN", () => {
    expect(isPinCorrect("4822", "4821")).toBe(false);
    expect(isPinCorrect("482", "4821")).toBe(false);
    expect(isPinCorrect("48210", "4821")).toBe(false);
  });
  it("ignores surrounding whitespace typed by the user", () => {
    expect(isPinCorrect(" 4821 ", "4821")).toBe(true);
  });
  it("never accepts when no PIN is configured", () => {
    expect(isPinCorrect("", "")).toBe(false);
    expect(isPinCorrect("4821", undefined)).toBe(false);
  });
});

describe("attempt limiter", () => {
  const t0 = new Date("2026-10-07T10:00:00Z").getTime();

  it("allows the first attempts", () => {
    const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
    expect(limiter.isLocked("ip", t0)).toBe(false);
  });

  it("locks a client after 5 failures", () => {
    const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
    for (let i = 0; i < 4; i++) limiter.registerFailure("ip", t0);
    expect(limiter.isLocked("ip", t0)).toBe(false);
    limiter.registerFailure("ip", t0);
    expect(limiter.isLocked("ip", t0)).toBe(true);
    expect(limiter.isLocked("other-ip", t0)).toBe(false);
  });

  it("unlocks after the lock duration", () => {
    const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
    for (let i = 0; i < 5; i++) limiter.registerFailure("ip", t0);
    expect(limiter.isLocked("ip", t0 + 14 * 60_000)).toBe(true);
    expect(limiter.isLocked("ip", t0 + 15 * 60_000 + 1)).toBe(false);
  });

  it("reports how long the client must wait", () => {
    const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
    for (let i = 0; i < 5; i++) limiter.registerFailure("ip", t0);
    expect(limiter.retryAfterMs("ip", t0 + 5 * 60_000)).toBe(10 * 60_000);
    expect(limiter.retryAfterMs("other", t0)).toBe(0);
  });

  it("forgets failures after a success", () => {
    const limiter = createAttemptLimiter({ maxFailures: 5, lockMs: 15 * 60_000 });
    for (let i = 0; i < 4; i++) limiter.registerFailure("ip", t0);
    limiter.reset("ip");
    limiter.registerFailure("ip", t0);
    expect(limiter.isLocked("ip", t0)).toBe(false);
  });
});

describe("attempt limiter with a time window", () => {
  const t0 = new Date("2026-10-07T10:00:00Z").getTime();

  it("forgets old failures once the window has passed", () => {
    const limiter = createAttemptLimiter({ maxFailures: 3, lockMs: 60 * 60_000, windowMs: 60 * 60_000 });
    limiter.registerFailure("global", t0);
    limiter.registerFailure("global", t0 + 10 * 60_000);
    // 2 h plus tard : les deux anciens échecs ne comptent plus
    limiter.registerFailure("global", t0 + 2 * 60 * 60_000);
    expect(limiter.isLocked("global", t0 + 2 * 60 * 60_000)).toBe(false);
  });

  it("locks when the failures happen inside the window", () => {
    const limiter = createAttemptLimiter({ maxFailures: 3, lockMs: 60 * 60_000, windowMs: 60 * 60_000 });
    limiter.registerFailure("global", t0);
    limiter.registerFailure("global", t0 + 1000);
    limiter.registerFailure("global", t0 + 2000);
    expect(limiter.isLocked("global", t0 + 3000)).toBe(true);
  });
});
