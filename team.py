class Team:
    
    team_id = 0
    name = "default_team_name"
    players = []
    game_allEmpty = len(players)
    game_team_hits = 0,
    game_team_hat_tricks = 0,

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



