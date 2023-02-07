import re
from collections import deque


def part_one(str_list):
    return [play_game(i.strip(), 2020) for i in str_list]


def say(history, turn, value_to_say):
    old_val = history.get(value_to_say, deque([], 2))
    old_val.append(turn)
    history.update({value_to_say: old_val})

    return value_to_say


def play_game(start_str, stop):
    seed = [int(x) for x in re.split(",", start_str)]
    history = {}
    last = -1

    for i in range(stop):
        if i < len(seed):
            last = say(history, i, seed[i])
        else:
            q = history[last]
            v = q.popleft()
            if q:
                v2 = q.popleft()
                q.append(v)
                q.append(v2)
                last = say(history, i, v2 - v)
            else:
                q.append(v)
                last = say(history, i, 0)
        print("i: {}, n: {}".format(i, last))

    return last


def part_two(str_list):
    ret = []
    for i in str_list:
        result = play_game(i.strip(), 30000000)
        print(result)
        ret.append(result)

    return ret
