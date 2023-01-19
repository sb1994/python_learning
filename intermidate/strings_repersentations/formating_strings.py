class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def __repr__(self) -> str:
        return 'Point2D(x={},y={})'.format(self.x, self.y)

    # not really needed use __str__ and __repr__
    def __format__(self, f):
        if f == 'r':
            return '({},{})'.format(self.y, self.x)
        else:
            return '({},{})'.format(self.x, self.y)
