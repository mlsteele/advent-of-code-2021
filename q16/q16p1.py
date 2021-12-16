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
    if type == 4:
        # literal
        value = 0
        while True:
            value <<= 4
            chunk = shift(stream, 5)
            value |= b2i(chunk[1:])
            if chunk[0] == 0:
                break
        print("-> ", (version, type, value))
        return (version, type, value)
    # operator
    lti = shift(stream, 1)[0]
    print("op", type, lti)
    if lti == 0:
        # next 15 bits are subpackets
        subpacket_len = b2i(shift(stream, 15))
        print("subp len", subpacket_len)
        substream = deque(shift(stream, subpacket_len))
        subpackets = []
        while len(substream):
            subpackets.append(packet(substream))
        return (version, type, subpackets)
    else:
        subpacket_count = b2i(shift(stream, 11))
        return (version, type, [packet(stream) for _ in range(subpacket_count)])


def version_sum(ast):
    res = ast[0]
    if type(ast[2]) == list:
        for sub in ast[2]:
            res += version_sum(sub)
    return res


inhex = next(fileinput.input()).strip()
stream = deque(map(int, ''.join([HEX[c] for c in inhex])))
print(''.join(map(str, stream)))
ast = packet(stream)
print("remainder", ''.join(map(str, stream)))
print(ast)
print(version_sum(ast))
