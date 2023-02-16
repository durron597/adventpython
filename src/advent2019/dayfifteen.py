import re
import heapq
from collections import defaultdict

from advent2019.intcode.IntCode import IntCode
from util.DirEnum import DirEnum


def part_one(str_list):
    grid, target = map_grid(str_list)

    res = dijkstra(grid, (0, 0), target)

    draw_game(grid, res[0], res[2])

    print()

    return res[1][res[0]]


def map_grid(str_list):
    left = play_maze(str_list, 0)
    right = play_maze(str_list, 1)
    left.update(right)

    target = [k for k, v in left.items() if v > 2][0]

    return left, target


def dijkstra(vertices, start, target=None):
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[start] = 0

    q = []

    heapq.heappush(q, (dist[start], start))

    while q:
        u = heapq.heappop(q)
        n = u[1]

        if u[0] != dist[n]:
            continue

        for i in DirEnum:
            v = (n[0] + i.value[0], n[1] + i.value[1])
            if vertices[v] > 1:
                alt = dist[n] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = n
                    heapq.heappush(q, (dist[v], v))
            if v == target:
                return v, dist, prev

    return None, dist, prev


def play_maze(str_list, turn):
    a = run_prog(str_list)
    print()
    pixels = defaultdict(int)
    r, c = 0, 0
    curr_dir = DirEnum.L
    d = {DirEnum.U: 1, DirEnum.D: 2, DirEnum.L: 3, DirEnum.R: 4}
    done = False
    while not done:
        order = generate_order(curr_dir, turn)
        for i in order:
            res = a.resume(d[i])
            match res[-1]:
                case 1:
                    r += i.value[0]
                    c += i.value[1]
                    pixels[(r, c)] = 2
                    curr_dir = i.turn(turn)
                    break
                case 0:
                    pixels[(r + i.value[0], c + i.value[1])] = 1
                case _:
                    r += i.value[0]
                    c += i.value[1]
                    pixels[(r, c)] = res[-1] + 1
                    done = True
    return pixels


def generate_order(d: DirEnum, turn):
    return [d, d.turn(1 - turn), d.turn(turn).turn(turn), d.turn(turn)]


def draw_game(pixels, target, prev=None):
    print()

    path = set()

    if prev:
        curr = target
        while curr != (0, 0):
            path.add(curr)
            curr = prev[curr]

    minr = min(pixels.items(), key=lambda x: x[0][0])[0][0]
    minc = min(pixels.items(), key=lambda x: x[0][1])[0][1]
    maxr = max(pixels.items(), key=lambda x: x[0][0])[0][0]
    maxc = max(pixels.items(), key=lambda x: x[0][1])[0][1]

    for y in range(minr, maxr + 1):
        for x in range(minc, maxc + 1):
            if (x == 0) and (y == 0):
                ch = '!'
            elif (x, y) in path:
                ch = '*'
            else:
                match pixels[(x, y)]:
                    case 0:
                        ch = ' '
                    case 1:
                        ch = '#'
                    case 2:
                        ch = '_'
                    case _:
                        ch = '&'
            print(ch, end="")
        print()


def run_prog(str_list):
    inst = [int(x) for x in re.split(",", str_list[0].strip())]

    a = IntCode(len(inst))
    _ = a.process(inst)

    return a


def part_two(str_list):
    grid, target = map_grid(str_list)

    res = dijkstra(grid, target)

    draw_game(grid, res[0])

    print()

    return max(res[1].items(), key=lambda x: x[1])
