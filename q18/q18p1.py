import fileinput
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
import functools


def add(a, b): return [a, b]


def add_explode(x, n, right=False):
    if n == None:
        return x
    if type(x) == int:
        return x + n
    if right:
        return [x[0], add_explode(x[1], n, right)]
    else:
        return [add_explode(x[0], n, right), x[1]]


def reduce_(x, level):
    """Do one step of reduction.
    returns (value, changed, send_left, send_right)"""
    if type(x) != list:
        if x >= 10:
            return ([int(Decimal(x/2).quantize(1, rounding=ROUND_HALF_DOWN)),
                    int(Decimal(x/2).quantize(1, rounding=ROUND_HALF_UP))], True, None, None)
        return (x, False, None, None)
    if level == 4:
        return (0, True, x[0], x[1])  # explode
    a, changed, send_left, send_right = reduce_(x[0], level+1)
    if changed:
        return ([a, add_explode(x[1], send_right, False)], True, send_left, None)
    b, changed, send_left, send_right = reduce_(x[1], level+1)
    return ([add_explode(a, send_left, True), b], changed, None, send_right)


def reduce(x):
    while True:
        x, changed, _, _ = reduce_(x, 0)
        if not changed:
            return x


inputs = [eval(line) for line in fileinput.input()]
# print(inputs)
sum = reduce(functools.reduce(lambda acc, x: reduce(add(acc, x)), inputs))
print(sum)
