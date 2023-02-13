from pathlib import Path

from advent2019 import daytwo


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day2_input.txt'

    f = p.open('r')

    result = daytwo.part_one(f.readlines(), {1: 12, 2: 2})

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day2_input.txt'

    f = p.open('r')

    result = daytwo.part_two(f.readlines(), 19690720)

    print(result)
