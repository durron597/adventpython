from pathlib import Path
from advent2020 import dayfifteen_v2


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day15_input.txt'

    f = p.open('r')

    result = dayfifteen_v2.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day15_input.txt'

    f = p.open('r')

    result = dayfifteen_v2.part_two(f.readlines())

    print(result)
