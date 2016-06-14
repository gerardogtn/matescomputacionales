import sys
from belongs import belongs

states = []
initialState = ''
finalStates = []
transitionFunction = {}

with open(sys.argv[1], 'r') as file:
    states = file.readline().split()
    initialState = file.readline().split()[0]
    finalStates = file.readline().split()

    n = 0
    for line in file:
        values = line.split()
        current = {}
        for i in range(0, len(values), 2):
            current[values[i]] = values[i + 1]
        transitionFunction[states[n]] = current
        n = n + 1

print transitionFunction
print ("Belongs" if belongs(transitionFunction, initialState, finalStates, sys.argv[2]) else "DOESN'T belong")
