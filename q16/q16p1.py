import fileinput
from collections import deque

HEX = {
    '0': "0000", '1': "0001", '2': "0010", '3': "0011",
    '4': "0100", '5': "0101", '6': "0110", '7': "0111",
    '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
    'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111",
}


def b2i(bin):
    """bin list [0, 1, 1] to int 3"""
    return int(''.join(map(str, bin)), 2)


def shift(stream, n):
    return [stream.popleft() for _ in range(n)]


def packet(stream):
    version = b2i(shift(stream, 3))
    type = b2i(shift(stream, 3))
    if type != 4:
        print("unrecognized packet type", type)
        exit()
    if type == 4:
        # literal
        value = 0
        while True:
            value <<= 4
            chunk = shift(stream, 5)
            print('chunk', chunk)
            value |= b2i(chunk[1:])
            if chunk[0] == 0:
                break
        return (version, type, value)
    return (version, type)


inhex = next(fileinput.input()).strip()
stream = deque(map(int, ''.join([HEX[c] for c in inhex])))
print(''.join(map(str, stream)))
print(packet(stream))
print(''.join(map(str, stream)))
