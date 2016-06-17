import matescomputacionales.project03.transform as t

def test_transform():
    input_states = ['q0', 'q1']
    input_sigma = {'0', '1'}
    input_delta = {'q0': {'0': ['q0', 'q1'], '1': ['q.1']}, 'q1': {'0': [], '1': ['q0', 'q1']}}
    input_initialState = 'q0'
    input_finalStates = {'q1'}

    expected_states = {'', '[q0]', '[q1]', '[q0,q1]'}
    expected_sigma = {'0', '1'}
    expected_delta = {'': {'0': '', '1': ''}, '[q0]': {'0': '[q0,q1]', '1': '[q1]'}, '[q1]': {'0': '', '1': '[q0,q1]'}, '[q0,q1]': {'0': '[q0,q1]', '1': '[q0,q1]'}}
    expected_initialState = '[q0]'
    expected_finalStates = {'[q1]', '[q0,q1]'}

    actual = t.transform(input_states, input_sigma, input_delta, input_initialState, input_finalStates)

    assert expected_states == actual[0]
    assert expected_sigma == actual[1]
    assert expected_delta == actual[2]
    assert expected_initialState == actual[3]
    assert expected_finalStates == actual[4]

def test_empty_nfa_states():
    expected = {''}
    actual = t.get_dfa_states([])
    assert actual == expected

def test_double_nfa_states():
    doubleSet = ['1', '2']

    expected = {'', '[1]', '[2]', '[1,2]'}
    actual = t.get_dfa_states(doubleSet)
    assert actual == expected

def test_triple_nfa_states():
    tripleSet = ['1', '2', '3']

    expected = {'', '[1]', '[2]', '[3]', '[1,2]', '[1,3]', '[2,3]', '[1,2,3]'}
    actual = t.get_dfa_states(tripleSet)
    assert actual == expected

def test_transition_function():
    input_delta = {'q0': {'0': ['q0', 'q1'], '1': ['q1']}, 'q1': {'0': [], '1': ['q0', 'q1']}}
    sigma = ['0', '1']
    nfaStates= {'q0', 'q1'}
    dfaStates = ['', '[q0]', '[q1]', '[q0,q1]']

    expected = {'': {'0': '', '1': ''}, '[q0]': {'0': '[q0,q1]', '1': '[q1]'}, '[q1]': {'0': '', '1': '[q0,q1]'}, '[q0,q1]': {'0': '[q0,q1]', '1': '[q0,q1]'}}
    actual = t.get_transition_function(input_delta, sigma, dfaStates, nfaStates)
    print 'ACTUAL: \n', actual, '\n ESPERADO: \n', expected
    assert actual == expected

def test_empty_initial_state():
    emptyString = ''

    expected = '[]'
    actual = t.get_initial_state(emptyString)
    assert actual == expected

def test_q0_initial_state():
    q0 = 'q0'

    expected = '[q0]'
    actual = t.get_initial_state(q0)
    assert actual == expected

def test_empty_final_states():
    dfaStates = {frozenset(), frozenset({'q0'})}
    nfaFinalStates = set()

    expected = set()
    actual = t.get_final_states(dfaStates, nfaFinalStates)
    assert actual == expected

def test_double_final_states():
    dfaStates = {frozenset(), frozenset({'q0'}), frozenset({'q1'}), frozenset({'q0', 'q1'})}
    nfaFinalStates = {'q1'}

    expected = {frozenset({'q1'}), frozenset({'q0', 'q1'})}
    actual = t.get_final_states(dfaStates, nfaFinalStates)
    assert actual == expected
