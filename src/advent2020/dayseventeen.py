import numpy as np


def part_one(str_list, cycles):
    conv = str.maketrans(".#", "01")
    inst = np.array([[[int(y) for y in x.strip().translate(conv)] for x in str_list]])

    for i in range(cycles):
        inst = np.pad(inst, 2)
        nxt = inst.copy()
        for r, c, z in np.ndindex(*inst.shape):
            n = inst[r - 1:r + 2, c - 1:c + 2, z - 1:z + 2]
            if n.shape != (3, 3, 3):
                continue
            count = np.count_nonzero(n == 1)
            if inst[r, c, z] == 1:
                if count != 3 and count != 4:
                    nxt[r, c, z] = 0
            else:
                if count == 3:
                    nxt[r, c, z] = 1
        while True:
            if np.count_nonzero(nxt[0, :, :]) == 0:
                nxt = nxt[1:, :, :]
                continue
            if np.count_nonzero(nxt[:, 0, :]) == 0:
                nxt = nxt[:, 1:, :]
                continue
            if np.count_nonzero(nxt[:, :, 0]) == 0:
                nxt = nxt[:, :, 1:]
                continue
            if np.count_nonzero(nxt[-1, :, :]) == 0:
                nxt = nxt[:-1, :, :]
                continue
            if np.count_nonzero(nxt[:, -1, :]) == 0:
                nxt = nxt[:, :-1, :]
                continue
            if np.count_nonzero(nxt[:, :, -1]) == 0:
                nxt = nxt[:, :, :-1]
                continue
            break
        inst = nxt

    return inst


def part_two(str_list, cycles):
    conv = str.maketrans(".#", "01")
    inst = np.array([[[[int(y) for y in x.strip().translate(conv)]] for x in str_list]])

    for i in range(cycles):
        inst = np.pad(inst, 2)
        nxt = inst.copy()
        for r, c, z, w in np.ndindex(*inst.shape):
            n = inst[r - 1:r + 2, c - 1:c + 2, z - 1:z + 2, w - 1: w + 2]
            if n.shape != (3, 3, 3, 3):
                continue
            count = np.count_nonzero(n == 1)
            if inst[r, c, z, w] == 1:
                if count != 3 and count != 4:
                    nxt[r, c, z, w] = 0
            else:
                if count == 3:
                    nxt[r, c, z, w] = 1
        while True:
            if np.count_nonzero(nxt[0, :, :, :]) == 0:
                nxt = nxt[1:, :, :, :]
                continue
            if np.count_nonzero(nxt[:, 0, :, :]) == 0:
                nxt = nxt[:, 1:, :, :]
                continue
            if np.count_nonzero(nxt[:, :, 0, :]) == 0:
                nxt = nxt[:, :, 1:, :]
                continue
            if np.count_nonzero(nxt[:, :, :, 0]) == 0:
                nxt = nxt[:, :, :, 1:]
                continue
            if np.count_nonzero(nxt[-1, :, :, :]) == 0:
                nxt = nxt[:-1, :, :, :]
                continue
            if np.count_nonzero(nxt[:, -1, :, :]) == 0:
                nxt = nxt[:, :-1, :, :]
                continue
            if np.count_nonzero(nxt[:, :, -1, :]) == 0:
                nxt = nxt[:, :, :-1, :]
                continue
            if np.count_nonzero(nxt[:, :, :, -1]) == 0:
                nxt = nxt[:, :, :, :-1]
                continue
            break
        inst = nxt

    return inst
