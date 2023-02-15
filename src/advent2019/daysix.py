import re
from collections import defaultdict


def traverse(d, c, node):
    total = 0
    for i in d[node]:
        total += 1 + traverse(d, c, i)

    c[node] = total

    return total


def part_one(str_list):
    d = build_tree(str_list)

    c = {}
    traverse(d, c, "COM")

    return sum(v for _, v in c.items())


def build_tree(str_list):
    d = defaultdict(set)
    for i in str_list:
        sp = re.split("\\)", i.strip())
        d[sp[0]].add(sp[1])
    return d


def part_two(str_list):
    d = {i: k for k, v in build_tree(str_list).items() for i in v}

    dist = {}

    you = "YOU"
    san = "SAN"
    
    you_count = 0
    san_count = 0

    while True:
        if you in d:
            you = d[you]
            you_count += 1
            if you in dist:
                return you_count + dist[you]
            else:
                dist[you] = you_count

        if san in d:
            san = d[san]
            san_count += 1
            if san in dist:
                return san_count + dist[san]
            else:
                dist[san] = san_count

