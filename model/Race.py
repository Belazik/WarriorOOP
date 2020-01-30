# coding=utf-8
"""     Класс Рассы
Properties:
    name - наименования рассы
    health - здоровье
    strength - сила [0,1]
    dexterity - ловкность [0,1]
"""


class Race:
    DEFAULT_RATE = 1
    DEFAULT_HEALTH = 100
    name = int
    health = int
    strength = float
    dexterity = float

    def __init__(self, name, health=DEFAULT_HEALTH, strength=DEFAULT_RATE, dexterity=DEFAULT_RATE):
        self.name = name
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
