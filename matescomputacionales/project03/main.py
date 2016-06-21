import sys
import transform as t
from matescomputacionales.datastructures.set import Set
import igraph as ig

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

g = ig.Graph(directed=True)

edgeLabels = []
g.add_vertices(map(lambda x: x + '*' if x == dfaInitialState else x, dfaStates))
for node, destinations in dfaDelta.iteritems():
    for weight, destination in dfaDelta[node].iteritems():
        if (node != destination):
            node = node + '*' if node == dfaInitialState else node
            destination = destination + '*' if node == dfaInitialState else destination
            g.add_edge(node, destination)
            edgeLabels.append(weight)

layout = g.layout("kk")

plotProperties = {}
plotProperties["vertex_size"] = 40
plotProperties["vertex_color"] = map(lambda x: 'light blue' if x.replace('*', '') in dfaFinalStates else 'pink', g.vs['name'])
plotProperties["vertex_label"] = g.vs["name"]
g.es["label"] = edgeLabels
plotProperties["edge_label_dist"] = 10
plotProperties["margin"] = 80
ig.plot(g, 'a.png', layout=layout, **plotProperties)
