import re

from advent2020 import dayfour
from pathlib import Path


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


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day4_example.txt'

    f = p.open('r')

    result = dayfour.part_two(f.readlines())

    print(result)
