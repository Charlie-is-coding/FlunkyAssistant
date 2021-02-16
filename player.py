class Player:

    player_id = 0
    name = "default"
    games_played = 0
    games_won = 0
    games_lost = 0
    average_hits_per_game = 0
    hat_tricks = 0
    penalties_given = 0
    penalties_taken = 0
    rewinds = 0
    i_was_so_thirsty = 0
    behind_enemy_lines = 0
    game_empty = 1
    game_penalites = 0
    game_i_was_so_thisty = 0


    def __init__(self):
        pass

    
    def __str__(self):
        print("ID:", self.player_id)
        print("Name:", self.name)
        print("Games won:", self.games_won)
        print("Games lost:", self.games_lost)
        print("Average hits per game:", self.average_hits_per_game)
        print("Hat tricks:", self.hat_tricks)
        print("Penalties given:", self.penalties_given)
        print("Penalties taken:", self.penalties_taken)
        print("Rewinds:", self.rewinds)
        print("I was so thirsty achivment:", self.i_was_so_thirsty)
        print("Bottle behind enemy lines:", self.behind_enemy_lines)
        
        return str(self.player_id)
    
