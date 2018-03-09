#!/usr/bin/env python3

import math as m
import numpy as np
import copy as cp


def norm(p_1, p_2):
    return m.sqrt((p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2)


def common_tan(o_1, o_2, Eps):
    """Finds all common tangents between two circles
    returns list of lines
    """
    out = open('gens/tanlist.gen', 'w')

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

    if (norm(o_1, o_2) > 2 * Eps):

        sin = m.sin(m.pi / 2 - m.asin(2 * Eps / norm(o_1, o_2)) + arctan)
        cos = m.cos(m.pi / 2 - m.asin(2 * Eps / norm(o_1, o_2)) + arctan)

        sig = [0, 0]
        sig[0] = (o_1[0] - o_2[0]) / abs(o_1[0] - o_2[0])
        sig[1] = (o_1[1] - o_2[1]) / abs(o_1[1] - o_2[1])

        p_1[0] = o_1[0] + Eps * cos
        p_1[1] = o_1[1] + Eps * sin
        p_2[0] = o_2[0] - Eps * cos
        p_2[1] = o_2[1] - Eps * sin

        line = [p_1, p_2]
        tanList.append(cp.deepcopy(line))

        sin = m.sin(+m.pi / 2 + m.asin(2 * Eps / norm(o_1, o_2)) + arctan)
        cos = m.cos(+m.pi / 2 + m.asin(2 * Eps / norm(o_1, o_2)) + arctan)

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


def point_tan(point, O, circleList, Eps):
    tanList = []
    p = [0.0, 0.0]

    arctan = m.atan2(circleList[O][1] - point[1], circleList[O][0] - point[0])

    cos = m.cos(m.pi / 2 + arctan - m.atan2(Eps, norm(point, circleList[O])))
    sin = m.sin(m.pi / 2 + arctan - m.atan2(Eps, norm(point, circleList[O])))

    p[0] = circleList[O][0] - Eps * cos
    p[1] = circleList[O][1] - Eps * sin

    line = [point, p]

    for i in range(0, len(circleList)):
        if i != O:
            f = check_collisions(line, circleList, point, circleList[O], Eps)

    if f:
        tanList.append(cp.deepcopy(line))

    cos = m.cos(m.pi / 2 + arctan + m.atan2(Eps, norm(point, circleList[O])))
    sin = m.sin(m.pi / 2 + arctan + m.atan2(Eps, norm(point, circleList[O])))

    p[0] = circleList[O][0] + Eps * cos
    p[1] = circleList[O][1] + Eps * sin

    line = [point, p]

    for i in range(0, len(circleList)):
        if i != O:
            f = check_collisions(line, circleList, point, circleList[O], Eps)

    if f:
        tanList.append(cp.deepcopy(line))

    return tanList


def point_to_line_dist(point, s_line):
    """Calculate the distance between a point and a line segment.

    To calculate the closest distance to a line segment, we first need to check
    if the point projects onto the line segment.  If it does, then we calculate
    the orthogonal distance from the point to the line.
    If the point does not project to the line segment, we calculate the
    distance to both endpoints and take the shortest distance.

    :param point: Numpy array of form [x,y], describing the point.
    :type point: numpy.core.multiarray.ndarray
    :param line: list of endpoint arrays of form [P1, P2]
    :type line: list of numpy.core.multiarray.ndarray
    :return: The minimum distance to a point.
    :rtype: float
    """
    # unit vector
    line = np.asarray(s_line)
    unit_line = line[1] - line[0]
    norm_unit_line = unit_line / np.linalg.norm(unit_line)

    # compute the perpendicular distance to the theoretical infinite line
    segment_dist = (
        np.linalg.norm(np.cross(line[1] - line[0], line[0] - point)) /
        np.linalg.norm(unit_line)
    )

    diff = (
        (norm_unit_line[0] * (point[0] - line[0][0])) +
        (norm_unit_line[1] * (point[1] - line[0][1]))
    )

    x_seg = (norm_unit_line[0] * diff) + line[0][0]
    y_seg = (norm_unit_line[1] * diff) + line[0][1]

    endpoint_dist = min(
        np.linalg.norm(line[0] - point),
        np.linalg.norm(line[1] - point)
    )

    # decide if the intersection point falls on the line segment
    lp1_x = line[0][0]  # line point 1 x
    lp1_y = line[0][1]  # line point 1 y
    lp2_x = line[1][0]  # line point 2 x
    lp2_y = line[1][1]  # line point 2 y
    is_betw_x = lp1_x <= x_seg <= lp2_x or lp2_x <= x_seg <= lp1_x
    is_betw_y = lp1_y <= y_seg <= lp2_y or lp2_y <= y_seg <= lp1_y
    if is_betw_x and is_betw_y:
        return segment_dist
    else:
        # if not, then return the minimum distance to the segment endpoints
        return endpoint_dist


def check_collisions(tan, circleList, cur_1, cur_2, Eps):
    """Checks intersections between the line and all of the circles

    Returns True if there are no collision and False otherwise
    """
    for c in circleList:
        if ((c[0] != cur_1[0]) and (c[1] != cur_1[1])) and (
                (c[0] != cur_2[0]) and (c[1] != cur_2[1])):
            if point_to_line_dist(c, tan) < Eps - 0.0000000000001:
                return False

    return True


def all_tans(M, circleList, Eps, offset):
    tanList = []

    C_1 = [offset, M + offset]
    C_2 = [M + offset, offset]

    line = [C_1, C_2]

    f = check_collisions(line, circleList, C_1, C_2, Eps)
    if f:
        tanList.append(cp.deepcopy(line))

    for circ in range(0, len(circleList)):
        tans_1 = (point_tan(C_1, circ, circleList, Eps))
        for t in tans_1:
            tanList.append(cp.deepcopy(t))

        tans_2 = (point_tan(C_2, circ, circleList, Eps))
        for t in tans_2:
            tanList.append(cp.deepcopy(t))

    for circ_1 in range(0, len(circleList)):
        for circ_2 in range(circ_1, len(circleList)):
            if (circleList[circ_1][0] != circleList[circ_2][0]) or (
                    circleList[circ_1][1] != circleList[circ_2][1]):
                tans = common_tan(circleList[circ_1], circleList[circ_2], Eps)
                for t in tans:
                    if check_collisions(
                        t, circleList,
                            circleList[circ_1], circleList[circ_2], Eps):
                        tanList.append(t)

    return tanList
