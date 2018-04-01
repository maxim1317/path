import calculations as calc
import math as m
import copy as cp

class Grid():
    '''
        Сетка, на вход подается размер шага, список центров окружностей и
        параметры: (M, N, Eps, offset)
    '''
    def __init__(self, step, cList, params):
        self.step = step
        self.side = int(params[0]/step)
        self.cList = cList
        self.params = params

        self.build_grid()

    def build_grid(self):
        self.grid = []
        for y in range(0, self.side + 1):
            row = []
            # print(self.side)
            for x in range(0, self.side + 1):
                row.append(Sector(x, y, self.step, self.cList, self.params, (self.params[0], self.params[0])))

            self.grid.append(row)

    def plot(self):
        out = open('gens/plot.txt', 'w')
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
                val = str(x*self.step) + " " + str(y*self.step) + " " + str(self.grid[x][y].value) + "\n"
                out.write(str(val))
            out.write("\n")

    def waving(self):
        pass

    def find_path(self):
        pass

class Sector():
    '''
    Одна клетка сетки
    '''
    cList = []
    params = ()

    def __init__(self, x, y, step, cList, params, finish):
        self.passed = False
        self.cList = cList
        self.params = params
        self.speed = 1
        self.step = step
        self.xy = (x*step, y*step)
        # print(self.xy)

        # self.value = self.is_obstacle() + finish

        self.finish = finish

        self.x = x
        self.y = y
        self.value = self.potential()
        # print(self.xy, self.value)

    def is_obstacle(self):
        Eps = self.params[2]
        obst = 0
        for c in self.cList:
            d = calc.my_norm(c.center, self.xy)
            if d <= Eps:
                return 3
            if d < self.params[0]:
                # obst += 3 * (Eps / d)**2
                # obst += 3 * m.exp(-d/5)
                obst = 0

        return min(obst, 3)

    def potential(self):
        # d = calc.my_norm((0, 0), (self.params[0], self.params[0]))
        return max(1/self.params[0] * calc.my_norm(self.xy, self.finish), self.is_obstacle())
        # print(self.xy)
        # return  1/self.params[0]**2 * calc.my_norm(self.xy, self.finish)**2


class Circle():
    def __init__(self, circle, center, Eps, params):
        self.pList = []
        self.aList = []

        self.circle = cp.deepcopy(circle)
        self.center = cp.deepcopy(center)
        self.Eps = Eps

        self.M = params[0]
        self.offset = params[1]

    def add_clist(self, cList):
        self.cList = cList

    def sort(self):
        self.aList, self.pList = zip(*sorted(zip(self.aList, self.pList)))
        self.aList, self.pList = (list(t) for t in zip(*sorted(zip(self.aList, self.pList))))
