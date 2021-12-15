import fileinput
import numpy as np
import heapq

DIRS = np.array([
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
])

grid = np.array([list(map(int, line.strip())) for line in fileinput.input()])
print(grid)
target = grid.shape - np.array([1, 1])


def neighbors(x, y):
    for dx, dy in DIRS:
        nx, ny = x + dx, y+dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            yield nx, ny


# [(priority, cost, x, y)]
q = [(0, 0, 0, 0)]
visited = set()
while len(q):
    p, cost, x, y = heapq.heappop(q)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    # print(x, y, p, cost)
    if np.all(np.array([x, y]) == target):
        print("arrived", x, y, cost)
        exit()
    for nx, ny in neighbors(x, y):
        distance = np.sum(np.abs(target - np.array([nx, ny])))
        cost_ = cost + grid[nx, ny]
        # print('n', nx, ny, distance, cost_)
        heapq.heappush(q, (cost_ + distance, cost_, nx, ny))
