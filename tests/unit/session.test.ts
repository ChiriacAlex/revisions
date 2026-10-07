import { describe, expect, it } from "vitest";
import {
  SESSION_TTL_SECONDS,
  createSessionToken,
  verifySessionToken,
} from "@/lib/auth/session";

const SECRET = "test-secret-with-at-least-32-characters!!";

describe("session token", () => {
  it("is valid right after it has been created", async () => {
    const now = new Date("2026-10-07T10:00:00Z");
    const token = await createSessionToken(SECRET, now);
    const result = await verifySessionToken(token, SECRET, now);
    expect(result.valid).toBe(true);
  });

  it("lasts exactly one hour", async () => {
    expect(SESSION_TTL_SECONDS).toBe(3600);
    const now = new Date("2026-10-07T10:00:00Z");
    const token = await createSessionToken(SECRET, now);
    const result = await verifySessionToken(token, SECRET, now);
    expect(result.valid && result.expiresAt.toISOString()).toBe("2026-10-07T11:00:00.000Z");
  });

  it("is still valid 59 minutes later", async () => {
    const now = new Date("2026-10-07T10:00:00Z");
    const token = await createSessionToken(SECRET, now);
    const later = new Date(now.getTime() + 59 * 60 * 1000);
    expect((await verifySessionToken(token, SECRET, later)).valid).toBe(true);
  });

  it("expires after one hour", async () => {
    const now = new Date("2026-10-07T10:00:00Z");
    const token = await createSessionToken(SECRET, now);
    const later = new Date(now.getTime() + 60 * 60 * 1000 + 1000);
    expect((await verifySessionToken(token, SECRET, later)).valid).toBe(false);
  });

  it("rejects a token signed with another secret", async () => {
    const token = await createSessionToken("another-secret-with-at-least-32-chars!!");
    expect((await verifySessionToken(token, SECRET)).valid).toBe(false);
  });

  it("rejects garbage and empty tokens", async () => {
    expect((await verifySessionToken("not-a-jwt", SECRET)).valid).toBe(false);
    expect((await verifySessionToken("", SECRET)).valid).toBe(false);
    expect((await verifySessionToken(undefined, SECRET)).valid).toBe(false);
  });

  it("refuses to work with a short secret", async () => {
    await expect(createSessionToken("short")).rejects.toThrow(/secret/i);
  });
});
