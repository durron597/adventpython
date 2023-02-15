import math
import re
from collections import defaultdict

import numpy as np


def part_one(str_list, steps):
    start = np.array([tuple([int(y) for y in re.findall("-?\\d+", x)]) for x in str_list])
    curr = start

    old_v = np.zeros_like(curr)

    for i in range(steps):
        v = np.array([np.array([np.array([sgn(x, y, 0), sgn(x, y, 1), sgn(x, y, 2)]) for x in curr if x is not y])\
                      for y in curr]).sum(axis=1)
        old_v = np.add(old_v, v)
        curr = np.add(old_v, curr)

    v2 = np.absolute(old_v).sum(axis=1)
    d2 = np.absolute(curr).sum(axis=1)
    return np.multiply(v2, d2).sum()


def sgn(x, y, d):
    return 1 if x[d] - y[d] > 0 else 0 if x[d] == y[d] else -1


def part_two(str_list):
    start = np.array([tuple([int(y) for y in re.findall("-?\\d+", x)]) for x in str_list], dtype=object)
    curr = start

    old_v = np.zeros_like(curr)

    seen = defaultdict(set)

    steps = 0

    while True:
        nothing_new = False
        for i in range(3):
            state = (tuple(curr[:, i]), tuple(old_v[:, i]))
            if state not in seen[i]:
                nothing_new = True
                seen[i].add(state)
        if not nothing_new:
            break
        steps += 1
        v = np.array([np.array([np.array([sgn(x, y, 0), sgn(x, y, 1), sgn(x, y, 2)], dtype=object)
                                for x in curr if x is not y], dtype=object) for y in curr], dtype=object).sum(axis=1)
        old_v = np.add(old_v, v)
        curr = np.add(old_v, curr)

    return math.lcm(*(len(v) for k, v in seen.items()))
