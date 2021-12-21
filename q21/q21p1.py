import fileinput
import numpy as np
from itertools import cycle, count, islice

pos = np.array([int(line.split(':')[1].strip())
                for line in filter(None, fileinput.input())])
scores = np.zeros(pos.shape, dtype=int)
die = cycle(range(1, 101))
rolls = 0
for p in cycle((0, 1)):
    pos[p] += sum(islice(die, 0, 3))
    rolls += 3
    pos = (pos - 1) % 10 + 1
    scores[p] += pos[p]
    print(pos, scores)
    if np.any(scores >= 1000):
        print("complete")
        print('rolls', rolls)
        print(np.min(scores)*rolls)
        exit()
