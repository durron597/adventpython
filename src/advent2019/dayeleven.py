import re
from collections import defaultdict

from advent2019.intcode.IntCode import IntCode
from util.DirEnum import DirEnum


def part_one(str_list):
    res = run_prog(str_list)

    return len(res.items())


def run_prog(str_list, start_white=False):
    inst = [int(x) for x in re.split(",", str_list[0].strip())]

    a = IntCode(len(inst))
    next_out = a.process(inst)

    r, c = (0, 0)
    d = DirEnum.U

    white = defaultdict(list)
    if start_white:
        white[(r, c)].append(1)
    last_out = []

    while a.get_stop_command() != 99:
        if next_out != last_out:
            new_out = next_out[-2:]
            white[(r, c)].append(new_out[0])
            d = d.turn(new_out[1])
            last_out = next_out.copy()
            r += d.value[0]
            c += d.value[1]
        next_value = white[(r, c)][-1] if white[(r, c)] else 0
        next_out = a.resume(next_value)

    return white


def part_two(str_list):
    res = run_prog(str_list, True)

    minr = min(res.items(), key=lambda x: x[0][0])[0][0]
    minc = min(res.items(), key=lambda x: x[0][1])[0][1]
    maxr = max(res.items(), key=lambda x: x[0][0])[0][0]
    maxc = max(res.items(), key=lambda x: x[0][1])[0][1]

    print()

    for r in range(minr, maxr + 1):
        for c in range(minc, maxc + 1):
            p = res[(r, c)]
            v = res[(r, c)][-1] if res[(r, c)] else 0
            if v == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
