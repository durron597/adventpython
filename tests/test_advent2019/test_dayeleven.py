from pathlib import Path

from advent2019 import dayeleven


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day11_example.txt'

    f = p.open('r')

    result = dayeleven.part_one(f.readlines())

    print(result)


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day11_input.txt'

    f = p.open('r')

    result = dayeleven.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day11_input.txt'

    f = p.open('r')

    result = dayeleven.part_two(f.readlines())

    print(result)
