import tkinter as tk
from tkinter import messagebox
import random
from Players import CopyCat, Selfish, Generous, Grudger, Detective, Simpleton, Copykitten,RandomPlayer
from RLagent import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Trust of Evolution Game")

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

        self.label_smart = tk.Label(master, text="Enter the number of Smart players: ")
        self.label_smart.grid(row=11    , column=0, padx=10, pady=5, sticky="w")
        self.entry_smart = tk.Entry(master)
        self.entry_smart.grid(row=11, column=1, padx=10, pady=5)

        self.label_ch_ch = tk.Label(master, text="Cheat-Cheat payoff: ")
        self.label_ch_ch.grid(row=12, column=0, padx=10, pady=5, sticky="w")
        self.entry_ch_ch = tk.Entry(master)
        self.entry_ch_ch.grid(row=12, column=1, padx=10, pady=5)

        self.label_c_c = tk.Label(master, text="Cooperate-Cooperate payoff: ")
        self.label_c_c.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        self.entry_c_c = tk.Entry(master)
        self.entry_c_c.grid(row=13, column=1, padx=10, pady=5)

        self.label_c_ch = tk.Label(master, text="Cooperate-Cheat payoff (COOPERATE): ")
        self.label_c_ch.grid(row=14, column=0, padx=10, pady=5, sticky="w")
        self.entry_c_ch = tk.Entry(master)
        self.entry_c_ch.grid(row=14, column=1, padx=10, pady=5)

        self.label_ch_c = tk.Label(master, text="Cheat-Cooperate payoff (CHEAT): ")
        self.label_ch_c.grid(row=15, column=0, padx=10, pady=5, sticky="w")
        self.entry_ch_c = tk.Entry(master)
        self.entry_ch_c.grid(row=15, column=1, padx=10, pady=5)

        self.button_start = tk.Button(master, text="Start Game", command=self.start_game)
        self.button_start.grid(row=16, column=0, columnspan=2, padx=10, pady=10,sticky='w')

        self.button_next_round = tk.Button(master, text="Next Round", command=self.show_next_round, state=tk.DISABLED)
        self.button_next_round.grid(row=16, column=1, columnspan=1, padx=10, pady=10,sticky = 'E')
        # Similar buttons can be added for other entry fields
        self.button_skip = tk.Button(master, text="Skip", command=self.skip_to_final_result, state=tk.DISABLED)
        self.button_skip.grid(row=16, column=2, columnspan=1, padx=10, pady=10,sticky = "E")


        self.rounds = []
        self.player_counts = []
        self.player_money = []
        self.player_counts_dict = {}
        self.plot_index = 0
        self.player_counts_2 ={}
        self.player_mean={}
        
    


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
            num_smart = int(self.entry_smart.get())
            ch_ch= int(self.entry_ch_ch.get())
            c_c = int(self.entry_c_c.get())
            c_ch= int(self.entry_c_ch.get())
            ch_c = int(self.entry_ch_c.get())
            if num_players <= 0 or num_rounds <= 0 or num_replace <= 0:
                raise ValueError("All values must be positive integers.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return


        self.game = Game(num_players, num_rounds, num_replace, num_generous, num_selfish, num_copycat, num_grudger, num_detective, num_simpleton, num_copykitten, num_random,num_smart,ch_ch,c_c,c_ch,ch_c)
        self.game.start()
        self.button_next_round.config(state=tk.NORMAL)
        self.button_skip.config(state=tk.NORMAL)
        self.button_start.config(state=tk.DISABLED)
        self.update_plot_data()
        self.plot_data()

    

    def plot_data(self):
        fig = plt.Figure(figsize=(12, 9))
        gs = GridSpec(3, 4, figure=fig)

        ax1 = fig.add_subplot(gs[0, :2])
        ax2 = fig.add_subplot(gs[0, 2:])
        ax3 = fig.add_subplot(gs[1, :])
        ax4 = fig.add_subplot(gs[2 , :])
        
        player_types = [player.__class__.__name__ for player in self.game.players]
        player_counts = {player_type: player_types.count(player_type) for player_type in set(player_types)}

        counts_per_round = {player_type: {self.rounds[-1]: player_types.count(player_type)} for player_type in player_types}
        self.player_counts_2[self.rounds[-1]] = counts_per_round
        randomshit=self.player_counts_2
        player_types = list(player_counts.keys())
        counts = list(player_counts.values())
        ax1.bar(player_types, counts, color='skyblue')
        for i in range(len(player_types)):
            ax1.text(i, counts[i], str(counts[i]), ha='center', va='bottom')
        ax1.set_xticklabels(player_types, rotation=30)
        ax1.set_title('Player Counts')
        
        mean_money = {}
        for player_type in set(player_types):
            money_sum = sum(player.money for player in self.game.players if player.__class__.__name__ == player_type)
            player_count = player_counts[player_type]
            mean_money[player_type] = money_sum / player_count

        self.player_mean[self.rounds[-1]] = mean_money
        randomshit2=self.player_mean
        mean_money_values = list(mean_money.values())
        ax2.bar(player_types, mean_money_values, color='skyblue')
        for i in range(len(player_types)):
            ax2.text(i, mean_money_values[i], str(mean_money_values[i]), ha='center', va='bottom')
        ax2.set_xticklabels(player_types, rotation=30)
        ax2.set_title('Group Mean Money')

        player_y = {}
        x_values = sorted(randomshit.keys())
        for round_number, round_data in randomshit.items():
            for player_type, player_data in round_data.items():
                if player_type not in player_y:
                    player_y[player_type] = [0] * len(randomshit)
                player_y[player_type][round_number - 1] = player_data.get(round_number, 0)

        for player_type, y_values in player_y.items():
            ax3.plot(x_values, y_values,marker='.', label=player_type)
        ax3.set_title('Player Counts per Round')
        ax3.legend()


        x_values_mean = list(randomshit2.keys())
        player_types = set()
        for round_data in randomshit2.values():
            player_types.update(round_data.keys())
        for player_type in player_types:
            y_values = [round_data.get(player_type, 0) for round_data in randomshit2.values()]
            ax4.plot(x_values, y_values,marker='.', label=player_type)

        ax4.set_title('Group Mean Money per Round')
        ax4.legend()

        fig.tight_layout(pad=5.0)
        
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=4, rowspan=18, columnspan=4)

        # Add toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.master)
        toolbar.update()
        canvas.get_tk_widget().grid(row=0, column=4, rowspan=18, columnspan=4)


    def update_plot_data(self):
        self.plot_index += 1
        self.rounds.append(self.plot_index)
        self.player_counts.append(len(set(type(player) for player in self.game.players)))
        total_money = sum(player.money for player in self.game.players)
        self.player_money.append(total_money)


    def show_next_round(self):
        if len(set(type(player) for player in self.game.players)) > 1:
            self.game.next_generation()
            self.game.reset_player_money()
            self.game.start()
            # self.display_result(self.game.show_result())
            self.update_plot_data()
            self.plot_data()
        else:
            self.display_winner(self.game.announce_winner())
            
            self.button_next_round.config(state=tk.DISABLED)
            self.button_skip.config(state=tk.DISABLED)
            self.button_start.config(state=tk.NORMAL)
            self.update_plot_data()
            self.plot_data()

    def skip_to_final_result(self):
        while len(set(type(player) for player in self.game.players)) > 1:
            self.game.next_generation()
            self.game.reset_player_money()
            self.game.start()
        # self.display_result(self.game.show_result())
        self.display_winner(self.game.announce_winner())
        self.button_start.config(state=tk.NORMAL)
        self.button_skip.config(state=tk.DISABLED)
        self.button_next_round.config(state=tk.DISABLED)
        self.update_plot_data()
        self.plot_data() 


    def display_result(self, result):
        self.result_label.config(text=result)

    def display_winner(self, winner):
        winner_label = tk.Label(self.master, text=winner)
        winner_label.config(fg="red", font=("Arial", 12, "bold"))
        winner_label.grid(row=18, column=0, columnspan=2, padx=10, pady=5)


class Game:
    def __init__(self, num_players, num_rounds, num_replace,num_generous,num_selfish,num_copycat,num_grudger,num_detective,num_simpleton,num_copykitten,num_random,num_smart,ch_ch,c_c,c_ch,ch_c):
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
        self.num_smart = num_smart
        self.ch_ch = ch_ch
        self.c_c = c_c
        self.c_ch =c_ch
        self.ch_c= ch_c
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
        for i in range(self.num_smart):
            self.players.append(RLPlayer(f"RLPlayer Player {i+1}"))     


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
                    


                    if isinstance(player1, RLPlayer):
                        reward1 = self.get_reward(action1, action2)
                        player1.update_q_table(reward1)
                    if isinstance(player2, RLPlayer):
                        reward2 = self.get_reward(action2, action1)
                        player2.update_q_table(reward2)

                    player1.money += self.get_reward(action1, action2)
                    player2.money += self.get_reward(action2, action1)

                    player1_last_action = action1  
                    player2_last_action = action2

    def get_reward(self, action1, action2):
        if action1 == "Cooperate" and action2 == "Cooperate":
            return self.c_c
        elif action1 == "Cooperate" and action2 == "Betray":
            return self.c_ch
        elif action1 == "Betray" and action2 == "Cooperate":
            return self.ch_c
        elif action1 == "Betray" and action2 == "Betray":
            return self.ch_ch 
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
                    money_values.remove(min_money)
                else:
                    min_money=money_values[0]
                for player in self.players:
                    if player.money == min_money:
                        poors.append(player)
                if len(poors)+ len(very_poors)<self.num_replace:
                    for i in range(len(poors)):
                        element=poors.pop(-1)
                        very_poors.append(element)
                    poors=[]
                else:
                    break
                i+=1
            random.shuffle(poors)
            for i in range(len(very_poors), self.num_replace):
                element = poors.pop(-1)
                very_poors.append(element)

            j=-1
            
            while len(self.players)-len(very_poors)+len(reaches)<self.num_players:
                if len(money_values)>1:
                    max_money=max(money_values)
                    money_values.remove(max_money)
                else:
                    max_money=money_values[0]
                for player in self.players:
                    if player.money == max_money:
                        reaches.append(player)
                        
                j+=1
            random.shuffle(reaches)
            new_players = []
        
            for player in reaches[:self.num_replace]:
                random_number = random.randint(1, 50)
                if random_number == 26:
                    players=self.players
                    random_player = random.choice(players)
                    if random_player =='CopyCat':
                        new_players.append(CopyCat(f"CopyCat Player {self.num_copycat + 1}"))
                        self.num_copycat += 1
                    elif random_player =='Selfish':
                        new_players.append(Selfish(f"Selfish Player {self.num_selfish + 1}"))
                        self.num_selfish += 1
                    elif random_player =='Generous':
                        new_players.append(Generous(f"Generous Player {self.num_generous + 1}"))
                        self.num_generous += 1
                    elif random_player =='Grudger':
                        new_players.append(Grudger(f"Grudger Player {self.num_grudger + 1}"))
                        self.num_grudger += 1
                    elif random_player =='Detective':
                        new_players.append(Detective(f"Detective Player {self.num_detective + 1}"))
                        self.num_detective += 1
                    elif random_player =='Simpleton':
                        new_players.append(Simpleton(f"Simpleton Player {self.num_simpleton + 1}"))
                        self.num_simpleton += 1  
                    elif random_player =='Copykitten':
                        new_players.append(Copykitten(f"Copykitten Player {self.num_copykitten + 1}"))
                        self.num_copykitten += 1  
                    elif random_player =='RandomPlayer':
                        new_players.append(RandomPlayer(f"RandomPlayer Player {self.num_random + 1}"))
                        self.num_random += 1
                    elif random_player =='RLPlayer':
                        new_players.append(RLPlayer(f"RLPlayer Player {self.num_smart + 1}"))
                        self.num_smart += 1 
                else:
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
                    elif isinstance(player, RLPlayer):
                        new_players.append(RLPlayer(f"RLPlayer Player {self.num_smart + 1}"))
                        self.num_smart += 1    
                

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
        elif isinstance(player, RLPlayer):
            return "Winners are Smarts"


def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
