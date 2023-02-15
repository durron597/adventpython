import numpy as np


def part_one(str_list):
    layers = make_layers(str_list)

    m = 2_000_000_000
    r = None

    for sl in layers:
        c = np.count_nonzero(sl == '0')
        if c < m:
            m = c
            r = sl

    return np.count_nonzero(r == '1') * np.count_nonzero(r == '2')


def make_layers(str_list):
    inp = str_list[0].strip()
    layers = []
    for i in range(len(inp) // 150):
        layers.append(np.array(list(inp[i * 150:i * 150 + 150])))
    return layers


def merge_cell(sl):
    for i in sl:
        if i == '1':
            return ' '
        if i == '0':
            return '#'

    return '?'


def part_two(str_list):
    layers = make_layers(str_list)

    stacked = np.stack((np.reshape(x, (6, 25)) for x in layers), 2)

    merged_array = [merge_cell(stacked[r, c, :]) for r, c in np.ndindex(6, 25)]
    to_numpy = np.array(merged_array)
    res = np.reshape(to_numpy, (6, 25))

    return res