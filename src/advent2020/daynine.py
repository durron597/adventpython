from itertools import combinations


def part_one(slide, str_list):
    inst = [int(x) for x in str_list]

    for i in range(len(inst) - slide):
        prev = inst[i:i+slide]
        com = {sum(x) for x in combinations(prev, 2)}
        if inst[i + slide] not in com:
            return i + slide, inst[i + slide]

    return None, None


def part_two(slide, str_list):
    inst = [int(x) for x in str_list]
    res = part_one(slide, str_list)

    for i in range(res[0], 0, -1):
        j = 0
        while True:
            j += 1
            s = sum(inst[i-j:i])
            if s == res[1]:
                return min(inst[i-j:i]), max(inst[i-j:i])
            if s > res[1]:
                break

    return None
