from collections import Counter


def part_one(low, high):
    a = range(1, 10)
    b = (''.join((str(u), str(v), str(w), str(x), str(y), str(z)))
         for u in a for v in a if v >= u for w in a if w >= v for x in a if x >= w
         for y in a if y >= x for z in a if z >= y)
    c = [x for x in b if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]]

    return [x for x in c if low <= int(x) <= high]


def part_two(low, high):
    res = part_one(low, high)

    return [x for x in res if not_bigger_group(x)]


def not_bigger_group(x):
    c = Counter()
    c.update(x)

    for _, v in c.items():
        if v == 2:
            return True

    return False
