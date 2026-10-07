"use client";

import { useState } from "react";
import type { Item } from "@/lib/content/types";
import { itemKey, useStored, type ItemRecord } from "@/lib/storage";

type Qcm = Extract<Item, { type: "qcm" }>;

export function QcmItem({ item }: { item: Qcm }) {
  const [record, setRecord] = useStored<ItemRecord | null>(itemKey(item.id), null);
  const [picked, setPicked] = useState<number[] | null>(null);
  const selection = picked ?? ((record?.answer as number[] | undefined) ?? []);
  const submitted = picked === null && record !== null;

  const toggle = (index: number) => {
    const base = submitted ? [] : selection;
    if (item.multi) setPicked(base.includes(index) ? base.filter((i) => i !== index) : [...base, index]);
    else setPicked([index]);
  };

  const check = () => {
    const good = item.options.every((o, i) => o.correct === selection.includes(i));
    setRecord({ status: good ? "ok" : "ko", at: Date.now(), answer: selection });
    setPicked(null);
  };

  const retry = () => {
    setRecord(undefined);
    setPicked([]);
  };

  return (
    <div className="item" data-item={item.id}>
      <div className="item-head">
        <span>{item.multi ? "QCM · plusieurs réponses possibles" : "QCM · une seule réponse"}</span>
        {submitted && (
          <span className={`item-badge ${record!.status}`}>{record!.status === "ok" ? "Réussi" : "À revoir"}</span>
        )}
      </div>
      <div className="item-prompt" dangerouslySetInnerHTML={{ __html: item.promptHtml }} />
      <div className="options" role={item.multi ? "group" : "radiogroup"}>
        {item.options.map((option, i) => {
          const chosen = selection.includes(i);
          let state = "";
          if (submitted) {
            if (chosen && option.correct) state = " is-correct";
            else if (chosen && !option.correct) state = " is-wrong";
            else if (!chosen && option.correct) state = " is-missed";
          }
          return (
            <label key={i} className={`option${state}`}>
              <input
                type={item.multi ? "checkbox" : "radio"}
                name={item.id}
                checked={chosen}
                onChange={() => toggle(i)}
              />
              <span dangerouslySetInnerHTML={{ __html: option.html }} />
              {submitted && (chosen || option.correct) && (
                <span className="option-why" dangerouslySetInnerHTML={{ __html: option.whyHtml }} />
              )}
            </label>
          );
        })}
      </div>
      <div className="item-actions">
        {!submitted && (
          <button className="btn" onClick={check} disabled={selection.length === 0}>
            Valider
          </button>
        )}
        {submitted && (
          <button className="btn btn-ghost" onClick={retry}>
            Recommencer
          </button>
        )}
      </div>
      {submitted && (
        <div className={`feedback ${record!.status}`}>
          <strong>{record!.status === "ok" ? "Bonne réponse." : "Pas tout à fait."}</strong>{" "}
          {record!.status === "ko" && "Les bonnes réponses sont encadrées en vert ; lis l'explication sous chaque option."}
          {item.explanationHtml && <div className="explain" dangerouslySetInnerHTML={{ __html: item.explanationHtml }} />}
        </div>
      )}
    </div>
  );
}
