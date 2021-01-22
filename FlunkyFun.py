""" Flunky Fun
a.k.a. Flunky Spirit a.k.a. Flappka
A flunky game assistant"""


import random
import json
import pprint
import copy

"""
player = [
    {"ID": "000000001"},
    {"Name": "Name"},
    {"Games played": 0},
    {"Game won": 0},
    {"Games lost": 0},
    {"Average hits per game": 0},
    {"Hat tricks": 0},
    {"Penalties given": 0},
    {"Penalties taken": 0},
    {"Rewinds": 0},
    {"'I was so thirsty' achievement": 0},
    {"Bottle behind enemy lines": 0}
    ]
"""

"""Creating "players.json" file."""

"""with open("players.json", "r", encoding="UTF-8") as file:
    for lines in file:
        print(line)
"""


players = []


def add_player(ID, name):

    with open("players.json", "r", encoding="UTF-8") as file:

        for lines in file:
            player = json.loads(lines)
            if player[0]["ID"] == ID:
                print("Player with ID:", ID, "already registered")
                return

        player = [
            {"ID": ID},
            {"Name": name},
            {"Games played": 0},
            {"Game won": 0},
            {"Games lost": 0},
            {"Average hits per game": 0},
            {"Hat tricks": 0},
            {"Penalties given": 0},
            {"Penalties taken": 0},
            {"Rewinds": 0},
            {"'I was so thirsty' achievement": 0},
            {"Bottle behind enemy lines": 0}
        ]

        with open("players.json", "a", encoding="UTF-8") as file:
            file.write(json.dumps(player))
            file.write("\n")


def load_player(ID=1):
    with open("players.json", "r", encoding="UTF-8") as file:
        for lines in file:
            player = json.loads(lines)

            for i in range(len(players)):
                if player[0]["ID"] == players[i][0]["ID"]:
                    print("Player already in game")
                    break
            else:
                if player[0]["ID"] == ID:
                    print("Player found")
                    players.append(player)

                else:
                    print("Player not found")
                    break


def auto_load():
    load_player("000000001")
    load_player("000000002")
    load_player("000000003")
    load_player("000000004")
    load_player("000000005")
    load_player("000000006")


def list_players():
    print(players)


team1 = set()
team2 = set()


def make_teams():

    global team1
    global team2
    team1 = list()
    team2 = list()

    temp_players_list = copy.deepcopy(players)

    print("Choosing from players:")
    for i in range(len(temp_players_list)):
        print(temp_players_list[i][1])

    while temp_players_list != list():

        pick_player = random.sample(temp_players_list, 1)
        print("Random player:", pick_player[0][1]["Name"], "goes to team1")

        team1.append(pick_player)
        temp_players_list.remove(pick_player[0])

        if temp_players_list == list():
            break
        pick_player = random.sample(temp_players_list, 1)
        print("Random player", pick_player[0][1]["Name"], "goes to team2")

        team2.append(pick_player)
        temp_players_list.remove(pick_player[0])

        # print(temp_players_list)

    print("Team 1:")
    for i in range(len(team1)):
        print(team1[i][0][1]["Name"])
    print("\n")

    print("Team 2:")
    for i in range(len(team2)):
        print(team2[i][0][1]["Name"])


def change_order(team, number=1):

    team_copy = copy.deepcopy(team)
    team_temp = list()

    print("Change order of team.", number)
    print("Players availble:", len(team), "from:")
    for i in range(len(team)):
        print(team[i][0])

    i = 0
    team_players = len(team)

    while i < team_players:
        print(i)
        print("Give", (i+1), "player name:")
        player = input("Set player:")

        for j in range(len(team)):

            if player in team[j][0][1]["Name"]:
                print("Player found")
                team_temp.append(team[j])
                team_copy.remove(team[j])
                i += 1

            else:
                print("Wrong name")
    # does not work!
    team = team_temp
    return team


game = {
    "ID": 0,
    "Players": list(),
    "Rounds": [0, ],
    "Turns": [0, ],
}


def play(game):

    print("Let's play flunky!")
    print("Match between:")
    print("Team 1:", team1)
    print("and")
    print("Team 2:", team2)
    print("BEGIN!")

    game["Players"].append(team1)
    game["Players"].append(team2)

    print("Game info:", game)

    empty = 1
    all_empty1 = len(team1)
    all_empty2 = len(team2)
    game_turn = 1
    game_round = 1

    while all_empty1 or allempty2 != 0:

        game["Rounds"].append(game_round)
        print("Round", game["Rounds"][-1])

        while empty != 0:

            game["Turns"].append(game_turn)

            print("Turn:", game_turn)

            hit = input("Hit?  ( y / n )")
            if hit == "y":
                print("Congrats")
                bottle_empty = input("Player bottle empty?")
                if bottle_empty == "y":
                    all_empty1 -= 1

            if hit == "n":
                print("Too bad...")

            penalty = input("Was a penalty? ( y / n )")

            while penalty == "y":
                # give_penalty()
                penalty_player = input("Type penalty player name?")
                if penalty_player in players:
                    print("Player", penalty_player, "will receive penalty")

                else:
                    print("Player not found")

            if penalty == "n":
                print("Ok, no penalty. Clean shot...")

            proceed = input("Ok to proceed? (y/n)")

            if proceed == "y":
                turn += 1
            if proceed == "n":
                print("Come on, what the heck?. (Proceed anyway)")
                turn += 1

    print("Game over")
    print("Turns:", game["Turns"][-1])


print("Welcome to the Flunky_Fun game")


def auto():
    auto_load()
    make_teams()
