#!/usr/bin/env python3

import math as m
# import numpy as np
from numpy import arccos, array, dot, pi, cross
from numpy.linalg import det, norm


def my_norm(p_1, p_2):
    """Takes to points and counts distance between them"""
    return m.sqrt((p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2)


def arc_length(Eps, alpha):
    """This should count arc length in Rads"""
    return Eps * alpha


# def point_to_line_dist(point, s_line):
#     """Calculate the distance between a point and a line segment.

#     To calculate the closest distance to a line segment, we first need to check
#     if the point projects onto the line segment.  If it does, then we calculate
#     the orthogonal distance from the point to the line.
#     If the point does not project to the line segment, we calculate the
#     distance to both endpoints and take the shortest distance.

#     :param point: Numpy array of form [x,y], describing the point.
#     :type point: numpy.core.multiarray.ndarray
#     :param line: list of endpoint arrays of form [P1, P2]
#     :type line: list of numpy.core.multiarray.ndarray
#     :return: The minimum distance to a point.
#     :rtype: float

#     Did't write it myself. Found on stackoverflow
#     """
#     # unit vector
#     line = np.asarray(s_line)
#     unit_line = line[1] - line[0]
#     norm_unit_line = unit_line / np.linalg.norm(unit_line)

#     # compute the perpendicular distance to the theoretical infinite line
#     segment_dist = (
#         np.linalg.norm(np.cross(line[1] - line[0], line[0] - point)) /
#         np.linalg.norm(unit_line)
#     )

#     diff = (
#         (norm_unit_line[0] * (point[0] - line[0][0])) +
#         (norm_unit_line[1] * (point[1] - line[0][1]))
#     )

#     x_seg = (norm_unit_line[0] * diff) + line[0][0]
#     y_seg = (norm_unit_line[1] * diff) + line[0][1]

#     endpoint_dist = min(
#         np.linalg.norm(line[0] - point),
#         np.linalg.norm(line[1] - point)
#     )

#     # decide if the intersection point falls on the line segment
#     lp1_x = line[0][0]  # line point 1 x
#     lp1_y = line[0][1]  # line point 1 y
#     lp2_x = line[1][0]  # line point 2 x
#     lp2_y = line[1][1]  # line point 2 y
#     is_betw_x = lp1_x <= x_seg <= lp2_x or lp2_x <= x_seg <= lp1_x
#     is_betw_y = lp1_y <= y_seg <= lp2_y or lp2_y <= y_seg <= lp1_y
#     if is_betw_x and is_betw_y:
#         return segment_dist
#     else:
#         # if not, then return the minimum distance to the segment endpoints
#         return endpoint_dist


# from: https://gist.github.com/nim65s/5e9902cd67f094ce65b0
def distance_numpy(A, B, P):
    """ segment line AB, point P, where each one is an array([x, y]) """
    if all(A == P) or all(B == P):
        return 0
    if arccos(dot((P - A) / norm(P - A), (B - A) / norm(B - A))) > pi / 2:
        return norm(P - A)
    if arccos(dot((P - B) / norm(P - B), (A - B) / norm(A - B))) > pi / 2:
        return norm(P - B)
    return norm(cross(A-B, A-P))/norm(B-A)

def collision(tan, cList, Eps):
    """Checks intersections between the line and all of the circles

    Returns True if there are no collisions and False otherwise
    """
    ds = []
    for c in cList:
        # d = point_to_line_dist(c.center, tan)
        A = array(tan[0])
        B = array(tan[1])
        P = array([c.center[0], c.center[1]])
        d = distance_numpy(A, B, P)
        ds.append(d)
        if d < Eps + 0.5:
            # print("no", point_to_line_dist(c.center, tan))
            # print("d =",point_to_line_dist([c.center[0], c.center[1]], tan))
            return True
    print("so", min(ds))
    return False



