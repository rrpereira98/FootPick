import json
import random
import itertools

choice1 = ""
choice2 = ""

#save the json file with teams and ratings as "data"
with open("data.json", "r") as json_file:
    data = json.load(json_file)

def teams_picker():
    #pick a random team, if team rating is below 81 pick random team again to have a bit less games between low rating teams
    choice1 = team, rating = random.choice(list(data.items()))
    if int(choice1[1]) < 81:
        choice1 = team, rating = random.choice(list(data.items()))
    print(choice1[0], choice1[1])

    #pick the other random team but this time in smaler dictionaries to have fair games, 83+ teams only play with 83+ teams
    if int(choice1[1]) >= 83:
        table1 = dict(itertools.islice(data.items(), 11))
        choice2 = team, rating = random.choice(list(table1.items()))
        if choice2 == choice1:
            while choice2 == choice1:
                choice2 = team, rating = random.choice(list(table1.items()))
        print(choice2[0], choice2[1])
    
    else:
        table2 = dict(itertools.islice(data.items(), 11, 43))
        choice2 = team, rating = random.choice(list(table2.items()))
        if choice2 == choice1:
            while choice2 == choice1:
                choice2 = team, rating = random.choice(list(table2.items()))
        print(choice2[0], choice2[1])

    return choice1, choice2
    
teams_picker()