from matescomputacionales.datastructures.set import SortedSet

def test_add_empty():
    set = SortedSet()
    set.add(1)

    assert set.entries == [1]

def test_add_all():
    set = SortedSet()
    set.addAll([5, 3, 2, 8])

    assert set.entries == [2, 3, 5, 8]

def test_add_duplicates():
    set = SortedSet(entries=[2, 2, 1])
    assert set.entries = [1, 2]
