import abc


# Интерфейс обработчика
import random


class Handler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, request):
        if self.next is not None:
            self.next.handle(request)

    def link(self, next):
        self.next = next
        return self.next


# Конкретный класс оператора
class Operator(Handler):
    probability = 0.75

    def __init__(self, name):
        self.name = name

    def handle(self, request):
        if self.is_busy():
            print(f'Оператор {self.name} занят')
            super().handle(request)
        else:
            print(f'Оператор {self.name}')

    def is_busy(self):
        return random.Random() < __class__.probability
