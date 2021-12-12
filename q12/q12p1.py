import fileinput
from collections import defaultdict

lines = [tuple(line.strip().split('-'))
         for line in fileinput.input()]
links = defaultdict(lambda: set())
[links[a].add(b) for (a, b) in lines]
[links[a].add(b) for (b, a) in lines]

# (path, banned)
q = [(['start'], set())]
complete_paths = []
while len(q):
    path, banned = q.pop()
    pivot = path[-1]
    if pivot == 'end':
        complete_paths.append(path)
        continue
    if not pivot.isupper():
        banned = banned.union([pivot])
    for reach in links[pivot]:
        if reach not in banned:
            q.append((path + [reach], banned))
print(len(complete_paths))
