from team import Team
from player import Player
import json

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
    
    def play():
        pass

    def load_player_from_json_file(self, ID=1): 

        for i in range(len(self.players)):
            if self.players[i].id == ID:
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
                   temp_player.id = player["ID"]
                   temp_player.name = player["Name"]
                   self.players.append(temp_player)
                   appended = True

        if appended:
            print("Player with ID:", ID, "added to the game.")
            print("\n")

        else:
            print("Player with ID:", ID, "not found.")
            print("\n")

