""" All strings used as patterns in a recursive definition"""
patternStrings = ['u', 'v', 'w', 'x', 'y', 'z']

def getAllCombinationsForStep(step, combinations, out):
    """" Given a single recursive definition and all possible combinations to fill
    each pattern with, return all possible combinations

    Keyword arguments:
    step -- a string representing a single recursive definition
    combinations -- a python set containing all possible combinations until N
    out -- a python set (initially empty) that accumulates all possible combinations
    for the current step
    """"
    patternsInStep = filter(lambda x: x in patternStrings, step)
    if not patternsInStep :
        out.add(step)
        return out
    else:
        for c in combinations:
            out.union(getAllCombinationsForStep(step.replace(patternsInStep[0], c), combinations, out))
    return out


def getStringsUntilNRecursiveStep(baseCases, recursiveSteps, N, callback=(lambda n, x: x)):
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
    callback(n, allStrings)
    while n < N:
        current = set()
        for step in recursiveSteps:
            current = current.union(getAllCombinationsForStep(step, allStrings, set()))
        callback(n + 1, current - current.intersection(allStrings))
        allStrings = allStrings.union(current)
        n = n + 1

    return allStrings
