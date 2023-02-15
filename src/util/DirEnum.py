from enum import Enum


class DirEnum(Enum):
    D = (1, 0)
    U = (-1, 0)
    L = (0, -1)
    R = (0, 1)

    def turn(self, i):
        if i == 0:
            match self.name:
                case "U":
                    return DirEnum.L
                case "L":
                    return DirEnum.D
                case "D":
                    return DirEnum.R
                case _:
                    return DirEnum.U
        else:
            match self.name:
                case "U":
                    return DirEnum.R
                case "L":
                    return DirEnum.U
                case "D":
                    return DirEnum.L
                case _:
                    return DirEnum.D