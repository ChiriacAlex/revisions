import { describe, expect, it } from "vitest";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

describe("KaTeX", () => {
  it("uses the same version for the CSS and for the server-side renderer", () => {
    const cssVersion = require("katex/package.json").version;
    const rehypeKatexDir = require.resolve("rehype-katex");
    const rendererVersion = createRequire(rehypeKatexDir)("katex/package.json").version;
    expect(cssVersion).toBe(rendererVersion);
  });
});
