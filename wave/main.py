import generator as g
import path as p
from classes import *
import pygame
import calculations as calc
import multiprocessing as mp
import os


def draw_scene(cList, Eps, path, params, text):
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
    offset = 50

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
            screen, blue, (round(c.center[0])+offset, M - round(c.center[1])+offset), Eps, 2)

        pygame.draw.circle(
            screen, magenta, (round(c.center[0])+offset, M - round(c.center[1])+offset), 3, 2)

    # Draw tangent lines (comment if you can't see shit):
    # for t in tList:
        # if t.drawable:
        #     pygame.draw.line(screen, green, t.p_1, t.p_2, 1)

    # Draw a solution path:
    for line in range(0, len(path) - 1):
        pygame.draw.line(screen, magenta, (path[line][0][0]+offset, M - path[line][0][1]+offset), (path[line + 1][0][0]+offset, M - path[line + 1][0][1]+offset), 3)

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

def plot(grid):
    for x in range(0, len(grid.grid)):
        for y in range(0, len(grid.grid)):
            grid.grid[x][y].eval()

    grid.plot()

    os.system("gnuplot --persist wave/plots/plot.gnu& > /dev/null 2>&1")

if __name__ == '__main__':

    M = 500      # Size of rectangle
    N = 30     # Number of circles
    Eps = 35     # Radius of circles
    offset = 0  # offset from (0, 0)
    step = 1

    params = (M, N, Eps, offset)

    text = []
    text.append(str(calc.my_norm((0, 0), (500, 500))))

    # Generate circles coordinates:
    cList = g.generator(M, N, Eps, offset)
    grid = Grid(step, cList, params)
    path = p.findPath((0, 0), (int(M/step), int(M/step)), M, step, grid)
    if path:
        print("All good")
        path, pList = p.pathShorten(path, cList, Eps)
        text.append(str(p.pathLength(path)))

processDraw = mp.Process(target=draw_scene, args=(cList, Eps, path, params, text,))
processPlot = mp.Process(target=plot, args=(grid,))

processDraw.start()
processPlot.start()
