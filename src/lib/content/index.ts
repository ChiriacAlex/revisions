import "server-only";
import bundle from "@/generated/content.json";
import type { Chapter, ContentBundle, Course, Item, PyLab } from "./types";

const content = bundle as unknown as ContentBundle;

export function getCourses(): Course[] {
  return content.courses;
}

export function getCourse(slug: string): Course | undefined {
  return content.courses.find((c) => c.slug === slug);
}

export function getChapter(courseSlug: string, chapterSlug: string): { course: Course; chapter: Chapter; index: number } | undefined {
  const course = getCourse(courseSlug);
  if (!course) return undefined;
  const index = course.chapters.findIndex((c) => c.slug === chapterSlug);
  if (index === -1) return undefined;
  return { course, chapter: course.chapters[index], index };
}

export function getItem(id: string): Item | undefined {
  return content.items[id];
}

export function getPyLab(id: string): PyLab | undefined {
  return content.pylabs[id];
}
