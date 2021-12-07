import fileinput
import numpy as np


def tri(size): return np.fromfunction(
    np.vectorize(lambda x: np.sum(np.arange(x+1))), (size,), dtype=int)


def focus(size, x):
    return np.concatenate([np.flip(tri(x+1)[1:]), tri(size-x)])


positions = list(map(int, fileinput.input()[0].split(',')))
print(f"{positions=}")
crabs = np.zeros(max(positions)+1, dtype=int)
for x in positions:
    crabs[x] += 1
print(f"{crabs=}")
print(f"{crabs.shape=}")
fuels = np.fromfunction(np.vectorize(lambda x: np.sum(
    focus(crabs.shape[0], x)*crabs)), crabs.shape, dtype=int)
print(f"{fuels=}")
print(np.argmin(fuels))
print(min(fuels))
