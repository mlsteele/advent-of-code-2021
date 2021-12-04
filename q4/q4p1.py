import fileinput
import numpy as np


def shout(x, boards, bolds):
    bolds[np.where(boards == x)] = 1


def check_win(bolds):
    col_winners = np.argwhere(bolds.sum(axis=1) >= 5)[:, 0]
    row_winners = np.argwhere(bolds.sum(axis=2) >= 5)[:, 0]
    winners = np.concatenate((col_winners, row_winners))
    if len(winners) > 0:
        return winners[0]  # the board number


def score(which_board, boards, bolds):
    unmarked = boards[which_board][np.where(bolds[which_board] == 0)]
    return sum(unmarked)


lines = [line for line in fileinput.input()]
picks = list(map(int, lines[0].strip().split(',')))
print(f"{picks=}")
boards = np.array([list(map(int, line.strip().split()))
                   for line in lines[1:] if line.strip() != ""])
nboards = int(len(boards)/5)
boards = boards.reshape((nboards, 5, 5))
print(f"{boards=}")
bolds = np.zeros((nboards, 5, 5), dtype=int)
# print(f"{bolds=}")

for pick in picks:
    shout(pick, boards, bolds)
    winner = check_win(bolds)
    if winner != None:
        answer = pick * score(winner, boards, bolds)
        print(answer)
        break
