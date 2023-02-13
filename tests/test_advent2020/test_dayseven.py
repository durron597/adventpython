from collections import Counter
from pathlib import Path

from advent2020 import dayseven


def test_extract_one_type():
    res = dayseven.extract("striped indigo bags contain 4 posh aqua bags.\n")
    assert res == {"striped indigo": Counter({"posh aqua": 4})}


def test_extract_multiple_types():
    res = dayseven.extract("pale magenta bags contain 4 striped black bags, 3 shiny orange bags, 1 vibrant teal bag, "
                           "5 plaid olive bags.\n")
    assert res == {"pale magenta": Counter({"striped black": 4, "shiny orange": 3,
                                            "vibrant teal": 1, "plaid olive": 5})}


def test_extract_none():
    res = dayseven.extract("bright fuchsia bags contain no other bags.\n")
    assert res == {"bright fuchsia": Counter()}


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day7_input.txt'

    f = p.open('r')

    result = dayseven.part_one(f.readlines())

    print(len(result))


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day7_input.txt'

    f = p.open('r')

    result = dayseven.part_two(f.readlines())

    print(result)
