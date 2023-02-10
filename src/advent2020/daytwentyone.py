import re


def both_parts(str_list):
    print()
    d = {}
    all_foods = []

    for i in str_list:
        sp = re.split("(?: \\(contains )|\\)", i.strip())
        entries = {x for x in re.split(" ", sp[0])}
        for j in sp[1].split(", "):

            if j in d:
                d[j] = set.intersection(d[j], entries)
            else:
                d[j] = entries
        for j in entries:
            all_foods.append(j)

    items = [x for x in d.items()]

    stop = len(items)
    bad_food = set()
    allergen = []

    while len(allergen) < stop:
        items = sorted(items, key=lambda x: len(x[1]), reverse=True)
        n = items.pop()
        food_entry = next(iter(n[1]))
        bad_food.add(food_entry)
        allergen.append((n[0], food_entry))
        items = [(k, v.difference(n[1])) for k, v in items]

    res = [x for x in all_foods if x not in bad_food]

    sa = ','.join([v for k, v in sorted(allergen, key=lambda x: x[0])])

    return len(res), sa


def part_two(str_list):
    print()
    return 0