"""Адаптер уровня класса
Обеспечить работу с квадратами как с круглыми объектами
"""
import abc
import math


# нечто круглое
class Roundable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_radius(self):
        pass


# окружность
class Circle(Roundable):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


# квадрат
class Square:
    def __init__(self, side):
        self._side = side

    def get_side(self):
        return self._side


# круглый квадрат - использование адаптера обеспечило работу с квадратом как с круглым объектом
class RoundbleSquare(Square, Roundable):
    def get_radius(self):
        return self.get_side() * math.sqrt(2) / 2


circle_1 = Circle(5)
roundable_square_1 = RoundbleSquare(5)

print(circle_1.get_radius())
print(roundable_square_1.get_radius())

print(issubclass(circle_1.__class__, Roundable))
print(issubclass(roundable_square_1.__class__, Roundable))
