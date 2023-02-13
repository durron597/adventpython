from pathlib import Path

import numpy as np

from advent2020 import daytwentyfour


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day24_example.txt'

    f = p.open('r')

    result = daytwentyfour.part_one(f.readlines())

    assert np.count_nonzero(result) == 10


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day24_input.txt'

    f = p.open('r')

    result = daytwentyfour.part_one(f.readlines())

    print(np.count_nonzero(result))


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day24_example.txt'

    f = p.open('r')

    result = daytwentyfour.part_two(f.readlines())

    assert np.count_nonzero(result == 1) == 2208


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day24_input.txt'

    f = p.open('r')

    result = daytwentyfour.part_two(f.readlines())

    print(result)
