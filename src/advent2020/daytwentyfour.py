import numpy as np
from numpy import int16


def part_one(str_list):
    reference = max((len(x) for x in str_list))

    grid = np.zeros(((reference * 3) + 1, (reference * 3) + 1), dtype=int16)

    for i in str_list:
        mode = None
        x = reference
        y = reference
        for j in i.strip():
            if j == 'n' or j == 's':
                mode = j
            else:
                if mode is None:
                    x_d = 2
                else:
                    x_d = 1
                    if mode == 'n':
                        y -= 1
                    else:
                        y += 1
                if j == 'e':
                    x += x_d
                else:
                    x -= x_d
                mode = None

        grid[x, y] = 1 - grid[x, y]

    return grid


def part_two(str_list):
    grid = part_one(str_list)

    grid = strip_edges(grid)
    grid = np.pad(grid, 100)

    for x, y in np.ndindex(*grid.shape):
        if (x + y) % 2 == 0:
            grid[x, y] = -1

    for i in range(100):
        nxt = grid.copy()
        for x, y in np.ndindex(*grid.shape):
            if grid[x, y] == -1:
                continue
            if (x < 2) or (y < 2) or x >= grid.shape[0] - 2 or y >= grid.shape[1] - 2:
                continue
            count = grid[x - 2, y] + grid[x + 2, y] + \
                grid[x - 1, y - 1] + grid[x - 1, y + 1] + \
                grid[x + 1, y - 1] + grid[x + 1, y + 1]
            if grid[x, y] > 0:
                if count == 0 or count > 2:
                    nxt[x, y] = 0
                else:
                    nxt[x, y] = 1
            elif count == 2:
                nxt[x, y] = 1

        grid = nxt
        print(f"{i}: {np.count_nonzero(grid == 1)}")

    return grid


def strip_edges(nxt):
    while True:
        if np.count_nonzero(nxt[0, :]) == 0:
            nxt = nxt[1:, :]
            continue
        if np.count_nonzero(nxt[:, 0]) == 0:
            nxt = nxt[:, 1:]
            continue
        if np.count_nonzero(nxt[-1, :]) == 0:
            nxt = nxt[:-1, :]
            continue
        if np.count_nonzero(nxt[:, -1]) == 0:
            nxt = nxt[:, :-1]
            continue
        break
    return nxt
