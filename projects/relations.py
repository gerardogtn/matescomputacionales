from set import Set
## Given a list of pairs, representing a relation, return true if
## the relation is reflexive, False otherwise.
def isReflexive(pairs):
    allSet = Set()
    reflexiveSet = Set()
    for p in pairs:
        allSet.addAll(p)
        if (p[0] == p[1]):
            reflexiveSet.add(p[0])
    return allSet == reflexiveSet

## List<List<Char>> -> Bool
## Given a list of pairs, representing a relation, return true if
## the relation is irreflexive, False otherwise.
def isIrreflexive(pairs):
    for p in pairs:
        if (p[0] == p[1]):
            return False
    return True

## List<List<Char>> -> Bool
## Given a list of pairs, representing a relation, return true if
## the relation is transitive, False otherwise.
def isTransitive(pairs):
    transitiveSet = Set()
    for p1 in pairs:
        for p2 in pairs:
            for p3 in pairs:
                if (not containsAll(p1, p2, transitiveSet) and p1[0] == p3[1] and p1[1] == p2[0] and p2[1] == p3[0]):
                    transitiveSet.addAll(p1)
                    transitiveSet.addAll(p2)

    allSet = Set()
    [allSet.addAll(x) for x in pairs]
    return transitiveSet.size() == allSet.size()


def containsAll(firstPair, secondPair, set):
    out = True
    for e in firstPair:
        out = out and set.contains(e)
    for e in secondPair:
        out = out and set.contains(e)
    return out


## List<List<Char>> -> Bool
## Given a list of pairs, representing a relation, return true if
## the relation is symmetric, False otherwise.
def isSymmetric(pairs):
    out = True
    for p1 in pairs:
        found = False
        for p2 in pairs:
            if (p1[0] == p2[1] and p1[1] == p2[0]):
                found = True
                break
        out = out and found
    return out

## List<List<Char>> -> Bool
## Given a list of pairs, representing a relation, return true if
## the relation is asymetric, False otherwise.
def isAsymmetric(pairs):
    for p1 in pairs:
        for p2 in pairs:
            if (p1[0] == p2[1] and p1[1] == p2[0]):
                return False
    return True

## List<List<Char>> -> Bool
## Given a list of pairs, representing a relation, return true if
## the relation is equivalent, False otherwise.
def isEquivalent(pairs):
    return isReflexive(pairs) and isSymmetric(pairs) and isTransitive(pairs)
