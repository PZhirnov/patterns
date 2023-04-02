import abc


# Опишем абстракцию - абстрактный датчик, использующий реализацию физического датчика по интерфейсу
class AbstractSensor:
    def __init__(self, implementor):
        self._implementor = implementor

    def get_value(self):
        return self._implementor.get_value_impl()


# Описываем сам интерфейс
class SensorImplementor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_value_impl(self):
        pass


# Описываем базовый интерфейс физического датчика
class BaseSensorImplementor(SensorImplementor):
    value_list = [12.3, 12.25, 12.18, 12.41, 12.43, 14.5, 14.9]

    def __init__(self):
        self.values = iter(__class__.value_list)

    def get_value_impl(self):
        return next(self.values)


class BaseSensor(AbstractSensor):
    pass

print('BaseSensor')
base_sensor_1 = BaseSensor(BaseSensorImplementor())
print(base_sensor_1.get_value())
print(base_sensor_1.get_value())
print(base_sensor_1.get_value())


# раширим возможности со стороны абстракции - создадим датчик, возращающий среднее значение
class AverageSensor(AbstractSensor):
    def __init__(self, implementor, n):
        super().__init__(implementor)
        # очередь последних изменений
        self.queue = []
        self.n = n

    # среднее по последним n изменениям
    def get_average_value(self):
        self.queue.append(self._implementor.get_value_impl())
        if len(self.queue) > self.n:
            self.queue.pop(0)

        return sum(self.queue) / len(self.queue)


print('AverageSensor')
average_sensor_1 = AverageSensor(BaseSensorImplementor(), 5)
print(average_sensor_1.get_value())
[print(average_sensor_1.get_average_value()) for _ in range(7)]
