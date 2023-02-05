from pathlib import Path

from advent2020 import dayfive


def test_str_to_tup():
    res = dayfive.str_to_tup("FBBFBBFRLR")

    assert res == [54, 5]


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day5_input.txt'

    f = p.open('r')

    result = dayfive.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day5_input.txt'

    f = p.open('r')

    result = dayfive.part_two(f.readlines())

    print(result)

