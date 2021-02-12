from team import Team

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


"""Below is just copied from previous version - still under developement"""

"""
#loading players to game from JSON file
    
    def load_player(ID=1):

        for i in range(len(players)):
            if players[i]["ID"] == ID:
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
                   players.append(player)
                   appended = True

        if appended:
            print("Player with ID:", ID, "added to the game.")
            print("\n")
        else:
            print("Player with ID:", ID, "not found.")
            print("\n")

#players list
            
    def list_players():
        print(players)

#make teams (random)
"""
        
