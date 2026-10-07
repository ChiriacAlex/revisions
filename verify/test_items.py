"""Toute réponse marquée d'un champ `verify` est recalculée indépendamment."""
from pathlib import Path

import pytest
import yaml

from checks import evaluate_check

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
