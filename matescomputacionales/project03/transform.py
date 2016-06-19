import math
from matescomputacionales.datastructures.set import Set
from matescomputacionales.datastructures.set import SortedSet

def transform(states, sigma, delta, initialState, finalStates):
    """ Return a 5-tuple representing a nfa given the 5-tuple describing a dfa.

    Keyword arguments:
    states -- A matescomputacionales.datastructures.set.Set of strings,
    where each string is a state.
    sigma -- A set of characters, representing the alphabet of the nfa.
    delta -- A Dictionary<String, Dictionary<String, List<String>>> representing
    the transition function of the nfa.
    initialState -- A string representing the initial state of the nfa.
    finalStates -- A set of strings, each string represent a final state.
    """

    out_states = get_dfa_states(states)
    out_delta = get_transition_function(delta, sigma, out_states, states)
    out_initial_state = surround_with_brackets(initialState)
    out_final_states = get_final_states(out_states, finalStates)

    return [out_states, sigma, out_delta, out_final_states, out_final_states]


def get_dfa_states(nfaStates):
    """ Return a python set containing all dfa states given the nfa states.

    Keyword arguments:
    nfaStates -- a list of states in the nfa.
    """
    elementList = nfaStates.entries
    numberOfElements = len(elementList)
    dfaStates = set()

    for i in range(int(math.pow(2, numberOfElements))):
        currentState = []
        binary_i = bin(i)[2:].zfill(numberOfElements)
        for j in range(numberOfElements):
            if binary_i[j] == '1':
                currentState.append(elementList[j])

        dfaStates.add('' if len(currentState) == 0 else '[{}]'.format(','.join(currentState)))

    return dfaStates

def get_transition_function(delta, sigma, dfaStates, nfaState):
    """ Return the transition function of a dfa given the transition function
    of a nfa

    Keyword arguments:
    delta -- A Dictionary<String, Dictionary<String, List<String>>> representing
    the transition funcion of a nfa.
    sigma -- A set containing all characters in the alphabet.
    dfaStates -- All the states in the dfa representation of the nfa.
    """
    transitionFunction = {}
    transitionFunction[''] = get_empty_states(sigma)

    for nfas in nfaState:
        transitionFunction[surround_with_brackets(nfas)] = get_single_states(delta, nfas)

    for dfas in dfaStates:
        nfaStates = dfas[1:-1].split(',')
        if len(nfaStates) > 1:
            transitionFunction[dfas] = get_compound_states(nfaStates, sigma, transitionFunction)

    return transitionFunction

def get_empty_states(sigma):
    """ Return a dict from each character to sigma to the empty string.

    Keyword arguments:
    sigma -- An iterable with all the characters in an alphabet,
    with no repetitions.
    """
    emptyKey = {}
    for a in sigma: emptyKey[a] = ''
    return emptyKey

def get_single_states(delta, nfaState):
    """ Return a Dictionary<String, String> representing the dfa transitions
    from a nfaState with a transition function delta.

    Keyword arguments:
    delta -- A Dictionary<String, Dictionary<String, List<String>>> representing
    all the possible states that can be reached from a state with input char.
    nfaState -- A String representing a state in the nfa.
    """
    dfaState = {}
    for char in delta[nfaState]:
        if len(delta[nfaState][char]) == 0:
            dfaState[char] = ''
        else:
            dfaState[char] = '[{}]'.format(','.join(delta[nfaState][char]))
    return dfaState

def get_compound_states(nfaStates, sigma, transitionFunction):
    """ Given the transitionfunction for all individual states, and the nfaStates
    that are part of a dfa state, return a dict with each character poiting to the
    appropiate dfa state

    Keyword arguments:
    nfaStates -- An iterable of string where each represents a reachable state.
    sigma -- The alphabet of the nfa.
    transitionFunction -- The transitionFunction for the dfa, at least filled with
    the transition states for all the single states.
    """
    
    dfaState = {}
    for a in sigma:
        current = SortedSet()
        for nfas in nfaStates:
            current.addAll(transitionFunction[surround_with_brackets(nfas)][a][1:-1].split(','))
        current.remove('')
        dfaState[a] = '' if current.isEmpty() else '[{}]'.format(','.join(current.entries))
    return dfaState

def surround_with_brackets(initialState):
    """ Return the given string surrounded by brackets """
    return '[{}]'.format(initialState)

def get_final_states(dfaStates, nfaFinalStates):
    """ All the states in dfaStates, with at least one element in nfaFinalStates

    Keyword arguments:
    dfaStates -- A set representing all the possible states in the dfa.
    nfaFinalStates -- A set representing all the final states in the nfa.
    """
    out = set()

    for ds in dfaStates:
        for fs in nfaFinalStates:
            if fs in ds:
                out.add(ds)
                break
    return out
