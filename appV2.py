import random

from Fight import Fight
from model.Race import Race
from model.Warrior import Warrior
from model.Weapon import Weapon, WeaponType

# определяем рассы
elfRace = Race(name="elf", strength=0.8, dexterity=1.3, health=90)
humanRace = Race(name="human", strength=1, dexterity=1)
ogcRace = Race(name="orc", strength=1.5, dexterity=0.3, health=140)
fairyRace = Race(name="fairy", strength=0.0001, dexterity=2, health=1)

# определяем оружия
swordWeapon = Weapon(type=WeaponType.SWORD)
bowWeapon = Weapon(type=WeaponType.BOW)
hammerWeapon = Weapon(type=WeaponType.HAMMER, damage=30)
magicWand = Weapon(type=WeaponType.MAGIC_WAND)
weaponsPool = [swordWeapon, bowWeapon, hammerWeapon, magicWand]

# определяем бойцов
aragornTheSonOfArathorn = Warrior(name="Арагорн сын Араторна", race=humanRace)
legalas = Warrior(name="Легалас", race=elfRace)
randomOrc = Warrior(name="Какой-то орк", race=ogcRace)
fairyGodmother = Warrior(name="Фея крестная", race=fairyRace)
warriorPool = [aragornTheSonOfArathorn, legalas, randomOrc, fairyGodmother]

# определяем кто будет сражаться
firstWarrior = random.choice(warriorPool)
warriorPool.remove(firstWarrior)
secondWarrior = random.choice(warriorPool)

# раздаем оружие
firstWarrior.weapon = random.choice(weaponsPool)
secondWarrior.weapon = random.choice(weaponsPool)

# погнали
Fight(firstWarrior, secondWarrior).mortalCombat()
