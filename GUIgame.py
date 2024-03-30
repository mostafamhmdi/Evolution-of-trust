import tkinter as tk
from tkinter import messagebox
import random
from Players import CopyCat, Selfish, Generous, Grudger, Detective, Simpleton, Copykitten,RandomPlayer


class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Trust of Evolution Game")

        # Labels and Entries for user input
        self.label_players = tk.Label(master, text="How many players do you want to have:")
        self.label_players.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_players = tk.Entry(master)
        self.entry_players.grid(row=0, column=1, padx=10, pady=5)

        self.label_rounds = tk.Label(master, text="How many rounds players play:")
        self.label_rounds.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_rounds = tk.Entry(master)
        self.entry_rounds.grid(row=1, column=1, padx=10, pady=5)

        self.label_replace = tk.Label(master, text="How many players do you want to replace:")
        self.label_replace.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_replace = tk.Entry(master)
        self.entry_replace.grid(row=2, column=1, padx=10, pady=5)

        self.label_generous = tk.Label(master, text="Enter the number of Generous players: ")
        self.label_generous.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_generous = tk.Entry(master)
        self.entry_generous.grid(row=3, column=1, padx=10, pady=5)

        self.label_selfish = tk.Label(master, text="Enter the number of Selfish players: ")
        self.label_selfish.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_selfish = tk.Entry(master)
        self.entry_selfish.grid(row=4, column=1, padx=10, pady=5)

        self.label_copycat = tk.Label(master, text="Enter the number of CopyCat players: ")
        self.label_copycat.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_copycat = tk.Entry(master)
        self.entry_copycat.grid(row=5, column=1, padx=10, pady=5)

        self.label_grudger = tk.Label(master, text="Enter the number of Grudger players: ")
        self.label_grudger.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_grudger = tk.Entry(master)
        self.entry_grudger.grid(row=6, column=1, padx=10, pady=5)

        self.label_detective = tk.Label(master, text="Enter the number of Detective players: ")
        self.label_detective.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entry_detective = tk.Entry(master)
        self.entry_detective.grid(row=7, column=1, padx=10, pady=5)

        self.label_simpleton = tk.Label(master, text="Enter the number of Simpleton players: ")
        self.label_simpleton.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.entry_simpleton = tk.Entry(master)
        self.entry_simpleton.grid(row=8, column=1, padx=10, pady=5)

        self.label_copykitten = tk.Label(master, text="Enter the number of Copykitten players: ")
        self.label_copykitten.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.entry_copykitten = tk.Entry(master)
        self.entry_copykitten.grid(row=9, column=1, padx=10, pady=5)

        self.label_random = tk.Label(master, text="Enter the number of Random players: ")
        self.label_random.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.entry_random = tk.Entry(master)
        self.entry_random.grid(row=10, column=1, padx=10, pady=5)

        # Button to start the game
        self.button_start = tk.Button(master, text="Start Game", command=self.start_game)
        self.button_start.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        # Label to display the game result
        self.result_label = tk.Label(master, text="", wraplength=400)
        self.result_label.grid(row=12, column=0, columnspan=2, padx=10, pady=5)




    def start_game(self):
        try:
            num_players = int(self.entry_players.get())
            num_rounds = int(self.entry_rounds.get())
            num_replace = int(self.entry_replace.get())
            num_generous = int(self.entry_generous.get())
            num_selfish = int(self.entry_selfish.get())
            num_copycat = int(self.entry_copycat.get())
            num_grudger = int(self.entry_grudger.get())
            num_detective = int(self.entry_detective.get())
            num_simpleton = int(self.entry_simpleton.get())
            num_copykitten = int(self.entry_copykitten.get())
            num_random = int(self.entry_random.get())

            if num_players <= 0 or num_rounds <= 0 or num_replace <= 0:
                raise ValueError("All values must be positive integers.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Create and run the game
        game = Game(num_players, num_rounds, num_replace, num_generous, num_selfish, num_copycat, num_grudger, num_detective, num_simpleton, num_copykitten, num_random)
        game.start()
        self.display_result(game.show_result())
        while len(set(type(player) for player in game.players)) > 1:
            game.next_generation()
            game.reset_player_money()
            game.start()
            self.display_result(game.show_result())
        self.display_winner(game.announce_winner())

    def display_result(self, result):
        self.result_label.config(text=result)

    def display_winner(self, winner):
        winner_label = tk.Label(self.master, text=winner)
        winner_label.grid(row=14, column=0, columnspan=2, padx=10, pady=5)


class Game:
    def __init__(self, num_players, num_rounds, num_replace,num_generous,num_selfish,num_copycat,num_grudger,num_detective,num_simpleton,num_copykitten,num_random):
        self.players = []
        self.num_rounds = num_rounds
        self.num_players = num_players
        self.num_replace = num_replace
        self.num_generous = num_generous
        self.num_selfish = num_selfish
        self.num_copycat = num_copycat
        self.num_grudger = num_grudger
        self.num_detective = num_detective
        self.num_simpleton = num_simpleton
        self.num_copykitten = num_copykitten
        self.num_random = num_random
        self.create_players()

    def create_players(self):
        
        for i in range(self.num_generous):
            self.players.append(Generous(f"Generous Player {i+1}"))
        for i in range(self.num_selfish):
            self.players.append(Selfish(f"Selfish Player {i+1}"))
        for i in range(self.num_copycat):
            self.players.append(CopyCat(f"CopyCat Player {i+1}"))
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

    def start(self):
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]

                player1_last_action = "Cooperate"
                player2_last_action = "Cooperate"


                for round_number in range(1, self.num_rounds + 1):
                    action1 = player1.perform_action(player2_last_action, round_number)
                    action2 = player2.perform_action(player1_last_action, round_number)

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
        print("Final Results:")
        for player in self.players:
            print(f"{player.name}: {player.money}")

    def show_result(self):
        result = "Final Results:\n"
        for player in self.players:
            result += f"{player.name}: {player.money}\n"
        return result

    def next_generation(self):
        very_poors=[]
        reaches = []
        poors = []
        if len(self.players) > self.num_replace:
            money_values = {player.money for player in self.players}
            money_values = sorted(money_values)
            i=0
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
                i+=1
            random.shuffle(poors)
            for i in range(len(very_poors), self.num_replace):
                element = poors.pop(-1)
                very_poors.append(element)

            j=-1
            
            while len(self.players)-len(very_poors)+len(reaches)<self.num_players:
                if len(money_values)>1:
                    max_money=max(money_values)
                else:
                    max_money=money_values[0]
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
                elif isinstance(player, Simpleton):
                    new_players.append(Simpleton(f"Simpleton Player {self.num_simpleton + 1}"))
                    self.num_simpleton += 1  
                elif isinstance(player, Copykitten):
                    new_players.append(Copykitten(f"Copykitten Player {self.num_copykitten + 1}"))
                    self.num_copykitten += 1  
                elif isinstance(player, RandomPlayer):
                    new_players.append(RandomPlayer(f"RandomPlayer Player {self.num_random + 1}"))
                    self.num_random += 1      
                

            self.players = [player for player in self.players if player not in very_poors]+new_players

    def reset_player_money(self):
        for player in self.players:
            player.money = 0        

    def announce_winner(self):
        player = self.players[0]
        if isinstance(player, CopyCat):
            return "Winners are COPYCATS"
        elif isinstance(player, Selfish):
            return "Winners are SELFISHES"
        elif isinstance(player, Generous):
            return "Winners are GENEROUSES"
        elif isinstance(player, Grudger):
            return "Winners are GRUDGERS"
        elif isinstance(player, Detective):
            return "Winners are DETECTIVES"
        elif isinstance(player, Simpleton):
            return "Winners are Simpleton"
        elif isinstance(player, Copykitten):
            return "Winners are Copykitten"
        elif isinstance(player, RandomPlayer):
            return "Winners are RandomPlayer"


def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
