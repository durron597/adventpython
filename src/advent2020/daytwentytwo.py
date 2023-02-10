import re
from collections import deque
from typing import Deque, Tuple, List
import time


def part_one(str_list):
    print()
    a = build_decks(str_list)

    while a[0] and a[1]:
        left = a[0].popleft()
        right = a[1].popleft()
        if left > right:
            a[0].append(left)
            a[0].append(right)
        else:
            a[1].append(right)
            a[1].append(left)

    return score(next(filter(lambda x: x, a)))


def score(d):
    mult = 1
    total = 0

    while d:
        total += mult * d.pop()
        mult += 1

    return total


def build_decks(str_list):
    a = [deque(), deque()]
    index = 0
    for i in str_list:
        stripped = i.strip()
        m = re.fullmatch("Player (\\d):", stripped)
        if m:
            index = int(m[1]) - 1
        elif stripped:
            a[index].append(int(stripped))

    return a


def part_two(str_list):
    print()
    a = build_decks(str_list)

    total = 0.0
    start_time = time.perf_counter()
    _, res = play_game(a)
    end_time = time.perf_counter()
    total += (end_time - start_time)
    print(f"{total} seconds")

    return score(res)


def play_game(x: List[Deque[int]]) -> Tuple[int, Deque[int]]:
    a = [x[0].copy(), x[1].copy()]
    turn_timer = -1
    length = len(x[0]) + len(x[1])
    copy = set()
    while a[0] and a[1]:
        turn_timer += 1
        # Best effort attempt to not copy the whole array over and over unnecessarily
        # just play for a little while first. 4 was the best number over trying 0 to 9
        if turn_timer > length * 4:
            entry = tuple(a[0]), tuple(a[1])
            if entry in copy:
                return 0, a[0]
            else:
                copy.add(entry)
        left = a[0].popleft()
        right = a[1].popleft()
        if left <= len(a[0]) and right <= len(a[1]):
            copies = [a[0].copy(), a[1].copy()]
            while len(copies[0]) > left:
                copies[0].pop()
            while len(copies[1]) > right:
                copies[1].pop()
            win, _ = play_game(copies)
            if win == 0:
                a[0].append(left)
                a[0].append(right)
            else:
                a[1].append(right)
                a[1].append(left)
        elif left > right:
            a[0].append(left)
            a[0].append(right)
        else:
            a[1].append(right)
            a[1].append(left)

    if a[0]:
        return 0, a[0]
    return 1, a[1]
