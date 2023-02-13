from pathlib import Path
from advent2020 import daynineteen


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day19_example.txt'

    f = p.open('r')

    result = daynineteen.part_one(f.readlines())

    print(result)


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day19_input.txt'

    f = p.open('r')

    result = daynineteen.part_one(f.readlines())

    print(result)


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day19_input.txt'

    f = p.open('r')

    result = daynineteen.part_two(f.readlines())

    print(result)
