import fileinput
import operator
from functools import reduce
import numpy as np

# [horizontal depth aim 1] x MAT
DIRECTIONS = {
    "up": lambda x: np.array([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1],
                              [0, 0, -x]]),
    "down": lambda x: np.array([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 1],
                                [0, 0, x]]),
    "forward": lambda x: np.array([[1, 0, 0],
                                   [0, 1, 0],
                                   [0, x, 1],
                                   [x, 0, 0]]),
}

commands = [line.strip().split() for line in fileinput.input()]
commands = [(direction, int(distance)) for (direction, distance) in commands]
moves = [DIRECTIONS[direction](distance) for (direction, distance) in commands]
position = reduce(lambda prev, move: np.concatenate((prev, [1])) @ move,
                  moves, [0, 0, 0])
print(position)
answer = operator.mul(*position[:2])
print(answer)
