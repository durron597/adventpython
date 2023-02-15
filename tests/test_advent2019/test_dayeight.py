from pathlib import Path

import numpy as np

from advent2019 import dayeight


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day8_input.txt'

    f = p.open('r')

    result = dayeight.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day8_input.txt'

    f = p.open('r')

    result = dayeight.part_two(f.readlines())

    fmt = {"all": lambda x: x}
    print()
    with np.printoptions(formatter=fmt, threshold=np.inf, linewidth=np.inf):
        print(result)
