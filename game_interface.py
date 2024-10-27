from abc import ABC, abstractmethod

class Game_interface(ABC):
    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass

    @abstractmethod
    def round_launcher(self):
        pass

    @abstractmethod
    def check_hp(self):
        pass