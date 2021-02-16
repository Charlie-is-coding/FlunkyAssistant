class Team:
    
    team_id = 0
    name = "default_team_name"
    players = []
    game_allEmpty = 0
    game_team_hits = 0
    game_team_hat_tricks = 0
    game_penalties = 0

    def __init__(self, i):
       self.team_id = i
       self.players = []
    
    def __str__(self):
        print("Team ID:", self.id)
        print("Team name:", self.name)
        print("Players:", self.players)
        return str(self.id)

    def change_team_name(self, name):
        self.name = name
        return

    def change_id(self, team_id):
        self.team_id = team_id
        return

    def change_players_order(self):
        pass

    def count_empty(self):
        for i in range(len(self.players)):
            self.game_allEmpty += self.players[i].game_empty
        return self.game_allEmpty

    def reset(self):
        for i in range(len(self.players)):
            self.players[i].game_empty = 1
            
        self.game_allEmpty = self.count_empty()
        self.game_team_hits = 0
        self.game_team_hat_tricks = 0
        self.game_penalties = 0
        return

    def show_team_info(self):
        print("Team id:", self.team_id)
        print("Team name:", self.name)
        print("Bottles to empty:", self.game_allEmpty)
        print("Players:")
        for j in range(len(self.players)):
            print(j+1, self.players[j].name)
        print("\n")
        return
