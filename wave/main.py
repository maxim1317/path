import generator as g
import path as p
from classes import *

M = 500      # Size of rectangle
N = 100     # Number of circles
Eps = 12     # Radius of circles
offset = 0  # offset from (0, 0)
step = 1

params = (M, N, Eps, offset)
# Generate circles coordinates:
cList = g.generator(M, N, Eps, offset)
grid = Grid(step, cList, params)
grid.plot()
path = p.findPath((0, 0), (int(M/step), int(M/step)), M, step, grid)
if path:
    path = p.pathShorten(path, cList, Eps)
    print(p.pathLength(path))

