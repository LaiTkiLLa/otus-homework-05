"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class NotStartedError(Exception):
    pass

class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass