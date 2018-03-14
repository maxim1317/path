""" Нужно запилить класс или несколько классов, в которых нормальным образом
 будут храниться точки и их принадлежность и положение на кругах """

import math as m
import networkx as nx
import calculations as calc
import copy as cp


class Point():
    def __init__(self, x, y, alpha, circle):
        self.xy = cp.deepcopy((x, y))
        a = alpha
        while a < 0:
            a += 2 * m.pi

        # print(int(a/(2 * m.pi)))
        self.alpha = a - (int(a/(2 * m.pi)) * 2 * m.pi)

        # s = (a/m.pi)
        # print('a = pi *', s)

        self.circle = cp.deepcopy(circle)


class Circle():
    def __init__(self, circle, center, Eps, params):
        self.pList = []
        self.aList = []

        self.circle = cp.deepcopy(circle)
        self.center = cp.deepcopy(center)
        self.Eps = Eps

        self.M = params[0]
        self.offset = params[1]

    def add_clist(self, cList):
        self.cList = cList

    def add_point(self, point):
        if point.circle != self.circle:
            return None

        self.pList.append(cp.deepcopy(point))
        self.aList.append(cp.deepcopy(point.alpha))

    def sort(self):
        self.aList, self.pList = zip(*sorted(zip(self.aList, self.pList)))
        self.aList, self.pList = (list(t) for t in zip(*sorted(zip(self.aList, self.pList))))

    def build_subgraph(self):
        self.G = nx.MultiGraph()
        self.cir_length = 2 * m.pi * self.Eps
        self.real_length = 0

        self.sort()

        for a in range(0, len(self.aList) - 1):
            self.G = Arc(self.pList[a], self.pList[a + 1], self.cList, self.Eps, (self.M, self.offset)).push_to_graph(self.G)
        self.G = Arc(self.pList[a + 1], self.pList[0], self.cList, self.Eps, (self.M, self.offset)).push_to_graph(self.G)

    def push_to_graph(self, G):
        self.build_subgraph()
        joinedG = nx.compose(self.G, G)
        return joinedG


class Tangent():
    def __init__(self, p_1, p_2, cList, params):
        self.C_1 = cp.deepcopy(p_1.circle)
        self.p_1 = cp.deepcopy(p_1.xy)

        self.drawable = False

        self.C_2 = cp.deepcopy(p_2.circle)
        self.p_2 = cp.deepcopy(p_2.xy)

        self.line = cp.deepcopy([[self.p_1[0], self.p_1[1]], [self.p_2[0], self.p_2[1]]])
        self.length = cp.deepcopy(calc.norm(self.p_1, self.p_2))

        self.cList = cList
        self.M = (params[0])
        self.offset = (params[1])

    def check_collisions(self):
        return calc.chk_tan_collisions(self)

    def build_subgraph(self):
        self.G = nx.MultiGraph()

        f = False
        f = self.check_collisions()

        if f:
            self.drawable = True
            self.G.add_edge(self.p_1, self.p_2, weight=self.length, label=str(self.C_1) + '-' + str(self.C_2))

    def push_to_graph(self, G):
        self.build_subgraph()
        joinedG = nx.compose(self.G, G)
        # print(joinedG.edges())
        return joinedG

class Arc():
    def __init__(self, p_1, p_2, cList, Eps, params):
        # print(p_1.circle)
        self.C = cp.deepcopy(p_1.circle)
        self.p_1 = cp.deepcopy(p_1.xy)
        self.a_1 = cp.deepcopy(p_1.alpha)

        self.p_2 = cp.deepcopy(p_2.xy)
        self.a_2 = cp.deepcopy(p_2.alpha)

        self.Eps = Eps

        self.length = cp.deepcopy(calc.arc_length(self.Eps, abs(self.a_2 - self.a_1)))

        self.cList = cList
        self.M = (params[0])
        self.offset = (params[1])

    def check_collisions(self):
        return calc.chk_arc_collisions(self)

    def build_subgraph(self):
        self.G = nx.MultiGraph()

        # if self.check_collisions() is True:
        self.G.add_edge(self.p_1, self.p_2, weight=self.length, label=str(self.C) + '_' + str(round(self.a_1)) + '-' + str(round(self.a_2)))

    def push_to_graph(self, G):
        self.build_subgraph()
        joinedG = nx.compose(self.G, G)
        return joinedG
