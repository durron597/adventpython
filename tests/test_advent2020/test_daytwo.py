from pathlib import Path

from advent2020 import daytwo


def test_day_two_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day2_input.txt'

    f = p.open('r')

    result = daytwo.part_one(f.readlines())

    print(result)


def test_day_two_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day2_input.txt'

    f = p.open('r')

    result = daytwo.part_two(f.readlines())

    print(result)


