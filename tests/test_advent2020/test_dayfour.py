from pathlib import Path

from advent2020 import dayfour


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day4_input.txt'

    f = p.open('r')

    result = dayfour.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day4_input.txt'

    f = p.open('r')

    result = dayfour.part_two(f.readlines())

    print(result)
