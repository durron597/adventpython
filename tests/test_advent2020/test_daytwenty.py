from pathlib import Path
from advent2020 import daytwenty


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day20_example.txt'

    f = p.open('r')

    result = daytwenty.part_one(f.readlines())

    print(result)


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day20_input.txt'

    f = p.open('r')

    result = daytwenty.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day20_input.txt'

    f = p.open('r')

    result = daytwenty.part_two(f.readlines())

    print(result)
