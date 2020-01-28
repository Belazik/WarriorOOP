import random
import time

class Warrior:
    def setAll(self, name, race, weapon):
        if type(name) == list:
            self.name = random.choice(name)
        elif type(name) == str:
            self.name = name
        else:
            self.name = 'NoNaMe'

        self.race = random.choice(race)
        if self.race == 'nigger':
            self.health = 250
        elif self.race == 'vegan':
            self.health = 220
        else:
            self.health = 200

        self.weapon = random.choice(weapon)
        if self.weapon == 'sword':
            self.strength = 35
        elif self.weapon == 'knife':
            self.strength = 25
        else:
            self.strength = 20
        return self.name, self.health, self.strength



class Fight:
    def start(self, *args):
        print('Fight of Baikal')
        time.sleep(2)
        self.warrior1 = list(args[0])
        self.warrior2 = list(args[1])
        print('Today will take place, grand fight {} vs {}'.format(self.warrior1[0], self.warrior2[0]))
        time.sleep(3)
        print('Let the battle begin!')
        while self.warrior1[1] >= 1 and self.warrior2[1] >= 1:
            time.sleep(2)
            queueAttack = random.randint(0,1)
            if queueAttack == 0:
                self.warrior1[1] -= self.warrior2[2]
                print('Hit deal {}, and hurt {}. Heal {} at {}'.format(self.warrior2[0], self.warrior1[0],
                      self.warrior1[1], self.warrior1[0]))
            else:
                self.warrior2[1] -= self.warrior1[2]
                print('Hit deal {}, and hurt {}. Heal {} at {}'.format(self.warrior1[0], self.warrior1[0],
                      self.warrior2[1], self.warrior2[0]))

        if self.warrior1[1] > self.warrior2[1]:
            print('Winner', self.warrior1[0])
        else:
            print('Winner', self.warrior2[0])

















