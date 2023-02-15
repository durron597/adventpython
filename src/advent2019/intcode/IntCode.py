import numpy as np


class IntCode:
    def __init__(self, inst_size):
        self.inst = np.zeros(inst_size * 100, dtype=object)
        self.outp = []
        self.inp = tuple([0])
        self.inpi = 0
        self.curr = 0
        self.rel = 0

    def process(self, ins, *inp):
        self.inp = inp if inp else tuple([0])
        self.outp = []
        self.inpi = 0
        self.curr = 0
        self.rel = 0
        for idx, i in enumerate(ins):
            self.inst[idx] = i

        return self._execute()

    def resume(self, *inp):
        self.inpi = 0
        self.inp = inp
        return self._execute()

    def _execute(self):
        while self.inst[self.curr] != 99:
            delta = self._execute_once()

            if delta == -1:
                return self.outp

            self.curr += delta

        return self.outp

    def _execute_once(self):
        as_str = f"{self.inst[self.curr]:05d}"
        match int(as_str[-2:]):
            case 1:
                left = self._lookup(as_str[-3], self.curr + 1)
                right = self._lookup(as_str[-4], self.curr + 2)
                self.inst[self._target_lookup(as_str[-5], self.curr + 3)] = left + right
                return 4
            case 2:
                left = self._lookup(as_str[-3], self.curr + 1)
                right = self._lookup(as_str[-4], self.curr + 2)
                self.inst[self._target_lookup(as_str[-5], self.curr + 3)] = left * right
                return 4
            case 3:
                if self.inpi >= len(self.inp):
                    return -1
                else:
                    self.inst[self._target_lookup(as_str[-3], self.curr + 1)] = self.inp[self.inpi]
                    self.inpi += 1
                    return 2
            case 4:
                self.outp.append(self._lookup(as_str[-3], self.curr + 1))
                return 2
            case 5:
                if self._lookup(as_str[-3], self.curr + 1) != 0:
                    self.curr = self._lookup(as_str[-4], self.curr + 2)
                    return 0
                else:
                    return 3
            case 6:
                if self._lookup(as_str[-3], self.curr + 1) == 0:
                    self.curr = self._lookup(as_str[-4], self.curr + 2)
                    return 0
                else:
                    return 3
            case 7:
                left = self._lookup(as_str[-3], self.curr + 1)
                right = self._lookup(as_str[-4], self.curr + 2)
                self.inst[self._target_lookup(as_str[-5], self.curr + 3)] = 1 if left < right else 0
                return 4
            case 8:
                left = self._lookup(as_str[-3], self.curr + 1)
                right = self._lookup(as_str[-4], self.curr + 2)
                self.inst[self._target_lookup(as_str[-5], self.curr + 3)] = 1 if left == right else 0
                return 4
            case 9:
                self.rel += self._lookup(as_str[-3], self.curr + 1)
                return 2
            case _:
                raise Exception("Unknown opcode")

    def _lookup(self, mode, value):
        match mode:
            case '0':
                return self.inst[self.inst[value]]
            case '1':
                return self.inst[value]
            case '2':
                return self.inst[self.inst[value] + self.rel]
            case _:
                raise Exception("Unknown position")

    def _target_lookup(self, mode, value):
        match mode:
            case '0':
                return self.inst[value]
            case '2':
                return self.inst[value] + self.rel
            case _:
                raise Exception("Unknown position")

    def get_stop_command(self):
        return self.inst[self.curr]
