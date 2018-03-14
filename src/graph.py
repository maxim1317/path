# Graph class with fancy graph algorithms:
import networkx as nx

# Draws graph:
from nxpd import draw

def build_graph(tList, cList):
    G = nx.MultiGraph()

    for t in tList:
        G = t.push_to_graph(G)
    for c in cList:
        G = c.push_to_graph(G)

    # print(G.edges())
    # draw(G)

    return G

def dijkstra_path(G, from_point, to_point):
    # draw(G)
    return nx.dijkstra_path(G, tuple(from_point), tuple(to_point))

def path_length(G, from_point, to_point):
    return str(round(nx.dijkstra_path_length(G, tuple(from_point), tuple(to_point)), 3))

