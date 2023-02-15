from pathlib import Path

from advent2019 import daytwelve


def test_part_one_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_example.txt'

    f = p.open('r')

    result = daytwelve.part_one(f.readlines(), 10)

    assert result == 179


def test_part_one_example2():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_example2.txt'

    f = p.open('r')

    result = daytwelve.part_one(f.readlines(), 100)

    assert result == 1940


def test_part_one():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_input.txt'

    f = p.open('r')

    result = daytwelve.part_one(f.readlines(), 1000)

    print(result)


def test_part_two_example():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_example.txt'

    f = p.open('r')

    result = daytwelve.part_two(f.readlines())

    assert result == 2772


def test_part_two_example2():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_example2.txt'

    f = p.open('r')

    result = daytwelve.part_two(f.readlines())

    assert result == 4686774924


def test_part_two():
    p = Path(__file__).parents[2] / 'resources' / '2019' / 'day12_input.txt'

    f = p.open('r')

    result = daytwelve.part_two(f.readlines())

    print(result)