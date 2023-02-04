def day_one_part_one(str_list):
    int_list = [int(i) for i in str_list]
    sub_list = set([2020 - i for i in int_list]).intersection(int_list)

    for x in sub_list:
        return x * (2020 - x)

    return 0


def day_one_part_two(str_list):
    int_list = [int(i) for i in str_list]

    cross = ((x, y, z) for x in int_list for y in int_list if y > x and y + x < 2020
             for z in int_list if z > y and x + y + z == 2020)
    result = [k1*k2*k3 for (k1, k2, k3) in cross]

    return result
