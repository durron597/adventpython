import re
from enum import Enum

import numpy as np
from numpy import int16, int32


class DirEnum(Enum):
    D = (1, 0)
    U = (-1, 0)
    L = (0, -1)
    R = (0, 1)


def bounds(grid, rc):
    return 0 <= rc[0] < grid.shape[0] and 0 <= rc[1] < grid.shape[1]


def part_one(str_list):
    inst_first = [(x[0], int(''.join(x[1:]))) for x in re.split(",", str_list[0].strip())]
    inst_second = [(x[0], int(''.join(x[1:]))) for x in re.split(",", str_list[1].strip())]

    grid = np.ones((4001, 4001), dtype=int16)

    rc_first = [2000, 2000]
    rc_second = [2000, 2000]
    dist = 2_000_000_000

    for n in range(max(len(inst_first), len(inst_second))):
        if n < len(inst_first):
            d_first, v_first = inst_first[n]
            delta = DirEnum[d_first]
            for i in range(v_first):
                rc_first = [rc_first[0] + delta.value[0], rc_first[1] + delta.value[1]]
                if bounds(grid, rc_first):
                    if grid[*rc_first] % 3 == 0:
                        new_dist = abs(rc_first[0] - (grid.shape[0] // 2)) + abs(rc_first[1] - (grid.shape[1] // 2))
                        if new_dist < dist:
                            dist = new_dist
                    elif grid[*rc_first] % 2 == 1:
                        grid[*rc_first] *= 2
        if n < len(inst_second):
            d_second, v_second = inst_second[n]
            delta = DirEnum[d_second]
            for i in range(v_second):
                rc_second = [rc_second[0] + delta.value[0], rc_second[1] + delta.value[1]]
                if bounds(grid, rc_second):
                    if grid[*rc_second] % 2 == 0:
                        new_dist = abs(rc_second[0] - (grid.shape[0] // 2)) + abs(rc_second[1] - (grid.shape[1] // 2))
                        if new_dist < dist:
                            dist = new_dist
                    elif grid[*rc_second] % 3 == 1:
                        grid[*rc_second] *= 3

    return dist


def part_two(str_list):
    inst_first = [(x[0], int(''.join(x[1:]))) for x in re.split(",", str_list[0].strip())]
    inst_second = [(x[0], int(''.join(x[1:]))) for x in re.split(",", str_list[1].strip())]

    grid = np.zeros((4001, 4001), dtype=int32)

    rc = [2000, 2000]
    dist = 2_000_000_000
    stp_cnt = 0

    for d, v in inst_first:
        delta = DirEnum[d]
        for i in range(v):
            stp_cnt += 1
            rc = [rc[0] + delta.value[0], rc[1] + delta.value[1]]
            if bounds(grid, rc) and grid[*rc] == 0:
                grid[*rc] = stp_cnt

    stp_cnt = 0
    rc = [2000, 2000]

    for d, v in inst_second:
        delta = DirEnum[d]
        for i in range(v):
            stp_cnt += 1
            rc = [rc[0] + delta.value[0], rc[1] + delta.value[1]]
            if bounds(grid, rc) and grid[*rc] > 0 and rc != [2000, 2000]:
                dist = min(dist, grid[*rc] + stp_cnt)

    return dist
