from matescomputacionales.datastructures.set import Set

""" All strings used as patterns in a recursive definition"""
patternStrings = ['u', 'v', 'w', 'x', 'y', 'z']

def getStringsUntilNRecursiveStep(baseCase, recursiveSteps, N):
    """ Get all the strings formed until N recursive steps

    Keyword arguments:
    baseCase -- BaseRecursiveString defining the base case of the language.
    recursiveSteps -- a set of RecursiveString indicating the valid strings.
    N -- number of recursive steps to perform
    onStringsAtStep -- A function (Set<RecursiveString> -> Void) executed every time
    a recursive step occurs.
    """

    n = 0
    set = Set([baseCase])
    previous = [baseCase]
    while n < N :
        current = []
        for step in recursiveSteps:
            for p in previous:
                newElement = step
                for pattern in patternStrings:
                    newElement = newElement.replace(pattern, p)
                current.append(newElement)
                set.add(newElement)

        previous = current
        n = n + 1

    return set
