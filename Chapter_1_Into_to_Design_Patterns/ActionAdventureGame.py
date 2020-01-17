'''
Page. 25

Below you’ll fi nd a mess of classes and interfaces for an action adventure game. You’ll
fi nd classes for game characters along with classes for weapon behaviors the characters
can use in the game. Each character can make use of one weapon at a time, but can
change weapons at any time during the game. Your job is to sort it all out...

'''
from abc import ABC, abstractmethod

# Abstract class for Character
class Character(ABC):
    def __init__(self):
        self.weapon = None

    @abstractmethod
    def display(self):
        pass

    def fight(self):
        self.weapon.useWeapon()

    def setWeapon(self, w):
        self.weapon = w

# Weapon Behavior
class WeaponBehavior(ABC):
    @abstractmethod
    def useWeapon(self):
        pass

# Implemented behavior
class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("cutting with a knife")

class BowAndArrow(WeaponBehavior):
    def useWeapon(self):
        print("shooting arrow with a bow")

class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("chopping with an axe")

class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("swinging a sword")

# Characters inheritence
class Queen(Character):
    def display(self):
        print("I'm the Queen")

class King(Character):
    def display(self):
        print("I'm the King")

class Troll(Character):
    def display(self):
        print("I'm the Troll")

class Knight(Character):
    def display(self):
        print("I'm the Knight")

# Testing
def AdventureGameSimulator():
    knight = Knight()
    knight.setWeapon(SwordBehavior())
    knight.display()
    knight.fight()

    king = King()
    king.setWeapon(BowAndArrow())
    king.display()
    king.fight()

if __name__ == "__main__":
    AdventureGameSimulator()