import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, initial_money=0):
        self.name = name
        self.money=initial_money

    @abstractmethod
    def perform_action(self):
        pass

class Generous(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return "Cooperate"

class Selfish(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        return "Betray"

class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        actions = ["Cooperate", "Betray"]
        return random.choice(actions)



