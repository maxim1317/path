""" Нужно запилить класс или несколько классов, в которых нормальным образом
 будут храниться точки и их принадлежность и положение на кругах """

import math as m
import networkx as nx
import calculations as calc


class Point():
    def __init__(self, x, y, alpha, circle):
        self.xy = (x, y)
        self.alpha = alpha
        self.circle = circle


class Circle():
    def __init__(self, circle, center, Eps):
        self.pList = []
        self.aList = []

        self.circle = circle
        self.center = center
        self.Eps = Eps

    def add_point(self, point):
        if point.circle != self.circle:
            return None

        self.pList.append(point)
        self.aList.append(point.alpha)

    def sort(self):
        self.aList, self.pList = zip(*sorted(zip(self.aList, self.pList)))
        self.aList, self.pList = (list(t) for t in zip(*sorted(zip(self.aList, self.pList))))

    def built_subgraph(self):
        self.G = nx.MultiGraph()
        self.cir_length = 2 * m.pi * self.Eps
        self.real_length = 0

        self.sort

        for a in range(0, len(self.aList) - 1):
            self.G = Arc(self.pList[a], self.pList[a + 1], self.cList, self.M, self.offset).push_to_graph(self.G)

    def push_to_graph(self, G):
        self.built_subgraph()
        joinedG = nx.join(self.G, G)
        return joinedG


class Tangent():
    def __init__(self, p_1, p_2, cList, params):
        self.C_1 = p_1.circle
        self.p_1 = p_1.xy

        self.C_2 = p_2.circle
        self.p_2 = p_2.xy

        self.line = (self.p_1, self.p_2)
        self.length = calc.norm(self.p_1, self.p_2)

        self.cList = cList
        self.M = params[0]
        self.offset = params[1]

    def check_collisions(self):
        return calc.chk_tan_collisions(self)

    def build_subgraph(self):
        self.G = nx.MultiGraph()

        if self.check_collisions() is True:
            self.G.add_edge(self.p_1, self.p_2, self.length, label=str(self.C_1) + '-' + str(self.C_2))

    def push_to_graph(self, G):
        self.build_subgraph
        joinedG = nx.join(self.G, G)
        return joinedG

class Arc():
    def __init__(self, p_1, p_2, cList, params):
        self.C = p_1.circle
        self.p_1 = p_1.xy
        self.a_1 = p_1.alpha

        self.p_2 = p_2.xy
        self.a_2 = p_2.alpha

        self.length = calc.norm(p_1, p_2)

        self.cList = cList
        self.M = params[0]
        self.offset = params[1]

    def check_collisions(self):
        return calc.chk_ark_collisions(self)

    def build_subgraph(self):
        self.G = nx.MultiGraph()

        if self.check_collisions() is True:
            self.G.add_edge(self.p_1, self.p_2, self.length, label=str(self.C_1) + '_' + str(round(self.a_1)) + '-' + str(round(self.a_2)))

    def push_to_graph(self, G):
        self.build_subgraph()
        joinedG = nx.join(self.G, G)
        return joinedG
