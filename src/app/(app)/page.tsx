import Link from "next/link";
import { getCourses } from "@/lib/content";
import { CourseProgress } from "@/components/Progress";

export default function Dashboard() {
  const courses = getCourses();
  return (
    <main className="page">
      <h1>Mes cours</h1>
      <p className="page-lead">
        Cours rédigés, exercices auto-corrigés, TD corrigés pas à pas et fiches de révision. La progression est
        enregistrée sur cet appareil.
      </p>
      <div className="course-grid">
        {courses.map((course) => (
          <Link
            key={course.slug}
            href={`/courses/${course.slug}`}
            className="course-card"
            style={{ "--card-accent": course.accent } as React.CSSProperties}
          >
            <span className="subject">{course.subject}</span>
            <h2>{course.title}</h2>
            <p>{course.description}</p>
            <span className="meta">
              {course.chapters.length} parties · mis à jour le {course.updated}
            </span>
            <div className="tags">
              {course.tags.map((tag) => (
                <span key={tag} className="tag">
                  {tag}
                </span>
              ))}
            </div>
            <CourseProgress
              course={course.slug}
              chapters={course.chapters.map((c) => ({ slug: c.slug, itemIds: c.itemIds }))}
            />
          </Link>
        ))}
      </div>
    </main>
  );
}
