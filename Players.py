import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, initial_money=0):
        self.name = name
        self.money=initial_money

    @abstractmethod
    def perform_action(self, opponent_last_action):
        pass

class Generous(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action):
        return "Cooperate"

class Selfish(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action):
        return "Betray"


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action):
        actions = ["Cooperate", "Betray"]
        return random.choice(actions)
    

class CopyCat(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action):
        return opponent_last_action


class Grudger(Player):
    def __init__(self, name):
        super().__init__(name)

    
    def perform_action(self, opponent_last_action):
        actions=[]
        actions.append(opponent_last_action)
        if "Betray" in actions:
            return "Betray"
        else:
            return "Cooperate"
            

class Detective(Player):
    def __init__(self, name):
        super().__init__(name)

    
    def perform_action(self, opponent_last_action):
        actions=[]
        i=1
        actions.append(opponent_last_action)
        if i==1:
            return "Cooperate"
        elif i==2:
            return "Betray"
        elif i==3:
            return "Cooperate"
        elif i==4:
            return "Cooperate"

        elif i > 4:
            if "Betray" in actions:
                return opponent_last_action
            else:
                return "Cooperate"
