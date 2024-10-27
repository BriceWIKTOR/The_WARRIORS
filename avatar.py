from abc import ABC, abstractmethod
from weapon import Weapon

class Avatar(ABC):
    def __init__(self, name: str):
        self._name = name
        self._weapon = Weapon("weapon", 0) # Ici j'ai fait une Composition: chaque avatar a sa propre arme par défaut
        self._hp = 100
        self._mp = 0
        self._gold = 20

    @abstractmethod
    def greet(self):        
        pass

    @abstractmethod
    def drink_potion(self):  
        pass

    @abstractmethod
    def attack(self, other): 
        pass

    def check_hp(self, other):
        if self._hp <= 0:
            other._gold += self._gold
            raise SystemExit(f"Game Over! {self._name} has been defeated by {other._name} and has now {other._gold} 🪙🪙🪙 gold")
        else:
            print(f"{self._name} has {self._hp} ❤️ HP")