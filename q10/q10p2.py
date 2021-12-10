import fileinput
from functools import reduce
PAIRS = {'(': ')', '{': '}', '[': ']', '<': '>', }
START = set(PAIRS.keys())
END = set(PAIRS.values())
POINTS = {')': 1, ']': 2, '}': 3, '>': 4, }


def scan(line):
    stack = []
    for x in line:
        if x in START:
            stack.append(x)
        else:
            y = stack.pop()
            if PAIRS[y] != x:
                return None
    return ''.join([PAIRS[open] for open in stack[::-1]])


def score(closers):
    if closers == None:
        return 0
    return reduce(lambda acc, x: acc*5+POINTS[x], closers, 0)


lines = [list(line.strip()) for line in fileinput.input()]
scores = [score(scan(line)) for line in lines]
scores = sorted([score for score in scores if score > 0])
print(scores[len(scores)//2])
