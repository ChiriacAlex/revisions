"use client";

import { useEffect, useState } from "react";
import { doneKey, itemKey, readStored, useStored, type ItemRecord } from "@/lib/storage";

type ChapterRef = { slug: string; itemIds: string[] };

function chapterScore(course: string, chapter: ChapterRef) {
  const done = readStored<boolean>(doneKey(course, chapter.slug), false);
  const ok = chapter.itemIds.filter((id) => readStored<ItemRecord | null>(itemKey(id), null)?.status === "ok").length;
  return { done, ok, total: chapter.itemIds.length };
}

function useTick() {
  const [tick, setTick] = useState(0);
  useEffect(() => {
    const bump = () => setTick((t) => t + 1);
    bump();
    window.addEventListener("revisions:storage", bump);
    window.addEventListener("storage", bump);
    return () => {
      window.removeEventListener("revisions:storage", bump);
      window.removeEventListener("storage", bump);
    };
  }, []);
  return tick;
}

/** Barre de progression d'un cours : chapitres marqués « lu » sur le total. */
export function CourseProgress({ course, chapters }: { course: string; chapters: ChapterRef[] }) {
  const tick = useTick();
  if (tick === 0) return <div className="progress" aria-hidden><span style={{ width: 0 }} /></div>;
  const done = chapters.filter((c) => chapterScore(course, c).done).length;
  const pct = chapters.length ? Math.round((100 * done) / chapters.length) : 0;
  return (
    <div title={`${done}/${chapters.length} chapitres terminés`}>
      <div className="progress">
        <span style={{ width: `${pct}%` }} />
      </div>
      <span className="meta">
        {done}/{chapters.length} terminés
      </span>
    </div>
  );
}

export function ChapterStatus({ course, chapter }: { course: string; chapter: ChapterRef }) {
  const tick = useTick();
  if (tick === 0) return null;
  const { done, ok, total } = chapterScore(course, chapter);
  return (
    <>
      {total > 0 && (
        <>
          {ok}/{total} exos auto
          <br />
        </>
      )}
      {done ? "✓ terminé" : ""}
    </>
  );
}

export function DoneToggle({ course, chapter }: { course: string; chapter: string }) {
  const [done, setDone, loaded] = useStored<boolean>(doneKey(course, chapter), false);
  if (!loaded) return null;
  return (
    <div className="done-toggle">
      <button className={done ? "is-done" : ""} onClick={() => setDone(done ? undefined : true)}>
        {done ? "✓ Chapitre terminé" : "Marquer ce chapitre comme terminé"}
      </button>
    </div>
  );
}

export function DoneMarker({ course, chapter }: { course: string; chapter: string }) {
  const tick = useTick();
  if (tick === 0) return null;
  return readStored<boolean>(doneKey(course, chapter), false) ? <span aria-label="terminé">✓</span> : null;
}
