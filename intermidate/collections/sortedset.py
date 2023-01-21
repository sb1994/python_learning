# contains a collection which is
# sized ,  iternable,sequence container  of a set of distinct items and
# constructable from from an iterable

class SortedSet:
    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []
