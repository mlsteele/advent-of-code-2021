import fileinput
import numpy as np

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

segments = np.array([
    # [a b c d e f g]
    [1, 1, 1, 0, 1, 1, 1],  # 0: -d
    [0, 0, 1, 0, 0, 1, 0],  # 1: cf
    [1, 0, 1, 1, 1, 0, 1],  # 2: -bf
    [1, 0, 1, 1, 0, 1, 1],  # 3: -be
    [0, 1, 1, 1, 0, 1, 0],  # 4: -aeg
    [1, 1, 0, 1, 0, 1, 1],  # 5: -ce
    [1, 1, 0, 1, 1, 1, 1],  # 6: -c
    [1, 0, 1, 0, 0, 1, 0],  # 7: acf
    [1, 1, 1, 1, 1, 1, 1],  # 8: all
    [1, 1, 1, 1, 0, 1, 1],  # 9: -e
])

print(f"{segments=}")
brightness = np.sum(segments, axis=1)
print(f"{brightness=}")
unique = sorted([brightness.tolist().index(b)
                 for b in np.nonzero(np.bincount(brightness) == 1)[0]])
print(f"{unique=}")

code = np.ones((7, 7))
print(code)

# # acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# rows = [tuple(half.strip().split() for half in line.split('|'))
#         for line in fileinput.input()]
# mush = sum(sum(np.isin(np.vectorize(len)(np.array(row[1])), [2, 4, 3, 7]))
#            for row in rows)
# print(mush)
