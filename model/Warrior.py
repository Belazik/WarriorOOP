# coding=utf-8
from model.Race import Race
from model.Weapon import Weapon

"""     Класс оружия
Properties:
    name - наименования воина
    race - расса 
    weapon - экипированное оружие
"""


class Warrior:
    DEFAULT_NAME = "unnamed"
    name = str
    race = Race
    weapon = Weapon

    def __init__(self, race, weapon, name=DEFAULT_NAME):
        self.race = race
        self.weapon = weapon
        self.name = name
