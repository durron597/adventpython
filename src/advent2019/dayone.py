def part_one(str_list):
    return sum(int(x) // 3 - 2 for x in str_list)


class FuelCalc:
    def __init__(self):
        self._cache = {}

    def compute(self, v):
        if v in self._cache:
            return self._cache[v]

        if v == 0:
            return 0

        r = max(int(v) // 3 - 2, 0)
        return r + self.compute(r)


def part_two(str_list):
    fc = FuelCalc()

    return sum(fc.compute(int(x)) for x in str_list)
