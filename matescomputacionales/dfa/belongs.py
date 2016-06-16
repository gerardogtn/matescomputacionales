def belongs(transitionFunction, initialState, finalStates, string, defaultState="",):
    currentState = initialState
    for s in string:
        try:
            currentState = transitionFunction[currentState][s]
        except KeyError:
            currentState = defaultState
    return currentState in finalStates
