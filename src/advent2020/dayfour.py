import re
from collections import Counter


def part_one(str_list):
    exp = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    count = 0
    er = Counter()
    for i in range(len(str_list)):
        if str_list[i].strip() == "":
            if exp <= er.keys():
                count += 1
            er = Counter()
        else:
            er.update(map(lambda x: re.split(":", x)[0], re.split(" ", str_list[i].strip())))

    if exp <= er.keys():
        count += 1

    return count


def part_two(str_list):
    exp = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    count = 0
    er = Counter()
    for i in range(len(str_list)):
        if str_list[i].strip() == "":
            if exp <= er.keys():
                count += 1
            er = Counter()
        else:
            er.update(map(lambda x: valid_keys(x), re.split(" ", str_list[i].strip())))

    if exp <= er.keys():
        count += 1

    return count


def hgt_method(x):
    match = re.fullmatch("((\\d{3})cm|(\\d{2})in)", x)

    if match is None:
        return False
    elif match[2] is None:
        return 59 <= int(match[3]) <= 76
    else:
        return 150 <= int(match[2]) <= 193


def valid_keys(typ):
    exp = {'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
           'pid': lambda x: re.fullmatch("[0-9]{9}", x) is not None,
           'eyr': lambda x: 2020 <= int(x) <= 2030,
           'byr': lambda x: 1920 <= int(x) <= 2002,
           'iyr': lambda x: 2010 <= int(x) <= 2020,
           'hcl': lambda x: re.fullmatch("#[0-9a-f]{6}", x) is not None,
           'hgt': lambda x: hgt_method(x)}
    spl = re.split(":", typ)
    return (spl[0] if exp[spl[0]](spl[1]) else None) if spl[0] in exp else None
