import fileinput
import operator
from functools import reduce

DIRECTIONS = {
    "forward": (1, 0),
    "backward": (-1, 0),
    "up": (0, -1),
    "down": (0, 1),
}
def smul(scalar, vec): return tuple(scalar*x for x in vec)


commands = [line.strip().split() for line in fileinput.input()]
commands = [(direction, int(distance)) for (direction, distance) in commands]
moves = [smul(distance, DIRECTIONS[direction])
         for (direction, distance) in commands]
position = reduce(lambda a, b: map(operator.add, a, b), moves)
answer = operator.mul(*position)
print(answer)
