"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import type { PyLab as PyLabData } from "@/lib/content/types";
import { summarize, type TestResult } from "@/lib/pylab";
import { readStored, writeStored } from "@/lib/storage";

const TIMEOUT_MS = 60_000;
// À incrémenter à chaque modification de public/pyodide-worker.js (contourne le cache du navigateur).
const WORKER_VERSION = 4;

type RunState =
  | { phase: "idle" }
  | { phase: "loading" }
  | { phase: "running" }
  | { phase: "done"; results: TestResult[]; output: string; ms: number }
  | { phase: "error"; message: string };

function useDarkMode() {
  const [dark, setDark] = useState(false);
  useEffect(() => {
    const media = window.matchMedia("(prefers-color-scheme: dark)");
    const update = () => setDark(media.matches);
    update();
    media.addEventListener("change", update);
    return () => media.removeEventListener("change", update);
  }, []);
  return dark;
}

export function PyLab({ lab }: { lab: PyLabData }) {
  const storageKey = `rev:pylab:${lab.id}`;
  const [code, setCode] = useState(lab.starter);
  const [state, setState] = useState<RunState>({ phase: "idle" });
  const [showSolution, setShowSolution] = useState(false);
  const workerRef = useRef<Worker | null>(null);
  const dark = useDarkMode();
  const fns = lab.questions.map((q) => q.fn);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setCode(readStored(storageKey, lab.starter));
  }, [storageKey, lab.starter]);

  useEffect(() => () => workerRef.current?.terminate(), []);

  const onChange = useCallback(
    (value: string) => {
      setCode(value);
      writeStored(storageKey, value);
    },
    [storageKey],
  );

  const run = () => {
    if (!workerRef.current) workerRef.current = new Worker(`${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/pyodide-worker.js?v=${WORKER_VERSION}`, { type: "module" });
    const worker = workerRef.current;
    const started = performance.now();
    const runId = Math.random().toString(36).slice(2);
    setState({ phase: "loading" });

    const timer = window.setTimeout(() => {
      worker.terminate();
      workerRef.current = null;
      setState({
        phase: "error",
        message: `Temps dépassé (${TIMEOUT_MS / 1000} s) : boucle infinie, ou algorithme trop lent (attention aux triples boucles).`,
      });
    }, TIMEOUT_MS);

    worker.onmessage = (event: MessageEvent) => {
      const data = event.data;
      if (data.id !== runId) return;
      if (data.type === "ready") setState({ phase: "running" });
      if (data.type === "done") {
        window.clearTimeout(timer);
        setState({
          phase: "done",
          results: data.payload.results,
          output: data.payload.output,
          ms: Math.round(performance.now() - started),
        });
      }
      if (data.type === "crash") {
        window.clearTimeout(timer);
        setState({ phase: "error", message: data.message });
      }
    };

    worker.postMessage({
      id: runId,
      files: [{ name: lab.filename, code }, ...lab.testFiles],
      testModules: lab.testFiles.map((f) => f.name.replace(/\.py$/, "")),
    });
  };

  const reset = () => {
    if (!window.confirm("Effacer ton code et repartir du modèle fourni ?")) return;
    onChange(lab.starter);
    setState({ phase: "idle" });
  };

  const download = () => {
    const blob = new Blob([code], { type: "text/x-python" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = lab.filename;
    a.click();
    URL.revokeObjectURL(url);
  };

  const summary = state.phase === "done" ? summarize(state.results, fns) : null;
  const failures = state.phase === "done" ? state.results.filter((r) => r.status !== "pass") : [];
  const passed = state.phase === "done" ? state.results.filter((r) => r.status === "pass").length : 0;

  return (
    <div className="pylab">
      <div className="pylab-bar">
        <strong>
          {lab.title} — <code>{lab.filename}</code>
        </strong>
        <button className="btn" onClick={run} disabled={state.phase === "loading" || state.phase === "running"}>
          {state.phase === "loading" ? "Chargement de Python…" : state.phase === "running" ? "Tests en cours…" : "▶ Lancer les tests"}
        </button>
        <button className="btn btn-ghost" onClick={download}>
          Télécharger
        </button>
        <button className="btn btn-ghost" onClick={reset}>
          Réinitialiser
        </button>
      </div>
      <div className="pylab-editor">
        <CodeMirror value={code} height="520px" extensions={[python()]} onChange={onChange} theme={dark ? "dark" : "light"} />
      </div>
      <div className="pylab-status">
        {state.phase === "idle" && "Écris tes fonctions puis lance les tests. Ton code est sauvegardé automatiquement sur cet appareil."}
        {state.phase === "loading" && "Premier lancement : téléchargement de Python dans le navigateur (quelques secondes)…"}
        {state.phase === "running" && "Exécution des tests…"}
        {state.phase === "error" && <span style={{ color: "var(--ko)" }}>{state.message}</span>}
        {state.phase === "done" && (
          <span>
            <strong style={{ color: failures.length ? "var(--ko)" : "var(--ok)" }}>
              {passed}/{state.results.length} tests réussis
            </strong>{" "}
            en {(state.ms / 1000).toFixed(1)} s
          </span>
        )}
      </div>
      {summary && (
        <div className="pylab-results">
          {lab.questions.map((q, i) => {
            const s = summary[q.fn];
            const status = s.total === 0 ? "" : s.passed === s.total ? "ok" : "ko";
            return (
              <div key={q.fn} className="pylab-q">
                <span className={`dot ${status}`}>{status === "ok" ? "✓" : status === "ko" ? "✗" : i + 1}</span>
                <span>
                  Q{i + 1}. <code>{q.fn}</code> — {q.title}
                </span>
                <span className="meta">
                  {s.passed}/{s.total}
                </span>
              </div>
            );
          })}
          {failures.length > 0 && (
            <details className="reveal">
              <summary>Détail des échecs ({failures.length})</summary>
              <pre className="pylab-log">
                {failures
                  .map((f) => `● ${f.test} [${f.status}]\n${f.message ?? ""}`)
                  .join("\n")}
              </pre>
            </details>
          )}
          {state.phase === "done" && state.output.trim() && (
            <details className="reveal">
              <summary>Sortie de ton programme (print)</summary>
              <pre className="pylab-log">{state.output}</pre>
            </details>
          )}
        </div>
      )}
      <div className="pylab-status">
        {!showSolution ? (
          <button
            className="btn btn-ghost"
            onClick={() => {
              if (window.confirm("Afficher la solution complète ? Essaie d'abord avec les indices de chaque question.")) setShowSolution(true);
            }}
          >
            Voir la solution complète
          </button>
        ) : (
          <>
            <p style={{ margin: "0 0 8px" }}>Solution de référence (elle passe tous les tests) :</p>
            <CodeMirror value={lab.solution} editable={false} extensions={[python()]} theme={dark ? "dark" : "light"} />
          </>
        )}
      </div>
    </div>
  );
}
