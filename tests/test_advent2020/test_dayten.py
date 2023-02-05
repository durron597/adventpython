from pathlib import Path

from advent2020 import dayten


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / 'day10_example.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    print(result)

    assert result == (22, 10)


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day10_input.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day10_example.txt'

    f = p.open('r')

    result = dayten.part_two(f.readlines())

    assert result == 19208


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day10_input.txt'

    f = p.open('r')

    result = dayten.part_two(f.readlines())

    print(result)
