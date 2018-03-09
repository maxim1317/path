#!/usr/bin/env python3

import generator as g
import calculations as calc
import pygame


def draw_scene(M, circleList, tanList, Eps, offset):

    background_colour = (255, 255, 255)
    (width, height) = (600, 600)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Shortest Path')
    screen.fill(background_colour)

    pygame.draw.rect(screen, (0, 0, 0), (offset, offset, M, M), 1)

    for circ in circleList:
        pygame.draw.circle(
            screen, (0, 0, 255), (round(circ[0]), round(circ[1])), Eps, 2)
        pygame.draw.circle(
            screen, (255, 0, 0), (round(circ[0]), round(circ[1])), 5, 5)

    for tan in tanList:
        pygame.draw.line(screen, (255, 0, 255), tan[0], tan[1], 1)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return 0


M = 500
N = 7
Eps = 50
offset = 50

circleList = g.generator(M, N, offset)
tanList = calc.all_tans(M, circleList, Eps, offset)
draw_scene(M, circleList, tanList, Eps, offset)
