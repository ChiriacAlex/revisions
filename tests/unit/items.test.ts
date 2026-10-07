import { describe, expect, it } from "vitest";
import { parseItemsYaml, renderItem } from "@/lib/content/items";

describe("items validation", () => {
  it("accepts a well-formed single-answer qcm", () => {
    const items = parseItemsYaml(
      `- id: q1
  type: qcm
  prompt: Combien ?
  options:
    - text: "1"
      correct: true
      why: Parce que.
    - text: "2"
      why: Non.
`,
      "test.yaml",
    );
    expect(items).toHaveLength(1);
    expect(items[0].id).toBe("q1");
  });

  it("rejects a qcm without any correct option", () => {
    expect(() =>
      parseItemsYaml(
        `- id: q1
  type: qcm
  prompt: Combien ?
  options:
    - text: "1"
      why: a
    - text: "2"
      why: b
`,
        "t.yaml",
      ),
    ).toThrow(/q1.*bonne réponse/);
  });

  it("rejects a single-answer qcm with two correct options", () => {
    expect(() =>
      parseItemsYaml(
        `- id: q1
  type: qcm
  prompt: x
  options:
    - {text: a, correct: true, why: a}
    - {text: b, correct: true, why: b}
`,
        "t.yaml",
      ),
    ).toThrow(/q1.*multi/);
  });

  it("requires an explanation for every option", () => {
    expect(() =>
      parseItemsYaml(
        `- id: q1
  type: qcm
  prompt: x
  options:
    - {text: a, correct: true}
    - {text: b, why: b}
`,
        "t.yaml",
      ),
    ).toThrow(/q1.*why/);
  });

  it("requires a numeric answer and an explanation", () => {
    expect(() => parseItemsYaml(`- {id: n1, type: numeric, prompt: x, explanation: y}\n`, "t.yaml")).toThrow(/n1.*answer/);
    expect(() => parseItemsYaml(`- {id: n1, type: numeric, prompt: x, answer: 3}\n`, "t.yaml")).toThrow(/n1.*explanation/);
  });

  it("requires a boolean answer for each true/false statement", () => {
    expect(() =>
      parseItemsYaml(
        `- id: tf
  type: truefalse
  prompt: x
  statements:
    - {text: a, why: b}
`,
        "t.yaml",
      ),
    ).toThrow(/tf.*answer/);
  });

  it("rejects unknown types and missing ids", () => {
    expect(() => parseItemsYaml(`- {id: z, type: essay, prompt: x}\n`, "t.yaml")).toThrow(/z.*type/);
    expect(() => parseItemsYaml(`- {type: qcm, prompt: x}\n`, "t.yaml")).toThrow(/id/);
  });
});

describe("items rendering", () => {
  it("renders math in prompts, options and explanations", async () => {
    const [raw] = parseItemsYaml(
      `- id: q1
  type: qcm
  prompt: Que vaut $A \\cap \\emptyset$ ?
  options:
    - {text: "$\\\\emptyset$", correct: true, why: "Rien n'est dans $\\\\emptyset$."}
    - {text: "$A$", why: "Seulement si $A = \\\\emptyset$."}
`,
      "t.yaml",
    );
    const item = await renderItem(raw);
    expect(item.type).toBe("qcm");
    if (item.type !== "qcm") return;
    expect(item.promptHtml).toContain("katex");
    expect(item.options[0].html).toContain("katex");
    expect(item.options[0].whyHtml).toContain("katex");
    expect(item.multi).toBe(false);
  });
});
