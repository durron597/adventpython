def part_one(str_list):
    res_list = [y[0] * 8 + y[1] for y in [str_to_tup(x) for x in str_list]]
    return max(res_list)


def str_to_tup(seat):
    cmap = {'F': "0", 'B': "1", 'L': "0", 'R': "1"}
    return [int(y, 2) for x in [seat[0:7], seat[7:10]] for y in ["".join(cmap[e] for e in x)]]


def part_two(str_list):
    pairs = sorted([str_to_tup(x)[0] * 8 + str_to_tup(x)[1] for x in str_list])
    for i in range(len(pairs) - 1):
        if pairs[i+1] - pairs[i] > 1:
            return pairs[i] + 1
