import re

from advent2019.intcode.IntCode import IntCode


def part_one(str_list):
    inst = [int(x) for x in re.split(",", str_list[0])]
    m = -1
    for ai in range(5):
        for bi in range(5):
            for ci in range(5):
                for di in range(5):
                    for ei in range(5):
                        if ai == bi or ai == ci or ai == di or ai == ei or bi == ci or bi == di or bi == ei \
                                or ci == di or ci == ei or di == ei:
                            continue
                        a = IntCode(len(inst))
                        b = IntCode(len(inst))
                        c = IntCode(len(inst))
                        d = IntCode(len(inst))
                        e = IntCode(len(inst))
                        ares = a.process(inst, ai, 0)
                        bres = b.process(inst, bi, ares[0])
                        cres = c.process(inst, ci, bres[0])
                        dres = d.process(inst, di, cres[0])
                        eres = e.process(inst, ei, dres[0])
                        m = max(m, eres[0])

    return m


def part_two(str_list):
    inst = [int(x) for x in re.split(",", str_list[0])]
    m = -1
    for ai in range(5, 10):
        for bi in range(5, 10):
            for ci in range(5, 10):
                for di in range(5, 10):
                    for ei in range(5, 10):
                        if ai == bi or ai == ci or ai == di or ai == ei or bi == ci or bi == di or bi == ei \
                                or ci == di or ci == ei or di == ei:
                            continue
                        eres = [0]
                        a = IntCode(len(inst))
                        b = IntCode(len(inst))
                        c = IntCode(len(inst))
                        d = IntCode(len(inst))
                        e = IntCode(len(inst))
                        ares = a.process(inst, ai, eres[-1])
                        bres = b.process(inst, bi, ares[-1])
                        cres = c.process(inst, ci, bres[-1])
                        dres = d.process(inst, di, cres[-1])
                        eres = e.process(inst, ei, dres[-1])
                        while e.get_stop_command() != 99:
                            ares = a.resume(eres[-1])
                            bres = b.resume(ares[-1])
                            cres = c.resume(bres[-1])
                            dres = d.resume(cres[-1])
                            eres = e.resume(dres[-1])
                        m = max(m, eres[-1])

    return m
