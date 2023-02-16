from pathlib import Path

from advent2019 import dayfourteen


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day14_input.txt'

    f = p.open('r')

    result = dayfourteen.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day14_input.txt'

    f = p.open('r')

    result = dayfourteen.part_two(f.readlines())

    print(result)