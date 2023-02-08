import re
from collections import deque
from typing import List


def ev(pre_map, param: List[str]):
    operator = deque()
    operand = deque()

    for token in param:
        if token.isdigit():
            operand.append(int(token))
        elif not operator or token == "(":
            operator.append(token)
        elif token == ")":
            while operator[-1] != "(":
                eval_once(operand, operator)
            operator.pop()
        else:
            while operator and operator[-1] != "(" and pre_map[token] <= pre_map[operator[-1]]:
                eval_once(operand, operator)
            operator.append(token)

    while operator:
        eval_once(operand, operator)

    return operand[-1]


def eval_once(operand, operator):
    if operator[-1] == "*":
        operator.pop()
        operand.append(operand.pop() * operand.pop())
    elif operator[-1] == "+":
        operator.pop()
        operand.append(operand.pop() + operand.pop())


def part_one(str_list):
    return list(ev({"(": 2, "+": 1, "*": 1}, split_input(n)) for n in str_list)


def split_input(n):
    return [x for x in re.split(" |(\\()|(\\))", n.strip()) if x is not None and x != '']


def part_two(str_list):
    return list(ev({"(": 3, "+": 2, "*": 1}, split_input(n)) for n in str_list)
