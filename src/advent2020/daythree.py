import re
from collections import Counter

from util import maybe


def part_one(str_list):
    res = map(lambda x: re.split("-|:? ", x), str_list)
    count = 0
    for l, r, c, s in res:
        if int(l) <= (Counter(s)[c] or 0) <= int(r):
            count += 1

    return count


def part_two(str_list):
    res = map(lambda x: re.split("-|:? ", x), str_list)
    count = 0
    for l, r, c, s in res:
        lc = s[int(l)-1] or '_'
        rc = s[int(r)-1] or '_'
        if (lc == c and rc != c) or (lc != c and rc == c):
            count += 1

    return count
