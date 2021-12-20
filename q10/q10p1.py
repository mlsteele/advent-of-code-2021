import fileinput
PAIRS = {'(': ')', '{': '}', '[': ']', '<': '>', }
START = set(PAIRS.keys())
END = set(PAIRS.values())
POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0, }


def scan(line):
    stack = []
    for x in line:
        if x in START:
            stack.append(x)
        else:
            y = stack.pop()
            if PAIRS[y] != x:
                return x


lines = [list(line.strip()) for line in fileinput.input()]
print(sum([POINTS[scan(line)] for line in lines]))
