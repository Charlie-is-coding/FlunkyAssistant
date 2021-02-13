"""Flunky Assistant"""

""" This is a new version of FlunkyFun game.
    As the previous version had some functionality, which
    this version does not yet have, both versions are still available,
    but please mind, that only this version will be developed.
    
    The game is made for users registered in a database storing users stats.
    For now this is made in a local 'simulation of a database' in JSON file.
    Some 'database' functionality given at the bottom of the file"""


"""Flunky Assistant - real-life Flunky game assistant"""

from game import Game
from team import Team
from player import Player
import database


""" For auto-mode (game simulation for testing purpouse)"""

game = Game()

def auto():

    print("Auto mode activated", "\n")

    print("Initial game info:")
    print(game)

    print("Auto making teams (2):")
    game.make_teams(2)

    print("Teams made:", len(game.teams), "\n")

    print("Auto changing teams names:")

    print("Team id:", game.teams[0].team_id)
    game.teams[0].change_team_name("This is name of team number one!")
    print("Team name:", game.teams[0].name)

    print("Team id:", game.teams[1].team_id)
    game.teams[1].change_team_name("It's team number 2!")
    print("Team name:", game.teams[1].name)

    print("\n")

    print("Auto loading players from database in JSON file...")
    game.load_player_from_json_file("000000001")
    game.load_player_from_json_file("000000002")
    game.load_player_from_json_file("000000003")
    game.load_player_from_json_file("000000004")
    game.load_player_from_json_file("000000005")
    game.load_player_from_json_file("000000006")
    game.load_player_from_json_file("000000007")
    game.load_player_from_json_file("000000420")

    print("Players added:", len(game.players))

    print("Players names:")
    for i in range(len(game.players)):
        print(game.players[i].name)

    print("\n")

    print("Auto adding players to teams...")

    game.teams[0].players.append(game.players[0])
    game.teams[1].players.append(game.players[1])
    game.teams[0].players.append(game.players[2])
    game.teams[1].players.append(game.players[3])
    game.teams[1].players.append(game.players[4])
    game.teams[0].players.append(game.players[5])
    game.teams[1].players.append(game.players[6])
    game.teams[0].players.append(game.players[7])

    print("\n")

    print("Showing teams info:")
    print("\n")
    for i in range(len(game.teams)):
        print("Team id", i,":")
        print("Team name:", game.teams[i].name)
        print("Players:")
        for j in range(len(game.teams[i].players)):
            print(j+1, game.teams[i].players[j].name)
        print("\n")
    

    return game


auto()


"""Adding a new user to the JSON file database (players.json)"""

#database.register_new_player("000000001", "Lyubitshka")
#database.register_new_player("000000002", "Ola")
#database.register_new_player("000000003", "bJusta")
#database.register_new_player("000000004", "Aris")
#database.register_new_player("000000005", "Miauga")
#database.register_new_player("000000006", "GZB")
#database.register_new_player("000000420", "Charlie")
#database.register_new_player("000000007", "Test user")

"""Creating a new players.json file (handle with care!)"""

#database.create_new_json_file_database()








