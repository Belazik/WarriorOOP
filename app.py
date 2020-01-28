import random
from wariorlib import Warrior, Fight



weapon = ['sword', 'knife', 'hands']
race = ['niger', 'vegan', 'hipster']
name = ['BillyG', 'Thunder', 'Morgenshtern', 'Yarik']
a = Warrior()
warriorOne = a.setAll(name, race, weapon)
b = Warrior()
warriorTwo = b.setAll(name, race, weapon)
fight = Fight()
fight.start(warriorOne, warriorTwo)