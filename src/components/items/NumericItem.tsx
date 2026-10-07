"use client";

import { useState } from "react";
import type { Item } from "@/lib/content/types";
import { itemKey, useStored, type ItemRecord } from "@/lib/storage";

type Numeric = Extract<Item, { type: "numeric" }>;

function parseNumber(raw: string): number | null {
  const cleaned = raw.replace(/\s/g, "").replace(",", ".");
  if (!cleaned) return null;
  if (/^-?\d+\/\d+$/.test(cleaned)) {
    const [a, b] = cleaned.split("/").map(Number);
    return b === 0 ? null : a / b;
  }
  const value = Number(cleaned);
  return Number.isFinite(value) ? value : null;
}

export function NumericItem({ item }: { item: Numeric }) {
  const [record, setRecord] = useStored<ItemRecord | null>(itemKey(item.id), null);
  const [draft, setDraft] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const value = draft ?? ((record?.answer as string | undefined) ?? "");
  const submitted = draft === null && record !== null;

  const check = () => {
    const n = parseNumber(value);
    if (n === null) return;
    const good = Math.abs(n - item.answer) <= item.tolerance + 1e-9;
    setRecord({ status: good ? "ok" : "ko", at: Date.now(), answer: value });
    setDraft(null);
  };

  return (
    <div className="item" data-item={item.id}>
      <div className="item-head">
        <span>Réponse numérique</span>
        {submitted && (
          <span className={`item-badge ${record!.status}`}>{record!.status === "ok" ? "Réussi" : "À revoir"}</span>
        )}
      </div>
      <div className="item-prompt" dangerouslySetInnerHTML={{ __html: item.promptHtml }} />
      <form
        className="numeric-row"
        onSubmit={(e) => {
          e.preventDefault();
          check();
        }}
      >
        <input
          inputMode="decimal"
          value={value}
          placeholder="Ta réponse"
          aria-label="Ta réponse"
          onChange={(e) => setDraft(e.target.value)}
        />
        {item.unit && <span>{item.unit}</span>}
        <button className="btn" type="submit" disabled={parseNumber(value) === null || submitted}>
          Vérifier
        </button>
        {!submitted && !revealed && (
          <button type="button" className="btn btn-ghost" onClick={() => setRevealed(true)}>
            Je bloque
          </button>
        )}
      </form>
      {(submitted || revealed) && (
        <div className={`feedback ${submitted ? record!.status : "ko"}`}>
          {submitted ? (
            <strong>{record!.status === "ok" ? "Exact." : `Non : la bonne réponse est ${item.answer}.`}</strong>
          ) : (
            <strong>Réponse : {item.answer}.</strong>
          )}
          <div className="explain" dangerouslySetInnerHTML={{ __html: item.explanationHtml }} />
        </div>
      )}
    </div>
  );
}
