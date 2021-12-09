import fileinput
import numpy as np

field = np.array([list(map(int, line.strip()))
                 for line in fileinput.input()])
print(field)
lots = np.max(field) * 100 // 10
shifted_right = np.c_[np.full(field.shape[0], lots), field[:, :-1]]
shifted_left = np.c_[field[:, 1:], np.full(field.shape[0], lots)]
shifted_down = np.r_[np.full((1, field.shape[1]), lots), field[:-1]]
shifted_up = np.r_[field[1:, :], np.full((1, field.shape[1]), lots)]
shifteds = [shifted_right, shifted_left, shifted_down, shifted_up]
minimums = np.all(field < shifteds, axis=0)
print(np.sum(field[minimums] + 1))
