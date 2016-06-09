from matescomputacionales.datastructures.set import Set

def isReflexive(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are reflexive, false otherwise.
    """
    allSet = Set()
    reflexiveSet = Set()
    for p in pairs:
        allSet.addAll(p)
        if (p[0] == p[1]):
            reflexiveSet.add(p[0])
    return allSet == reflexiveSet

def isIrreflexive(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are irreflexive, false otherwise.
    """
    for p in pairs:
        if (p[0] == p[1]):
            return False
    return True

def isTransitive(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are transitive, false otherwise.
    """
    transitivePairs = []
    for p1 in pairs:
        for p2 in pairs:
            if p1[1] == p2[0]:
                transitivePairs.append([p1[0], p2[1]])
    return containsAll(pairs, transitivePairs)

def containsAll(pairs, targets):
    for t in targets:
        if t not in pairs:
            return False
    return True

def isSymmetric(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are symmetric, false otherwise.
    """
    symmetricPairs = []
    for p in pairs:
        symmetricPairs.append([p[1], p[0]])
    return containsAll(pairs, symmetricPairs)

def isAsymmetric(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are asymmetric, false otherwise.
    """
    for p1 in pairs:
        for p2 in pairs:
            if (p1[0] == p2[1] and p1[1] == p2[0]):
                return False
    return True

def isEquivalent(pairs):
    """ Given a list of pair(a list of two elements). Return true if
    the pairs are equivalent, false otherwise.
    """
    return isReflexive(pairs) and isSymmetric(pairs) and isTransitive(pairs)
