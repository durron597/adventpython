from pathlib import Path
from advent2020 import dayeighteen


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / 'day18_example.txt'

    f = p.open('r')

    result = dayeighteen.part_one(f.readlines())

    assert result == [71, 51, 26, 437, 12240, 13632]


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / 'day18_input.txt'

    f = p.open('r')

    result = dayeighteen.part_one(f.readlines())

    print(sum(result))


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / 'day18_example.txt'

    f = p.open('r')

    result = dayeighteen.part_two(f.readlines())

    assert result == [231, 51, 46, 1445, 669060, 23340]


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / 'day18_input.txt'

    f = p.open('r')

    result = dayeighteen.part_two(f.readlines())

    print(sum(result))
