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

    out_states = get_dfa_states(states)
    out_delta = get_transition_function(delta, sigma, out_states, states)
    out_initial_state = get_initial_state(initialState)
    out_final_states = get_final_states(out_states, finalStates)

    return [out_states, sigma, out_delta, out_final_states, out_final_states]


def get_dfa_states(nfaStates):
    """ Return all the dfa states given the nfa states

    Keyword arguments:
    nfaStates -- a list of states in the nfa.
    """
    elementList = list(nfaStates)
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
    emptyKey = {}
    for a in sigma: emptyKey[a] = ''
    transitionFunction[''] = emptyKey

    for nfas in nfaState:
        current = {}
        for key in delta[nfas]:
            if len(delta[nfas][key]) == 0:
                current[key] = ''
            else:
                 current[key] = '[{}]'.format(','.join(delta[nfas][key]))

        transitionFunction[get_initial_state(nfas)] = current

    for dfas in dfaStates:
        nfaStates = dfas[1:-1].split(',')
        if len(nfaStates) > 1:
            myDict = {}
            for a in sigma:
                current = set()
                for nfas in nfaStates:
                    current = current.union(transitionFunction[get_initial_state(nfas)][a][1:-1].split(','))
                orderedElements = list(current)
                orderedElements.sort()
                orderedElements = filter(lambda x: x != '', orderedElements)
                myDict[a] = '' if len(current) == 0 else '[{}]'.format(','.join(orderedElements))
            transitionFunction[dfas] = myDict

    # for dfas in dfaStates:
    #     newState = {}
    #     nfaStates = dfas[1:-1].split(',')
    #     for nfas in nfaStates:
    #         for a in sigma:
    #             try:
    #                 newState[a].add(nfas)
    #             except KeyError:
    #                 newState[a] = {nfas}
    #
    #     for a in sigma:
    #         print newState[a]
    #         newState[a] = '' if newState[a] == {''} else '[{}]'.format(','.join(newState[a]))
    #
    #     transitionFunction[dfas] = newState

    return transitionFunction

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
