from pathlib import Path

from advent2019 import dayseven


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day7_input.txt'

    f = p.open('r')

    result = dayseven.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day7_example.txt'

    f = p.open('r')

    result = dayseven.part_two(f.readlines())

    print(result)


def test_part_two_example2():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day7_example2.txt'

    f = p.open('r')

    result = dayseven.part_two(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day7_input.txt'

    f = p.open('r')

    result = dayseven.part_two(f.readlines())

    print(result)
