from pathlib import Path
from advent2020 import daytwentytwo


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day22_example.txt'

    f = p.open('r')

    result = daytwentytwo.part_one(f.readlines())

    assert result == 306


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day22_input.txt'

    f = p.open('r')

    result = daytwentytwo.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day22_example.txt'

    f = p.open('r')

    result = daytwentytwo.part_two(f.readlines())

    assert result == 291


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day22_input.txt'

    f = p.open('r')

    result = daytwentytwo.part_two(f.readlines())

    print(result)
