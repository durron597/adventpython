from pathlib import Path

from advent2019 import dayten


def test_can_see():
    p = {(0, 0), (3, 9), (2, 6), (1, 3), (3, 1), (6, 8), (9, 7)}
    
    assert dayten.can_see(p, (0, 0), (2, 6)) == False
    assert dayten.can_see(p, (0, 0), (3, 9)) == False
    assert dayten.can_see(p, (0, 0), (1, 3)) == True
    assert dayten.can_see(p, (0, 0), (3, 1)) == True
    assert dayten.can_see(p, (3, 9), (6, 8)) == True
    assert dayten.can_see(p, (3, 9), (9, 7)) == False


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_example.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    assert result[0] == (8, 5)
    assert len(result[1]) == 33


def test_part_one_example2():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_example2.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    assert result[0] == (2, 1)
    assert len(result[1]) == 35


def test_part_one_example3():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_example3.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    assert result[0] == (3, 6)
    assert len(result[1]) == 41


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_input.txt'

    f = p.open('r')

    result = dayten.part_one(f.readlines())

    print(result)
    print(len(result[1]))


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_example2.txt'

    f = p.open('r')

    result = dayten.part_two(f.readlines())

    assert result - 2 == 2


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day10_input.txt'

    f = p.open('r')

    result = dayten.part_two(f.readlines())

    print(result)
    pt = result[2][200 - (result[1] + 1)]
    print(pt[0] + result[0][0] + 100 * (pt[1] + result[0][1]))