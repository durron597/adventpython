from advent2020 import daythree
from pathlib import Path


def test_day_three_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day3_input.txt'

    f = p.open('r')

    result = daythree.part_one(f.readlines())

    print(result)


def test_day_three_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / 'day3_example.txt'

    f = p.open('r')

    result = daythree.part_one(f.readlines())

    print(result)


def test_day_three_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day3_input.txt'

    f = p.open('r')

    result = daythree.part_two(f.readlines())

    print(result)


def test_day_three_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day3_example.txt'

    f = p.open('r')

    result = daythree.part_two(f.readlines())

    print(result)