"""Flunky Assistant"""

"""This is a new version of FlunkyFun game.
    As the previous version has some functionality, which
    this version does not yet have, both versions are still available,
    but please mind, that only this version will be developed."""


"""Flunky Assistant - real-life Flunky game assistant"""

from game import Game
from team import Team
from player import Player


""" For auto-mode (game simulation for testing purpouse)"""

def auto():

    print("Auto mode activated", "\n")

    print("Auto making new game instance:")

    game = Game()
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
    
    print("Auto adding new player instance:")

    player1 = Player()
    print(player1)

    print("\n")

    print("Auto changing name and id:")

    player1.name = "Charlie"
    player1.id = "000000420"
    print(player1.name)
    print(player1.id)

    print("Auto adding more players:")
    player2 = Player()
    player2.name = "Lyubitshka"
    player2.id = "000000001"
    player3 = Player()
    player3.name = "Igor '2020 master'"
    player3.id = "000000002"

    
    print("\n")

    print("Auto adding player to teams:")

    game.teams[0].players.append(player1)
    game.teams[1].players.append(player2)
    game.teams[0].players.append(player3)

    print("\n")

    print("Showing teams info:")
    print("\n")
    for i in range(len(game.teams)):
        print("Team", i,":")
        print("Team name:", game.teams[i].name)
        print("Players:")
        for j in range(len(game.teams[i].players)):
            print(j+1, game.teams[i].players[j].name)
        print("\n")



auto()
