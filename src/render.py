#!/usr/bin/env python3

import pygame
import generator as g
import calculations as calc


def draw_scene(M, circleList, tanList, Eps, offset):

    background_colour = (255, 255, 255)
    (width, height) = (600, 600)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    screen.fill(background_colour)

    pygame.draw.rect(screen, (0, 0, 0), (offset, offset, M, M), 1)

    for circ in circleList:
        pygame.draw.circle(
            screen, (0, 0, 255), (round(circ[0]), round(circ[1])), Eps, 2)
        pygame.draw.circle(
            screen, (255, 0, 0), (round(circ[0]), round(circ[1])), 5, 5)

    for tan in tanList:
        pygame.draw.line(screen, (255, 0, 0), tan[0], tan[1], 2)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


circleList = g.generator(500, 2, 50)
tanList = calc.all_tans(circleList, 50)
draw_scene(500, circleList, tanList, 50, 50)
