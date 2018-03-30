import calculations as calc

class Grid():
    '''
        Сетка, на вход подается размер шага, список центров окружностей и
        параметры: (M, N, Eps, offset)
    '''
    def __init__(self, step, cList, params):
        self.step
        self.side = int(params[0]/step)
        self.cList = cList
        self.params = params

        self.build_grid()

    def build_grid(self):
        self.grid = []
        for y in self.side:
            row = []
            for x in self.side:
                row.append(Sector(x, y, self.step, self.cList, self.params))

            self.grid.append(row)

    def is_obstacle(self):
        pass

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
    step = 0

    def __init__(self, x, y, step, cList, params, finish=0):
        self.cList = cList
        self.params = params
        self.step = step

        self.value = self.is_obstacle() + finish

        self.xy = (params[3] + x*step + step/2, params[3] + y*step + step/2)

        self.x = x
        self.y = y

    def is_obstacle(self):
        Eps = self.params[2]
        for c in self.cList:
            if calc.norm(c, self.xy) < Eps:
                return 1

        return 0
