import fileinput
from functools import reduce
from collections import defaultdict
import numpy as np


def step(prev, rules):
    next = defaultdict(int)
    for key, freq in prev.items():
        b = rules[key]
        a, c = key[0], key[1]
        next[a + b] += freq
        next[b + c] += freq
    return next


fi = fileinput.input()
poly = next(fi).strip()
rules = {x: y for (x, y) in [tuple(line.strip().split(" -> "))
         for line in fi if len(line) > 1]}
rules = defaultdict(str, rules)
print(rules)
print(poly)
participants = defaultdict(int)
for (a, b) in zip(poly, poly[1:]):
    participants[a + b] += 1
print(participants)

for i in range(40):
    print('step', i, len(participants), participants)
    participants = step(participants, rules)

singles = defaultdict(int)
for key, freq in participants.items():
    singles[key[0]] += freq
singles[poly[-1]] += 1

print(singles)
counts = sorted(singles.values())
print(counts[-1] - counts[0])
