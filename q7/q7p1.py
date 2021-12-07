import fileinput
import numpy as np

positions = list(map(int, fileinput.input()[0].split(',')))
print(f"{positions=}")
crabs = np.zeros(max(positions)+1, dtype=int)
for x in positions:
    crabs[x] += 1
print(f"{crabs=}")
print(f"{crabs.shape=}")
fuels = np.fromfunction(np.vectorize(lambda x: np.sum(
    np.abs(np.arange(-x, crabs.shape[0]-x))*crabs)), crabs.shape, dtype=int)
print(f"{fuels=}")
print(np.argmin(fuels))
print(min(fuels))
