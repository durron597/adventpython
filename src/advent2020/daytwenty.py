import re
from enum import IntEnum

import numpy as np
from collections import defaultdict, deque

from numpy import uint16


class Orient(IntEnum):
    U = 0
    L = 1
    D = 2
    R = 3
    FU = 4
    FL = 5
    FD = 6
    FR = 7

    def invert(self):
        match self:
            case Orient.U:
                return Orient.U
            case Orient.R:
                return Orient.L
            case Orient.D:
                return Orient.D
            case Orient.L:
                return Orient.R
            case Orient.FU:
                return Orient.FU
            case Orient.FR:
                return Orient.FR
            case Orient.FD:
                return Orient.FD
            case _:
                return Orient.FL


def part_one(str_list):
    tiles, tiles_by_shape, _ = compute_tiles_by_edge(str_list)

    corner_ids = compute_corner_ids(tiles_by_shape)

    return np.prod(np.array([x[0] for x in corner_ids], dtype=object))


def compute_corner_ids(tiles_by_shape):
    res = defaultdict(list)
    for v, k in [x for x in tiles_by_shape.items() if len(x[1]) == 1]:
        res[list(k.items())[0][0]].append(v)
    corner_ids = [x for x in res.items() if len(x[1]) == 4]
    return corner_ids


def compute_tiles_by_edge(str_list):
    trans = str.maketrans(".#", "01")
    tiles = {}
    for tile_count in range((len(str_list) + 1) // 12):
        tid = int(re.findall("\\d+", str_list[tile_count * 12])[0])
        arr = np.array([[j for j in str.translate(i.strip(), trans)]
                        for i in str_list[tile_count * 12 + 1:tile_count * 12 + 11]])
        tiles[tid] = arr
    tiles_by_shape = defaultdict(dict)
    res = defaultdict(dict)
    for tid, tile in tiles.items():
        record_edges(tid, tile, tiles_by_shape, res)
    return tiles, tiles_by_shape, res


def record_edges(tid, tile, tiles_by_shape, res):
    for o in Orient:
        trans = transform_tile(tile, o)
        register_edge(trans[0, :], tid, tiles_by_shape, res, o)


def register_edge(sl, tid, tiles_by_shape, res, orient: Orient):
    s = ''.join(e for e in sl)
    tiles_by_shape[int(s, 2)][tid] = orient
    res[tid][orient.invert()] = int(s, 2)


def adjust_stored_tile(tiles, tiles_by_shape, res, i, first_trans: Orient, second_trans: Orient):
    tile = tiles[i]
    tile = transform_tile(tile, first_trans)
    tile = transform_tile(tile, second_trans)
    tiles[i] = tile

    record_edges(i, tile, tiles_by_shape, res)


def transform_tile(tile, trans: Orient):
    if trans > 3:
        tile = np.fliplr(tile)
        trans -= 4
    for i in range(trans):
        tile = np.rot90(tile)

    return tile


def part_two(str_list):
    print()

    tiles, finished = join_tiles(str_list)

    vertical_concat = [np.concatenate([tiles[x][1:-1, 1:-1] for x in finished[:, y]]) for y in range(len(finished))]
    full_concat = np.concatenate(vertical_concat, axis=1)

    sea_m = sea_monster_array()

    count = 0
    for o in Orient:
        trans = transform_tile(full_concat, o)
        count = 0
        for r, c in np.ndindex(*trans.shape):
            if r + sea_m.shape[0] >= trans.shape[0] or c + sea_m.shape[1] >= trans.shape[1]:
                continue
            sl = trans[r:r+sea_m.shape[0], c:c+sea_m.shape[1]]
            found_it = True
            for i, j in np.ndindex(*sl.shape):
                if sea_m[i, j] == ' ':
                    continue
                elif sl[i, j] == '0':
                    found_it = False
                    break
            if found_it:
                count += 1
        if count > 0:
            break

    total = np.count_nonzero(full_concat == '1')

    return total - count * 15


def join_tiles(str_list):
    tiles, tiles_by_edge, res = compute_tiles_by_edge(str_list)
    corner_ids = compute_corner_ids(tiles_by_edge)
    start = corner_ids[0][0]
    finished = np.zeros((12, 12), dtype=uint16)
    adjust_stored_tile(tiles, tiles_by_edge, res, start, Orient.L, Orient.U)
    finished[11, 11] = start
    d = deque()
    d.appendleft((11, 11))
    while d:
        n = d.pop()
        cell = finished[*n]
        # left
        if n[1] - 1 >= 0 and finished[n[0], n[1] - 1] == 0:
            edge = res[cell][Orient.L]
            neighbor_tile = next(filter(lambda x: x[0] != cell, tiles_by_edge[edge].items()))
            adjust_stored_tile(tiles, tiles_by_edge, res, neighbor_tile[0], neighbor_tile[1], Orient.FR)
            finished[n[0], n[1] - 1] = neighbor_tile[0]
            d.appendleft((n[0], n[1] - 1))
        # top
        if n[0] - 1 >= 0 and finished[n[0] - 1, n[1]] == 0:
            edge = res[cell][Orient.U]
            neighbor_tile = next(filter(lambda x: x[0] != cell, tiles_by_edge[edge].items()))
            adjust_stored_tile(tiles, tiles_by_edge, res, neighbor_tile[0], neighbor_tile[1], Orient.FD)
            finished[n[0] - 1, n[1]] = neighbor_tile[0]
            d.appendleft((n[0] - 1, n[1]))
    return tiles, finished


def sea_monster_array():
    a = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

    return np.array([[str(y) for y in x] for x in a])


def render_tile(tile):
    fmt = {"all": lambda x: "#" if x == "1" else "."}
    with np.printoptions(formatter=fmt, threshold=np.inf, linewidth=np.inf):
        print(tile)
        return f"{tile}"
