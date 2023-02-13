from pathlib import Path
from advent2020 import daythirteen


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day13_input.txt'

    f = p.open('r')

    result = daythirteen.part_one(f.readlines())

    print(result)
    print(result[0] * result[1])


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day13_example.txt'
    f = p.open('r')
    result = daythirteen.part_two(f.readlines())
    print(result)


def test_generate_congruences():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day13_example.txt'
    f = p.open('r')
    result = daythirteen.generate_congruences(f.readlines())
    assert set(result) == {(7, 0), (13, 12), (19, 12), (31, 25), (59, 55)}


def test_solve_diophantine_congruence_example():
    result = daythirteen.solve_diophantine(7, 5, 3)
    assert 7 * result[0] + 5 * result[1] == 3


def test_solve_diophantine_big_numbers():
    result = daythirteen.solve_diophantine(87, -64, 3)
    assert 87 * result[0] + -64 * result[1] == 3


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2020' / 'day13_input.txt'

    f = p.open('r')

    result = daythirteen.part_two(f.readlines())

    print(result)
