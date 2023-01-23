import math as mat

# create an exception class


class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "Triangle Error({!r})".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0]+sides[1]:
        raise TriangleError("Illegal Triangle", sides)

    p = (a+b+c) / 2
    a = mat.sqrt(int(p*(p-a)*(a-b)*(p-c)))
    return a
