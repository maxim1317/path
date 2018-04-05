import calculations as calc

def findPath(start, finish, M, step, grid):
    out = open('gens/path.txt', 'w')

    path = []

    xyCandidates = []
    mCandidates = []

    border = M/step

    way = -1
    _way = -2

    x = start[0]
    y = start[1]

    minim = grid.grid[0][0].eval()
    _minim = grid.grid[0][0].eval()

    val = str(x*step) + " " + str(y*step) + " " + str(grid.grid[int(x)][int(y)].eval()) + "\n"
    out.write(str(val))
    path.append([(x, y), minim])

    ways = []
    ways.append([ 1, 0])
    ways.append([-1, 0])
    ways.append([ 0, 1])
    ways.append([ 0,-1])
    ways.append([ 1, 1])
    ways.append([ 1,-1])
    ways.append([-1, 1])
    ways.append([-1,-1])

    while (x, y) != finish:

        for i in range(0, len(ways)):
            nx = x + ways[i][0]
            ny = y + ways[i][1]
            if (0 <= nx) and (nx <= border) and (0 <= ny) and (ny <= border):
                if (not grid.grid[int(nx)][int(ny)].passed) and grid.grid[int(nx)][int(ny)].eval() < 3:
                    # print(ny)
                    xyCandidates.append(((nx, ny), i))
                    mCandidates.append(grid.grid[int(nx)][int(ny)].eval())

        if len(mCandidates) != 0:
            _minim = min(mCandidates)
            mIndex = mCandidates.index(_minim)

            # if _minim != minim:
            x = xyCandidates[mIndex][0][0]
            y = xyCandidates[mIndex][0][1]
            grid.grid[x][y].passed = True
            minim = _minim
            # else:
            #     print("! ", mCandidates)
            #     return 0

            _way = xyCandidates[mIndex][1]

            mCandidates = []
            xyCandidates = []

            if _way != way:
                val = str(x*step) + " " + str(y*step) + " " + str(minim) + "\n"
                out.write(str(val))
                path.append([(x, y), minim])
                way = _way



    val = str(x*step) + " " + str(y*step) + " " + str(minim) + "\n"
    out.write(str(val))
    path.append([(x, y), minim])
    return path

def pathLength(path):
    length = 0

    for dot in range(1, len(path)):
        length += calc.my_norm(path[dot][0], path[dot - 1][0])
    return length

def pathShorten(path, cList, Eps):
    out = open('gens/shortenedpath.txt', 'w')
    listlen = len(path)
    s = 0

    pList = []
    # for s in range(0, listlen):
    while s <= listlen - 1:
        f = listlen - 1
        while f > s+1:
            if not calc.collision([path[s][0], path[f][0]], cList, pList, Eps):
                # print(s, f)
                # print(path[s][0], path[f][0])
                del path[s+1:f]
                if len(path[s+1:f]) != 0:
                    listlen -= f - (s+1)
                    f = listlen - 1
                else:
                    f -= 1
            else:
                # print(s, f)
                f -= 1
        s += 1
    # print("!:", listlen)
    for t in path:
        val = str(t[0][0]) + " " + str(t[0][1]) + " " + str(t[1]) + "\n"
        out.write(str(val))
    return path, pList
