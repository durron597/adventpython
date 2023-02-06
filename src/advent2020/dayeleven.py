import numpy as np


def part_one(str_list):
    conv = str.maketrans(".L#", "012")
    inst = np.pad(np.array([[int(y) for y in x.strip().translate(conv)] for x in str_list]), 1)
    while True:
        nxt = inst.copy()
        for r, c in np.ndindex(*inst.shape):
            if inst[r, c] == 0:
                continue
            n = inst[r - 1:r + 2, c - 1:c + 2]
            count = np.count_nonzero(n == 2)
            if inst[r, c] == 1:
                if count == 0:
                    nxt[r, c] = 2
            else:
                if count >= 5:
                    nxt[r, c] = 1
        if (nxt == inst).all():
            break
        inst = nxt

    count = np.count_nonzero(inst == 2)

    return count


def build_neighbors(inst):
    res = np.full(inst.shape, set())
    for r, c in np.ndindex(*inst.shape):
        if inst[r, c] == 0:
            continue
        res[r, c] = set()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                mult = 1
                while True:
                    nx = r + x * mult
                    ny = c + y * mult
                    if nx < 0 or ny < 0 or nx >= len(inst) or ny >= len(inst[0]):
                        break
                    if inst[nx, ny] > 0:
                        res[r, c].add((nx, ny))
                        break
                    mult += 1

    return res


def part_two(str_list):
    conv = str.maketrans(".L#", "012")
    inst = np.pad(np.array([[int(y) for y in x.strip().translate(conv)] for x in str_list]), 1)

    neighbors = build_neighbors(inst)

    while True:
        nxt = inst.copy()
        for r, c in np.ndindex(*inst.shape):
            if inst[r, c] == 0:
                continue
            count = sum([1 for x in neighbors[r, c] if inst[x] == 2])
            if inst[r, c] == 1:
                if count == 0:
                    nxt[r, c] = 2
            else:
                if count >= 5:
                    nxt[r, c] = 1
        if (nxt == inst).all():
            break
        inst = nxt

    count = np.count_nonzero(inst == 2)

    return count
