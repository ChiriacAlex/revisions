import { describe, expect, it } from "vitest";
import path from "node:path";
import { buildContent } from "@/lib/content/build";

const fixtures = path.resolve(__dirname, "../fixtures");

describe("buildContent", () => {
  it("loads courses with chapters sorted by their numeric prefix", async () => {
    const bundle = await buildContent(path.join(fixtures, "content"));
    expect(bundle.courses).toHaveLength(1);
    const course = bundle.courses[0];
    expect(course.slug).toBe("demo");
    expect(course.chapters.map((c) => c.slug)).toEqual(["premier", "second"]);
    expect(course.chapters[0].kind).toBe("chapter");
    expect(course.chapters[1].kind).toBe("td");
    expect(course.chapters[1].minutes).toBe(20);
  });

  it("renders the items referenced by the chapters", async () => {
    const bundle = await buildContent(path.join(fixtures, "content"));
    expect(Object.keys(bundle.items).sort()).toEqual(["demo-n1", "demo-q1"]);
    expect(bundle.items["demo-n1"].type).toBe("numeric");
    expect(bundle.courses[0].chapters[0].itemIds).toEqual(["demo-q1"]);
  });

  it("loads python labs with starter, solution and test files", async () => {
    const bundle = await buildContent(path.join(fixtures, "content"));
    const lab = bundle.pylabs["demo-lab"];
    expect(lab.filename).toBe("demo.py");
    expect(lab.solution).toContain("return 2 * x");
    expect(lab.testFiles[0].name).toBe("test_demo.py");
  });

  it("fails when a chapter references an unknown item", async () => {
    await expect(buildContent(path.join(fixtures, "broken"))).rejects.toThrow(/nope/);
  });
});
