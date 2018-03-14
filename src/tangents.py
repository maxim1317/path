# You know what it is:
import math as m

# From src/calculations.py:
import calculations as calc

# For deepcopy:
import copy as cp

from classes import *


def all_tans(cList, Eps, params):
    """ Very heavy function that should calculate all the tangents """
    M = params[0]
    offset = params[1]

    tList = []
    # graffyGraph = nx.MultiGraph()

    # Dots of start and finish
    C_1 = (offset, M + offset)
    C_2 = (M + offset, offset)

    startPoint= Point(C_1[0], C_1[1], -1, -1)
    finishPoint = Point(C_2[0], C_2[1], -1, -2)
    # 1) Trying to connect start and finish with straight line

    line = Tangent(startPoint, finishPoint, cList, params)
    tList.append(cp.deepcopy(line))

    print("Straight path:", calc.norm(C_1, C_2))

    # 2) Finding all tangents from start/finish

    for c in cList:
        for t in point_tan(startPoint, c, Eps, cList, params):
            tList.append(cp.deepcopy(t))

        for t in point_tan(finishPoint, c, Eps, cList, params):
            tList.append(cp.deepcopy(t))

    # 3) Finding all common tangents between circles

    for c_1 in range(0, len(cList)):
        for c_2 in range(c_1 + 1, len(cList)):
            for t in common_tan(cList[c_1], cList[c_2], Eps, cList, params):
                tList.append(cp.deepcopy(t))

    return tList

def common_tan(circ_1, circ_2, Eps, cList, params):
    """Finds all common tangents between
        two cList, сircles
    returns list of lines with their angle
    """

    o_1 = circ_1.center
    o_2 = circ_2.center

    tanList = []

    # print(o_1[0])
    # print(o_2[0])

    # Find outer tangents
    arctan = m.atan2(o_2[1] - o_1[1], o_2[0] - o_1[0])
    cos = m.cos(m.pi / 2 + arctan)
    sin = m.sin(m.pi / 2 + arctan)

    alpha = arctan

    x = o_1[0] + Eps * cos
    y = o_1[1] + Eps * sin

    p_1 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_1.circle)
    circ_1.add_point(cp.deepcopy(p_1))

    x = o_2[0] + Eps * cos
    y = o_2[1] + Eps * sin

    p_2 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_2.circle)
    circ_2.add_point(cp.deepcopy(p_2))

    line = Tangent(cp.deepcopy(p_1), cp.deepcopy(p_2), cList, params)

    tanList.append(cp.deepcopy(line))

    alpha = m.pi + arctan

    x = o_1[0] - Eps * cos
    y = o_1[1] - Eps * sin

    p_1 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_1.circle)
    circ_1.add_point(cp.deepcopy(p_1))

    x = o_2[0] - Eps * cos
    y = o_2[1] - Eps * sin

    p_2 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_2.circle)
    circ_2.add_point(cp.deepcopy(p_2))

    line = Tangent(cp.deepcopy(p_1), cp.deepcopy(p_2), cList, params)
    tanList.append(cp.deepcopy(line))

    # find inner tangents if exist

    if (calc.norm(o_1, o_2) > 2 * Eps):

        sin = m.sin(m.pi / 2 - m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)
        cos = m.cos(m.pi / 2 - m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)

        alpha = -m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan

        x = o_1[0] + Eps * cos
        y = o_1[1] + Eps * sin
        p_1 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_1.circle)
        circ_1.add_point(cp.deepcopy(p_1))

        x = o_2[0] - Eps * cos
        y = o_2[1] - Eps * sin
        p_2 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(m.pi + alpha), circ_2.circle)
        circ_2.add_point(cp.deepcopy(p_2))

        line = Tangent(p_1, p_2, cList, params)
        tanList.append(cp.deepcopy(line))

        sin = m.sin(m.pi / 2 + m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)
        cos = m.cos(m.pi / 2 + m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan)

        alpha = m.asin(2 * Eps / calc.norm(o_1, o_2)) + arctan

        x = o_1[0] - Eps * cos
        y = o_1[1] - Eps * sin
        p_1 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(m.pi + alpha), circ_1.circle)
        circ_1.add_point(cp.deepcopy(p_1))

        x = o_2[0] + Eps * cos
        y = o_2[1] + Eps * sin
        p_2 = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ_2.circle)
        circ_2.add_point(cp.deepcopy(p_2))

        line = Tangent(p_1, p_2, cList, params)
        tanList.append(cp.deepcopy(line))

    return tanList


def point_tan(point, circ, Eps, cList, params):
    """ Finds tangents between points of start/finish and circles in their
        field of view
        Returns list of tangents and their angle on the circle"""
    tanList = []

    O = circ.center

    arctan = m.atan2(O[1] - point.xy[1], O[0] - point.xy[0])

    cos = m.cos(m.pi / 2 + arctan - m.atan2(Eps, calc.norm(point.xy, O)))
    sin = m.sin(m.pi / 2 + arctan - m.atan2(Eps, calc.norm(point.xy, O)))
    alpha = m.pi + arctan - m.atan2(Eps, calc.norm(point.xy, O))

    x = O[0] - Eps * cos
    y = O[1] - Eps * sin
    p = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ.circle)
    circ.add_point(cp.deepcopy(p))

    line = Tangent(point, cp.deepcopy(p), cList, params)
    tanList.append(cp.deepcopy(line))

    cos = m.cos(m.pi / 2 + arctan + m.atan2(Eps, calc.norm(point.xy, O)))
    sin = m.sin(m.pi / 2 + arctan + m.atan2(Eps, calc.norm(point.xy, O)))
    alpha = arctan + m.atan2(Eps, calc.norm(point.xy, O))

    x = O[0] + Eps * cos
    y = O[1] + Eps * sin
    p = Point(cp.deepcopy(x), cp.deepcopy(y), cp.deepcopy(alpha), circ.circle)
    circ.add_point(cp.deepcopy(p))

    line = Tangent(point, cp.deepcopy(p), cList, params)
    tanList.append(cp.deepcopy(line))

    return tanList
