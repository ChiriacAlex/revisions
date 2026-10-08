/** Lecture et affichage des réponses numériques des quiz (fractions, virgule française). */

/** « 0,167 », « 0.1666 », « 1/6 », « 6 / 36 », « -3/4 » → nombre ; sinon null. */
export function parseAnswer(raw: string): number | null {
  const cleaned = raw.replace(/\s/g, "").replace(/,/g, ".");
  if (!cleaned) return null;
  const fraction = cleaned.match(/^(-?\d+(?:\.\d+)?)\/(\d+(?:\.\d+)?)$/);
  if (fraction) {
    const [num, den] = [Number(fraction[1]), Number(fraction[2])];
    return den === 0 ? null : num / den;
  }
  const value = Number(cleaned);
  return Number.isFinite(value) ? value : null;
}

export function isAccepted(raw: string, answer: number, tolerance: number): boolean {
  const value = parseAnswer(raw);
  return value !== null && Math.abs(value - answer) <= tolerance + 1e-9;
}

const french = (s: string) => s.replace(".", ",");

function decimalsFor(tolerance: number): number {
  return Math.max(0, Math.ceil(-Math.log10(tolerance)));
}

/** Écriture lisible de la réponse : « 1/6 ≈ 0,167 », « 0,25 », « 58 », « ≈ 2,682 ». */
export function formatAnswer(answer: number, tolerance: number): string {
  if (Math.abs(answer - Math.round(answer)) < 1e-9) return String(Math.round(answer));

  for (let k = 1; k <= 4; k++) {
    const scaled = answer * 10 ** k;
    if (Math.abs(scaled - Math.round(scaled)) < 1e-6) return french(answer.toFixed(k));
  }

  const rounded = french(answer.toFixed(decimalsFor(tolerance)));
  for (let q = 2; q <= 100; q++) {
    const p = Math.round(answer * q);
    if (Math.abs(p / q - answer) < 1e-6) return `${p}/${q} ≈ ${rounded}`;
  }
  return `≈ ${rounded}`;
}
