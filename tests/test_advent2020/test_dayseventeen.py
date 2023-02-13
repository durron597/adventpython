from pathlib import Path
from advent2020 import dayseventeen
import numpy as np


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day17_example.txt'

    f = p.open('r')

    result = dayseventeen.part_one(f.readlines(), 6)

    assert np.count_nonzero(result) == 112


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day17_input.txt'

    f = p.open('r')

    result = dayseventeen.part_one(f.readlines(), 6)

    print(np.count_nonzero(result))


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day17_example.txt'

    f = p.open('r')

    result = dayseventeen.part_two(f.readlines(), 6)

    assert np.count_nonzero(result) == 848


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day17_input.txt'

    f = p.open('r')

    result = dayseventeen.part_two(f.readlines(), 6)

    print(np.count_nonzero(result))
