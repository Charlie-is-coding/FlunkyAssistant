from team import Team
from player import Player
import json
import copy
import random

class Game:

    players = []
    teams = list()
    rounds = 0
    turns = 0
    
    def __init__(self):
        pass

    def __str__(self):
        print("Players:", self.players)
        print("Teams:", self.teams)
        print("Rounds:", self.rounds)
        print("Turns:", self.turns)
        return ""

    def add_team(self):
        self.teams.append(Team())
    
        
    def make_teams(self, number):
        self.teams = []  # if not declared here will later cause reference problems (note to myself)
        for i in range(number):
            self.teams.append(Team(i))     

    def load_player_from_json_file(self, ID=1): 

        for i in range(len(self.players)):
            if self.players[i].player_id == ID:
                print("Player already in game")
                print("\n")
                return


        appended = False
        
        with open("players.json", "r", encoding="UTF-8") as file:
            for lines in file:
                player = json.loads(lines)
                if player["ID"] == ID:               
                   print("Player with ID:", player["ID"], "found.")
                   print("Adding player:", player["Name"])

                   temp_player = Player()
                   temp_player.player_id = player["ID"]
                   temp_player.name = player["Name"]
                   temp_player.game_empty = 0
                   temp_player.game_penalties = 0
                   temp_player.game_i_was_so_thisty = 0
                   self.players.append(temp_player)
                   appended = True

        if appended:
            print("Player with ID:", ID, "added to the game.")
            print("\n")

        else:
            print("Player with ID:", ID, "not found.")
            print("\n")

    def show_teams_info(self):
        for i in range(len(self.teams)):
            print("Team number:", i+1)
            self.teams[i].show_team_info()
            
    def make_random_teams(self):

        temp_players_list = copy.deepcopy(self.players)

        print("Choosing from players:")

        for i in range(len(temp_players_list)):
            print(temp_players_list[i].name)

        print("\n")

        while temp_players_list != list():

            for i in range(len(self.teams)):

                pick_player = random.sample(temp_players_list, 1)
                print("Random player:", pick_player[0].name, "goes to team", i+1)
                self.teams[i].players.append(pick_player[0])
                temp_players_list.remove(pick_player[0])

                if temp_players_list == list():
                    print("\n")
                    break

        for i in range(len(self.teams)):
            print("Team", int(self.teams[i].team_id)+1, "players:")
            for j in range(len(self.teams[i].players)):
                print(self.teams[i].players[j].name)
            print("\n")

        print("\n")

        
    def play(self):

        print("Let's play Flunky!")

        """Initializing game"""
        
        for i in range(len(self.teams)):
            self.teams[i].reset()

        self.rounds = 1
        self.turns = 1
            
        players_in_game = 0

        for i in range(len(self.teams)):
            players_in_game += len(self.teams[i].players)

        print("Players in game:", players_in_game)

        
        print("Match between teams:")

        self.show_teams_info()


        """game under dev"""

        empty = 1

        i = 0

        while empty != 0:
            print("Game round:", self.rounds)
            for j in range(len(self.teams)):
                print(i)
                print("Team", j+1, "turn")
                try:


                    #for x in range(len(self.teams[j].players)):
                     #   team_penalties += self.teams[j].players[x].game_penalties             

                    #if team_penalties != 0:
                    #    print("Player from this team has a penalty!")
                    #else:
                    #    print("Non of players of the team have a penalty.")


                    print("Player turn:", self.teams[j].players[i].name)

                    if self.teams[j].players[i].game_empty == 1:
                        print("Player bottle not empty!")         
                    
                    
                    empty = int(input("Empty?"))
                    if empty == 0:
                        print("Empty! (game over)")
                        break

                    else:
                        print("No empty!")
                        pass
                        

                except IndexError:
                    print("All")
                    
                    self.rounds += 1
                    i = -1
                    break
                    
            i += 1



