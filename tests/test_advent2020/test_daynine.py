from pathlib import Path

from advent2020 import daynine


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / 'day9_example.txt'

    f = p.open('r')

    result = daynine.part_one(5, f.readlines())

    assert result == 127


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day9_input.txt'

    f = p.open('r')

    result = daynine.part_one(25, f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day9_example.txt'

    f = p.open('r')

    result = daynine.part_two(5, f.readlines())

    assert result == (15, 47)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day9_input.txt'

    f = p.open('r')

    result = daynine.part_two(25, f.readlines())

    print(result)
    print(result[0] + result[1])
