"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.engine import Engine
from homework_05.base import Vehicle


class Car(Vehicle):
    def __init__(self, engine: Engine):
        super().__init__()
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine