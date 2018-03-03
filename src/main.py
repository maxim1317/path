import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import math as m

# vertices = []
# codes = []

# codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
# vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
# vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]

# vertices = np.array(vertices, float)
# path = Path(vertices, codes)

# pathpatch = PathPatch(path, facecolor='None', edgecolor='green')

# fig, ax = plt.subplots()
# ax.add_patch(pathpatch)
# ax.set_title('A compound path')

# ax.dataLim.update_from_data_xy(vertices)
# ax.autoscale_view()


# plt.show()

cir_1 = [0.0,3.0]
cir_2 = [7.0,3.0]

def norm(p_1, p_2):
    return m.sqrt((p_2[0]-p_1[0])**2+(p_2[1]-p_1[1])**2)

def common(o_1, o_2, rad):
    p_1=[0.0,0.0]
    p_2=[0.0,0.0]
    p_3=[0.0,0.0]
    p_4=[0.0,0.0]
    p_5=[0.0,0.0]
    p_6=[0.0,0.0]
    p_7=[0.0,0.0]
    p_8=[0.0,0.0]

    arctan = m.atan((o_2[1] - o_1[1]) / (o_2[0] - o_1[0]))
    cos = m.cos(m.pi/2 - arctan)
    sin = m.sin(m.pi/2 - arctan)
    
    p_1[0] = o_1[0] + rad * cos
    p_1[1] = o_1[1] + rad * sin
    p_2[0] = o_2[0] + rad * cos
    p_2[1] = o_2[1] + rad * sin
    
    line_1 = [p_1, p_2]

    p_3[0] = o_1[0] - rad * cos
    p_3[1] = o_1[1] - rad * sin
    p_4[0] = o_2[0] - rad * cos
    p_4[1] = o_2[1] - rad * sin
    
    line_2 = [p_3, p_4]

    if (norm(o_1, o_2)<=2*rad):
        out = (line_1, line_2)
        print(norm(o_1,o_2))
    
    else:
        sin = m.sin(m.pi/2 - m.asin(2 * rad / norm(o_1, o_2)))
        cos = m.cos(m.pi/2 - m.asin(2 * rad / norm(o_1, o_2)))
        
        p_5[0] = o_1[0] + rad * cos
        p_5[1] = o_1[1] + rad * sin
        p_6[0] = o_2[0] - rad * cos
        p_6[1] = o_2[1] - rad * sin

        line_3 = [p_5, p_6]

        p_7[0] = o_1[0] - rad * cos
        p_7[1] = o_1[1] - rad * sin
        p_8[0] = o_2[0] + rad * cos
        p_8[1] = o_2[1] + rad * sin

        line_4 = [p_7, p_8]

        out = (line_1, line_2, line_3, line_4)

    return out

out = common(cir_1,cir_2,3)
print(out)