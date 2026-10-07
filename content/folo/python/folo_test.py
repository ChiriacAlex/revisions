import sys
import os
from unittest import TestCase
import random
from typing import TypeVar, Set

# this path insertion is needed for VS Code, and does no harm for PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import_exception = None
try:
    from folo import *
except Exception as e:
    print(e)
    import_exception = e

E = TypeVar('E')


def some_element(es: Set[E]) -> E:
    assert len(es) > 0
    for e in es:
        return e


def check_load(self, pyfiles, exe):
    if exe is None:
        return
    self.fail(f"Exception while importing one of {pyfiles}: {exe}")


def sample_list(ts):
    return set(k for k in range(ts)
               if random.choice([True, False]))


def get_relation(a, b, f) -> set:
    return {(x, y)
            for x in a
            for y in b
            if f(x, y)}


def set_ef_fs():
    es = {(x, (x, None)) for x in range(100)}
    fs = {(x, y) for x in range(20)
          for y in range(20)}
    return es, fs


class SanityTestCase(TestCase):
    def test_load(self):
        # test whether the student code loads at all
        check_load(self, ["folo.py"], import_exception)


class RelationsTestCase(TestCase):
    # test is_relation
    def test_is_relation(self):
        es, fs = set_ef_fs()
        for r in range(10):
            for k in range(r):
                if random.random() < 0.2:
                    pairs = get_relation(es, fs, lambda x, y: random.random() < 0.01)
                    self.assertTrue(is_relation(es, fs, pairs))
                    self.assertFalse(is_relation(es, fs, pairs.union({("hello", "world")})))

    # test gen_equiv_class
    def test_gen_equiv_class_1(self):
        words = {"now", "is", "the", "time", "for", "all",
                 "good", "men", "to", "come", "to", "the",
                 "aid", "of", "their", "county"}
        # equiv by string len
        pairs = {(u, v)
                 for u in words
                 for v in words
                 if len(u) == len(v)}
        for word in words:
            n = len(word)
            expected = {w for w in words
                        if len(w) == n}
            got = gen_equiv_class(words, word, pairs)
            self.assertEqual(expected, got)

    # test is_partial_function
    def test_is_partial_function(self):
        for r in range(10):
            for k in range(r):
                if random.random() < 0.5:
                    pairs = {(x, 3 * x) for x in range(k)
                             if random.random() < 0.01}
                    es = {x for x, y in pairs}
                    fs = {y for x, y in pairs}
                    self.assertTrue(is_partial_function(es, fs, pairs),
                                    f"pairs is a partial function\n  es={es}\n  fs={fs}\n  pairs={pairs}")
                    self.assertFalse(is_partial_function(es, fs, pairs.union({(0, 1), (0, 2)})))
                    self.assertTrue(is_partial_function(es.union({-1}), fs, pairs))

    # test is_function

    def test_is_function(self):
        for r in range(10):
            for k in range(r):
                if random.random() < 0.5:
                    pairs = {(x, 3 * x) for x in range(k)
                             if random.random() < 0.01}
                    es = {x for x, y in pairs}
                    fs = {y for x, y in pairs}
                    self.assertTrue(is_function(es, fs, pairs),
                                    f"pairs is a function\n  es={es}\n  fs={fs}\n  pairs={pairs}")
                    self.assertFalse(is_function(es, fs, pairs.union({(0, 1), (0, 2)})))
                    self.assertFalse(is_function(es.union({-1}), fs, pairs))

    # test is_symmetric

    def test_is_symmetric_0(self):
        self.assertTrue(is_symmetric(set(), set()))
        self.assertTrue(is_symmetric({1}, {(1, 1)}))
        self.assertFalse(is_symmetric({1}, {(1, 2)}))
        self.assertFalse(is_symmetric({1, 2}, {(1, 2)}))
        self.assertTrue(is_symmetric({1, 2}, {(1, 1), (2, 2)}))
        self.assertFalse(is_symmetric({1, 2}, {(1, 1), (1, 2)}))
        self.assertTrue(is_symmetric({1, 2}, {(2, 1), (1, 2)}))
        self.assertTrue(is_symmetric({1, 2, 3, 4, 5}, set()))

    # test is_antisymmetric

    def test_is_antisymmetric_1(self):
        num_repetitions = 50
        test_size = 10
        for ts in range(1, test_size):
            for r1 in range(num_repetitions):
                a = sample_list(ts)
                for r2 in range(num_repetitions):
                    for r in [get_relation(a, a, lambda x, y: x > y),
                              get_relation(a, a, lambda x, y: x < y)
                              ]:
                        self.assertTrue(is_antisymmetric(a, r))

    # test is_reflexive

    def test_is_reflexive_1(self):
        num_repetitions = 50
        test_size = 10
        for ts in range(1, test_size):
            for r1 in range(num_repetitions):
                a = sample_list(ts)
                for r2 in range(num_repetitions):
                    for r in [get_relation(a, a, lambda x, y: x <= y),
                              get_relation(a, a, lambda x, y: x == y),
                              get_relation(a, a, lambda x, y: x >= y)]:
                        self.assertTrue(is_reflexive(a, r),
                                        f"reflexive: a={a} r={r}")

    # test is_transitive

    def test_is_transitive_3(self):
        es = {x for x in range(10)}
        pairs = {(x, y)
                 for x in es
                 for y in es}
        self.assertTrue(is_transitive(es, {(x, y) for x, y in pairs
                                           if x == y}))
        self.assertFalse(is_transitive(es, {(x, y) for x, y in pairs
                                            if x != y}))
        self.assertTrue(is_transitive(es, {(x, y) for x, y in pairs
                                           if x > y}))
        self.assertTrue(is_transitive(es, {(x, y) for x, y in pairs
                                           if x <= y}))
        self.assertFalse(is_transitive(es, {(-1, -1)}.union({(x, y) for x, y in pairs
                                                             if x <= y})))

    # test is_equivalence

    def test_is_equivalence_1(self):
        es = {x for x in range(10)}
        pairs = {(x, y)
                 for x in es
                 for y in es}
        self.assertTrue(is_equivalence(es, {(x, y) for x, y in pairs
                                            if x == y}))
        self.assertFalse(is_equivalence(es, {(x, y) for x, y in pairs
                                             if x != y}))
        self.assertFalse(is_equivalence(es, {(x, y) for x, y in pairs
                                             if x > y}))
        self.assertFalse(is_equivalence(es, {(x, y) for x, y in pairs
                                             if x <= y}))

    # test is_partial_order

    def test_is_partial_order(self):
        num_repetitions = 50
        test_size = 10
        for ts in range(1, test_size):
            for r1 in range(num_repetitions):
                a = set(x for x in range(4, r1))
                for r in [get_relation(a, a, lambda x, y: x <= y),
                          get_relation(a, a, lambda x, y: x >= y)]:
                    self.assertTrue(is_partial_order(a, r),
                                    f"{a=}, {r=}")

    # test_is_total_order

    def test_is_total_order(self):
        num_repetitions = 50
        test_size = 10
        for ts in range(1, test_size):
            for r1 in range(num_repetitions):
                a = set(x for x in range(4, r1))
                for r in [get_relation(a, a, lambda x, y: x <= y),
                          get_relation(a, a, lambda x, y: x >= y)]:
                    self.assertTrue(is_total_order(a, r),
                                    f"{a=}, {r=}")
                for r in [get_relation(a, a, lambda x, y: x < y),
                          get_relation(a, a, lambda x, y: x > y)]:
                    if len(r) > 0:
                        self.assertFalse(is_total_order(a, r),
                                         f"{a=}, {r=}")


class BijectionsTestCase(TestCase):
    # test is_injection

    def test_is_injection_0(self):
        self.assertTrue(is_injection(lambda x: 0, set(), set()))
        self.assertTrue(is_injection(lambda x: 0, {0}, {0}))
        self.assertTrue(is_injection(lambda x: 1, {0}, {0, 1}))
        self.assertFalse(is_injection(lambda x: 1, {0, 1}, {0, 1}))
        self.assertTrue(is_injection(lambda x: 1, {0}, {1}))
        self.assertTrue(
            is_injection(lambda x: x * x,
                         {x for x in range(10)},
                         {x for x in range(100)}))
        self.assertTrue(
            is_injection(lambda x: (x * x, x * x),
                         {x for x in range(10)},
                         {(x, x) for x in range(100)}))
        self.assertTrue(
            is_injection(lambda x: (x * x, 1),
                         {x for x in range(10)},
                         {(x, 1) for x in range(100)}))
        self.assertFalse(
            is_injection(lambda x: x // 2,
                         {x for x in range(100)},
                         {x for x in range(50)}))

    # test is_surjection

    def test_is_surjection_0(self):
        self.assertTrue(is_surjection(lambda x: 0, set(), set()))
        self.assertFalse(
            is_surjection(lambda x: x * x,
                          {x for x in range(10)},
                          {x for x in range(100)}))
        self.assertTrue(
            is_surjection(lambda x: x // 2,
                          {x for x in range(100)},
                          {x for x in range(50)}))
        self.assertTrue(
            is_surjection(lambda x: (x // 2,),
                          {x for x in range(100)},
                          {(x,) for x in range(50)}))

    # test is_bijection

    def test_is_bijection_0(self):
        self.assertTrue(is_bijection(lambda x: 0, set(), set()))
        self.assertTrue(is_bijection(lambda x: x, {1}, {1}))
        self.assertFalse(is_bijection(lambda x: 0, {0, 1}, {0}))
        self.assertTrue(is_bijection(lambda x: x, {0, 1}, {1, 0}))
        self.assertFalse(is_bijection(lambda x: x, {0, 1}, {2, 1, 0}))
        self.assertTrue(is_bijection(lambda x: x + 1,
                                     {x for x in range(10, 20)},
                                     {x for x in range(11, 21)}))
        self.assertTrue(is_bijection(lambda x: x + 1,
                                     {x for x in range(10, 20)},
                                     {x for x in range(11, 21)}))
        self.assertFalse(is_bijection(abs,
                                      {x for x in range(-10, 10)},
                                      {abs(x) for x in range(-10, 10)}))
        self.assertFalse(is_bijection(abs,
                                      {x for x in range(-10, 10)},
                                      {abs(x) for x in range(-11, 11)}))
    # test find_inverse

    def test_find_inverse_1(self):
        for m in [19, 21, 23]:
            es = {x for x in range(m)}
            for g in [lambda x: x + 1,
                      lambda x: x - 1,
                      lambda x: x,
                      lambda x: 2 * x
                      ]:
                fs = {g(x) for x in es}
                self.assertTrue(is_bijection(g, es, fs),
                                f"{g=} {es=} {fs=}")
                h = find_inverse(g, es, fs)
                self.assertIsNotNone(find_inverse(g, es, fs),
                                     f"{g=} {es=} {fs=}")
                self.assertTrue(callable(find_inverse(g, es, fs)),
                                f"{g=} {es=} {fs=}")
                for f in fs:
                    self.assertEqual(f, g(h(f)),
                                     f"h=find_inverse(g, es, fs), {f=} {g=} {es=} {fs}")
                for e in es:
                    self.assertEqual(e, h(g(e)),
                                     f"h=find_inverse(g, es, fs), {e=} {g=} {es=} {fs}")
