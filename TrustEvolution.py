import random
from Players import Player,Generous,Selfish,RandomPlayer,CopyCat,Grudger,Detective
class Game:
    def __init__(self):
        self.players = []
        self.num_rounds = 10
        self.num_players = int(input("how many players you want to have: "))
        self.num_replace = int(input("how many players you want to replace: "))
        self.num_copycat=0
        self.num_selfish=0
        self.num_generous=0
        self.num_grudger=0
        self.num_detective=0

    def create_players(self):
        while True:
            try:
                self.num_copycat = int(input("Enter the number of CopyCat players: "))
                self.num_selfish = int(input("Enter the number of Selfish players: "))
                self.num_generous = int(input("Enter the number of Generous players: "))
                self.num_grudger = int(input("Enter the number of Grudger players: "))
                self.num_detective = int(input("Enter the number of Detective players: "))
            
                break
            except ValueError:
                print("Please enter a valid number.")
        
        for i in range(self.num_copycat):
            self.players.append(CopyCat(f"CopyCat Player {i+1}"))
        for i in range(self.num_selfish):
            self.players.append(Selfish(f"Selfish Player {i+1}"))
        for i in range(self.num_generous):
            self.players.append(Generous(f"Generous Player {i+1}"))
        for i in range(self.num_grudger):
            self.players.append(Grudger(f"Grudger Player {i+1}"))
        for i in range(self.num_detective):
            self.players.append(Detective(f"Detective Player {i+1}"))

    def start(self):
        self.create_players()
        print(len(self.players))
        print("Welcome to the Trust of Evolution game!")
        print("Let's start...\n")

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]


                player1_last_action = "Cooperate"
                player2_last_action = "Cooperate"

                print(f"{player1.name} vs {player2.name}:")
                player1.money = player1.money
                player2.money = player2.money
                print(f"{player1.name} :{player1.money} vs {player2.name}:{player2.money} :")
                for round_number in range(1, self.num_rounds + 1):
                    

                    action1 = player1.perform_action(player2_last_action,round_number)
                    action2 = player2.perform_action(player1_last_action,round_number)

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

                    player1_last_action = action1  
                    player2_last_action = action2

                print(f"{player1.name} final money: {player1.money}")
                print(f"{player2.name} final money: {player2.money}")
                print()
        print("Game over!")
    def show_result(self):
        print("Final Results:")
        for player in self.players:
            print(f"{player.name}: {player.money}")
    def next_generation(self):
        sorted_players = sorted(self.players, key=lambda player: player.money, reverse=True)
        for player in sorted_players:
            print(f"{player.name}: {player.money}")

        print("Replacation:")
        if len(self.players) > self.num_replace:
            money_values = {player.money for player in self.players}
            money_values = sorted(money_values)
            i=0
            poors = []
            while len(poors)<self.num_replace:
                min_money = money_values.pop(i)
                for player in self.players:
                    if player.money == min_money:
                        poors.append(player)
                i+=1
            random.shuffle(poors)
            very_poors=[]
            for i in range(self.num_replace):
                element=poors.pop(-1)
                very_poors.append(element)

            j=-1
            reaches = []
            while len(self.players)-len(very_poors)+len(reaches)<self.num_players:
                max_money = money_values.pop(j)
                for player in self.players:
                    if player.money == max_money:
                        reaches.append(player)
                j+=1
            random.shuffle(reaches)
            new_players = []
        
            for player in reaches[:self.num_replace]:
                if isinstance(player, CopyCat):
                    new_players.append(CopyCat(f"CopyCat Player {self.num_copycat + 1}"))
                    self.num_copycat += 1
                elif isinstance(player, Selfish):
                    new_players.append(Selfish(f"Selfish Player {self.num_selfish + 1}"))
                    self.num_selfish += 1
                elif isinstance(player, Generous):
                    new_players.append(Generous(f"Generous Player {self.num_generous + 1}"))
                    self.num_generous += 1
                elif isinstance(player, Grudger):
                    new_players.append(Grudger(f"Grudger Player {self.num_grudger + 1}"))
                    self.num_grudger += 1
                elif isinstance(player, Detective):
                    new_players.append(Detective(f"Detective Player {self.num_detective + 1}"))
                    self.num_detective += 1    

            self.players = [player for player in self.players if player not in very_poors]+new_players
            sorted_players2 = sorted(self.players, key=lambda player: player.money, reverse=True)
            for player in sorted_players2:
                print(f"{player.name}: {player.money}")






def main():
    game = Game()
    game.start()
    # game.show_result()
    game.next_generation()
    

if __name__ == "__main__":
    main()
