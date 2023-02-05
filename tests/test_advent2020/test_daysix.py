from pathlib import Path

from advent2020 import daysix


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day6_input.txt'

    f = p.open('r')

    result = daysix.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day6_example.txt'

    f = p.open('r')

    result = daysix.part_two(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day6_input.txt'

    f = p.open('r')

    result = daysix.part_two(f.readlines())

    print(result)

