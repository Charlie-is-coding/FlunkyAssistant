"""For now this is mentioned to work with players database in local JSON file"""

"""Later will be connected to PostgeSQL database"""

import json

def register_new_player(ID, name):

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

def create_new_json_file_database():
    #name of file changed to players2.json to avoid overwrite
    with open("players2.json", "w+", encoding="UTF-8") as file:
        return



    
