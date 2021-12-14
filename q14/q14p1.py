import fileinput
from functools import reduce
from collections import defaultdict
import numpy as np


def step(poly, rules):
    inter = reduce(lambda acc, x:
                   acc + [rules[''.join(x)]],
                   zip(poly, poly[1:]), [])
    return ''.join(''.join(pair)
                   for pair in zip(poly, inter)) + poly[-1]


fi = fileinput.input()
poly = next(fi).strip()
rules = {x: y for (x, y) in [tuple(line.strip().split(" -> "))
         for line in fi if len(line) > 1]}
rules = defaultdict(lambda: '', rules)
print(rules)
print(poly)

for _ in range(10):
    poly = step(poly, rules)
    print(poly)

counts = sorted(np.unique(np.array(list(poly)), return_counts=True)[1])
print(counts[-1] - counts[0])
