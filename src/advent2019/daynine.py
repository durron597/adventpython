import re

from advent2019.intcode.IntCode import IntCode


def part_one(str_list):
    res = run_prog(str_list, 1)

    return res


def run_prog(str_list, v):
    res = None
    for q in str_list:
        inst = [int(x) for x in re.split(",", q)]

        a = IntCode(len(inst))
        res = a.process(inst, v)
        print(res)

    return res


def part_two(str_list):
    res = run_prog(str_list, 2)

    return res
