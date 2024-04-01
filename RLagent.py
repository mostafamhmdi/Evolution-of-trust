import random
from Players import Player,Generous,Selfish,RandomPlayer,CopyCat,Grudger,Detective,Simpleton,Copykitten
from RLENV import *
import pickle

class RLPlayer(Player):
    def __init__(self, name, alpha=0.1, gamma=0.9, epsilon=0.1, history_length=2):
        super().__init__(name)
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.history_length = history_length  # Length of opponent action history
        self.q_table = {}  # Q-table to store action-values
        self.opponent_history = []  # List to store opponent action history
        self.last_action = None


    def perform_action(self, opponent_last_action, round_number):

        self.load_q_table("q_table.pkl")

        # Add opponent's last action to history
        self.opponent_history.append(opponent_last_action)
        if len(self.opponent_history) > self.history_length:
            self.opponent_history.pop(0)  # Remove oldest action if history exceeds length

        # Construct state from opponent action history
        state = tuple(self.opponent_history)

        # Select action using epsilon-greedy strategy
        if random.random() < self.epsilon or state not in self.q_table:
            action = random.choice(["Cooperate", "Betray"])
        else:
            action = max(self.q_table[state], key=self.q_table[state].get)

        # Store last action
        self.last_action = action
        return action

    def update_q_table(self, reward):
        # Construct state from opponent action history
        state = tuple(self.opponent_history)

        if state not in self.q_table:
            self.q_table[state] = {"Cooperate": 0, "Betray": 0}

        # Update Q-value using Q-learning update rule
        prev_q_value = self.q_table[state][self.last_action]
        max_q_value = max(self.q_table[state].values())
        new_q_value = prev_q_value + self.alpha * (reward + self.gamma * max_q_value - prev_q_value)
        self.q_table[state][self.last_action] = new_q_value
        self.save_q_table("q_table.pkl")

    def reset(self):
        self.opponent_history = []
        self.last_action = None

    def save_q_table(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self, filename):
        with open(filename, 'rb') as f:
            self.q_table = pickle.load(f)

