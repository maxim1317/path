#!/usr/bin/env python3

import calculations as calc
import generator as g
import tangents as tn
import graph as gph
import pygame

# import colored_traceback
# colored_traceback.add_hook()


def draw_scene(cList, tList, Eps, path, params, text):
    """ Drawing using pygame."""

    """--------COLORS--------"""
    bg_dark = (73 , 72 , 62 )
    purple  = (104, 77 , 153)
    magenta = (249, 38 , 114)
    green   = (166, 226, 46 )
    blue    = (102, 217, 239)
    orange  = (253, 151, 31 )
    """----------------------"""

    M = params[0]
    offset = params[1]

    (width, height) = (600, 600)  # Screen size

    pygame.font.init()
    myfont = pygame.font.SysFont('DejaVu Sans Mono Book', 25)
    calculatedSurf = myfont.render('Calculated path = ' + text[1], True, orange)
    straightSurf = myfont.render('Straight path = ' + text[0], True, orange)

    # Draw screen:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Shortest Path')
    screen.fill(bg_dark)

    # Draw frame with size = M:
    pygame.draw.rect(screen, orange, (offset, offset, M, M), 3)

    # Draw circles and dots inside them:
    for c in cList:
        pygame.draw.circle(
            screen, blue, (round(c.center[0]), round(c.center[1])), Eps, 2)

        pygame.draw.circle(
            screen, magenta, (round(c.center[0]), round(c.center[1])), 3, 2)

    # Draw tangent lines (comment if you can't see shit):
    for t in tList:
        if t.drawable:
            pygame.draw.line(screen, green, t.p_1, t.p_2, 1)

    # Draw a solution path:
    for line in range(0, len(path) - 1):
        pygame.draw.line(screen, magenta, path[line], path[line + 1], 3)

    screen.blit(straightSurf,(400, 5))
    screen.blit(calculatedSurf,(5, 5))

    # pygame shit:
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return 0


M = 500      # Size of rectangle
N = 15      # Number of circles
Eps = 50     # Radius of circles
offset = 50  # offset from (0, 0)

params = (M, offset)
# Generate circles coordinates:
cList = g.generator(M, N, Eps, offset)

# Calculate tangents to and between circles.
# Returns tangent coords and solution:
tList = tn.all_tans(cList, Eps, params)
G = gph.build_graph(tList, cList)

C_1 = (offset, M + offset)
C_2 = (M + offset, offset)

path = gph.dijkstra_path(G, C_1, C_2)

text = ['a', 'a']
text[0] = str(round(calc.norm(C_1, C_2), 3))
text[1] = gph.path_length(G, C_1, C_2)

# Draw everything with pygame
draw_scene(cList, tList, Eps, path, params, text)
