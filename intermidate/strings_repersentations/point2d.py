class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def __repr__(self) -> str:
        return 'Point2D(x={},y={})'.format(self.x, self.y)
