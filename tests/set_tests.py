from nose.tools import *
from projects.set import Set
import projects

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_add():
    set = Set()
    set.add(1)
    assert set.contains(1)

def test_add_duplicates():
    set = Set()
    set.addAll([1, 1, 3])
    assert set.size() == 2
    assert set.contains(1)
    assert set.contains(3)

def test_remove():
    set = Set()
    set.addAll([1, 3, 5])
    assert set.size() == 3
    assert set.contains(3)
    set.remove(3)
    assert set.size() == 2
    assert (not set.contains(3))

def test_empty_equals():
    set = Set()
    other = Set()
    assert set == other

def test_equals():
    set = Set()
    set.addAll([1, 2, 3])
    other = Set()
    other.addAll([3, 2, 1])
    assert set == other

def test_not_equals():
    set = Set()
    other = Set()
    other.add(1)
    assert not set == other
