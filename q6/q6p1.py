import fileinput
import numpy as np
CYCLE = 6
START = 8
DAYS = 80

counters_flat = list(map(int, fileinput.input()[0].split(',')))
pop = np.array([[i, 0] for i in range(START+1)])
print(f"{counters_flat=}")
for c in counters_flat:
    pop[c, 1] += 1
print(f"{pop=}")
for _ in range(DAYS):
    spawn = pop[0, 1]
    pop[0, 1] = 0
    pop[:, 1] = np.roll(pop[:, 1], -1)
    pop[CYCLE, 1] += spawn
    pop[START, 1] += spawn
    print(f"{pop=}")
fish = sum(pop[:, 1])
print(f"{fish=}")
