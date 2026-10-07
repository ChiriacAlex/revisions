import { readFile, readdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { parse } from "yaml";
import { renderChapterMarkdown } from "./markdown";
import { parseItemsYaml, renderItem, type RawItem } from "./items";
import type { Chapter, ChapterKind, ContentBundle, Course, Item, PyLab } from "./types";

const KINDS: ChapterKind[] = ["chapter", "td", "sheet", "project", "exam"];

type CourseMeta = Omit<Course, "chapters">;

async function loadPyLabs(dir: string): Promise<PyLab[]> {
  const file = path.join(dir, "pylabs.yaml");
  if (!existsSync(file)) return [];
  const raw = parse(await readFile(file, "utf8")) as {
    id: string;
    title: string;
    filename: string;
    starter: string;
    solution: string;
    tests: string[];
    questions: { fn: string; title: string }[];
  }[];
  return Promise.all(
    raw.map(async (lab) => ({
      id: lab.id,
      title: lab.title,
      filename: lab.filename,
      starter: await readFile(path.join(dir, lab.starter), "utf8"),
      solution: await readFile(path.join(dir, lab.solution), "utf8"),
      testFiles: await Promise.all(
        lab.tests.map(async (t) => ({ name: path.basename(t), code: await readFile(path.join(dir, t), "utf8") })),
      ),
      questions: lab.questions,
    })),
  );
}

export async function buildContent(root: string): Promise<ContentBundle> {
  const metas = parse(await readFile(path.join(root, "courses.yaml"), "utf8")) as CourseMeta[];
  const items: Record<string, Item> = {};
  const pylabs: Record<string, PyLab> = {};
  const courses: Course[] = [];

  for (const meta of metas) {
    const dir = path.join(root, meta.slug);
    const files = (await readdir(dir)).sort();
    const rawItems = new Map<string, RawItem>();

    for (const file of files.filter((f) => f.endsWith(".items.yaml"))) {
      for (const item of parseItemsYaml(await readFile(path.join(dir, file), "utf8"), `${meta.slug}/${file}`)) {
        if (rawItems.has(item.id) || items[item.id]) throw new Error(`Exercice en double : ${item.id}`);
        rawItems.set(item.id, item);
      }
    }
    for (const lab of await loadPyLabs(dir)) pylabs[lab.id] = lab;

    const chapters: Chapter[] = [];
    const used = new Set<string>();
    for (const file of files.filter((f) => f.endsWith(".md"))) {
      const match = file.match(/^(\d+)-(.+)\.md$/);
      if (!match) throw new Error(`${meta.slug}/${file} : nom attendu NN-slug.md`);
      const { data, content } = matter(await readFile(path.join(dir, file), "utf8"));
      const where = `${meta.slug}/${file}`;
      if (!data.title || !data.summary) throw new Error(`${where} : title et summary obligatoires`);
      const kind = (data.kind ?? "chapter") as ChapterKind;
      if (!KINDS.includes(kind)) throw new Error(`${where} : kind inconnu ${kind}`);

      let rendered;
      try {
        rendered = await renderChapterMarkdown(content);
      } catch (error) {
        throw new Error(`${where} : ${(error as Error).message}`);
      }
      const itemIds: string[] = [];
      for (const segment of rendered.segments) {
        if (segment.type === "item") {
          if (!rawItems.has(segment.id)) throw new Error(`${where} : exercice inconnu « ${segment.id} »`);
          used.add(segment.id);
          itemIds.push(segment.id);
        }
        if (segment.type === "pylab" && !pylabs[segment.id]) {
          throw new Error(`${where} : labo Python inconnu « ${segment.id} »`);
        }
      }
      const html = rendered.segments.map((s) => (s.type === "html" ? s.html : "")).join("");
      if (html.includes("katex-error")) throw new Error(`${where} : formule LaTeX invalide`);

      chapters.push({
        slug: match[2],
        order: Number(match[1]),
        kind,
        title: String(data.title),
        summary: String(data.summary),
        tags: (data.tags as string[] | undefined) ?? [],
        minutes: Number(data.minutes ?? 0),
        segments: rendered.segments,
        toc: rendered.toc,
        itemIds,
      });
    }

    const unused = [...rawItems.keys()].filter((id) => !used.has(id));
    if (unused.length) throw new Error(`${meta.slug} : exercices jamais affichés : ${unused.join(", ")}`);

    for (const raw of rawItems.values()) {
      const item = await renderItem(raw);
      const html = JSON.stringify(item);
      if (html.includes("katex-error")) throw new Error(`${raw.id} : formule LaTeX invalide`);
      items[raw.id] = item;
    }

    chapters.sort((a, b) => a.order - b.order);
    courses.push({ ...meta, updated: String(meta.updated), chapters });
  }

  return { courses, items, pylabs };
}
