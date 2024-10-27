from avatar import Avatar
from weapon import Weapon

class Warrior(Avatar):
    def __init__(self, name: str):
        super().__init__(name)
        self._weapon = Weapon("Golden Axe", 40)
        self._mp = 10

    def greet(self):
        print(f"{self._name} says ARG! 😡 to his opponent")

    def drink_potion(self):
        if self._hp >= 100:
            self._hp = 100
        else:
            self._hp += 5
        print(f"After drinking this potion, {self._name} has {self._hp} HP")

    def attack(self, other):
        print(f"{self._name} is fighting against {other._name}")
        if self._hp > 0 and other._hp > 0:
            other._hp -= self._weapon.power
            print(f"{self._name} inflicts {self._weapon.power} damage points with his {self._weapon.name} to {other._name}")
