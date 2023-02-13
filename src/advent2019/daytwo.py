import re

from advent2019.intcode.IntCode import IntCode


def part_one(str_list, override):
    inst = [int(x) for x in re.split(",", str_list[0])]
    ic = IntCode(len(inst))
    for o in override.items():
        inst[o[0]] = o[1]
    return ic.process(inst)


def part_two(str_list, target):
    inst = [int(x) for x in re.split(",", str_list[0])]

    ic = IntCode(len(inst))
    for x in range(100):
        for y in range(100):
            inst[1] = x
            inst[2] = y
            res = ic.process(inst)
            if res == target:
                return x * 100 + y
    return -1
