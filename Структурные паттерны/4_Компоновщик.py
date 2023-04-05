import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class MachineOperation(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(self.name)


class CompositeOperation(Component):
    def __init__(self):
        self._child = set()

    def operation(self):
        for child in self._child:
            child.operation()

    def append(self, component):
        self._child.add(component)

    def remove(self, component):
        self._child.discard(component)


operation_1 = MachineOperation('сверлим отверстие №1')
operation_2 = MachineOperation('сверлим отверстие №2')
composit_1 = CompositeOperation()
composit_1.append(operation_1)
composit_1.append(operation_2)


operation_3 = MachineOperation('сверлим отверстие №3')
operation_4 = MachineOperation('сверлим отверстие №4')
composit_2 = CompositeOperation()

composit_2.append(composit_1)
composit_2.append(operation_3)
composit_2.append(operation_4)
composit_2.operation()
