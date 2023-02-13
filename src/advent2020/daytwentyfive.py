def part_one(nums):
    start = 1

    counter = 0
    while True:
        start *= 7
        start %= 20201227
        counter += 1
        if start == nums[0]:
            break

    start = 1
    for i in range(counter):
        start *= nums[1]
        start %= 20201227

    return start

