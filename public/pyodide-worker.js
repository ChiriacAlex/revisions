/* Exécute le code Python de l'étudiant + les tests unittest dans un Web Worker module (Pyodide). */
// Chemins relatifs au worker : fonctionne aussi sous un sous-dossier (GitHub Pages).
import { loadPyodide } from "./vendor/pyodide/pyodide.mjs";

const PYODIDE_URL = new URL("./vendor/pyodide/", self.location.href).href;
let pyodideReady = null;

function boot() {
  if (!pyodideReady) pyodideReady = loadPyodide({ indexURL: PYODIDE_URL });
  return pyodideReady;
}

const HARNESS = `
import sys, json, unittest, io, contextlib, os
os.chdir('/work')
if '/work' not in sys.path:
    sys.path.insert(0, '/work')
for name in list(sys.modules):
    if name in MODULES:
        del sys.modules[name]

results = []
class Collector(unittest.TestResult):
    def _name(self, test):
        return test.id().split('.')[-1]
    def addSuccess(self, test):
        results.append({'test': self._name(test), 'status': 'pass'})
    def addFailure(self, test, err):
        results.append({'test': self._name(test), 'status': 'fail', 'message': self._exc_info_to_string(err, test)})
    def addError(self, test, err):
        results.append({'test': self._name(test), 'status': 'error', 'message': self._exc_info_to_string(err, test)})

out = io.StringIO()
with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
    suite = unittest.TestSuite()
    for module in TEST_MODULES:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromName(module))
    suite.run(Collector())
json.dumps({'results': results, 'output': out.getvalue()[-20000:]})
`;

self.onmessage = async (event) => {
  const { id, files, testModules } = event.data;
  try {
    const pyodide = await boot();
    self.postMessage({ id, type: "ready" });
    try {
      pyodide.FS.mkdir("/work");
    } catch {
      /* déjà créé */
    }
    for (const file of files) pyodide.FS.writeFile("/work/" + file.name, file.code);
    const modules = files.filter((f) => f.name.endsWith(".py")).map((f) => f.name.slice(0, -3));
    pyodide.globals.set("MODULES", pyodide.toPy(modules));
    pyodide.globals.set("TEST_MODULES", pyodide.toPy(testModules));
    const json = await pyodide.runPythonAsync(HARNESS);
    self.postMessage({ id, type: "done", payload: JSON.parse(json) });
  } catch (error) {
    self.postMessage({ id, type: "crash", message: String(error && error.message ? error.message : error) });
  }
};
