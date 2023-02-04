import re
from collections import Counter

from util import maybe


def part_one(str_list):
    count = 0
    for i in range(len(str_list)):
        index = (i * 3) % (len(str_list[0]) - 1)
        count += 1 if str_list[i][index] == '#' else 0

    return count


def part_two(str_list):
    total = 1
    for j in range(1, 10, 2):
        count = 0
        for i in range(0, len(str_list), 2 if j == 9 else 1):
            index = int(i * (0.5 if j == 9 else j)) % (len(str_list[0]) - 1)
            count += 1 if str_list[i][index] == '#' else 0
        total = total * count

    return total
