"""Toute réponse marquée d'un champ `verify` est recalculée indépendamment."""
from pathlib import Path

import pytest
import yaml

from checks import evaluate_check, witness_refutes

CONTENT = Path(__file__).resolve().parent.parent / "content"


def collect():
    cases = []
    for file in sorted(CONTENT.glob("**/*.items.yaml")):
        for item in yaml.safe_load(file.read_text()) or []:
            where = f"{file.parent.name}/{item['id']}"
            if item["type"] == "truefalse":
                for i, s in enumerate(item["statements"]):
                    if "verify" in s:
                        cases.append((f"{where}#{i + 1}", s["verify"], s["answer"]))
            elif item["type"] == "qcm":
                for i, o in enumerate(item["options"]):
                    if "verify" in o:
                        cases.append((f"{where}#opt{i + 1}", o["verify"], o.get("correct", False)))
            elif item["type"] == "numeric" and "verify" in item:
                cases.append((where, item["verify"], item["answer"]))
    return cases


CASES = collect()


@pytest.mark.parametrize("where,spec,expected", CASES, ids=[c[0] for c in CASES])
def test_answer_is_independently_confirmed(where, spec, expected):
    computed = evaluate_check(spec)
    if isinstance(expected, bool):
        assert bool(computed) is expected, f"{where} : la réponse affichée est {expected}, le calcul donne {computed}"
    else:
        assert computed == pytest.approx(expected), f"{where} : réponse affichée {expected}, calcul {computed}"


WITNESSES = [c for c in CASES if isinstance(c[1], dict) and "witness" in c[1]]


@pytest.mark.parametrize("where,spec,expected", WITNESSES, ids=[c[0] for c in WITNESSES])
def test_cited_counterexample_really_refutes(where, spec, expected):
    assert expected is False, f"{where} : un contre-exemple n'a de sens que pour une affirmation fausse"
    assert witness_refutes(spec), f"{where} : le contre-exemple {spec['witness']} ne réfute pas l'énoncé"
