export type Segment =
  | { type: "html"; html: string }
  | { type: "item"; id: string }
  | { type: "pylab"; id: string };

export type TocEntry = { id: string; text: string; level: 2 | 3 };

export type ChapterKind = "chapter" | "td" | "sheet" | "project" | "exam";

export type Chapter = {
  slug: string;
  order: number;
  kind: ChapterKind;
  title: string;
  summary: string;
  tags: string[];
  minutes: number;
  segments: Segment[];
  toc: TocEntry[];
  itemIds: string[];
};

export type Course = {
  slug: string;
  subject: string;
  title: string;
  description: string;
  tags: string[];
  updated: string;
  accent: string;
  chapters: Chapter[];
};

export type QcmOption = { html: string; correct: boolean; whyHtml: string };

export type Item =
  | {
      id: string;
      type: "qcm";
      multi: boolean;
      promptHtml: string;
      options: QcmOption[];
      explanationHtml?: string;
    }
  | {
      id: string;
      type: "numeric";
      promptHtml: string;
      answer: number;
      tolerance: number;
      unit?: string;
      explanationHtml: string;
    }
  | {
      id: string;
      type: "truefalse";
      promptHtml: string;
      statements: { html: string; answer: boolean; whyHtml: string }[];
    };

export type PyLab = {
  id: string;
  title: string;
  filename: string;
  starter: string;
  solution: string;
  testFiles: { name: string; code: string }[];
  questions: { fn: string; title: string }[];
};

export type ContentBundle = {
  courses: Course[];
  items: Record<string, Item>;
  pylabs: Record<string, PyLab>;
};
