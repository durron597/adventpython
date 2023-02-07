from pathlib import Path
from advent2020 import dayfourteen


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day14_input.txt'

    f = p.open('r')

    result = dayfourteen.part_one(f.readlines())

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day14_example.txt'

    f = p.open('r')

    result = dayfourteen.part_two(f.readlines())

    assert result == 208


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day14_input.txt'

    f = p.open('r')

    result = dayfourteen.part_two(f.readlines())

    print(result)
