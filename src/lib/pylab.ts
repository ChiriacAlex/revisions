export type TestResult = { test: string; status: "pass" | "fail" | "error"; message?: string };

/** Associe `test_<fonction>[_suffixe]` à la fonction testée (le nom le plus long gagne). */
export function functionOfTest(test: string, fns: string[]): string | undefined {
  let best: string | undefined;
  for (const fn of fns) {
    const prefix = `test_${fn}`;
    if (test === prefix || test.startsWith(`${prefix}_`)) {
      if (!best || fn.length > best.length) best = fn;
    }
  }
  return best;
}

export function summarize(results: TestResult[], fns: string[]): Record<string, { passed: number; total: number }> {
  const summary = Object.fromEntries(fns.map((fn) => [fn, { passed: 0, total: 0 }]));
  for (const result of results) {
    const fn = functionOfTest(result.test, fns);
    if (!fn) continue;
    summary[fn].total += 1;
    if (result.status === "pass") summary[fn].passed += 1;
  }
  return summary;
}
