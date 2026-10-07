import { describe, expect, it } from "vitest";
import { functionOfTest, summarize } from "@/lib/pylab";

const FNS = ["is_relation", "is_partial_function", "is_function", "is_symmetric", "is_antisymmetric", "gen_equiv_class", "is_equivalence"];

describe("functionOfTest", () => {
  it("maps a test method to the function it checks", () => {
    expect(functionOfTest("test_is_relation", FNS)).toBe("is_relation");
    expect(functionOfTest("test_gen_equiv_class_1", FNS)).toBe("gen_equiv_class");
    expect(functionOfTest("test_is_function_rejects_missing_image", FNS)).toBe("is_function");
  });

  it("does not confuse functions whose names overlap", () => {
    expect(functionOfTest("test_is_partial_function", FNS)).toBe("is_partial_function");
    expect(functionOfTest("test_is_antisymmetric_1", FNS)).toBe("is_antisymmetric");
    expect(functionOfTest("test_is_symmetric_0", FNS)).toBe("is_symmetric");
  });

  it("returns undefined for generic tests", () => {
    expect(functionOfTest("test_load", FNS)).toBeUndefined();
  });
});

describe("summarize", () => {
  it("marks a function as passing only if all of its tests pass", () => {
    const summary = summarize(
      [
        { test: "test_is_relation", status: "pass" },
        { test: "test_is_function", status: "pass" },
        { test: "test_is_function_extra", status: "fail", message: "boom" },
      ],
      FNS,
    );
    expect(summary.is_relation).toEqual({ passed: 1, total: 1 });
    expect(summary.is_function).toEqual({ passed: 1, total: 2 });
    expect(summary.is_symmetric).toEqual({ passed: 0, total: 0 });
  });
});
