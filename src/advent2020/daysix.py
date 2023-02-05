from collections import Counter


def part_one(str_list):
    count = 0
    er = Counter()
    for i in range(len(str_list)):
        if str_list[i].strip() == "":
            count += len(er.keys())
            er = Counter()
        else:
            er.update(str_list[i].strip())

    count += len(er.keys())

    return count


def part_two(str_list):
    c = 0
    qc = 0
    er = Counter()
    for i in range(len(str_list)):
        if str_list[i].strip() == "":
            c += sum(1 for _, val in er.items() if qc == val)
            qc = 0
            er = Counter()
        else:
            er.update(str_list[i].strip())
            qc += 1

    c += sum(1 for _, val in er.items() if qc == val)

    return c
