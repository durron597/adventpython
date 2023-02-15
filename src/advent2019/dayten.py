import math
from collections import defaultdict
from typing import Tuple

import numpy as np
from numpy import arctan


def can_see(p, left, right):
    rd = abs(left[0] - right[0])
    rsgn = -1 if left[0] < right[0] else 1
    cd = abs(left[1] - right[1])
    csgn = -1 if left[1] < right[1] else 1
    gcd = math.gcd(rd, cd)
    rdr = rsgn * rd // gcd
    cdr = csgn * cd // gcd

    for i in range(1, gcd):
        if (right[0] + i * rdr, right[1] + i * cdr) in p:
            return False

    return True


def part_one(str_list):
    arr = np.array([[x for x in y.strip()] for y in str_list])
    s: set[Tuple[int, int]] = set()
    for r, c in np.ndindex(*arr.shape):
        if arr[r, c] == '#':
            s.add((r, c))

    p = [(x, y) for x in s for y in s if x[0] < y[0] or (x[0] == y[0] and x[1] < y[1])]
    d = defaultdict(set)

    for q in p:
        if can_see(s, *q):
            d[q[0]].add(q[1])
            d[q[1]].add(q[0])

    return max(d.items(), key=lambda x: len(x[1]))


def part_two(str_list):
    res = part_one(str_list)

    d = [(x[0] - res[0][0], x[1] - res[0][1]) for x in res[1]]
    dn = [x for x in d if x[1] < 0]
    dn.sort(key=lambda x: arctan(x[0]/x[1]))
    return res[0], len(d) - len(dn), dn
