import fileinput
import numpy as np
from collections import defaultdict
import itertools


def print_image(image):
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    for (x, y) in image.keys():
        if image[(x, y)] > 0:
            xmin = min(x, xmin)
            xmax = max(x, xmax)
            ymin = min(y, ymin)
            ymax = max(y, ymax)
    for x in range(xmin, xmax+1):
        print(''.join('#' if image[(x, y)]
              else '.' for y in range(ymin, ymax+1)))


DIRS = np.array([
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
])


def neighbors(pos):
    pos = np.array(pos)
    return [tuple(pos + dir) for dir in DIRS]


def calc(pos, image, pattern):
    bits = [image[n] for n in neighbors(pos)]
    return pattern[b2i(bits)]


def step(image, pattern):
    bright = frozenset(pos for pos in image.keys() if image[pos] > 0)
    lit = union(*(neighbors(pos) for pos in bright))
    next = defaultdict(lambda: 0)  # (x,y) -> bool
    for pos in lit:
        next[pos] = calc(pos, image, pattern)
    return next


def union(*args):
    return frozenset(itertools.chain.from_iterable(args))


def b2i(bin):
    """bin list [0, 1, 1] to int 3"""
    return int(''.join(map(str, bin)), 2)


pattern, image_str = ''.join(fileinput.input()).split('\n\n')
pattern = pattern.replace('\n', '')
image_str = list(filter(None, image_str.split('\n')))
pattern = [int(x != '.') for x in pattern]
image = defaultdict(lambda: 0)  # (x,y) -> bool
for x, row in enumerate(image_str):
    for y, c in enumerate(row):
        image[(x, y)] = int(c != '.')
print_image(image)
for _ in range(2):
    image = step(image, pattern)
    print('-' * 10)
    print_image(image)
print(sum(image.values()))
