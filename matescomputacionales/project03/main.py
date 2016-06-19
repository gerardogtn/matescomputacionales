import sys
import transform as t
from matescomputacionales.datastructures.set import Set
import networkx as nx
import matplotlib.pyplot as plt

inputFileName = sys.argv[1]
stringsInFileName = sys.argv[1].split('.')
outputFileName = '_solution.'.join(stringsInFileName)

outFile = open(outputFileName, 'w')


states = Set()
sigma = set()
initialState = ''
finalStates = set()
delta = {}

with open(inputFileName, 'r') as file:
    states.addAll(file.readline().split())
    sigma = sigma.union(file.readline().split())
    initialState = file.readline().split()[0]
    finalStates = finalStates.union(file.readline().split())

    for line in file:
        values = line.split()
        current = {}
        for i in range(1, len(values), 2):
            statesReached = values[i+1]
            if statesReached == 'empty':
                current[values[i]] = []
            else:
                current[values[i]] = statesReached[1:-1].split(',')
        delta[values[0]] = current

dfaStates, dfaSigma, dfaDelta, dfaInitialState, dfaFinalStates = t.transform(states, sigma, delta, initialState, finalStates)

outFile.write('{}\n'.format(' '.join(map(lambda x: 'empty' if x == '' else x, dfaStates))))
outFile.write('{}\n'.format(' '.join(dfaSigma)))
outFile.write('{}\n'.format(dfaInitialState))
outFile.write('{}\n'.format(' '.join(dfaFinalStates)))

for s in dfaDelta:
    text = [s] if s != '' else ['empty']
    for k,v in dfaDelta[s].iteritems():
        text.append(k if k != '' else 'empty')
        text.append(v if v != '' else 'empty')
    outFile.write('{}\n'.format(' '.join(text)))

outFile.close()

G = nx.DiGraph()
G.add_nodes_from(map(lambda x: x + '*' if x == dfaInitialState else x, dfaStates))

for node, destinations in dfaDelta.iteritems():
    for weight, destination in dfaDelta[node].iteritems():
        node = node + '*' if node == dfaInitialState else node
        destination = destination + '8' if node == dfaInitialState else destination
        G.add_edge(node, destination, {'':weight})

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1800)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos)
G = nx.DiGraph()
G.add_nodes_from(dfaFinalStates)
nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='b')

plt.savefig(inputFileName.split('.')[0] + "_solution.png")
