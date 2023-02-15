from pathlib import Path

from advent2019 import dayfive


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day5_input.txt'

    f = p.open('r')

    result = dayfive.part_one(f.readlines(), 1)

    print(result)


def test_part_five():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day5_input.txt'

    f = p.open('r')

    result = dayfive.part_one(f.readlines(), 5)

    print(result)
