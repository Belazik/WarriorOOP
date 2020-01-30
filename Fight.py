import random
from time import sleep

from model.Warrior import Warrior

"""
Класс поединок
"""


class Fight:
    firstWarrior: Warrior
    secondWarrior: Warrior

    def __init__(self, war1: Warrior, war2: Warrior):
        self.firstWarrior = war1
        self.secondWarrior = war2

    def mortalCombat(self):
        print("Приветствуем бойцов " + self.firstWarrior.name + " и " + self.secondWarrior.name)
        print(self.firstWarrior.name + " держит в руках " + self.firstWarrior.weapon.getName() +
              " с показателем урона = " + self.firstWarrior.getDamage().__str__())
        print(self.secondWarrior.name + " держит в руках " + self.secondWarrior.weapon.getName() +
              " с показателем урона = " + self.secondWarrior.getDamage().__str__())

        sleep(2)

        warriors = [self.firstWarrior, self.secondWarrior]

        print("\n Fight!!! (играет музыка из MortalCombat) \n")
        while self.firstWarrior.race.health > 0 and self.secondWarrior.race.health > 0:
            sleep(2)
            attaker: Warrior = random.choice(warriors)
            attakerIndex = warriors.index(attaker)
            defender: Warrior = warriors.__getitem__(len(warriors) - attakerIndex - 1)
            damage = attaker.getDamage()
            defender.race.health -= damage

            print(attaker.name + " нанес цели " + defender.name + " " + damage.__str__() + " единиц урона")

        winner = self.firstWarrior \
            if self.firstWarrior.race.health > self.secondWarrior.race.health \
            else self.secondWarrior

        print("Победил " + winner.name)
