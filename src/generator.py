#!/usr/bin/env python3

import random
import classes as cl
import calculations as calc
import math as m

def generator(M, N, Eps, offset):
    """ Takes M (rectangle size), N (number of circles) and
        offset to get coordinates right
        And generates coordinates of circle. Nothing fancy.
        Returns list of points """

    params = (M, offset)

    circleList = []
    out = open('gens/circlelist.gen', 'w')

    C_1 = (offset, M + offset)
    C_2 = (M + offset, offset)

    for i in range(N):
        center = (random.uniform(0, M) + offset, random.uniform(0, M) + offset)

        while (calc.norm(C_1, center) <= Eps * m.sqrt(2)) or (calc.norm(C_2, center) <= Eps * m.sqrt(2)):

            center = (random.uniform(0, M) + offset, random.uniform(0, M) + offset)

        circle = cl.Circle(i, center, Eps, params)
        circleList.append(circle)

    for c in circleList:
        c.add_clist(circleList)

    for p in circleList:
        for i in p.center:
            out.write("%s " % i)
        out.write("\n")

    return circleList
