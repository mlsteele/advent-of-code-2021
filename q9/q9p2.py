import fileinput
import numpy as np
from skimage.measure import label

field = np.array([list(map(int, line.strip()))
                 for line in fileinput.input()])
field = (field != np.max(field)).astype(int)
print(field)
labeled = label(field, connectivity=1)
print(labeled)
flat = labeled.flatten()
flat = flat[flat > 0]
basin_sizes = [len(flat[flat == name]) for name in np.unique(flat)]
print(np.product(np.sort(basin_sizes)[::-1][:3]))
