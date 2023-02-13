from pathlib import Path

from advent2020 import dayone


def test_day_one_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day1_input.txt'

    f = p.open('r')

    result = dayone.day_one_part_one(f.readlines())

    print(result)


def test_day_one_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day1_input.txt'

    f = p.open('r')

    result = dayone.day_one_part_two(f.readlines())

    print(result)
