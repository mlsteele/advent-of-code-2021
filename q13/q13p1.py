import fileinput
import numpy as np
from functools import reduce

lines = list(fileinput.input())
dots = np.array([tuple(map(int, line.strip().split(',')))
                 for line in lines if ',' in line])
# [(axis, offset), ...]
folds = [(line.split('=')[0][-1], int(line.split('=')[1].strip()))
         for line in lines if line.startswith("fold")]
print(f"{dots=}")
print(f"{folds=}")


def oddify(x):
    return x + (x+1) % 2


grid = np.zeros(tuple(oddify(np.max(dots[:, axis])+1)
                      for axis in (0, 1)), dtype=int)
grid[dots[:, 0], dots[:, 1]] = 1
print(grid)
print(grid.shape)


def foldx(grid, offset):
    return grid[:offset] + np.flip(grid[offset+1:], axis=0)


def foldy(grid, offset):
    return np.transpose(foldx(np.transpose(grid), offset))


for (axis, offset) in folds[:1]:
    print("folding: ", axis, offset)
    op = foldx if axis == 'x' else foldy
    grid = op(grid, offset)

print(grid)
print(np.sum(grid > 0))
