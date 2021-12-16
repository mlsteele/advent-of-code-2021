import fileinput
from collections import deque
import math

HEX = {
    '0': "0000", '1': "0001", '2': "0010", '3': "0011",
    '4': "0100", '5': "0101", '6': "0110", '7': "0111",
    '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
    'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111",
}

OPS = {
    0: lambda xs: sum(xs),
    1: lambda xs: math.prod(xs),
    2: lambda xs: min(xs),
    3: lambda xs: max(xs),
    5: lambda xs: int(xs[0] > xs[1]),
    6: lambda xs: int(xs[0] < xs[1]),
    7: lambda xs: int(xs[0] == xs[1]),
}


def b2i(bin):
    """bin list [0, 1, 1] to int 3"""
    return int(''.join(map(str, bin)), 2)


def shift(stream, n):
    return [stream.popleft() for _ in range(n)]


def packet(stream):
    version = b2i(shift(stream, 3))
    type = b2i(shift(stream, 3))
    if type == 4:
        # literal
        value = 0
        while True:
            value <<= 4
            chunk = shift(stream, 5)
            value |= b2i(chunk[1:])
            if chunk[0] == 0:
                break
        return (version, type, value)
    # operator
    lti = shift(stream, 1)[0]
    if lti == 0:
        # next 15 bits are subpackets
        subpacket_len = b2i(shift(stream, 15))
        substream = deque(shift(stream, subpacket_len))
        subpackets = []
        while len(substream):
            subpackets.append(packet(substream))
        return (version, type, subpackets)
    else:
        subpacket_count = b2i(shift(stream, 11))
        return (version, type, [packet(stream) for _ in range(subpacket_count)])


def evaluate(ast):
    if ast[1] == 4:
        return ast[2]
    return OPS[ast[1]](list(map(evaluate, ast[2])))


inhex = next(fileinput.input()).strip()
stream = deque(map(int, ''.join([HEX[c] for c in inhex])))
print("input", ''.join(map(str, stream)))
ast = packet(stream)
print("remainder", ''.join(map(str, stream)))
print("ast", ast)
print("->", evaluate(ast))
