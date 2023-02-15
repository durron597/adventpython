from pathlib import Path

from advent2019 import daysix


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day6_example.txt'

    f = p.open('r')

    result = daysix.part_one(f.readlines())

    assert result == 42


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day6_input.txt'

    f = p.open('r')

    result = daysix.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day6_example2.txt'

    f = p.open('r')

    result = daysix.part_two(f.readlines())

    assert result - 2 == 2


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day6_input.txt'

    f = p.open('r')

    result = daysix.part_two(f.readlines())

    print(result - 2)
