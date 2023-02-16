import re
from collections import defaultdict, deque


def to_entry(row):
    sp = re.split(" => ", row)
    n, k = re.split(" ", sp[1])
    as_set = {(int(y[0]), y[1]) for y in [re.split(" ", x) for x in re.split(", ", sp[0])]}
    return k, (int(n), as_set)


def part_one(str_list):
    entries = [to_entry(x.strip()) for x in str_list]
    d = {k: v for k, v in entries}

    return extract_fuel(d, 1)


def extract_fuel(d, amt):
    curr = deque()
    curr.append(tuple([amt, 'FUEL']))
    leftover = defaultdict(int)
    ore = 0
    while curr:
        n = curr.popleft()
        amount_to_make = n[0] - leftover[n[1]]
        del leftover[n[1]]
        r = d[n[1]]
        q = int(((amount_to_make - 0.1) / r[0]) + 1)
        if q * r[0] > amount_to_make:
            leftover[n[1]] = (q * r[0]) - amount_to_make
        for x in r[1]:
            if x[1] == 'ORE':
                ore += q * x[0]
            else:
                curr.append(tuple([q * x[0], x[1]]))
    return ore


def part_two(str_list):
    entries = [to_entry(x.strip()) for x in str_list]
    d = {k: v for k, v in entries}

    amt_to_try = 1

    while True:
        baseline = extract_fuel(d, amt_to_try)
        new_amt = int((1_000_000_000_000 / baseline) * amt_to_try)
        if new_amt == amt_to_try:
            return amt_to_try + 1
        else:
            amt_to_try = new_amt
