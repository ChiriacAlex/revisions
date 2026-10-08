"use client";

import { useState } from "react";
import type { Item } from "@/lib/content/types";
import { itemKey, useStored, type ItemRecord } from "@/lib/storage";
import { formatAnswer, isAccepted, parseAnswer } from "@/lib/numeric";

type Numeric = Extract<Item, { type: "numeric" }>;

export function NumericItem({ item }: { item: Numeric }) {
  const [record, setRecord] = useStored<ItemRecord | null>(itemKey(item.id), null);
  const [draft, setDraft] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const value = draft ?? ((record?.answer as string | undefined) ?? "");
  const submitted = draft === null && record !== null;

  const check = () => {
    if (parseAnswer(value) === null) return;
    const good = isAccepted(value, item.answer, item.tolerance);
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
          placeholder="ex. 1/6 ou 0,167"
          aria-label="Ta réponse"
          onChange={(e) => setDraft(e.target.value)}
        />
        {item.unit && <span>{item.unit}</span>}
        <button className="btn" type="submit" disabled={parseAnswer(value) === null || submitted}>
          Vérifier
        </button>
        {!submitted && !revealed && (
          <button type="button" className="btn btn-ghost" onClick={() => setRevealed(true)}>
            Je bloque
          </button>
        )}
      </form>
      {!submitted && <p className="numeric-hint">Fraction (1/6) ou décimal (0,167) : les deux sont acceptés.</p>}
      {(submitted || revealed) && (
        <div className={`feedback ${submitted ? record!.status : "reveal"}`}>
          {submitted ? (
            <strong>
              {record!.status === "ok"
                ? "Exact."
                : `Non : la bonne réponse est ${formatAnswer(item.answer, item.tolerance)}.`}
            </strong>
          ) : (
            <strong>Solution : {formatAnswer(item.answer, item.tolerance)}</strong>
          )}
          <div className="explain" dangerouslySetInnerHTML={{ __html: item.explanationHtml }} />
        </div>
      )}
    </div>
  );
}
