from typing import TypeVar, Callable, Tuple, Optional, Set

E = TypeVar('E')
F = TypeVar('F')


def is_relation(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *binary relation* on es × fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_partial_function(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *partial function* relation es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_function(es: Set[E], fs: Set[F], pairs: Set[Tuple[E, F]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × fs designates
    a *function* relation es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_injection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is an *injection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    raise NotImplementedError()


def is_surjection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is a *surjection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    raise NotImplementedError()


def is_bijection(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> bool:
    """Given 'es', a set of objects, 'fs', a set of objects,
    determine whether the function 'g' is a *bijection* es → fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"
    raise NotImplementedError()


def find_inverse(g: Callable[[E], F], es: Set[E], fs: Set[F]) -> Optional[Callable[[F], E]]:
    """Given 'es', a set of objects, 'fs', a set of objects, and a function 'g',
    if g is a bijection es → fs return its *inverse*, otherwise return None."""
    assert isinstance(es, set), type(es)
    assert isinstance(fs, set), type(fs)
    assert callable(g), type(g)
    assert all(g(x) in fs for x in es), f"internal testing error, {fs=} {es=} image={[g(x) for x in es]}"

    if not is_bijection(g, es, fs):
        raise NotImplementedError()


    def h(f: F) -> E:
        raise NotImplementedError()


    return h


def is_symmetric(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *symmetric, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_antisymmetric(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *antisymmetric, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_reflexive(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects, and 'fs', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *reflexive, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_transitive(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *transitive, binary* relation on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_equivalence(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    an *equivalence* relation on es × fs."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def gen_equiv_class(es: Set[E], e: E, equiv_pairs:Set[Tuple[E, E]]) -> Set[E]:
    """Given 'es', a set of objects, an element 'e' of 'es',
    and a set 'equiv_pairs' of pairs in es × es designating an equivalence relation,
    return as a set the equivalence class of e according to equiv_pairs."""
    assert is_equivalence(es, equiv_pairs)
    assert e in es
    raise NotImplementedError()


def is_partial_order(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *partial order relation* on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


def is_total_order(es: Set[E], pairs: Set[Tuple[E, E]]) -> bool:
    """Given 'es', a set of objects,
    determine whether the set 'pairs' of pairs in es × es designates
    a *total order relation* on es × es."""
    assert isinstance(es, set), type(es)
    assert isinstance(pairs, set), type(pairs)
    assert all(isinstance(p, tuple) for p in pairs), [type(p) for p in pairs]
    raise NotImplementedError()


