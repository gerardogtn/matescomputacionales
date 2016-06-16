import math

def transform(states, sigma, delta, initialState, finalStates):
    """ Return a 5-tuple representing a nfa given the 5-tuple describing a dfa.

    Keyword arguments:
    states -- A set of strings, where each string is a state.
    sigma -- A set of characters, representing the alphabet of the nfa.
    delta -- A Dictionary<String, Dictionary<String, Set<String>>> representing the
    transition function of the nfa.
    initialState -- A string representing the initial state of the nfa.
    finalStates -- A set of strings, each string represent a final state.
    """

    out_states = get_power_set(states)
    out_delta = get_transition_function(delta, sigma, out_states)
    out_initial_state = get_initial_state(initialState)
    out_final_states = get_final_states(out_states, finalStates)

    return [out_states, sigma, out_delta, out_final_states, out_final_states]


def get_dfa_states(givenSet):
    """ Return the power set of a given set"""
    elementList = list(givenSet)
    numberOfElements = len(elementList)
    powerSet = set()

    for i in range(int(math.pow(2, numberOfElements))):
        element = []
        binary = bin(i)[2:].zfill(numberOfElements)
        for j in range(numberOfElements):
            if binary[j] == '1':
                element.append(elementList[j])

        powerSet.add('' if len(element) == 0 else '[{}]'.format(''.join(element)))

    return powerSet

def get_transition_function(delta, sigma, dfaStates):
    """ Return the transition function of a dfa given the transition function
    of a nfa

    Keyword arguments:
    delta -- A Dictionary<String, Dictionary<String, List<String>>> representing
    the transition funcion of a nfa.
    """

    return delta ## STUB

def get_initial_state(initialState):
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
