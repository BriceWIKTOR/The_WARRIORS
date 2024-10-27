from warrior import Warrior
from wizard import Wizard
from thief import Thief
from game_controller import Game_controller

warrior1 = Warrior("THE BLACK PYTHON")
wizard1 = Wizard("HARRY POTIRON")
thief1 = Thief("SNEAKY PINKY")

# Guerrier vs Magicien
print("\n------------------------------------------- FIGHT! ---------------------------------------------\n")
warrior1.greet()
wizard1.greet()
warrior1.check_hp(wizard1)
wizard1.check_hp(warrior1)


print("\n------------------------------------------- ROUND 1 ---------------------------------------------\n")
warrior1.attack(wizard1)
wizard1.attack(warrior1)
warrior1.check_hp(wizard1)
wizard1.check_hp(warrior1)


print("\n------------------------------------------- ROUND 2 ---------------------------------------------\n")
warrior1.drink_potion()
wizard1.drink_potion()
wizard1.attack(warrior1)
warrior1.check_hp(wizard1)
wizard1.check_hp(warrior1)



print("\n------------------------------------------- ROUND 3 ---------------------------------------------\n")
warrior1.attack(wizard1)
wizard1.attack(warrior1)
warrior1.check_hp(wizard1)
wizard1.check_hp(warrior1)


print("\n------------------------------------------- ROUND 4 ---------------------------------------------\n")
warrior1.attack(wizard1)
wizard1.attack(warrior1)
warrior1.check_hp(wizard1)
wizard1.check_hp(warrior1)


