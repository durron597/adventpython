import re


def reduce_once(d, done, is_part_two):
    new_d = {}
    for i, j in d.items():
        if done.get(i, False):
            new_d.update({i: j})
            continue
        curr_done = True
        new_set = set()
        for t in j:  # iterating through the tuples
            new_elems = [[]]
            for x in t:  # iterating through the elements of tuples
                if isinstance(x, str) or ((x == 8 or x == 0 or x == 11) and is_part_two):
                    new_elems, merge_done = merge_tuples(new_elems, {(x, )})
                else:
                    new_elems, merge_done = merge_tuples(new_elems, d[x])
                curr_done = curr_done and merge_done
            new_set.update([tuple(x) for x in new_elems])
        new_d.update({i: new_set})
        done.update({i: curr_done})

    return new_d


def merge_tuples(new_elems, x):
    naive = [naive_merge(ft, y) for ft in new_elems for y in x]
    curr_done = True
    for j in naive:
        i = 0
        while i < len(j) - 1:
            if isinstance(j[i], str) and isinstance(j[i+1], str):
                j[i] = j[i] + j[i + 1]
                del j[i + 1]
            else:
                i = i + 1
                curr_done = False

    return naive, curr_done


def naive_merge(ft, x):
    lis = list(x)
    ret = ft + lis
    return ret


# Everything must take the form of (42){2,}(31)+
def valid(x, front, back):
    mode = 0
    front_count = 0
    back_count = 0
    order = True
    condensed_str = ""
    for i in range(len(x) // 8):
        sl = x[i*8:i*8+8]
        if mode == 0:
            if sl in front:
                front_count += 1
                condensed_str += "f"
            else:
                back_count += 1
                condensed_str += "b"
                mode = 1
        else:
            if sl in back:
                condensed_str += "b"
                back_count += 1
            else:
                condensed_str += "f"
                order = False
                front_count += 1
    result = order and front_count >= 2 and back_count >= 1 and front_count >= back_count + 1

    if condensed_str != "ffb":
        print(f"f:{condensed_str}, r:{result}")
    return result


def part_two(str_list):
    d = {}
    done = {}
    mode = 0
    x = 0
    front = set()
    back = set()
    done_count = 0

    for i in str_list:
        if i.strip() == "":
            mode += 1
            del d[0]
            del d[8]
            del d[11]
            while done_count < len(d.items()):
                d = reduce_once(d, done, True)
                done_count = sum(1 for x, y in done.items() if y is True)
            front = {x[0] for x in d[42]}
            back = {x[0] for x in d[31]}
        elif mode == 0:
            d.update(split_input(i))
        elif mode == 1:
            if valid(i.strip(), front, back):
                x += 1

    return x


def split_input(n):
    key_split = re.split(": ", n.strip())
    key = int(key_split[0])
    if key_split[1] == "\"a\"":
        return {key: {tuple("a")}}
    if key_split[1] == "\"b\"":
        return {key: {tuple("b")}}
    set_return = {make_list(x) for x in re.split(" \\| ", key_split[1])}
    return {key: set_return}


def make_list(num_str):
    return tuple(int(x) for x in re.split(" ", num_str))


def part_one(str_list):
    d = {}
    done = {}
    mode = 0
    x = 0
    valid_list = set()

    for i in str_list:
        if i.strip() == "":
            mode += 1
            while not done.get(0, False):
                d = reduce_once(d, done, False)
            valid_list = {y for x in d[0] for y in x}
        elif mode == 0:
            d.update(split_input(i))
        elif mode == 1:
            if i.strip() in valid_list:
                x += 1

    return x
