# Graph class with fancy graph algorithms:
import networkx as nx

# Draws graph:
from nxpd import draw

def build_graph(tList, cList):
    G = nx.MultiGraph()

    for t in tList:
        G = t.push_to_graph(G)

    # print(G.edges())
    # draw(G)

    return G

def dijkstra_path(G, from_point, to_point):
    return nx.dijkstra_path(G, tuple(from_point), tuple(to_point))
