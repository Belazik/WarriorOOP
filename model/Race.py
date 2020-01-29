# coding=utf-8

from enum import Enum

""" Enum for race"""


class RaceType(Enum):
    HUMAN = 0
    ELF = 1
    DWARF = 2
    FAIRY = 3


"""     Класс Рассы
Properties:
    name - наименования рассы
    strength - сила [0,1]
    dexterity - ловкность [0,1]
"""


class Race:
    DEFAULT_NAME = RaceType.HUMAN
    DEFAULT_RATE = 1
    name = int
    strength = float
    dexterity = float

    def __init__(self, name=DEFAULT_NAME, strength=DEFAULT_RATE, dexterity=DEFAULT_RATE):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
