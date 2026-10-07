import { describe, expect, it } from "vitest";
import { isPinCorrect, createAttemptLimiter } from "@/lib/auth/pin";

describe("isPinCorrect", () => {
  it("accepts the exact PIN", () => {
    expect(isPinCorrect("1503", "1503")).toBe(true);
  });
  it("rejects a wrong PIN", () => {
    expect(isPinCorrect("1504", "1503")).toBe(false);
    expect(isPinCorrect("150", "1503")).toBe(false);
    expect(isPinCorrect("15030", "1503")).toBe(false);
  });
  it("ignores surrounding whitespace typed by the user", () => {
    expect(isPinCorrect(" 1503 ", "1503")).toBe(true);
  });
  it("never accepts when no PIN is configured", () => {
    expect(isPinCorrect("", "")).toBe(false);
    expect(isPinCorrect("1503", undefined)).toBe(false);
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
