from avatar import Avatar
from weapon import Weapon

class Wizard(Avatar):
    def __init__(self, name: str):
        super().__init__(name)
        self._weapon = Weapon("Fireball", 20)
        self._mp = 50

    def greet(self):
        print(f"{self._name} says HELLO SIR! 😊 to his opponent")

    def drink_potion(self):
        if self._hp >= 100:
            self._hp = 100
        else:
            self._hp += 20
        print(f"After drinking this potion, {self._name} has {self._hp} ❤️ HP")

    def attack(self, other):
        print(f"{self._name} is fighting against {other._name}")
        print(f"{self._name} has {self._mp} 🎇 MP before fighting")
        if self._hp > 0 and other._hp > 0:
            if self._mp >= 5:
                self._mp -= 5
                other._hp -= self._weapon.power
                print(f"{self._name} inflicts {self._weapon.power} damage points with his {self._weapon.name} to {other._name}")
                print(f"{self._name} has now {self._mp} 🎇 MP")