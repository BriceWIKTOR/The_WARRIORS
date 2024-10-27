from avatar import Avatar
from weapon import Weapon
import random

class Thief(Avatar):
    def __init__(self, name: str):
        super().__init__(name)
        self._weapon = Weapon("Dagger", 1)
        self._mp = 15

    def greet(self, other):
        self._gold += 1
        other._gold -= 1
        print(f"{self._name} says HELLO, YOU LOOK SO GOOD TODAY! 😁 to his opponent and has {self._gold} 🪙🪙🪙 gold after stealing {other._name} who has now {other._gold}🪙🪙🪙")

    def drink_potion(self):
        if self._hp >= 100:
            self._hp = 100
        else:
            self._hp += 10
        print(f"After drinking this potion, {self._name} has {self._hp} ❤️ HP")

    def attack(self, other):
        print(f"{self._name} is fighting against {other._name}")
        if self._hp > 0 and other._hp > 0:
            critical_hit = self._weapon.power * (random.randint(1, 100))
            other._hp -= critical_hit
            print(f"{self._name} inflicts {critical_hit} damage points with his {self._weapon.name} to {other._name}")
