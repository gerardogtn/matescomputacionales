import matescomputacionales.project02.recursive_definitions as r

def test_empty_empty_at_zero():
    actual = r.getStringsUntilNRecursiveStep({''}, {'u'}, 0)
    expected = {""}
    print actual, expected
    assert actual == expected

def test_empty_empty_at_ten():
    actual = r.getStringsUntilNRecursiveStep({''}, {'u'}, 10)
    expected = {""}
    print actual, expected
    assert actual == expected

def test_empty_1_at_zero():
    actual = r.getStringsUntilNRecursiveStep({''}, {'u1'}, 0)
    expected = {""}
    print actual, expected
    assert actual == expected

def test_empty_1_at_three():
    expected = {"", "1", "11", "111"}
    actual = r.getStringsUntilNRecursiveStep({''}, {'u1'}, 3)
    print actual, expected
    assert actual == expected

def test_empty_1_or_zero_at_1():
    expected = {"", "1", "0"}
    actual = r.getStringsUntilNRecursiveStep({''}, {'u1', 'u0'}, 1)
    print actual, expected
    assert actual == expected


def test_empty_1_or_zero_at_2():
    expected = {'', '1', '0', '11', '01', '00', '10'}
    actual = r.getStringsUntilNRecursiveStep({''}, {'u1', 'u0'}, 2)
    print actual, expected
    assert actual == expected

def test_1__1_or_zero_at_2():
    expected = {'1', '11', '10', '111', '101', '100', '110'}
    actual = r.getStringsUntilNRecursiveStep({'1'}, {'u1', 'u0'}, 2)
    print actual, expected
    assert actual == expected

def test_multiple_patterns_at_1():
    expected = {'', '0', '1'}
    actual = r.getStringsUntilNRecursiveStep({''}, {'uu0', 'w1u'}, 1)
    print actual, expected
    assert actual == expected

def test_multiple_patterns_at_2():
    expected = {'', '0', '1', '000', '110', '010', '111', '011', '01', '11', '10'}
    actual = r.getStringsUntilNRecursiveStep({''}, {'uu0', 'w1u'}, 2)
    print actual, expected
    assert actual == expected
