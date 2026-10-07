"use client";

import { useCallback, useEffect, useState } from "react";

/** Progression stockée dans le navigateur (par appareil) : simple confort, jamais critique. */
const EVENT = "revisions:storage";

export function readStored<T>(key: string, fallback: T): T {
  try {
    const raw = window.localStorage.getItem(key);
    return raw === null ? fallback : (JSON.parse(raw) as T);
  } catch {
    return fallback;
  }
}

export function writeStored<T>(key: string, value: T | undefined): void {
  try {
    if (value === undefined) window.localStorage.removeItem(key);
    else window.localStorage.setItem(key, JSON.stringify(value));
    window.dispatchEvent(new CustomEvent(EVENT, { detail: key }));
  } catch {
    /* stockage indisponible (navigation privée…) : on continue sans mémoriser */
  }
}

export function useStored<T>(key: string, initial: T): [T, (value: T | undefined) => void, boolean] {
  const [value, setValue] = useState<T>(initial);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    // Lecture après le montage pour éviter les écarts d'hydratation serveur/client.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setValue(readStored(key, initial));
    setLoaded(true);
    const sync = (event: Event) => {
      const changed = (event as CustomEvent<string>).detail;
      if (changed === undefined || changed === key) setValue(readStored(key, initial));
    };
    window.addEventListener(EVENT, sync);
    window.addEventListener("storage", sync);
    return () => {
      window.removeEventListener(EVENT, sync);
      window.removeEventListener("storage", sync);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  const update = useCallback(
    (next: T | undefined) => {
      setValue(next === undefined ? initial : next);
      writeStored(key, next);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [key],
  );

  return [value, update, loaded];
}

export type ItemRecord = { status: "ok" | "ko"; at: number; answer?: unknown };
export const itemKey = (id: string) => `rev:item:${id}`;
export const doneKey = (course: string, chapter: string) => `rev:done:${course}/${chapter}`;
