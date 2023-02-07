import sortedcontainers as sc


# For now, this is an add-only segment tree
class SegmentTree(dict[int, int]):
    def __init__(self, *args, **kwargs):
        self._tree = sc.SortedDict()
        self._update(*args, **kwargs)

    def __getitem__(self, item):
        return self._tree[item]

    def __setitem__(self, key, value):
        left = key
        right = value
        floor = self._floor_entry(key)
        if floor is not None:
            if left <= floor[1]:
                self._tree.pop(floor[0])
                left = floor[0]
            right = max(value, floor[1])

        while True:
            ceiling = self._ceiling_entry(left)
            if ceiling is not None:
                if ceiling[0] <= right:
                    self._tree.pop(ceiling[0])
                    right = max(ceiling[1], right)
                else:
                    break
            else:
                break

        self._tree.__setitem__(left, right)

    def _floor_entry(self, key):
        if key in self._tree:
            return key, self._tree[key]
        else:
            bisect = self._tree.bisect_left(key)
            if bisect > 0:
                return self._tree.peekitem(bisect - 1)
            else:
                return None

    def _ceiling_entry(self, key):
        if key in self._tree:
            return key, self._tree[key]
        else:
            bisect = self._tree.bisect_right(key)
            if bisect < len(self._tree):
                return self._tree.peekitem(bisect)
            else:
                return None

    def __delitem__(self, key):
        del self._tree[key]

    def update(self, *args, **kwargs):
        if not kwargs and len(args) == 1 and isinstance(args[0], dict):
            pairs = args[0]
        else:
            pairs = dict(*args, **kwargs)

        for i in pairs.items():
            self.__setitem__(i[0], i[1])

    _update = update

    def keys(self):
        return self._tree.keys()

    def items(self):
        return self._tree.items()

    def values(self):
        return self._tree.values()

    def clear(self) -> None:
        super().clear()

    def copy(self) -> dict[int, int]:
        return SegmentTree(self._tree)

    def popitem(self) -> tuple[int, int]:
        return self._tree.popitem()

    def setdefault(self, __key: int, __default: int = ...) -> int:
        return self._tree.setdefault(__key, __default)

    def __len__(self) -> int:
        return self._tree.__len__()

    def __str__(self) -> str:
        return self._tree.__str__().replace("SortedDict", "SegmentTree")

    def __contains__(self, __o: object) -> bool:
        floor = self._floor_entry(__o)
        if floor is None:
            return False
        else:
            return __o <= floor[1]

    def __repr__(self):
        return self._tree.__repr__().replace("SortedDict", "SegmentTree")
