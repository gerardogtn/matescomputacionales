""" All strings used as patterns in a recursive definition"""
patternStrings = ['u', 'v', 'w', 'x', 'y', 'z']

def getAllCombinationsForStep(step, combinations, out):
    # print 'Recursive call with step: ', step, " combinations: ", combinations, " out: ", out
    patternsInStep = filter(lambda x: x in patternStrings, step)
    if not patternsInStep :
        out.add(step)
        return out
    else:
        for c in combinations:
            out.union(getAllCombinationsForStep(step.replace(patternsInStep[0], c), combinations, out))
    return out


def getStringsUntilNRecursiveStep(baseCases, recursiveSteps, N, callback=(lambda x: x)):
    """ Get all the strings formed until N recursive steps

    Keyword arguments:
    baseCase -- a list of BaseRecursiveString defining the base case of the language.
    recursiveSteps -- a set of RecursiveString indicating the valid strings.
    N -- number of recursive steps to perform
    onStringsAtStep -- A function (Set<RecursiveString> -> Void) executed every time
    a recursive step occurs.
    """

    n = 0
    allStrings = set()
    allStrings = allStrings.union(baseCases)
    while n < N:
        current = set()
        for step in recursiveSteps:
            current = current.union(getAllCombinationsForStep(step, allStrings, set()))
        callback(current - current.intersection(allStrings))
        allStrings = allStrings.union(current)
        n = n + 1

    return allStrings
