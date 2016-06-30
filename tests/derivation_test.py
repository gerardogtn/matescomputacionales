from matescomputacionales.project04.derivation import Derivation

def test_empty():
    d = Derivation()
    assert d.isEmpty()

def test_add():
    d = Derivation()
    d.add("AAs", 1)

def test_add_no_variable():
    d = Derivation()
    d.add("aas", -1)

def test_pop_simple():
    d = Derivation()
    d.add("bBs", 2)
    d.pop()
    assert d.isEmpty()

def test_pop_double():
    d = Derivation()
    d.add("bbs", -1)
    d.add("bSa", 2)
    assert ("bSa", 2) == d.pop()
    assert ("bbs", -1) == d.pop()
    assert d.isEmpty()

def test_clear():
    d = Derivation()
    d.add("bbs", -1)
    d.add("bSa", 2)
    d.clear()
    assert d.isEmpty()
