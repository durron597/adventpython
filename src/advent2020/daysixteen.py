import re

from util.SegmentTree import SegmentTree


def part_one(str_list):
    d = SegmentTree()
    mode = 0
    sum_missing = 0
    for elem in str_list:
        if elem.strip() == "":
            mode += 1
            continue
        elif mode == 0:
            s = re.split(": ", elem)
            n = re.findall("\\d+", s[1])
            d.update({int(n[0]): int(n[1])})
            d.update({int(n[2]): int(n[3])})
        elif mode == 1:
            continue
        else:
            sum_missing += sum((int(x) for x in re.findall("\\d+", elem) if int(x) not in d))

    return sum_missing


def part_two(str_list):
    valid_mappings, my_ticket, ticket_list = parse_file(str_list)

    mapping = extract_candidates(valid_mappings, ticket_list)

    proved = identify_types(valid_mappings, mapping)

    product = 1

    for i in range(len(my_ticket)):
        t = proved[i]
        if t.startswith("departure"):
            product *= my_ticket[i]

    return product


def parse_file(str_list):
    valid_mappings = {}
    top_st = SegmentTree()
    mode = 0
    my_ticket = []
    ticket_list = []
    for elem in str_list:
        if elem.strip() == "":
            mode += 1
            continue
        elif mode == 0:
            parse_mapping_entry(elem, top_st, valid_mappings)
        elif mode == 1:
            findall = re.findall("\\d+", elem)
            if findall:
                my_ticket = [int(x) for x in findall]
        else:
            parse_nearby_tickets(elem, ticket_list, top_st)

    return valid_mappings, my_ticket, ticket_list


def parse_nearby_tickets(elem, ticket_list, top_st):
    findall = re.findall("\\d+", elem)
    valid_ticket = [x for x in findall if int(x) not in top_st]
    if findall and not valid_ticket:
        ticket_list.append([int(x) for x in findall])


def parse_mapping_entry(elem, top_st, valid_mappings):
    s = re.split(": ", elem)
    n = re.findall("\\d+", s[1])
    st = SegmentTree()
    st.update({int(n[0]): int(n[1])})
    st.update({int(n[2]): int(n[3])})
    valid_mappings.update({s[0]: st})
    top_st.update(st)


def identify_types(d, mapping):
    proved = {}
    while len(proved) < len(d):
        found_loc = ""
        for loc, cand in mapping.items():
            if len(cand) == 1:
                found_loc = cand.pop()
                proved.update({loc: found_loc})
                break
        mapping = {k: {i for i in v if i != found_loc} for k, v in mapping.items()}
    return proved


def extract_candidates(d, ticket_list):
    mapping = {}
    for i in range(len(ticket_list[0])):
        valid = set()
        for types in d.items():
            good = True
            for ticket in ticket_list:
                if ticket[i] not in types[1]:
                    good = False
                    break
            if good:
                valid.update([types[0]])

        mapping.update({i: valid})
    return mapping
