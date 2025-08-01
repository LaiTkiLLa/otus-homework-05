"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel, NotStartedError

"""
fuel_consumption указывается на 100 км
"""
class Vehicle(ABC):
    def __init__(self, weight = 3, started = False, fuel = 40, fuel_consumption = 8):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel == 0:
            raise LowFuelError("Недостаточно топлива")
        self.started = True

    def move(self, distance):
        if not self.started:
            raise NotStartedError("Необходимо завести машину")
        max_distance = self.fuel * 100 / self.fuel_consumption
        if distance > max_distance:
            raise NotEnoughFuel("Топлива не хватит на маршрут")
        self.fuel = self.fuel - distance / 100 * self.fuel_consumption

