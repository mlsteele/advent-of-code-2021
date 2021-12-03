import fileinput
import numpy as np
import itertools
from functools import reduce
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN


def whittle(xs, common):
    for place in range(xs.shape[1]):
        commbit = Decimal(sum(xs[:, place]) / xs.shape[0]
                          ).quantize(1, rounding=ROUND_HALF_UP)
        commbit = commbit if common else 1 - commbit
        # print(place, commbit, xs[:, place])
        xs = xs[xs[:, place] == commbit]
        # print(xs)
        if xs.shape[0] == 1:
            return xs[0]
    raise RuntimeError("unexpected")


entries = [list(map(int, line.strip())) for line in fileinput.input()]
entries = np.array(entries)
oxy = (whittle(entries, True))
co2 = (whittle(entries, False))
print(oxy, co2)
(oxy, co2) = (int(''.join(map(str, x)), base=2) for x in (oxy, co2))
print(oxy, co2)
print(oxy*co2)
