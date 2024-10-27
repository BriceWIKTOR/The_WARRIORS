from game_interface import Game_interface
from avatar import Avatar
import random

class Game_controller(Game_interface):
    def __init__(self, player_one: Avatar, player_two: Avatar):
        self.player_one = player_one  # Ici je fais une Association: le jeu est associé aux joueurs
        self.player_two = player_two
        self.round = 1
        self.max_rounds = 10

    def start_game(self):

        self.player_one.greet()
        self.player_two.greet()

    def end_game(self):

        if self.player_one._hp > self.player_two._hp:
            winner = self.player_one
            loser = self.player_two
        else:
            winner = self.player_two
            loser = self.player_one

        winner._gold += loser._gold

    def round_launcher(self):

        attacker = self.player_one
        defender = self.player_two

        for player in [attacker, defender]:
            if player._hp > 0 and player._hp < 50:
                if random.randint(1, 10) <= 3:
                    player.drink_potion()

    def check_hp(self, other):
        if self._hp <= 0:
            other._gold += self._gold
            raise SystemExit(f"Game Over! {self._name} has been defeated by {other._name} and has now {other._gold} 🪙🪙🪙 gold")
        else:
            print(f"{self._name} has {self._hp} ❤️ HP")
