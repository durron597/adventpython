import numpy as np

from advent2020 import daytwentythree


def test_part_one_example():
    result = daytwentythree.part_one(np.array([int(x) for x in "389125467"]))

    assert result == "67384529"


def test_part_one():
    result = daytwentythree.part_one(np.array([int(x) for x in "137826495"]))

    print(result)


def test_part_two_example():
    result = daytwentythree.part_two(np.array([int(x) for x in "389125467"]))

    print(f"first: {result[0]}, second: {result[1]}, answer: {result[2]}")


def test_part_two():
    test_part_two_example()
    result = daytwentythree.part_two(np.array([int(x) for x in "137826495"]))

    print(f"first: {result[0]}, second: {result[1]}, answer: {result[2]}")
