"""
Создайте dataclass `Engine`
"""

from dataclasses import dataclass

@dataclass
class Engine:
    volume: int
    pistons: int
