#!/usr/bin/env python3

import random


def generator(M, N, offset):
    """ Takes M (rectangle size), N (number of circles) and
        offset to get coordinates right
        And generates coordinates of circle. Nothing fancy.
        Returns list of points """

    circleList = []
    out = open('gens/circlelist.gen', 'w')

    for i in range(N):
        circle = [random.uniform(0, M) + offset, random.uniform(0, M) + offset]
        circleList.append(circle)
    for p in circleList:
        for i in p:
            out.write("%s " % i)
        out.write("\n")

    return circleList
