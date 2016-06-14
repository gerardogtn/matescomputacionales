import matescomputacionales.dfa.belongs as b

transitionFunction = {'q1': {'1': 'q3', '0': 'q0'}, 'q0': {'1': 'q2', '0': 'q1'}, 'q3': {'1': 'q1', '0': 'q2'}, 'q2': {'1': 'q0', '0': 'q3'}}
initialState = 'q0'
finalStates = ['q0']

def test_empty():
    assert b.belongs(transitionFunction, initialState, finalStates, '')

def test_one_digit():
    assert not b.belongs(transitionFunction, initialState, finalStates, '0') and not b.belongs(transitionFunction, initialState, finalStates, '1')

def test_simple_double():
    assert b.belongs(transitionFunction, initialState, finalStates, '00') and b.belongs(transitionFunction, initialState, finalStates, '11')

def test_complex_double():
    assert b.belongs(transitionFunction, initialState, finalStates, '1001') and b.belongs(transitionFunction, initialState, finalStates, '0110') and b.belongs(transitionFunction, initialState, finalStates, '0101') and b.belongs(transitionFunction, initialState, finalStates, '1010')
