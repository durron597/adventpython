from pathlib import Path

from advent2020 import dayeight


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day8_example.txt'

    f = p.open('r')

    result = dayeight.part_one(f.readlines())

    assert result == 5


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day8_input.txt'

    f = p.open('r')

    result = dayeight.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day8_example2.txt'

    f = p.open('r')

    result = dayeight.part_two(f.readlines())

    assert result == 8


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day8_input.txt'

    f = p.open('r')

    result = dayeight.part_two(f.readlines())

    print(result)
