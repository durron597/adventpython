import numpy as np
from numpy import int32


class IntCode:
    def __init__(self, inst_size):
        self.inst = np.zeros(inst_size, dtype=int32)

    def process(self, ins):
        for idx, i in enumerate(ins):
            self.inst[idx] = i

        return self._execute(0)

    def _execute(self, start):
        curr = start
        while self.inst[curr] != 99:
            delta = self._execute_once(curr)

            curr += delta

        return self.inst[0]

    def _execute_once(self, curr):
        match self.inst[curr]:
            case 1:
                left = self.inst[self.inst[curr + 1]]
                right = self.inst[self.inst[curr + 2]]
                self.inst[self.inst[curr + 3]] = left + right
                return 4
            case 2:
                left = self.inst[self.inst[curr + 1]]
                right = self.inst[self.inst[curr + 2]]
                self.inst[self.inst[curr + 3]] = left * right
                return 4
            case _:
                raise Exception("Unknown opcode")
