#!/usr/bin/env python3

import generator as g
import tangents as tn
import pygame


def draw_scene(M, circleList, tanList, path, Eps, offset):
    """ Drawing using pygame."""

    """--------COLORS--------"""
    bg_dark = (73 , 72 , 62 )
    # purple  = (104, 77 , 153)
    magenta = (249, 38 , 114)
    green   = (166, 226, 46 )
    blue    = (102, 217, 239)
    orange  = (253, 151, 31 )
    """----------------------"""

    (width, height) = (600, 600)  # Screen size

    # Draw screen:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Shortest Path')
    screen.fill(bg_dark)

    # Draw frame with size = M:
    pygame.draw.rect(screen, orange, (offset, offset, M, M), 3)

    # Draw circles and dots inside them:
    for circ in circleList:
        pygame.draw.circle(
            screen, blue, (round(circ[0]), round(circ[1])), Eps, 2)

        pygame.draw.circle(
            screen, magenta, (round(circ[0]), round(circ[1])), 3, 2)

    # Draw tangent lines (comment if you can't see shit):
    for tan in tanList:
        pygame.draw.line(screen, green, tan[0], tan[1], 1)

    # Draw a solution path:
    for line in range(0, len(path) - 1):
        pygame.draw.line(screen, magenta, path[line], path[line + 1], 2)

    # pygame shit:
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return 0


M = 500      # Size of rectangle
N = 10       # Number of circles
Eps = 40     # Radius of circles
offset = 50  # offset from (0, 0)

params = (M, offset)
# Generate circles coordinates:
cList = g.generator(M, N, Eps, offset)

# Calculate tangents to and between circles.
# Returns tangent coords and solution:
tans = tn.all_tans(cList, Eps, params)
# tanList = tans_n_path[0]
# path = tans_n_path[1]

# Draw everything with pygame
# draw_scene(M, circleList, tanList, path, Eps, offset)
