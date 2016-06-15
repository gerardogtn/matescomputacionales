import sys
from belongs import belongs

fileName = sys.argv[1]
stringToTest = sys.argv[2]

initialState = ''
finalStates = []
defaultState = ''
transitionFunction = {}

with open(fileName, 'r') as file:
    initialState = file.readline().split()[0]
    finalStates = file.readline().split()
    defaultState = file.readline().split()[0]

    for line in file:
        values = line.split()
        current = {}
        for i in range(1, len(values), 2):
            current[values[i]] = values[i + 1]
        transitionFunction[values[0]] = current

belongs = belongs(transitionFunction, initialState, finalStates, defaultState, stringToTest)
print ("Belongs" if belongs else "DOESN'T belong")
