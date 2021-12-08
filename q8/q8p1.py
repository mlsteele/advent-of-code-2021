import fileinput
import numpy as np

# n: segments
# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6
# unique: 1, 4, 7, 8

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
rows = [tuple(half.strip().split() for half in line.split('|'))
        for line in fileinput.input()]
mush = sum(sum(np.isin(np.vectorize(len)(np.array(row[1])), [2, 4, 3, 7]))
           for row in rows)
print(mush)
