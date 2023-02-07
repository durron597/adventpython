import re


def part_one(str_list):
    num = int(str_list[0])
    bus = ((int(x), int(x) - (num % int(x))) for x in re.split(",", str_list[1].strip()) if x != "x")

    return min(bus, key=lambda x: x[1])


def part_two(str_list):
    bus = list(generate_congruences(str_list))
    # bus = [(int(x), idx % int(x)) for idx, x in enumerate(re.split(",", str_list[1].strip())) if x != "x"]
    bus.sort(reverse=True)

    curr = None
    for i in bus:
        if curr is None:
            curr = i
            continue
        new_mod = (curr[0] * i[0])
        dio = solve_diophantine(curr[0], i[0], (i[1] - curr[1]) % i[0])[0] % i[0]
        new_diff = (curr[0] * dio + curr[1])
        curr = (new_mod, new_diff)

    last = bus[len(bus) - 1]

    final_remainder = (last[1] - curr[1]) % last[0]

    poop = final_remainder * curr[0] + curr[1]

    return poop


def generate_congruences(str_list):
    return ((int(x), (int(x) - idx) % int(x)) for idx, x in enumerate(re.split(",", str_list[1].strip())) if x != "x")



# we are solving:
# 7j == 3 (mod 5)
# The solution is 7*4 + 5*-5 = 3
# 2j == 3 (mod 5)
# 2j + 5k = 3
# 5k = 3 (mod 2)
# k = 1 (mod 2)


# 7 = (1 * 5) + 2
# 5 = (2 * 2) + 1
# 2 = (2 * 1) + 0
# THEN
# 1 = 5 - (2 * 2)
#


def solve_diophantine(a, b, c):
    gcd, x, y = gcd_extended(a, b)
    cx = c*x
    cy = c*y

    return cx, cy


def gcd_extended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y
