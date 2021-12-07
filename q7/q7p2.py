import fileinput
import numpy as np


def tri(size):
    """triangular series: 0 1 3 6 10"""
    return np.add.accumulate(np.arange(size))


def focus(size, x):
    big = tri(size)
    return np.concatenate([np.flip(tri(x+1)[1:]), big[:size-x]])


positions = list(map(int, next(fileinput.input()).split(',')))
print(f"{positions=}")
crabs = np.zeros(max(positions)+1, dtype=int)
for x in positions:
    crabs[x] += 1
print(f"{crabs=}")
print(f"{crabs.shape=}")
width = crabs.shape[0]
triw = tri(width)
sled = np.concatenate([np.flip(triw)[:-1], triw])
# print(f"{sled=}")
# for x in range(crabs.shape[0]):
#     print(x, width-x-1, width*2-x, sled[width-x-1:len(sled)-x])
fuels = np.fromfunction(np.vectorize(lambda x: np.sum(
    sled[width-x-1:len(sled)-x]*crabs)), crabs.shape, dtype=int)
print(f"{fuels=}")
print(np.argmin(fuels))
print(min(fuels))
