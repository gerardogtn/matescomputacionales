import sys
from belongs import belongs

states = []
initialState = ''
finalStates = []
transitionFunction = {}

with open(sys.argv[1], 'r') as file:
    initialState = file.readline().split()[0]
    finalStates = file.readline().split()

    for line in file:
        values = line.split()
        current = {}
        for i in range(1, len(values), 2):
            current[values[i]] = values[i + 1]
        transitionFunction[values[0]] = current

print ("Belongs" if belongs(transitionFunction, initialState, finalStates, sys.argv[2]) else "DOESN'T belong")
