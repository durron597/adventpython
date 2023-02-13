from pathlib import Path

from advent2019 import dayone


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day1_input.txt'

    f = p.open('r')

    result = dayone.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day1_input.txt'

    f = p.open('r')

    result = dayone.part_two(f.readlines())

    print(result)
