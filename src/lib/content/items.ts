import { parse } from "yaml";
import { renderInlineMarkdown } from "./markdown";
import type { Item } from "./types";

/** Forme brute d'un exercice auto-corrigé, telle qu'écrite dans les fichiers *.items.yaml. */
export type RawItem =
  | {
      id: string;
      type: "qcm";
      multi?: boolean;
      prompt: string;
      options: { text: string; correct?: boolean; why: string }[];
      explanation?: string;
      verify?: unknown;
    }
  | {
      id: string;
      type: "numeric";
      prompt: string;
      answer: number;
      tolerance?: number;
      unit?: string;
      explanation: string;
      verify?: unknown;
    }
  | {
      id: string;
      type: "truefalse";
      prompt: string;
      statements: { text: string; answer: boolean; why: string; verify?: unknown }[];
    };

const isText = (v: unknown): v is string => typeof v === "string" && v.trim().length > 0;

// Entre guillemets doubles, YAML interprète \n, \a, \b, \t, \f, \e, \L, \P… : « $\neg$ » devient
// « $<saut de ligne>eg$ ». Ces caractères n'ont rien à faire dans un énoncé : on les refuse.
const CONTROL = /[\u0000-\u0008\u000b-\u001f\u0085\u2028\u2029]/;
const BROKEN_INLINE_MATH = /(?<!\$)\$(?!\$)[^$]*[\n\t][^$]*\$/;

function findBadEscape(value: unknown): string | undefined {
  if (typeof value === "string") {
    if (CONTROL.test(value) || BROKEN_INLINE_MATH.test(value)) return value.slice(0, 60);
    return undefined;
  }
  if (Array.isArray(value)) {
    for (const v of value) {
      const bad = findBadEscape(v);
      if (bad) return bad;
    }
  } else if (value && typeof value === "object") {
    for (const v of Object.values(value)) {
      const bad = findBadEscape(v);
      if (bad) return bad;
    }
  }
  return undefined;
}

export function parseItemsYaml(source: string, file: string): RawItem[] {
  const data = parse(source) as unknown;
  if (!Array.isArray(data)) throw new Error(`${file} : la racine doit être une liste d'exercices`);

  return data.map((entry: Record<string, unknown>, index) => {
    const where = `${file} [${index}] ${entry?.id ?? ""}`;
    const fail = (msg: string): never => {
      throw new Error(`${where} : ${msg}`);
    };
    const bad = findBadEscape(entry);
    if (bad) fail(`échappement YAML suspect (double les \\ entre guillemets) dans « ${bad.replace(/\s/g, "␣")} »`);
    if (!isText(entry?.id)) fail("id manquant");
    if (!isText(entry.prompt)) fail("prompt manquant");

    switch (entry.type) {
      case "qcm": {
        const options = entry.options as { text?: unknown; correct?: unknown; why?: unknown }[];
        if (!Array.isArray(options) || options.length < 2) fail("au moins 2 options");
        options.forEach((o, i) => {
          if (!isText(o?.text) && typeof o?.text !== "number") fail(`option ${i + 1} sans text`);
          if (!isText(o.why)) fail(`option ${i + 1} sans why (explication obligatoire)`);
        });
        const correct = options.filter((o) => o.correct === true).length;
        if (correct === 0) fail("aucune bonne réponse");
        if (correct > 1 && entry.multi !== true) fail("plusieurs bonnes réponses : ajouter multi: true");
        return {
          ...entry,
          options: options.map((o) => ({ ...o, text: String(o.text) })),
        } as RawItem;
      }
      case "numeric": {
        if (typeof entry.answer !== "number" || Number.isNaN(entry.answer)) fail("answer numérique manquant");
        if (!isText(entry.explanation)) fail("explanation manquante");
        return entry as RawItem;
      }
      case "truefalse": {
        const statements = entry.statements as { text?: unknown; answer?: unknown; why?: unknown }[];
        if (!Array.isArray(statements) || statements.length === 0) fail("statements manquants");
        statements.forEach((s, i) => {
          if (!isText(s?.text)) fail(`affirmation ${i + 1} sans text`);
          if (typeof s.answer !== "boolean") fail(`affirmation ${i + 1} : answer doit valoir true ou false`);
          if (!isText(s.why)) fail(`affirmation ${i + 1} sans why`);
        });
        return entry as RawItem;
      }
      default:
        return fail(`type inconnu « ${String(entry.type)} » (qcm | numeric | truefalse)`);
    }
  });
}

export async function renderItem(raw: RawItem): Promise<Item> {
  const md = renderInlineMarkdown;
  switch (raw.type) {
    case "qcm":
      return {
        id: raw.id,
        type: "qcm",
        multi: raw.multi === true,
        promptHtml: await md(raw.prompt),
        options: await Promise.all(
          raw.options.map(async (o) => ({
            html: await md(o.text),
            correct: o.correct === true,
            whyHtml: await md(o.why),
          })),
        ),
        explanationHtml: raw.explanation ? await md(raw.explanation) : undefined,
      };
    case "numeric":
      return {
        id: raw.id,
        type: "numeric",
        promptHtml: await md(raw.prompt),
        answer: raw.answer,
        tolerance: raw.tolerance ?? 0,
        unit: raw.unit,
        explanationHtml: await md(raw.explanation),
      };
    case "truefalse":
      return {
        id: raw.id,
        type: "truefalse",
        promptHtml: await md(raw.prompt),
        statements: await Promise.all(
          raw.statements.map(async (s) => ({
            html: await md(s.text),
            answer: s.answer,
            whyHtml: await md(s.why),
          })),
        ),
      };
  }
}
