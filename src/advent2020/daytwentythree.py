import numpy as np
from numpy import uint32


def part_one(nums):
    print()

    m = 100

    nums = play_game_v1(m, nums)

    return ''.join(str(x) for x in nums if x != 1)


def play_game_v1(m, nums):
    index = 0
    for i in range(m):
        if index + 4 >= len(nums):
            nums = np.concatenate((nums[index:], nums[:index]))
            index = 0
        val = nums[index] - 1
        if val == 0:
            val = 9
        left = nums[:index + 1]
        mid = nums[index + 1:index + 4]
        right = nums[index + 4:]
        while val in mid:
            val = val - 1
            if val == 0:
                val = m - 1
        if len(left) < len(right):
            first = find_first(left, val)
            if first != -1:
                nums = move_left(first, left, mid, right)
                index += 3
            else:
                first = find_first(right, val)
                nums = move_right(first, left, mid, right)
        else:
            first = find_first(right, val)
            if first != -1:
                nums = move_right(first, left, mid, right)
            else:
                first = find_first(left, val)
                nums = move_left(first, left, mid, right)
                index += 3

        index += 1
    index = find_first(nums, 1)
    nums = np.concatenate((nums[index:], nums[:index]))
    return nums


def move_right(first, left, mid, right):
    right_left = right[:first + 1]
    right_right = right[first + 1:]
    return np.concatenate((left, right_left, mid, right_right))


def move_left(first, left, mid, right):
    left_left = left[:first + 1]
    left_right = left[first + 1:]
    return np.concatenate((left_left, mid, left_right, right))


def find_first(vec, needle):
    for k, val in enumerate(vec):
        if val == needle:
            return k
    return -1


def play_game_v2(start, m, game):
    current = start

    removed_cups = np.zeros(3, dtype=uint32)

    for i in range(m):
        for j in range(3):
            removed_cups[j] = game[current]
            game[current] = game[removed_cups[j]]
        v = current

        while True:
            v -= 1
            if v < 0:
                v = len(game) - 1
            if v not in removed_cups:
                break

        for j in removed_cups:
            game[j] = game[v]
            game[v] = j
            v = j

        current = game[current]


def part_two(nums):
    print()

    p2 = True

    if p2:
        m = 10000000
        game = np.zeros(1000000, dtype=uint32)
    else:
        m = 100
        game = np.zeros(len(nums), dtype=uint32)

    for i in range(len(nums) - 1):
        game[nums[i] - 1] = nums[i + 1] - 1

    if p2:
        game[nums[len(nums) - 1] - 1] = len(nums)
        for i in range(len(nums), len(game) - 1):
            game[i] = i + 1

        game[-1] = nums[0] - 1
    else:
        game[nums[len(nums) - 1] - 1] = nums[0] - 1

    play_game_v2(nums[0] - 1, m, game)

    return game[0] + 1, game[game[0]] + 1, int(game[0] + 1) * int(game[game[0]] + 1)
