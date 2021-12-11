import fileinput
import numpy as np
from scipy.signal import convolve2d
from functools import reduce


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


grid = np.array([list(map(int, line.strip())) for line in fileinput.input()])
nflashed = 0
for _ in range(100):
    grid, nflashed_ = step(grid)
    nflashed += nflashed_
print(nflashed)
