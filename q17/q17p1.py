import fileinput
import re
import numpy as np
from numpy.core.fromnumeric import shape


def step(pos, vel):
    return (pos + vel, vel + [-vel[0]//abs(vel[0]) if vel[0] != 0 else 0, -1])


def all_xs(xvel):
    pos = [0]
    while xvel != 0:
        pos.append(pos[-1]+xvel)
        xvel -= xvel//abs(xvel)
    return pos


def all_ys(yvel, floor):
    pos = [0]
    while pos[-1] >= floor:
        pos.append(pos[-1]+yvel)
        yvel -= 1
    return pos[:-1]


# target area: x=20..30, y=-10..-5
target = np.array([int(x)
                   for x in re.split("[^-\d]", next(fileinput.input()))
                   if len(x)]).reshape((2, 2))
print(target)


# consider x
pos = np.array([0, 0])
vel = np.array([20, 0])
for _ in range(10):
    pos, vel = step(pos, vel)
    print(pos)

print(all_ys(-3, -30))
