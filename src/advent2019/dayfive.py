import re

from advent2019.intcode.IntCode import IntCode


def part_one(str_list, inp):
    inst = [int(x) for x in re.split(",", str_list[0])]
    ic = IntCode(len(inst))
    return ic.process(inst, inp)
