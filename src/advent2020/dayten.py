from collections import Counter


def part_one(str_list):
    inst = [int(x) for x in str_list]
    inst.append(0)
    inst.append(max(inst) + 3)
    inst.sort()
    c = Counter()

    for i in range(len(inst) - 1):
        c[inst[i + 1] - inst[i]] += 1
    return c[1], c[3]


class Solver:
    def __init__(self, str_list):
        self.a = {int(x) for x in str_list}
        self.a.add(max(self.a) + 3)
        self.dp = {}

    def __getitem__(self, item):
        if item in self.dp:
            return self.dp[item]
        elif item == 0:
            return 1
        elif item < 0:
            return 0
        elif item not in self.a:
            return 0
        else:
            self.dp[item] = self[item-1] + self[item - 2] + self[item - 3]
            return self.dp[item]

    def solve(self):
        return self[max(self.a)]


def part_two(str_list):
    s = Solver(str_list)
    return s.solve()
