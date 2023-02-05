import re
from collections import Counter


def part_one(str_list):
    inst = [(idx, x[0], int(x[1])) for idx, x in enumerate(re.split(" ", x) for x in str_list)]

    return run_once(inst)[0]


def run_once(inst):
    c = Counter()
    idx = 0
    acc = 0
    while True:
        if idx == len(inst):
            return acc, None
        v = inst[idx]
        c[v[0]] += 1
        if c[v[0]] == 2:
            break
        match v[1]:
            case "acc":
                acc += v[2]
                idx += 1
            case "jmp":
                idx += v[2]
            case _:
                idx += 1
    return acc, idx


def part_two(str_list):
    inst = [(idx, x[0], int(x[1])) for idx, x in enumerate(re.split(" ", x) for x in str_list)]

    for i in range(len(inst)):
        curr = inst[i]
        if curr[1] == "acc":
            continue
        new_cmd = "nop" if curr[1] == "jmp" else "jmp"
        new_inst = [(curr[0], new_cmd, curr[2]) if x[0] == i else x for x in inst]
        res = run_once(new_inst)
        if res[1] is None:
            return res[0]

    return None
