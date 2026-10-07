import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getCourse } from "@/lib/content";
import type { ChapterKind } from "@/lib/content/types";
import { ChapterStatus, CourseProgress } from "@/components/Progress";

const GROUPS: { kind: ChapterKind; label: string }[] = [
  { kind: "chapter", label: "Cours" },
  { kind: "sheet", label: "Fiches de révision" },
  { kind: "td", label: "TD corrigés" },
  { kind: "project", label: "Projet" },
  { kind: "exam", label: "Entraînement examen" },
];


export async function generateMetadata({ params }: { params: Promise<{ course: string }> }): Promise<Metadata> {
  const course = getCourse((await params).course);
  return { title: course?.title ?? "Cours" };
}

export default async function CoursePage({ params }: { params: Promise<{ course: string }> }) {
  const course = getCourse((await params).course);
  if (!course) notFound();

  return (
    <main className="page">
      <nav className="breadcrumb">
        <Link href="/">← Tous les cours</Link>
      </nav>
      <span className="subject">{course.subject}</span>
      <h1>{course.title}</h1>
      <p className="page-lead">{course.description}</p>
      <div style={{ maxWidth: 360 }}>
        <CourseProgress course={course.slug} chapters={course.chapters.map((c) => ({ slug: c.slug, itemIds: c.itemIds }))} />
      </div>

      {GROUPS.map(({ kind, label }) => {
        const chapters = course.chapters.filter((c) => c.kind === kind);
        if (chapters.length === 0) return null;
        return (
          <section key={kind} className="chapter-group">
            <h2>{label}</h2>
            <ol className="chapter-list">
              {chapters.map((chapter) => (
                <li key={chapter.slug}>
                  <Link href={`/courses/${course.slug}/${chapter.slug}`} className="chapter-row">
                    <span className="chapter-num">{kind === "chapter" ? chapter.order : kind === "td" ? "TD" : "★"}</span>
                    <span>
                      <strong>{chapter.title}</strong>
                      <small>{chapter.summary}</small>
                    </span>
                    <span className="chapter-side">
                      {chapter.minutes > 0 && (
                        <>
                          ~{chapter.minutes} min
                          <br />
                        </>
                      )}
                      <ChapterStatus course={course.slug} chapter={{ slug: chapter.slug, itemIds: chapter.itemIds }} />
                    </span>
                  </Link>
                </li>
              ))}
            </ol>
          </section>
        );
      })}
    </main>
  );
}
