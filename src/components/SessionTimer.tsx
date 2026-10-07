"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

/** Affiche le temps restant ; à l'expiration (1 h après le PIN), retour à l'écran de connexion. */
export function SessionTimer({ expiresAt }: { expiresAt: string }) {
  const end = new Date(expiresAt).getTime();
  const [left, setLeft] = useState<number | null>(null);
  const router = useRouter();

  useEffect(() => {
    const tick = () => {
      const remaining = end - Date.now();
      setLeft(remaining);
      if (remaining <= 0) router.replace(`/login?next=${encodeURIComponent(window.location.pathname)}`);
    };
    tick();
    const timer = window.setInterval(tick, 15_000);
    return () => window.clearInterval(timer);
  }, [end, router]);

  if (left === null) return null;
  const minutes = Math.max(0, Math.ceil(left / 60_000));
  return (
    <span className={`session-timer${minutes <= 5 ? " is-low" : ""}`} title="Le code PIN sera redemandé à la fin de la session">
      Session : {minutes} min
    </span>
  );
}
