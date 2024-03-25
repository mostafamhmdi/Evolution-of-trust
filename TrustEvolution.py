import random
from Players import Player,Generous,Selfish,RandomPlayer
class Game:
    def __init__(self):
        self.players = [
            Generous("Generous Player"),
            Selfish("Selfish Player"),
            RandomPlayer("Random Player")
        ]
        self.num_rounds = 7

    def start(self):
        print("Welcome to the Trust of Evolution game!")
        print("Let's start...\n")

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]

                print(f"{player1.name} vs {player2.name}:")
                player1.money = player1.money
                player2.money = player2.money
                print(f"{player1.name} :{player1.money} vs {player2.name}:{player2.money} :")
                for _ in range(self.num_rounds):
                    action1 = player1.perform_action()
                    action2 = player2.perform_action()

                    if action1 == "Cooperate" and action2 == "Cooperate":
                        player1.money += 2
                        player2.money += 2

                    elif action1 == "Cooperate" and action2 == "Betray":
                        player1.money += -1
                        player2.money += 3

                    elif action1 == "Betray" and action2 == "Cooperate":
                        player1.money += 3
                        player2.money += -1

                    elif action1 == "Betray" and action2 == "Betray":
                        player1.money += 0
                        player2.money += 0


                print(f"{player1.name} final money: {player1.money}")
                print(f"{player2.name} final money: {player2.money}")
                print()
        print("Game over!")



def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
