import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkDirective from "remark-directive";
import remarkRehype from "remark-rehype";
import rehypeRaw from "rehype-raw";
import rehypeSlug from "rehype-slug";
import rehypeKatex from "rehype-katex";
import rehypeStringify from "rehype-stringify";
import { visit } from "unist-util-visit";
import type { Root as MdastRoot, Paragraph, PhrasingContent, RootContent } from "mdast";
import type { Root as HastRoot, Element } from "hast";
import type { Segment, TocEntry } from "./types";

/** Encadrés colorés : nom de directive → libellé affiché. */
const CALLOUTS: Record<string, string> = {
  definition: "Définition",
  theorem: "Théorème",
  property: "Propriété",
  method: "Méthode",
  warning: "Attention",
  key: "À retenir",
  note: "Remarque",
  example: "Exemple",
  intuition: "Intuition",
  pattern: "Motif de preuve",
  recall: "Rappel",
  exercise: "Exercice",
  exam: "Annale",
};

/** Blocs repliés : nom de directive → texte du bouton par défaut. */
const REVEALS: Record<string, string> = {
  correction: "Voir la correction",
  solution: "Voir la solution",
  hint: "Indice",
  skeleton: "Squelette de preuve",
  more: "Pour aller plus loin",
};

const SLOTS = new Set(["item", "pylab"]);

type DirectiveNode = {
  type: "containerDirective" | "leafDirective" | "textDirective";
  name: string;
  attributes?: Record<string, string | null | undefined> | null;
  children: RootContent[];
  data?: Record<string, unknown>;
};

function takeLabel(node: DirectiveNode): PhrasingContent[] | undefined {
  const first = node.children[0] as Paragraph | undefined;
  if (first && first.type === "paragraph" && (first.data as { directiveLabel?: boolean } | undefined)?.directiveLabel) {
    node.children.shift();
    return first.children;
  }
  return undefined;
}

function text(value: string): PhrasingContent {
  return { type: "text", value };
}

function span(className: string, children: PhrasingContent[]): PhrasingContent {
  return {
    type: "emphasis",
    children,
    data: { hName: "span", hProperties: { className: [className] } },
  } as PhrasingContent;
}

function remarkCourseDirectives() {
  return (tree: MdastRoot, file: { fail: (msg: string) => never }) => {
    visit(tree, (raw, index, parent) => {
      const node = raw as unknown as DirectiveNode;
      if (node.type === "textDirective") {
        // Pas de directives en ligne : on restaure le texte tel quel (ex. « 16:30 », « f:E »).
        const restored: PhrasingContent[] = [text(`:${node.name}`)];
        if (node.children.length) restored.push(text("["), ...(node.children as PhrasingContent[]), text("]"));
        (parent as { children: RootContent[] }).children.splice(index!, 1, ...restored);
        return index! + restored.length;
      }
      if (node.type !== "containerDirective" && node.type !== "leafDirective") return;

      if (node.type === "leafDirective" && SLOTS.has(node.name)) {
        const id = node.attributes?.id;
        if (!id) file.fail(`::${node.name} sans id`);
        node.data = {
          hName: "div",
          hProperties: { dataSlot: node.name, dataId: id },
        };
        node.children = [];
        return;
      }

      const name = node.name;
      const label = takeLabel(node);
      const data = (node.data ??= {});

      if (name in CALLOUTS) {
        const kind = CALLOUTS[name];
        const titleChildren: PhrasingContent[] =
          name === "exercise" || name === "exam"
            ? label ?? [text(kind)]
            : [span("callout-kind", [text(kind)]), ...(label ? [text(" — "), ...label] : [])];
        const title: Paragraph = {
          type: "paragraph",
          children: titleChildren,
          data: { hProperties: { className: ["callout-title"] } },
        };
        node.children.unshift(title);
        data.hName = "div";
        data.hProperties = {
          className: ["callout", `callout-${name}`],
          ...(node.attributes?.id ? { id: node.attributes.id } : {}),
        };
        return;
      }

      if (name in REVEALS) {
        const summary: Paragraph = {
          type: "paragraph",
          children: label ?? [text(REVEALS[name])],
          data: { hName: "summary" },
        };
        node.children.unshift(summary);
        data.hName = "details";
        data.hProperties = { className: ["reveal", `reveal-${name}`] };
        return;
      }

      file.fail(`Directive inconnue : ${node.type === "leafDirective" ? "::" : ":::"}${name}`);
    });
  };
}

function rehypeCollectToc(toc: TocEntry[]) {
  return (tree: HastRoot) => {
    visit(tree, "element", (node: Element) => {
      if ((node.tagName === "h2" || node.tagName === "h3") && typeof node.properties?.id === "string") {
        toc.push({
          id: node.properties.id,
          text: plainText(node).trim(),
          level: node.tagName === "h2" ? 2 : 3,
        });
      }
    });
  };
}

function plainText(node: Element | HastRoot): string {
  let out = "";
  visit(node, (child) => {
    if (child.type === "text") out += (child as { value: string }).value;
    // Pour un titre contenant des maths, on garde l'annotation TeX plutôt que le rendu.
    if (child.type === "element" && (child as Element).tagName === "annotation") {
      out += ((child as Element).children[0] as { value?: string })?.value ?? "";
      return "skip";
    }
    if (child.type === "element" && (child as Element).properties?.className?.toString().includes("katex-html")) {
      return "skip";
    }
  });
  return out;
}

function pipeline(toc: TocEntry[]) {
  return unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkMath)
    .use(remarkDirective)
    .use(remarkCourseDirectives)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeSlug)
    .use(rehypeCollectToc, toc)
    .use(rehypeKatex, { strict: false, trust: false, output: "htmlAndMathml" })
    .use(rehypeStringify);
}

const SLOT_RE = /<div data-slot="(item|pylab)" data-id="([^"]+)"><\/div>/g;

/** Une ligne qui n'est qu'une formule `$$…$$` devient un bloc centré (comme en LaTeX). */
function normalizeDisplayMath(source: string): string {
  return source.replace(/^([ \t]*)\$\$(.+)\$\$[ \t]*$/gm, (_m, indent: string, body: string) =>
    `${indent}$$\n${indent}${body.trim()}\n${indent}$$`,
  );
}

export async function renderChapterMarkdown(source: string): Promise<{ segments: Segment[]; toc: TocEntry[] }> {
  const toc: TocEntry[] = [];
  const html = String(await pipeline(toc).process(normalizeDisplayMath(source)));
  const segments: Segment[] = [];
  let last = 0;
  for (const match of html.matchAll(SLOT_RE)) {
    const before = html.slice(last, match.index).trim();
    if (before) segments.push({ type: "html", html: before });
    segments.push({ type: match[1] as "item" | "pylab", id: match[2] });
    last = (match.index ?? 0) + match[0].length;
  }
  const rest = html.slice(last).trim();
  if (rest) segments.push({ type: "html", html: rest });
  return { segments, toc };
}

/** Pour les champs courts (énoncés de quiz, options…) : pas de <p> autour d'une ligne unique. */
export async function renderInlineMarkdown(source: string): Promise<string> {
  const html = String(await pipeline([]).process(source)).trim();
  const single = html.match(/^<p>([\s\S]*)<\/p>$/);
  if (single && !single[1].includes("<p>")) return single[1];
  return html;
}
