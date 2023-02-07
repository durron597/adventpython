import re

import numpy


def part_one(str_list):
    return [play_game(i.strip(), 2020) for i in str_list]


# Use a Numpy array instead of a two element dict. the index of the repeated element is always last turn
# So we only need to store one number.
def play_game(start_str, stop):
    seed = [int(x) for x in re.split(",", start_str)]
    history = numpy.zeros(stop, dtype=int)
    last = 0

    for i in range(stop):
        if i < len(seed):
            n = seed[i]
        else:
            # we said it before
            if last == 0 or history[last] > 0 or last == seed[0]:
                n = i - 1 - history[last]
            else:
                n = 0
        history[last] = i - 1
        last = n

    return last


def part_two(str_list):
    ret = []
    for i in str_list:
        result = play_game(i.strip(), 30000000)
        print(result)
        ret.append(result)

    return ret
