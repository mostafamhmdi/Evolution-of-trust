import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, initial_money=0):
        self.name = name
        self.money=initial_money

    @abstractmethod
    def perform_action(self, opponent_last_action,round_number):
        pass

class Generous(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action,round_number):
        return "Cooperate"

class Selfish(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action,round_number):
        return "Betray"


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action,round_number):
        actions = ["Cooperate", "Betray"]
        return random.choice(actions)
    

class CopyCat(Player):
    def __init__(self, name):
        super().__init__(name)

    def perform_action(self, opponent_last_action,round_number):
        if round_number==1:
            return "Cooperate"
        else:
            return opponent_last_action


class Grudger(Player):
    def __init__(self, name):
        super().__init__(name)
        self.actions=[]
    
    def perform_action(self, opponent_last_action,round_number):
        if round_number==1:
            self.actions=[]
            return "Cooperate"
        if round_number==2:
            self.actions.append(opponent_last_action)
            if "Betray" in self.actions:
                return "Betray"
            else:
                return "Cooperate"
        self.actions.append(opponent_last_action)

        if "Betray" in self.actions:
            return "Betray"
        else:
            return "Cooperate"
            
    

class Detective(Player):
    def __init__(self, name):
        super().__init__(name)
        self.actions = []

    def perform_action(self, opponent_last_action,round_number):
        
        if round_number==1:
            self.actions=[]
            return "Cooperate"
        elif round_number==2:
            return "Betray"
        elif round_number==3:
            return "Cooperate"
        elif round_number==4:
            self.actions.append(opponent_last_action)
            return "Cooperate"
        elif round_number>4:
            self.actions.append(opponent_last_action)
            if "Betray" in self.actions[:-1]:
                return opponent_last_action
            else:
                return "Betray"
            

        
