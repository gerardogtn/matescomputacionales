def belongs(transitionFunction, initialState, finalStates, string):
    currentState = initialState
    for s in string:
        currentState = transitionFunction[currentState][s]
    return currentState in finalStates
