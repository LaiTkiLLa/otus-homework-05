"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        super().__init__()
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, volume):
        if self.cargo + volume > self.max_cargo:
            raise CargoOverload('Перегруз')
        self.cargo += volume

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo