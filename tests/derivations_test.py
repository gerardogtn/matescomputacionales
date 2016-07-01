import matescomputacionales.project04.derivations as d
from matescomputacionales.project04.derivation import Derivation

def test_all_derivations_void():
    cfg = ({"S", "A"}, {"a", "b"}, {"S": ["aAS", "a"], "A": ["SbA", "SS", "ba"]}, "S")
    string = "aabbaa"
    assert d.getAllDerivations(cfg, string) == []

def test_all_derivations_two():
    cfg = ({"E"}, {"a", "b"}, {"E": ["E+E", "E*E", "(E)", "a", "b"]}, "E")
    string = "a+b+a"

    firstDerivation = Derivation(entries=[("E", 0), ("E+E", 0), ("E+E+E", 0), ("a+E+E", 2), ("a+b+E", 4), ("a+b+a", -1)])
    secondDerivation = Derivation(entries=[("E", 0), ("E+E", 0), ("E+E+E", 0), ("a+E+E", 4), ("a+E+a", 2), ("a+b+a", -1)])

    derivations = d.getAllDerivations(cfg, string, MAX_SUBSTITUTIONS=5, MAX_DERIVATIONS=2)
    for de in derivations: print str(de)
    assert firstDerivation in derivations
    assert secondDerivation in derivations

def test_simple_derivations():
    cfg = (["S", "A"], ["a", "b"], {"S": ["aA"], "A": ["a", "b"]}, "S")
    string = "aa"
    firstDerivation = Derivation(entries=[("S", 0), ("aA", 1), ("aa", -1)])
    derivations = d.getAllDerivations(cfg, string, MAX_SUBSTITUTIONS=5, MAX_DERIVATIONS=2)
    for de in derivations: print str(de)
    assert firstDerivation in derivations


def test_replace_string_at_index_zero():
    string = "aaab"
    assert d.replaceAtIndexWithString(string, 0, "b") == "baab"

def test_replace_string_at_upper_bound():
    string = "aaab"
    assert d.replaceAtIndexWithString(string, 3, "c") == "aaac"

def test_replace_out_of_bounds():
    string = "aaab"
    try:
        d.replaceAtIndexWithString(string, 10, "c")
        assert False
    except ValueError:
        assert True

def test_replace_void():
    string = ""
    assert d.replaceAtIndexWithString(string, 0, "a") == "a"
