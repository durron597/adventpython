from pathlib import Path
from advent2020 import daysixteen


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day16_input.txt'

    f = p.open('r')

    result = daysixteen.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day16_input.txt'

    f = p.open('r')

    result = daysixteen.part_two(f.readlines())

    print(result)
