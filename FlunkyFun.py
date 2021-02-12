""" Flunky Fun
a.k.a. Flunky Spirit a.k.a. Flappka
A flunky game assistant"""


import random
import json
import pprint
import copy

"""
player = {
    "ID": "000000001",
    "Name": "Name",
    "Games played": 0,
    "Game won": 0,
    "Games lost": 0,
    "Average hits per game": 0,
    "Hat tricks": 0,
    "Penalties given": 0,
    "Penalties taken": 0,
    "Rewinds": 0,
    "'I was so thirsty' achievement": 0,
    "Bottle behind enemy lines": 0
    }
"""


"""Creating "players.json" file."""

"""with open("players.json", "r", encoding="UTF-8") as file:
    for lines in file:
        print(line)
"""




"""Adding new players to JSON file"""

def add_player(ID, name):

    with open("players.json", "r", encoding="UTF-8") as file:

        for lines in file:
            player = json.loads(lines)
            if player["ID"] == ID:
                print("Player with ID:", ID, "already registered")
                return

        player = {
            "ID": ID,
            "Name": name,
            "Games played": 0,
            "Games won": 0,
            "Games lost": 0,
            "Average hits per game": 0,
            "Hat tricks": 0,
            "Penalties given": 0,
            "Penalties taken": 0,
            "Rewinds": 0,
            "'I was so thirsty' achievement": 0,
            "Bottle behind enemy lines": 0
        }

        with open("players.json", "a", encoding="UTF-8") as file:
            file.write(json.dumps(player))
            file.write("\n")


def auto_add_player():

    add_player("000000001", "Lyubitshka")
    add_player("000000002", "Miauga")
    add_player("000000002", "Miauga")
    add_player("000000003", "bJusta")
    add_player("000000004", "Aris")
    add_player("000000005", "Gzb")
    add_player("000000006", "Ola")
    add_player("000000007", "Kuba")
    add_player("000000420", "Charlie")


players = []


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
                

def auto_load():
    load_player("000000001")
    load_player("000000100")
    load_player("000000002")
    load_player("000000003")
    load_player("000000004")
    load_player("000000005")
    load_player("000000006")
    load_player("000000006")
    load_player("000000006")
    load_player("000000420")


def list_players():
    print(players)


"""team = {
    "ID": 0,
    "players" = list(),
    "allEmpty" = 0,
    "teamHits" = 0,
    "teamHatTricks = 0,
    } 
"""

teams = []


def make_teams(howMany):
    for i in range(howMany):
        team = {
            "ID": i,
            "name": "No name",
            "players": list(),
            "allEmpty": 0,
            "teamHits": 0,
            "teamHatTricks": 0,
        }

        teams.append(team)
    print("Teams made", len(teams))

def change_team_name(teamID):

    for i in range(len(teams)):
        if teams[i]["ID"] == int(teamID):
            print("Change name of team ", i + 1)
            teams[i]["name"] = input("Type team name: ")
            break
    else:
        return
        

def random_teams():

    temp_players_list = copy.deepcopy(players)

    print("Choosing from players:")

    for i in range(len(temp_players_list)):
        print(temp_players_list[i]["Name"])

    print("\n")
    while temp_players_list != list():

        for i in range(len(teams)):

            pick_player = random.sample(temp_players_list, 1)
            print("Random player:", pick_player[0]["Name"], "goes to team", i+1)
            teams[i]["players"].append(pick_player)
            temp_players_list.remove(pick_player[0])

            if temp_players_list == list():
                print("\n")
                break

    for i in range(len(teams)):
        print("Team", int(teams[i]["ID"])+1, "players:")
        for j in range(len(teams[i]["players"])):
            print(teams[i]["players"][j][0]["Name"])
        print("\n")

    print("\n")



game = {
    "ID": 0,
    "Teams": teams,
    "Rounds": [0, ],
    "Turns": 0,
}


"""under dev"""


def play(game):

    print("Let's play flunky!")
    print("Match between:")
    
    for i in range(len(teams)):
        print("Team name:", teams[i]["name"])
        print("Team number:", int(teams[i]["ID"])+1,)
        teams[i]["allEmpty"] = len(teams[i]["players"])
        print("Bottles to empty:", teams[i]["allEmpty"])
        print("Team hits:", teams[i]["teamHits"])
        print("Team hat tricks", teams[i]["teamHatTricks"])
        print("Players:")
        for j in range(len(teams[i]["players"])):
            print(teams[i]["players"][j][0]["Name"])
        print("\n")


    #print("Game info:", game)

    gameRound = 0
    gameTurn = 0

    
    while int(teams[0]["allEmpty"]) > 0 and int(teams[1]["allEmpty"]) > 0:
        

        gameRound += 1

        game["Rounds"].append(gameRound)
        print("Round:", game["Rounds"][-1])
        #print("Turn:", gameTurn)
        game["Turns"] = 0

        a = len(teams[0]["players"])
        b = len(teams[1]["players"])
        c = 0
        
        if a > b:
            c = a
        else:
            c = b
        
        for j in range(c):
            #print(j)
            for i in range(len(teams)):
                
                try:
                    teams[i]["players"][j][0]["Name"] !=0
                    gameTurn += 1
                    game["Turns"] += 1
                    print("Game turn", gameTurn)
                    print("Now playing team:", i + 1)
                    print("Player turn:",teams[i]["players"][j][0]["Name"] )
                   
                    hit = input("Hit?  ( y / n )")

                    if hit == "y":
                        print("Congrats")
                        bottle_empty = input("Player bottle empty?")
                        if bottle_empty == "y":
                            teams[i]["allEmpty"] -= 1
                            print("Bottles left to empty:", teams[i]["allEmpty"])
                            if teams[i]["allEmpty"] == 0:
                                print("All empty!!!")
                                           
                        elif bottle_empty == "n":
                            print("Ok, bottle not empty yet. Drink faster!")
                
                    elif hit == "n":
                        print("Too bad...")

                    
                    penalty = input("Was a penalty? ( y / n )")

                    if penalty == "n":
                        print("Ok, no penalty.")

                    elif penalty == "y":
                        while penalty == "y":
                

                            penalty_player = input("Type penalty player name: ")

                            for i in range(len(players)):
                                if penalty_player == players[i]["Name"]:
                                    print("found")
                                    print("Player", penalty_player, "will receive penalty")
                                    players[i]["Penalties taken"] += 1
                                    print(players[i]["Penalties taken"])
                                    penalty = input("Someone else got a penalty? ( y / n )")
                                    break

                                else:
                                    print("Player not found")

                    proceed = input("Ok to proceed? (y/n)")

                    if proceed == "y":
                        pass
                    if proceed == "n":
                        print("Come on, what the heck?. (Proceed anyway)")
                        pass


                except IndexError:
                    break
        
                 
    print("Game over")
    print("Turns:", game["Turns"])


print("Welcome to the Flunky_Fun game")


def auto():
    print("\n", "Processing auto_load - loading players to the programm", "\n")
    auto_load()
    print("\n", "Auto making teams (2)", "\n")
    make_teams(2)
    print("\n", "Auto picking players to teams", "\n")
    random_teams()
    change_team_name(0)
    change_team_name(1)

    pprint.pprint(teams)
    print("\n")
    print("Type 'play(game)' to test")
    print("Auto starting game...", "\n")
    play(game)

auto()
