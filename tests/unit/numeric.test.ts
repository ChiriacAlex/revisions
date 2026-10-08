import { describe, expect, it } from "vitest";
import { formatAnswer, isAccepted, parseAnswer } from "@/lib/numeric";

describe("parseAnswer", () => {
  it("accepte décimaux (point ou virgule), fractions et espaces", () => {
    expect(parseAnswer("0,167")).toBeCloseTo(0.167);
    expect(parseAnswer("0.1666666666666666")).toBeCloseTo(1 / 6);
    expect(parseAnswer("1/6")).toBeCloseTo(1 / 6);
    expect(parseAnswer(" 6 / 36 ")).toBeCloseTo(1 / 6);
    expect(parseAnswer("-3/4")).toBe(-0.75);
    expect(parseAnswer("1,5/3")).toBe(0.5);
  });

  it("refuse ce qui n'est pas un nombre", () => {
    expect(parseAnswer("")).toBeNull();
    expect(parseAnswer("abc")).toBeNull();
    expect(parseAnswer("1/0")).toBeNull();
  });
});

describe("isAccepted", () => {
  it("accepte toute écriture assez proche de la réponse", () => {
    for (const raw of ["1/6", "6/36", "0,167", "0.1667", "0.1666666666666666", "0,166"]) {
      expect(isAccepted(raw, 1 / 6, 0.001), raw).toBe(true);
    }
    expect(isAccepted("0,17", 1 / 6, 0.001)).toBe(false);
    expect(isAccepted("1/5", 1 / 6, 0.001)).toBe(false);
  });
});

describe("formatAnswer", () => {
  it("écrit une fraction simple avec sa valeur approchée, au lieu de 0.16666666666666666", () => {
    expect(formatAnswer(0.16666666666666666, 0.001)).toBe("1/6 ≈ 0,167");
    expect(formatAnswer(1.3333333, 0.001)).toBe("4/3 ≈ 1,333");
  });

  it("écrit un décimal exact tel quel, avec une virgule", () => {
    expect(formatAnswer(0.25, 0.001)).toBe("0,25");
    expect(formatAnswer(-0.25, 0.0001)).toBe("-0,25");
    expect(formatAnswer(0.0625, 0.0001)).toBe("0,0625");
    expect(formatAnswer(58, 0.5)).toBe("58");
  });

  it("arrondit un irrationnel à la précision demandée", () => {
    expect(formatAnswer(2.6815171, 0.001)).toBe("≈ 2,682");
    expect(formatAnswer(0.6366198, 0.001)).toBe("≈ 0,637");
  });
});
