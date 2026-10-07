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


def test_project_page_snippets_match_reference_behaviour(tmp_path):
    """Les solutions affichées question par question (page Projet) passent elles aussi tous les tests."""
    import re
    page = (PY.parent / "40-projet-python.md").read_text()
    template = (PY / "folo_template.py").read_text()
    blocks = re.findall(r"```python\n(.*?)```", page, re.S)
    # Q1..Q7 : corps de fonction à insérer dans le modèle ; Q8..Q15 : fonctions complètes.
    bodies = {
        "is_relation": blocks[2], "is_partial_function": blocks[3], "is_function": blocks[4],
        "is_injection": blocks[5], "is_surjection": blocks[6], "is_bijection": blocks[7],
    }
    code = template
    for name, body in bodies.items():
        start = code.index(f"def {name}(")
        stop = code.index("raise NotImplementedError()", start)
        indented = "\n".join("    " + line if line else line for line in body.strip("\n").splitlines())
        code = code[:start] + code[start:stop] + indented.lstrip() + code[stop + len("raise NotImplementedError()"):]
    # find_inverse : on remplace tout le corps après les assert
    fi_start = code.index("    if not is_bijection(g, es, fs):\n        raise NotImplementedError()")
    fi_end = code.index("    return h\n", fi_start) + len("    return h\n")
    fi_body = "\n".join("    " + line if line else line for line in blocks[8].strip("\n").splitlines())
    code = code[:fi_start] + fi_body + "\n" + code[fi_end:]
    # Q8..Q15 : on remplace les définitions par celles de la page (les assert du modèle sont rappelés)
    full = blocks[9] + "\n" + blocks[10]
    for name in ["is_symmetric", "is_antisymmetric", "is_reflexive", "is_transitive",
                 "is_equivalence", "gen_equiv_class", "is_partial_order", "is_total_order"]:
        start = code.index(f"def {name}(")
        nxt = code.find("\ndef ", start + 1)
        code = code[:start] + code[nxt + 1:] if nxt != -1 else code[:start]
    code += "\n\n" + full
    assert "NotImplementedError" not in code
    (tmp_path / "folo.py").write_text(code)
    for name in TESTS:
        shutil.copy(PY / name, tmp_path / name)
    result = subprocess.run([sys.executable, "-m", "unittest", "folo_test", "folo_extra_test"],
                            cwd=tmp_path, capture_output=True, text=True, timeout=300)
    assert result.returncode == 0, result.stderr[-3000:]
