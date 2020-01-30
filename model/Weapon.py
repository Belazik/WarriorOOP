# coding=utf-8
"""     Класс оружия
Properties:
    type - тип оружия
    damage - базовый урон
"""
from enum import Enum


class WeaponType(Enum):
    SWORD = 0
    BOW = 1
    HAMMER = 2
    MAGIC_WAND = 3


class Weapon:
    DEFAULT_DAMAGE = 20
    type = int
    damage = int

    def __init__(self, type, damage=DEFAULT_DAMAGE):
        self.type = type
        self.damage = damage

    def getDamage(self, strength: float, dexterity: float):
        weapon_type_selector = {
            WeaponType.SWORD: self.damage * strength * dexterity,
            WeaponType.BOW: self.damage * dexterity,
            WeaponType.HAMMER: self.damage * strength,
            WeaponType.MAGIC_WAND: self.damage * 0.1
        }
        return weapon_type_selector[self.type]

    def getName(self):
        weapon_name_selector = {
            WeaponType.SWORD: "меч",
            WeaponType.BOW: "лук",
            WeaponType.HAMMER: "молот",
            WeaponType.MAGIC_WAND: "волшебная палочка"
        }
        return weapon_name_selector[self.type]
