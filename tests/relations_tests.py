from nose.tools import *
import projects.relations as r

def test_reflexive():
    assert r.isReflexive([[1, 1], [2, 2], [4, 4]])

def test_not_reflexive():
    assert not r.isReflexive([[1, 2]])

def test_irreflexive():
    assert r.isIrreflexive([[1, 2]])

def test_not_irreflexive():
    assert not r.isIrreflexive([[1, 1]])

def test_transitive():
    assert r.isTransitive([[1, 2], [2, 3], [3, 1]])

def test_not_transitive():
    assert not r.isTransitive([[1, 2], [3, 1]])

def test_symetric():
    assert r.isSymmetric([[1, 2], [2, 1], [3, 4], [4, 3], [1, 1]])

def test_not_symetric():
    assert not r.isSymmetric([[1, 2], [2, 3]])

def test_asymetric():
    assert r.isAsymmetric([[1, 2], [2, 3]])

def test_not_asymetric():
    assert not r.isAsymmetric([[1, 2], [2, 1]])
