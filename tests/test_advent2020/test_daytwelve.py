from pathlib import Path
from advent2020 import daytwelve


def test_turn():
    assert (0, 1) == daytwelve.turn((1, 0), 'R', 90)
    assert (0, -1) == daytwelve.turn((1, 0), 'L', 90)
    assert (-1, 0) == daytwelve.turn((1, 0), 'R', 180)
    assert (1, 0) == daytwelve.turn((0, 1), 'R', 270)
    assert (1, 0) == daytwelve.turn((0, -1), 'L', 270)


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day12_example.txt'

    f = p.open('r')

    result = daytwelve.part_one(f.readlines())

    assert result == 25


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day12_input.txt'

    f = p.open('r')

    result = daytwelve.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day12_example.txt'

    f = p.open('r')

    result = daytwelve.part_two(f.readlines())

    assert result == 286


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day12_input.txt'

    f = p.open('r')

    result = daytwelve.part_two(f.readlines())

    print(result)
