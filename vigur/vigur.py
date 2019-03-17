import sys
import math


class Vector:
    """
    Vector class
    Original: DSG
    Improved: Kristjan
    """

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __len__(self):
        """
        can only return int
        :return: int
        """
        return int(math.sqrt((math.pow(self._x, 2) + math.pow(self._y, 2))))

    def __str__(self):
        return "[{0._x} {0._y}]".format(self)

    def __repr__(self):
        return "Vigur(x={0._x}, y={0._y})".format(self)

    def __add__(self, other):
        n_x = self._x + other.x
        n_y = self._y + other.y
        return Vector(n_x, n_y)

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    def print(self):
        sys.stdout.write(str(self) + "\n")

    @property
    def lengd(self):
        """
        :return: length of vector in float
        """
        return math.sqrt((math.pow(self._x, 2) + math.pow(self._y, 2)))

    @property
    def halli(self):
        return self._y / self._x

    def þvervigur(self):
        n_x = (self._y * -1)
        n_y = self._x
        return Vector(n_x, n_y)

    @property
    def stefnuhorn(self):
        dg = math.degrees(math.atan2(self._y, self._x))
        return dg if dg < 180 else dg - 360

    def horn(self, other):
        _q = (
            (
                    (self._x * self._y) + (other.x * other.y)
            )
            /
            (
                (math.sqrt(self.lengd * other.lengd))
            )
        )
        return math.degrees(math.acos(_q))

    @property
    def summa(self):
        """
        Use __add__
        :return:
        """
        pass


if __name__ == '__main__':
    v = Vector(3, 4)
    g = Vector(1, 1)
    h = Vector(5, 3)
    sys.stdout.write(str(len(v)) + "\n")
    sys.stdout.write(str(v.lengd) + "\n")
    v.print()
    z = v + g
    sys.stdout.write(str(z) + "\n")
    sys.stdout.write(str(z.halli) + "\n")
    sys.stdout.write(str(h.stefnuhorn) + "\n")
