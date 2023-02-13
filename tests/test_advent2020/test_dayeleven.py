from pathlib import Path
from advent2020 import dayeleven
import numpy as np


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day11_example.txt'

    f = p.open('r')

    result = dayeleven.part_one(f.readlines())

    print(result)

    assert result == 37


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day11_input.txt'

    f = p.open('r')

    result = dayeleven.part_one(f.readlines())

    print(result)


def test_part_two_build_neighbors():
    inst = np.pad(np.array([[1, 1, 1], [0, 1, 0], [1, 1, 0]]), 1)

    result = dayeleven.build_neighbors(inst)

    # then
    expected = np.array([[set(), set(), set(), set(), set()],
                         [set(), {(3, 1), (1, 2), (2, 2)}, {(1, 1), (1, 3), (2, 2)}, {(1, 2), (2, 2)}, set()],
                         [set(), set(), {(1, 2), (3, 1), (1, 1), (3, 2), (1, 3)}, set(), set()],
                         [set(), {(1, 1), (3, 2), (2, 2)}, {(3, 1), (2, 2)}, set(), set()],
                         [set(), set(), set(), set(), set()]])
    assert (result == expected).all()


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day11_example.txt'

    f = p.open('r')

    result = dayeleven.part_two(f.readlines())

    assert result == 26


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day11_input.txt'

    f = p.open('r')

    result = dayeleven.part_two(f.readlines())

    print(result)
