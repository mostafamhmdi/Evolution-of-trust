import random
from Players import Player,Generous,Selfish,RandomPlayer,CopyCat,Grudger,Detective,Simpleton,Copykitten
class Game:
    def __init__(self):
        self.players = []
        self.num_rounds = 0
        self.num_players = 0
        self.num_replace = 0
        self.num_copycat=0
        self.num_selfish=0
        self.num_generous=0
        self.num_grudger=0
        self.num_detective=0
        self.num_simpleton=0
        self.num_copykitten=0
        self.num_random=0

    def create_players(self):
        while True:
            try:
                self.num_players = int(input("How many players do you want to have: "))
                self.num_rounds = int(input("How many rounds players play: "))
                self.num_replace = int(input("How many players do you want to replace: "))
                self.num_generous = int(input("Enter the number of Generous players: "))
                self.num_selfish = 0 if self.num_generous == self.num_players else int(input("Enter the number of Selfish players: "))
                self.num_copycat = 0 if self.num_generous + self.num_selfish == self.num_players else int(input("Enter the number of CopyCat players: "))
                self.num_grudger = 0 if self.num_generous + self.num_selfish + self.num_copycat == self.num_players else int(input("Enter the number of Grudger players: "))
                self.num_detective = 0 if self.num_generous + self.num_selfish + self.num_copycat + self.num_grudger == self.num_players else int(input("Enter the number of Detective players: "))
                self.num_simpleton = 0 if self.num_generous + self.num_selfish + self.num_copycat + self.num_grudger + self.num_detective == self.num_players else int(input("Enter the number of Simpleton players: "))
                self.num_copykitten = 0 if self.num_generous + self.num_selfish + self.num_copycat + self.num_grudger + self.num_detective + self.num_simpleton == self.num_players else int(input("Enter the number of Copykitten players: "))
                self.num_random = 0 if self.num_generous + self.num_selfish + self.num_copycat + self.num_grudger + self.num_detective + self.num_simpleton + self.num_copykitten== self.num_players else int(input("Enter the number of Random players: "))
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
        for i in range(self.num_simpleton):
            self.players.append(Simpleton(f"Simpleton Player {i+1}"))
        for i in range(self.num_copykitten):
            self.players.append(Copykitten(f"Copykitten Player {i+1}"))
        for i in range(self.num_random):
            self.players.append(RandomPlayer(f"RandomPlayer Player {i+1}"))            

    def start(self,iterate_num):
        if iterate_num==1:
            print("Welcome to the Trust of Evolution game!")
            print("Let's start...\n")
            self.create_players()
        

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]


                player1_last_action = "Cooperate"
                player2_last_action = "Cooperate"

                # print(f"{player1.name} vs {player2.name}:")
                player1.money = player1.money
                player2.money = player2.money
                # print(f"{player1.name} :{player1.money} vs {player2.name}:{player2.money} :")
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

        #         print(f"{player1.name} final money: {player1.money}")
        #         print(f"{player2.name} final money: {player2.money}")
        #         print()
        # print("Game over!")
    def show_result(self):
        print("Final Results:")
        for player in self.players:
            print(f"{player.name}: {player.money}")
    def next_generation(self):
        very_poors=[]
        reaches = []
        poors = []
        if len(self.players) > self.num_replace:
            money_values = {player.money for player in self.players}
            money_values = sorted(money_values)
            
            while len(poors) + len(very_poors) <self.num_replace:
                if len(money_values)>1:
                    min_money=min(money_values)
                else:
                    min_money=money_values[0]
                for player in self.players:
                    if player.money == min_money:
                        poors.append(player)
                if len(poors)<self.num_replace:
                    for i in range(len(poors)):
                        element=poors.pop(-1)
                        very_poors.append(element)
                    poors=[]
                
            random.shuffle(poors)
            for i in range(len(very_poors), self.num_replace):
                element = poors.pop(-1)
                very_poors.append(element)

            
            
            while len(self.players)-len(very_poors)+len(reaches)<self.num_players:
                if len(money_values)>1:
                    max_money=max(money_values)
                else:
                    max_money=money_values[0]
                for player in self.players:
                    if player.money == max_money:
                        reaches.append(player)
                        
                
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
    def reset_player_money(self):
        for player in self.players:
            player.money = 0        
    def announce_winner(self):
        player=self.players[0]
        if isinstance(player, CopyCat):
            print("Winners are COPYCATS")     
        elif isinstance(player, Selfish):
            print("Winners are SELFISHES")
        elif isinstance(player, Generous):
            print("Winners are GENEROUSES")
        elif isinstance(player, Grudger):
            print("Winners are GRUDGERS")
        elif isinstance(player, Detective):
            print("Winners are DETECTIVES")





def main():
    game = Game()
    game.start(1)
    game.show_result()
    game.next_generation()
    game.reset_player_money()
    c=2
    while len(set(type(player) for player in game.players)) > 1:
        print(f"round number {c} started")
        game.start(2)
        game.show_result()  
        game.next_generation()  
        game.reset_player_money()  
        c+=1

    game.announce_winner()


if __name__ == "__main__":
    main()
