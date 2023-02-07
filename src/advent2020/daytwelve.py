

def part_one(str_list):
    x, y = (0, 0)
    d = (1, 0)  # east

    for i in str_list:
        inst = i[0]
        num = int(i[1:])
        match inst:
            case 'N': y += - num
            case 'S': y += + num
            case 'W': x += - num
            case 'E': x += + num
            case 'F':
                x += d[0] * num
                y += d[1] * num
            case _:
                d = turn(d, inst, num)

    return abs(x) + abs(y)


def turn(curr, lr, deg):
    if lr == 'L':
        count = (360 - deg) / 90
    else:
        count = deg / 90

    ret = curr

    for i in range(int(count)):
        ret = (-ret[1], ret[0])

    return ret


def part_two(str_list):
    x, y = (0, 0)
    d = (10, -1)  # east

    for i in str_list:
        inst = i[0]
        num = int(i[1:])
        match inst:
            case 'N': d = (d[0], d[1]-num)
            case 'S': d = (d[0], d[1]+num)
            case 'W': d = (d[0]-num, d[1])
            case 'E': d = (d[0]+num, d[1])
            case 'F':
                x += d[0] * num
                y += d[1] * num
            case _:
                d = turn(d, inst, num)

    return abs(x) + abs(y)
