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

    def __init__(self, race, name=DEFAULT_NAME):
        self.race = race
        self.name = name

    def getDamage(self):
        return self.weapon.getDamage(strength=self.race.strength, dexterity=self.race.dexterity)
