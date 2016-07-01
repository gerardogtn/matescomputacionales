from derivation import Derivation
import Queue as q
import copy

def getAllDerivations(cfg, string, MAX_SUBSTITUTIONS=3, MAX_DERIVATIONS=5):
    """ Return the derivations of a cfg that generate string.

    Keyword arguments:
    cfg -- A four tuple (or list) that represents a cfg.
        First element must be a set of variables.
        Second element must be a set of terminals.
        Third element must be a Dict<String, List<String> representing all
        the strings that can be reached from string.
        Fourth element is the start symbol/string
    string -- A string to get its derivations using cfg.
    MAX_SUBSTITUTIONS -- Maximum number of substitutions to consider.
    MAX_DERIVATIONS -- Maximum number of derivations to consider.
    """
    return getAllDerivationsRecursive(cfg, string, cfg[3], MAX_SUBSTITUTIONS + 1, MAX_DERIVATIONS, [], 0, [])

def getAllDerivationsRecursive(cfg, string, currentString, maxSubs, maxDevs, derivations, subs, currentDevs):
    if len(derivations) == maxDevs or maxSubs == subs:
        pass
    elif string == currentString:
        currentDevs.append((currentString, -1))
        derivations.append(Derivation(entries=currentDevs))
        currentDevs.pop()
    else:
        numberOfElements = len(currentString)
        for i in range(len(currentString)):
            if (currentString[i] in cfg[0]):
                for v in cfg[2][currentString[i]]:
                    cs = replaceAtIndexWithString(currentString, i, v)
                    currentDevs.append((currentString, i))
                    getAllDerivationsRecursive(cfg, string, cs, maxSubs, maxDevs, derivations, subs + 1, currentDevs)
                    currentDevs.pop()

    return derivations


def replaceAtIndexWithString(base, index, string):
    if index > len(base):
        raise ValueError("index is out of bounds")
    else:
        out = base[:index] + string + base[index+1:]
        return out

def getBoundDerivation(cfg, string, positionFunction):
    queue = q.Queue()
    queue.put((cfg[3], Derivation(entries=[(cfg[3], 0)])))
    while (not queue.empty()):
        current, derivation = queue.get()
        if current == string:
            derivation.add(current, -1)
            derivation.clean()
            return derivation
        elif positionFunction(current, cfg[0]) != -1:
            pos = positionFunction(current, cfg[0])
            for v in cfg[2][current[pos]]:
                newDerivation = copy.deepcopy(derivation)
                newDerivation.add(current, pos)
                queue.put((replaceAtIndexWithString(current, pos, v), newDerivation))
        else:
            pass

def getLeftDerivation(cfg, string):
    return getBoundDerivation(cfg, string, getFirstVariablePosition)

def getRightDerivation(cfg, string):
    return getBoundDerivation(cfg, string, getLastVariablePosition)

def getFirstVariablePosition(string, variables):
    for i in range(len(string)):
        if string[i] in variables:
            return i

    return -1

def getLastVariablePosition(string, variables):
    for i in range(len(string)):
        if string[i - len(string)] in variables:
            return len(string) - i

    return -1
