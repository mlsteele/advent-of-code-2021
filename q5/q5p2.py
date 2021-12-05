import fileinput
import numpy as np
import re


def walk(xyxy):
    [a, b] = np.split(xyxy, 2)
    if (a == b).all():
        return a
    diff = b - a
    steps = np.amax(np.abs(diff))
    return np.array([a + diff/steps * i for i in range(steps+1)], dtype=int)


def mark(board, xyxy):
    path = walk(xyxy)
    board[path[:, 0], path[:, 1]] += 1


lines = [line for line in fileinput.input()]
arrows = [list(filter(None, re.split('[\->,\s]', line))) for line in lines]
arrows = np.array(arrows, dtype=int)
print(f"{arrows=}")
max_x = np.amax(arrows[:, (0, 2)])
max_y = np.amax(arrows[:, (1, 3)])
board = np.zeros((max_x+1, max_y+1), dtype=int)
print(f"{board=}")
[mark(board, arrow) for arrow in arrows]
print(f"{board=}")
print((board >= 2).sum())
