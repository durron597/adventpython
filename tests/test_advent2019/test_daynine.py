from pathlib import Path

from advent2019 import daynine


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day9_example.txt'

    f = p.open('r')

    result = daynine.part_one(f.readlines())

    print(result)


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day9_input.txt'

    f = p.open('r')

    result = daynine.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day9_input.txt'

    f = p.open('r')

    result = daynine.part_two(f.readlines())

    print(result)
