import fileinput
import numpy as np
from scipy.signal import convolve2d
from functools import reduce
import itertools


def step(grid):
    grid = grid + 1  # energy increase
    flashed = np.zeros(grid.shape, dtype=int)
    while True:
        flashing = (grid > 9).astype(int)
        flashing *= 1 - flashed
        flashed += flashing
        if np.sum(flashing) == 0:
            break
        kernel = np.full((3, 3), 1)
        grid += convolve2d(flashing, kernel, mode='same')
    grid[flashed > 0] = 0
    return grid, np.sum(flashed)


def main():
    grid = np.array([list(map(int, line.strip()))
                    for line in fileinput.input()])
    for i in itertools.count():
        grid, nflashed_ = step(grid)
        if nflashed_ >= np.product(grid.shape):
            return i+1


print(main())
