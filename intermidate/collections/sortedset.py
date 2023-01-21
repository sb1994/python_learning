# contains a collection which is
# sized ,  iternable,sequence container  of a set of distinct items and
# constructable from from an iterable

class SortedSet:
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]
