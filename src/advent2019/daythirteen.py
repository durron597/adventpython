import re
from collections import defaultdict

import numpy as np

from advent2019.intcode.IntCode import IntCode


def part_one(str_list):
    a, res = run_prog(str_list)

    print()

    pixels = defaultdict(int)
    _, _, _ = draw_game(res, pixels)

    return sum(1 for _, v in pixels.items() if v == 2)


def draw_game(res, pixels, actually_draw=True):
    shaped = np.array(res).reshape(-1, 3)

    as_dict_update = {(x, y): i for x, y, i in shaped}
    pixels.update(as_dict_update)

    if actually_draw:
        print(f"score: {pixels[(-1, 0)]}")
        print()

        ball = None
        paddle = None

        y = 0
        while True:
            x = 0
            if (x, y) not in pixels:
                break
            while True:
                if (x, y) not in pixels:
                    break
                match pixels[(x, y)]:
                    case 1:
                        ch = '#'
                    case 2:
                        ch = '*'
                    case 3:
                        ch = '-'
                        paddle = (x, y)
                    case 4:
                        ch = '.'
                        ball = (x, y)
                    case _:
                        ch = ' '
                print(ch, end="")
                x += 1
            print()
            y += 1

        return paddle, ball, pixels[(-1, 0)]
    else:
        new_out = defaultdict(tuple)
        new_out.update({i: (x, y) for x, y, i in shaped if i == 3 or i == 4})
        return new_out[3], new_out[4], pixels[(-1, 0)]


def run_prog(str_list, quarters=None):
    inst = [int(x) for x in re.split(",", str_list[0].strip())]
    if quarters:
        inst[0] = quarters

    a = IntCode(len(inst))
    next_out = a.process(inst)

    return a, next_out


def part_two(str_list):
    a, res = run_prog(str_list, 2)

    pixels = defaultdict(int)
    paddle, ball, score = draw_game(res, pixels, actually_draw=False)

    nxt = 0

    while a.get_stop_command() != 99:
        a.reset_output()
        res = a.resume(nxt)
        new_paddle, new_ball, score = draw_game(res, pixels, actually_draw=False)
        if new_paddle:
            paddle = new_paddle
        if new_ball:
            ball = new_ball
        if paddle[0] < ball[0]:
            nxt = 1
        elif paddle[0] > ball[0]:
            nxt = -1
        else:
            nxt = 0

    return score
