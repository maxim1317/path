#!/usr/bin/env python3

import generator as g
import tangents as tn
import pygame


def draw_scene(M, circleList, tanList, path, Eps, offset):

    bg      = (250, 250, 250)
    bg_dark = (73 , 72 , 62 )
    purple  = (104, 77 , 153)
    magenta = (249, 38 , 114)
    green   = (166, 226, 46 )
    blue    = (102, 217, 239)
    orange  = (253, 151, 31 )

    (width, height) = (600, 600)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Shortest Path')
    screen.fill(bg_dark)

    pygame.draw.rect(screen, orange, (offset, offset, M, M), 3)

    for circ in circleList:
        pygame.draw.circle(
            screen, blue, (round(circ[0]), round(circ[1])), Eps, 2)

        pygame.draw.circle(
            screen, magenta, (round(circ[0]), round(circ[1])), 3, 2)

    for tan in tanList:
        pygame.draw.line(screen, green, tan[0], tan[1], 1)

    for line in range(0, len(path) - 1):
        pygame.draw.line(screen, magenta, path[line], path[line + 1], 2)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return 0


M = 500
N = 4
Eps = 80
offset = 50

circleList = g.generator(M, N, offset)
tans_n_path = tn.all_tans(M, circleList, Eps, offset)
tanList = tans_n_path[0]
path = tans_n_path[1]
draw_scene(M, circleList, tanList, path, Eps, offset)
