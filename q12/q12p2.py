import fileinput
from collections import defaultdict

lines = [tuple(line.strip().split('-'))
         for line in fileinput.input()]
links = defaultdict(lambda: set())
[links[a].add(b) for (a, b) in lines]
[links[a].add(b) for (b, a) in lines]

# (path, banned, rush)
q = [(['start'], set(['start']), False)]
complete_paths = []
while len(q):
    path, banned, rush = q.pop()
    pivot = path[-1]
    if pivot == 'end':
        complete_paths.append(path)
        continue
    for reach in links[pivot]:
        if reach not in banned:
            if pivot.isupper():
                q.append((path + [reach], banned, rush))
            else:
                q.append((path + [reach], banned.union([pivot]), rush))
                if not rush:
                    q.append((path + [reach], banned, True))
complete_paths = set(map(tuple, complete_paths))
# [print(','.join(p)) for p in complete_paths]
print(len(complete_paths))
