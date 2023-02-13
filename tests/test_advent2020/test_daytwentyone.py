from pathlib import Path
from advent2020 import daytwentyone


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day21_input.txt'

    f = p.open('r')

    result = daytwentyone.both_parts(f.readlines())

    print(result)
