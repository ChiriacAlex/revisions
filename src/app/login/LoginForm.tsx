"use client";

import { useActionState } from "react";
import { login, type LoginState } from "./actions";

export function LoginForm({ next }: { next: string }) {
  const [state, action, pending] = useActionState<LoginState, FormData>(login, {});
  return (
    <form className="login-box" action={action} autoComplete="off">
      <div className="login-logo" aria-hidden>∀</div>
      <h1>Révisions</h1>
      <p className="login-hint">Entre ton code PIN pour accéder aux cours.</p>
      <label htmlFor="pin">Code PIN</label>
      <input
        id="pin"
        name="pin"
        type="password"
        inputMode="numeric"
        pattern="\d{4,8}"
        maxLength={8}
        required
        autoFocus
        autoComplete="off"
        onInput={(e) => {
          const el = e.currentTarget;
          el.value = el.value.replace(/\D/g, "").slice(0, 8);
        }}
      />
      <input type="hidden" name="next" value={next} />
      {state.error && (
        <p className="login-error" role="alert">
          {state.error}
        </p>
      )}
      <button type="submit" disabled={pending}>
        {pending ? "Vérification…" : "Entrer"}
      </button>
      <p className="login-foot">Session valable 1 heure.</p>
    </form>
  );
}
