import re
from collections import deque


def part_one(str_list):
    zero_mask = -1
    one_mask = 0
    zero_conv = str.maketrans("X", "1")
    one_conv = str.maketrans("X", "0")

    memory = {}

    for i in str_list:
        res = re.split(" = ", i)
        if res[0] == "mask":
            zero_mask = -1 & int(str.translate(res[1], zero_conv), 2)
            one_mask = 0 | int(str.translate(res[1], one_conv), 2)
        else:
            addr = int(re.split("\\[", res[0])[1].rstrip(']'))
            value = (int(res[1]) & zero_mask) | one_mask
            memory.update({addr: value})

    return sum((v for _, v in memory.items()))


def part_two(str_list):
    memory = {}
    mask = "000000000000000000000000000000000000"

    for i in str_list:
        res = re.split(" = ", i)
        if res[0] == "mask":
            mask = res[1].strip()
        else:
            baseAddr = int(re.split("\\[", res[0])[1].rstrip(']'))
            q1 = deque()
            q1.append(baseAddr)
            q2 = deque()
            for j in range(len(mask)):
                if mask[j] == '0':
                    continue
                while q1:
                    if mask[j] == '1':
                        q2.append(q1.popleft() | (1 << 35 - j))
                    else:
                        n = q1.popleft()
                        q2.append(n & ((1 << 35 - j) ^ -1))
                        q2.append(n | (1 << 35 - j))
                q1 = q2
                q2 = deque()

            while q1:
                number = int(res[1])
                memory.update({q1.popleft(): number})

    return sum((v for _, v in memory.items()))
