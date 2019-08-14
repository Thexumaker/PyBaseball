import requests
from datetime import datetime

import requests
import constants
d = {}
players = {}
##If teamids is empty get all teams with their ids
def getTeamIds():
    with open("TeamID.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
#def setTeamIds():
#If playerids is empty write all players with their ids
def setPlayerList():
    for id in d:
        roster = requests.get(constants.BASE_URL + "teams/{}/roster".format(id)).json()['roster']
        for i in roster:
            name = i['person']['fullName']
            id = i['person']['id']
            players[name] = id
    f = open("playerID.txt", "w")
    for player in players:
        result = "{}:{}\n".format(player,players[player])
        f.write(result)
    f.close()
def getPlayerList():
    with open("playerID.txt") as f:
        for line in f:
            (key, val) = line.split(":")
            players[key] = int(val)
#return whatever the user wants
#More or less works
def getPlayer(name, *args):
    r = []
    ids = players[name]
    r_url = constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(requests.get(r_url).json()["people"][0][arg])
    return r
#Get basic info which is age, position and player id
def getInfo(name):
    r = []
    args = ["currentAge", "primaryPosition", "id"]
    ids = players[name]
    r_url = constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(requests.get(r_url).json()["people"][0][arg])
    return r

getTeamIds()

getPlayerList()
print(len(players))
#print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())

print(getInfo("Matt Chapman"))
