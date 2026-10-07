import { describe, expect, it } from "vitest";
import { renderChapterMarkdown, renderInlineMarkdown } from "@/lib/content/markdown";

describe("chapter markdown", () => {
  it("renders inline and display math with KaTeX on the server", async () => {
    const { segments } = await renderChapterMarkdown("Soit $x \\in E$.\n\n$$A \\subseteq B$$\n");
    const html = segments.map((s) => (s.type === "html" ? s.html : "")).join("");
    expect(html).toContain('class="katex"');
    expect(html).toContain("katex-display");
  });

  it("turns a definition directive into a titled callout", async () => {
    const md = ":::definition[Ensemble vide]\nAucun élément n'appartient à $\\emptyset$.\n:::\n";
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain('class="callout callout-definition"');
    expect(html).toContain("Définition");
    expect(html).toContain("Ensemble vide");
  });

  it("turns a correction directive into a collapsed details block", async () => {
    const md = ":::correction\nLa réponse est 42.\n:::\n";
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toMatch(/<details class="reveal reveal-correction"><summary>Voir la correction<\/summary>/);
    expect(html).toContain("La réponse est 42.");
  });

  it("uses the label as the summary of a hint", async () => {
    const md = ":::hint[Indice 1]\nPense à la contraposée.\n:::\n";
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain("<summary>Indice 1</summary>");
  });

  it("splits the page around interactive item slots", async () => {
    const md = "Avant.\n\n::item{id=\"sets-q1\"}\n\nAprès.\n";
    const { segments } = await renderChapterMarkdown(md);
    expect(segments.map((s) => s.type)).toEqual(["html", "item", "html"]);
    expect(segments[1]).toEqual({ type: "item", id: "sets-q1" });
  });

  it("supports python lab slots", async () => {
    const { segments } = await renderChapterMarkdown('::pylab{id="folo"}\n');
    expect(segments).toEqual([{ type: "pylab", id: "folo" }]);
  });

  it("builds a table of contents from h2/h3 with stable ids", async () => {
    const md = "## 1. Les ensembles\n\ntexte\n\n### 1.1 Union\n\ntexte\n";
    const { toc, segments } = await renderChapterMarkdown(md);
    expect(toc).toEqual([
      { id: "1-les-ensembles", text: "1. Les ensembles", level: 2 },
      { id: "11-union", text: "1.1 Union", level: 3 },
    ]);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain('<h2 id="1-les-ensembles">');
  });

  it("renders a proof pattern box with goal and subgoals", async () => {
    const md = ":::pattern[Double inclusion]\n**But.** Montrer que $A = B$.\n:::\n";
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain('class="callout callout-pattern"');
    expect(html).toContain("Double inclusion");
  });

  it("keeps raw HTML such as inline SVG figures", async () => {
    const md = '<figure><svg viewBox="0 0 10 10"><circle cx="5" cy="5" r="4"></circle></svg><figcaption>Un cercle</figcaption></figure>\n';
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain("<svg");
    expect(html).toContain("<figcaption>Un cercle</figcaption>");
  });

  it("renders GFM tables", async () => {
    const md = "| a | b |\n|---|---|\n| 1 | 2 |\n";
    const { segments } = await renderChapterMarkdown(md);
    const html = segments[0].type === "html" ? segments[0].html : "";
    expect(html).toContain("<table>");
  });
});

describe("inline markdown", () => {
  it("renders math and emphasis without a wrapping paragraph for one-liners", async () => {
    const html = await renderInlineMarkdown("**Vrai** : $A \\cup \\emptyset = A$");
    expect(html).toContain("<strong>Vrai</strong>");
    expect(html).toContain('class="katex"');
    expect(html.startsWith("<p>")).toBe(false);
  });
});

describe("robustness", () => {
  it("leaves colon-separated text untouched (no inline directives)", async () => {
    const html = await renderInlineMarkdown("Il est 16:30 et f:E vers F");
    expect(html).toBe("Il est 16:30 et f:E vers F");
  });

  it("fails loudly on an unknown block directive (typo protection)", async () => {
    await expect(renderChapterMarkdown(":::definiton\nx\n:::\n")).rejects.toThrow(/inconnue/);
  });
});
