"""Le labo Python du projet FOLO : la solution de référence doit passer tous les tests
(publics + supplémentaires) et le modèle vide doit les échouer."""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

PY = Path(__file__).resolve().parent.parent / "content" / "folo" / "python"
TESTS = ["folo_test.py", "folo_extra_test.py"]


def run_suite(tmp_path: Path, implementation: str) -> subprocess.CompletedProcess:
    shutil.copy(PY / implementation, tmp_path / "folo.py")
    for name in TESTS:
        shutil.copy(PY / name, tmp_path / name)
    return subprocess.run(
        [sys.executable, "-m", "unittest", "folo_test", "folo_extra_test"],
        cwd=tmp_path, capture_output=True, text=True, timeout=300,
    )


def test_reference_solution_passes_every_test(tmp_path):
    result = run_suite(tmp_path, "folo_solution.py")
    assert result.returncode == 0, result.stderr[-3000:]
    assert "OK" in result.stderr


def test_empty_template_fails(tmp_path):
    result = run_suite(tmp_path, "folo_template.py")
    assert result.returncode != 0


def test_solution_runs_as_a_script(tmp_path):
    shutil.copy(PY / "folo_solution.py", tmp_path / "folo.py")
    result = subprocess.run([sys.executable, "folo.py"], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("name", ["folo_template.py", "folo_solution.py"])
def test_same_public_signatures_as_the_template(name):
    import ast
    def signatures(path):
        tree = ast.parse((PY / path).read_text())
        return {node.name: [a.arg for a in node.args.args] for node in tree.body if isinstance(node, ast.FunctionDef)}
    assert signatures(name) == signatures("folo_template.py")
