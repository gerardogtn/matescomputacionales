import math
import igraph as ig

def draw_automata(dfaStates, dfaDelta, dfaInitialState, dfaFinalStates, fileName):
    g = ig.Graph(directed=True)

    edgeLabels = []
    g.add_vertices(map(lambda x: x + '*' if x == dfaInitialState else x, dfaStates))
    for node, destinations in dfaDelta.iteritems():
        for weight, destination in dfaDelta[node].iteritems():
            if (node != destination):
                node = node + '*' if node == dfaInitialState else node
                destination = destination + '*' if destination == dfaInitialState else destination
                g.add_edge(node, destination)
                edgeLabels.append(weight)

    layout = g.layout("kk")

    nodeSize = 25 + int(math.log(2, len(dfaFinalStates))) * 30

    plotProperties = {}
    plotProperties["vertex_size"] = nodeSize
    plotProperties["vertex_color"] = map(lambda x: 'lightblue' if x.replace('*', '') in dfaFinalStates else 'pink', g.vs['name'])
    plotProperties["vertex_label"] = g.vs["name"]
    g.es["label"] = edgeLabels
    plotProperties["edge_label_dist"] = 10
    plotProperties["margin"] = nodeSize

    try:
        ig.plot(g, fileName + '_solution.png', layout=layout, **plotProperties)
    except TypeError:
        raise RuntimeError("You need to have pycairo installed in order to show a visual representation of the automata.")
