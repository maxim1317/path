import math as m
import calculations as calc
import copy as cp
import networkx as nx
import matplotlib.pyplot as plt


def all_tans(M, circleList, Eps, offset):
    tanList = []
    graffyGraph = nx.MultiGraph()

    C_1 = [offset, M + offset]
    C_2 = [M + offset, offset]

    line = [C_1, C_2]
    print("Shortest path", calc.norm(C_1, C_2))
    print

    f = check_collisions(line, circleList, C_1, C_2, Eps, M, offset)
    if f:
        tanList.append(cp.deepcopy(line))

    for circ in range(0, len(circleList)):
        tans_1 = (point_tan(
            C_1, circ, circleList, Eps, M, offset))
        for t in tans_1:
            tanList.append(cp.deepcopy(t))

        tans_2 = (point_tan(
            C_2, circ, circleList, Eps, M, offset))
        for t in tans_2:
            tanList.append(cp.deepcopy(t))

    for circ_1 in range(0, len(circleList)):
        for circ_2 in range(circ_1, len(circleList)):
            if (circleList[circ_1][0] != circleList[circ_2][0]) or (
                    circleList[circ_1][1] != circleList[circ_2][1]):

                tans = common_tan(
                    circ_1, circ_2, Eps, circleList)

                for t in tans:
                    if check_collisions(t, circleList, circleList[
                            circ_1], circleList[circ_2], Eps, M, offset):
                        tanList.append(t)

    for tan in tanList:
        graffyGraph.add_edge(tuple(tan[0]), tuple(
            tan[1]), weight=calc.norm(tan[0], tan[1]))

    # plt.subplot(121)
    # nx.draw(graffyGraph, with_labels=True, font_weight='bold')
    # plt.subplot(122)
    # nx.draw_shell(graffyGraph, nlist=[
    #     range(5, 10), range(5)], with_labels=True, font_weight='bold')

    # l = list(nx.connected_components(graffyGraph))
    # print(l)

    return tanList


def check_collisions(tan, circleList, cur_1, cur_2, Eps, M, offset):
    """Checks intersections between the line and all of the circles

    Returns True if there are no collision and False otherwise
    """
    for c in circleList:
        if ((c[0] != cur_1[0]) and (c[1] != cur_1[1])) and (
                (c[0] != cur_2[0]) and (c[1] != cur_2[1])):
            if calc.point_to_line_dist(c, tan) < Eps - 0.0000000000001:
                return False
            elif ((tan[0][0] < offset) or (tan[0][1] < offset) or (
                    tan[0][0] > offset + M) or (tan[0][1] > offset + M)) or (
                        (tan[1][0] < offset) or (tan[1][1] < offset) or (
                    tan[1][0] > offset + M) or (tan[1][1] > offset + M)):
                return False

    return True


def common_tan(circ_1, circ_2, Eps, circleList):
    """Finds all common tangents between
        two circleList, сircles
    returns list of lines
    """
    out = open('gens/tanlist.gen', 'w')

    o_1 = circleList[circ_1]
    o_2 = circleList[circ_2]

    p_1 = [0.0, 0.0]
    p_2 = [0.0, 0.0]
    tanList = []

    # print(o_1[0])
    # print(o_2[0])
    arctan = m.atan2(o_2[1] - o_1[1], o_2[0] - o_1[0])
    cos = m.cos(m.pi / 2 + arctan)
    sin = m.sin(m.pi / 2 + arctan)

    p_1[0] = o_1[0] + Eps * cos
    p_1[1] = o_1[1] + Eps * sin
    p_2[0] = o_2[0] + Eps * cos
    p_2[1] = o_2[1] + Eps * sin

    line = [p_1, p_2]
    tanList.append(cp.deepcopy(line))

    p_1[0] = o_1[0] - Eps * cos
    p_1[1] = o_1[1] - Eps * sin
    p_2[0] = o_2[0] - Eps * cos
    p_2[1] = o_2[1] - Eps * sin

    line = [p_1, p_2]
    tanList.append(cp.deepcopy(line))

    if (calc.norm(o_1, o_2) > 2 * Eps):

        sin = m.sin(m.pi / 2 - m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)
        cos = m.cos(m.pi / 2 - m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)

        sig = [0, 0]
        sig[0] = (o_1[0] - o_2[0]) / abs(o_1[0] - o_2[0])
        sig[1] = (o_1[1] - o_2[1]) / abs(o_1[1] - o_2[1])

        p_1[0] = o_1[0] + Eps * cos
        p_1[1] = o_1[1] + Eps * sin
        p_2[0] = o_2[0] - Eps * cos
        p_2[1] = o_2[1] - Eps * sin

        line = [p_1, p_2]
        tanList.append(cp.deepcopy(line))

        sin = m.sin(+m.pi / 2 + m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)
        cos = m.cos(+m.pi / 2 + m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)

        p_1[0] = o_1[0] - Eps * cos
        p_1[1] = o_1[1] - Eps * sin
        p_2[0] = o_2[0] + Eps * cos
        p_2[1] = o_2[1] + Eps * sin

        line = [p_1, p_2]
        tanList.append(cp.deepcopy(line))

    for t in tanList:
        for i in t:
            out.write("%s " % i)
        out.write("\n")

    return tanList


def point_tan(point, O, circleList, Eps, M, offset):
    tanList = []
    p = [0.0, 0.0]

    arctan = m.atan2(circleList[O][1] - point[1], circleList[O][0] - point[0])

    cos = m.cos(m.pi / 2 + arctan - m.atan2(
        Eps, calc.norm(point, circleList[O])))
    sin = m.sin(m.pi / 2 + arctan - m.atan2(
        Eps, calc.norm(point, circleList[O])))

    p[0] = circleList[O][0] - Eps * cos
    p[1] = circleList[O][1] - Eps * sin

    line = [point, p]

    f = True

    for i in range(0, len(circleList)):
        if i != O:
            f = check_collisions(line, circleList, point, circleList[
                O], Eps, M, offset)

    if f:
        tanList.append(cp.deepcopy(line))

    cos = m.cos(m.pi / 2 + arctan + m.atan2(
        Eps, calc.norm(point, circleList[O])))
    sin = m.sin(m.pi / 2 + arctan + m.atan2(
        Eps, calc.norm(point, circleList[O])))

    p[0] = circleList[O][0] + Eps * cos
    p[1] = circleList[O][1] + Eps * sin

    line = [point, p]

    f = True

    for i in range(0, len(circleList)):
        if i != O:
            f = check_collisions(line, circleList, point, circleList[
                O], Eps, M, offset)

    if f:
        tanList.append(cp.deepcopy(line))

    return tanList
