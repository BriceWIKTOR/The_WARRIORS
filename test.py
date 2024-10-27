import unittest
from warrior import Warrior
from wizard import Wizard
from thief import Thief
from weapon import Weapon


class TestGame(unittest.TestCase):

    #--------------------------------------------- Ici je teste l'initialisation des classes de players
    def test_warrior(self):
        warrior = Warrior("THE BLACK PYTHON")
        self.assertEqual(warrior._name, "THE BLACK PYTHON")  
        self.assertEqual(warrior._weapon.name, "Golden Axe")  
        self.assertEqual(warrior._weapon.power, 40)  
        self.assertEqual(warrior._hp, 100)  
        self.assertEqual(warrior._mp, 10)  
        self.assertEqual(warrior._gold, 20)  

    
    def test_wizard(self):
        wizard = Wizard("HARRY POTIRON")
        self.assertEqual(wizard._name, "HARRY POTIRON")
        self.assertEqual(wizard._weapon.name, "Fireball")
        self.assertEqual(wizard._weapon.power, 20)
        self.assertEqual(wizard._hp, 100)
        self.assertEqual(wizard._mp, 50)
        self.assertEqual(wizard._gold, 20)

    
    def test_thief(self):
        thief = Thief("SNEAKY PINKY")
        self.assertEqual(thief._name, "SNEAKY PINKY")
        self.assertEqual(thief._weapon.name, "Dagger")
        self.assertEqual(thief._weapon.power, 1)
        self.assertEqual(thief._hp, 100)
        self.assertEqual(thief._mp, 15)
        self.assertEqual(thief._gold, 20)

    #--------------------------------------------- Ici je teste les méthodes d'attaque 
    def test_warrior_attack(self):
        warrior = Warrior("THE BLACK PYTHON")
        oponent = Wizard("HARRY POTIRON")
        warrior.attack(oponent)
        self.assertEqual(oponent._hp, 60)  

    
    def test_wizard_attack(self):
        wizard = Wizard("HARRY POTIRON")
        oponent = Warrior("THE BLACK PYTHON")
        wizard.attack(oponent)
        self.assertEqual(oponent._hp, 80)  

    
    def test_thief_attack(self):
        thief = Thief("SNEAKY PINKY")
        oponent = Wizard("HARRY POTIRON")
        thief.attack(oponent)
        self.assertTrue(0 <= oponent._hp <= 100)  

    #--------------------------------------------- Ici je teste les méthodes drink_potion 
    def test_warrior_drink_potion(self):
        warrior = Warrior("THE BLACK PYTHON")
        warrior._hp = 50
        warrior.drink_potion()
        self.assertEqual(warrior._hp, 55)  

    
    def test_wizard_drink_potion(self):
        wizard = Wizard("HARRY POTIRON")
        wizard._hp = 50
        wizard.drink_potion()
        self.assertEqual(wizard._hp, 70) 

    
    def test_thief_drink_potion(self):
        thief = Thief("SNEAKY PINKY")
        thief._hp = 50
        thief.drink_potion()
        self.assertEqual(thief._hp, 60)  


unittest.main()
