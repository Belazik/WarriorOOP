# coding=utf-8
"""     Класс оружия
Properties:
    name - наименования оружия
    damage - базовый урон
"""


class Weapon:
    DEFAULT_NAME = "undefined"
    DEFAULT_DAMAGE = 20
    name = str
    damage = int

    def __init__(self, name=DEFAULT_NAME, damage=DEFAULT_DAMAGE):
        self.name = name
        self.damage = damage
