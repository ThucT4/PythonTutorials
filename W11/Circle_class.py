import math


class Circle:
    def __init__(self, radius):
        self._rad = radius

    def getArea(self):
        return math.pi * (self._rad ** 2)

    def getPerimeter(self):
        return math.pi * self._rad * 2


if __name__ == '__main__':
    circy = Circle(11)
    print(circy.getArea())

    # Should return 380.132711084365

    circy = Circle(4.44)
    print(circy.getPerimeter())

    # Should return 27.897342763877365
