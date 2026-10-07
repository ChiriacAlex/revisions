"use client";

import { useState } from "react";
import type { Item } from "@/lib/content/types";
import { itemKey, useStored, type ItemRecord } from "@/lib/storage";

type TrueFalse = Extract<Item, { type: "truefalse" }>;

export function TrueFalseItem({ item }: { item: TrueFalse }) {
  const [record, setRecord] = useStored<ItemRecord | null>(itemKey(item.id), null);
  const [draft, setDraft] = useState<(boolean | null)[] | null>(null);
  const answers = draft ?? ((record?.answer as (boolean | null)[] | undefined) ?? item.statements.map(() => null));
  const submitted = draft === null && record !== null;
  const complete = answers.every((a) => a !== null);

  const choose = (index: number, value: boolean) => {
    const base = submitted ? item.statements.map(() => null) : [...answers];
    base[index] = value;
    setDraft(base);
  };

  const check = () => {
    const good = item.statements.every((s, i) => answers[i] === s.answer);
    setRecord({ status: good ? "ok" : "ko", at: Date.now(), answer: answers });
    setDraft(null);
  };

  const score = item.statements.filter((s, i) => answers[i] === s.answer).length;

  return (
    <div className="item" data-item={item.id}>
      <div className="item-head">
        <span>Vrai ou faux</span>
        {submitted && (
          <span className={`item-badge ${record!.status}`}>
            {score}/{item.statements.length}
          </span>
        )}
      </div>
      <div className="item-prompt" dangerouslySetInnerHTML={{ __html: item.promptHtml }} />
      <div className="tf-list">
        {item.statements.map((statement, i) => {
          const state = submitted ? (answers[i] === statement.answer ? " is-correct" : " is-wrong") : "";
          return (
            <div key={i} className={`tf-row${state}`}>
              <div className="tf-statement" dangerouslySetInnerHTML={{ __html: statement.html }} />
              <div className="tf-buttons">
                <button type="button" aria-pressed={answers[i] === true} onClick={() => choose(i, true)}>
                  Vrai
                </button>
                <button type="button" aria-pressed={answers[i] === false} onClick={() => choose(i, false)}>
                  Faux
                </button>
              </div>
              {submitted && (
                <div className="tf-why">
                  <strong>{statement.answer ? "Vrai." : "Faux."}</strong>{" "}
                  <span dangerouslySetInnerHTML={{ __html: statement.whyHtml }} />
                </div>
              )}
            </div>
          );
        })}
      </div>
      <div className="item-actions">
        {!submitted ? (
          <button className="btn" onClick={check} disabled={!complete}>
            Valider
          </button>
        ) : (
          <button className="btn btn-ghost" onClick={() => setDraft(item.statements.map(() => null))}>
            Recommencer
          </button>
        )}
      </div>
    </div>
  );
}
