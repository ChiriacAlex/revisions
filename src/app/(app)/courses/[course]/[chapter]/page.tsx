import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getChapter } from "@/lib/content";
import { ItemView } from "@/components/items/ItemView";
import { PyLabView } from "@/components/pylab/PyLabView";
import { DoneToggle } from "@/components/Progress";
import type { TocEntry } from "@/lib/content/types";

type Params = { course: string; chapter: string };


export async function generateMetadata({ params }: { params: Promise<Params> }): Promise<Metadata> {
  const { course, chapter } = await params;
  return { title: getChapter(course, chapter)?.chapter.title ?? "Chapitre" };
}

function Toc({ toc }: { toc: TocEntry[] }) {
  return (
    <ol>
      {toc.map((entry) => (
        <li key={entry.id} className={`lvl-${entry.level}`}>
          <a href={`#${entry.id}`}>{entry.text}</a>
        </li>
      ))}
    </ol>
  );
}

export default async function ChapterPage({ params }: { params: Promise<Params> }) {
  const { course: courseSlug, chapter: chapterSlug } = await params;
  const found = getChapter(courseSlug, chapterSlug);
  if (!found) notFound();
  const { course, chapter, index } = found;
  const prev = course.chapters[index - 1];
  const next = course.chapters[index + 1];
  const mainToc = chapter.toc.filter((t) => t.level === 2);

  return (
    <div className="chapter-layout">
      <main className="chapter-main">
        <nav className="breadcrumb">
          <Link href="/">Cours</Link>
          <span>/</span>
          <Link href={`/courses/${course.slug}`}>{course.title}</Link>
        </nav>
        <header className="chapter-header">
          <span className="subject">{course.subject}</span>
          <h1>{chapter.title}</h1>
          <p>{chapter.summary}</p>
        </header>

        {mainToc.length > 2 && (
          <details className="reveal toc-inline">
            <summary>Sommaire</summary>
            <Toc toc={mainToc} />
          </details>
        )}

        <article className="prose">
          {chapter.segments.map((segment, i) => {
            if (segment.type === "html") return <div key={i} dangerouslySetInnerHTML={{ __html: segment.html }} />;
            if (segment.type === "item") return <ItemView key={i} id={segment.id} />;
            return <PyLabView key={i} id={segment.id} />;
          })}
        </article>

        <DoneToggle course={course.slug} chapter={chapter.slug} />

        <nav className="chapter-nav">
          {prev && (
            <Link href={`/courses/${course.slug}/${prev.slug}`}>
              <small>← Précédent</small>
              {prev.title}
            </Link>
          )}
          {next && (
            <Link href={`/courses/${course.slug}/${next.slug}`} className="next">
              <small>Suivant →</small>
              {next.title}
            </Link>
          )}
        </nav>
      </main>
      {chapter.toc.length > 0 && (
        <aside className="toc-aside">
          <h2>Sommaire</h2>
          <Toc toc={chapter.toc} />
        </aside>
      )}
    </div>
  );
}
