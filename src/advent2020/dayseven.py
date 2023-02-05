import re
from collections import Counter


def extract(line):
    m = re.fullmatch("(.*) bags contain (?:(?:no other bags.\n)|([0-9].*bags?(?:, |.\n)))+", line)
    if m[2] is None:
        return {m[1]: {}}
    else:
        v = list(filter(None, re.split(" bags?(?:.\n|, )", m[2])))
        q = (re.fullmatch("([0-9]) (.*)", x) for x in v)
        return {m[1]: {x[2]: int(x[1]) for x in q}}


def part_one(str_list):
    r = {k: v for d in [extract(x) for x in str_list] for k, v in d.items()}
    r = {k: v if k != "shiny gold" else {"shiny gold": 1} for k, v in r.items()}
    r = {k: dict(filter(lambda x: x[0] == "shiny gold", v.items())) if "shiny gold" in v else v for k, v in r.items()}

    while True:
        newrecords = {}
        # Example: k = 'wavy bronze':, v = Counter({'bright turquoise': 5, 'pale orange': 4, 'pale black': 3})
        for k, v in r.items():
            entry = {}
            # Example: tk = 'bright turquoise', tv = 5
            for tk, tv in v.items():
                for rk, rv in r[tk].items():
                    entry.update({rk: rv * tv})
            newrecords.update({k: entry})
        if newrecords == r:
            r = newrecords
            break
        else:
            r = newrecords

    return {k: v for k, v in r.items() if v != {} and k != "shiny gold"}


def part_two(str_list):
    r = {k: v for d in [extract(x) for x in str_list] for k, v in d.items()}
    newrecords = Counter({"shiny gold": 1})
    count = 0

    while len(newrecords) > 0:
        popped = newrecords.popitem()
        count += popped[1] if popped[0] != "shiny gold" else 0
        for k, v in r[popped[0]].items():
            newrecords.update({k: v * popped[1]})

    return count
