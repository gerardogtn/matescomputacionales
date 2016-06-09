import matescomputacionales.project02.recursive_definitions as r
from matescomputacionales.datastructures.set import Set

def test_empty_empty_at_zero():
    actual = r.getStringsUntilNRecursiveStep([''], ['u'], 0)
    expected = Set()
    expected.add('')
    print actual, expected
    assert actual == expected

def test_empty_empty_at_ten():
    actual = r.getStringsUntilNRecursiveStep([''], ['u'], 10)
    expected = Set()
    expected.add('')
    print actual, expected
    assert actual == expected

def test_empty_1_at_zero():
    actual = r.getStringsUntilNRecursiveStep([''], ['u1'], 0)
    expected = Set()
    expected.add('')
    print actual, expected
    assert actual == expected

def test_empty_1_at_three():
    expected = Set()
    expected.addAll(['', '1', '11', '111'])
    actual = r.getStringsUntilNRecursiveStep([''], ['u1'], 3)
    print actual, expected
    assert actual == expected

def test_empty_1_or_zero_at_2():
    expected = Set()
    expected.addAll(['', '1', '0', '11', '01', '00', '10'])
    actual = r.getStringsUntilNRecursiveStep([''], ['u1', 'u0'], 2)
    print actual, expected
    assert actual == expected

def test_1__1_or_zero_at_2():
    expected = Set()
    expected.addAll(['1', '11', '10', '111', '101', '100', '110'])
    actual = r.getStringsUntilNRecursiveStep(['1'], ['u1', 'u0'], 2)
    print actual, expected
    assert actual == expected
