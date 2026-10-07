import { describe, expect, it } from "vitest";
import { safeNextPath } from "@/lib/auth/redirect";

describe("safeNextPath", () => {
  it("keeps internal paths", () => {
    expect(safeNextPath("/courses/folo/sets")).toBe("/courses/folo/sets");
  });
  it("falls back to home for external or protocol-relative URLs", () => {
    expect(safeNextPath("https://evil.example")).toBe("/");
    expect(safeNextPath("//evil.example")).toBe("/");
    expect(safeNextPath("/\\evil.example")).toBe("/");
  });
  it("never sends back to the login or logout pages", () => {
    expect(safeNextPath("/login")).toBe("/");
    expect(safeNextPath("/logout")).toBe("/");
  });
  it("handles missing values", () => {
    expect(safeNextPath(undefined)).toBe("/");
    expect(safeNextPath(null)).toBe("/");
  });
});
