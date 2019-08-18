from datetime import datetime
import requests
import constants
import paths
PATHS = paths.PATHS
d = {}
players = {}
# If teamids is empty get all teams with their ids


def getTeamIds():

    with open("TeamID.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
# def setTeamIds():
# If playerids is empty write all players with their ids


def setPlayerList():
    for id in d:
        roster = requests.get(constants.BASE_URL +
                              "teams/{}/roster".format(id)).json()['roster']
        for i in roster:
            name = i['person']['fullName']
            id = i['person']['id']
            players[name] = id
    f = open("playerID.txt", "w")
    for player in players:
        result = "{}:{}\n".format(player, players[player])
        f.write(result)
    f.close()


def getPlayerList():
    with open("playerID.txt") as f:
        for line in f:
            (key, val) = line.split(":")
            players[key] = int(val)
# return whatever the user wants
# More or less works


def getPlayer(name, args):
    """A function to return the age, position and player id of a given player name"""
    r = []
    ids = players[name]
    r_url = get('people', {'personIds':ids, 'ver': 'v1'})
    #constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(r_url["people"][0][arg])
    return r



def getInfo(name):
    r = []
    args = ["currentAge", "primaryPosition", "id"]
    ids = players[name]
    r_url = constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(requests.get(r_url).json()["people"][0][arg])
    return r


def get(path, dict_params):
    """Main get function that given a dictionary of inputs and a path will return the correct results
    Example:
    get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'})"""
    curr = PATHS.get(path)
    url = curr['url']
    path_params = {}
    query_params = {}
    # search through the dictionary of params, categorize what kind of parameter, make sure they exist and then replace them in the url
    for k, v in dict_params.items():
        if curr['path_params'].get(k):
            path_params.update({k: str(v)})
            print(path_params)
        elif k in curr['query_params']:
            query_params.update({k: str(v)})
            print(query_params)
        else:
            break
    for s, t in path_params.items():

        url = url.replace("{{{}}}".format(s), t)
    print("broke here")
    while url.find('{') != -1:
        #so if u put in the wrong shit it repeats endlessly
        print(url)
        start_index = url.find('{')

        end_index = url.find('}')
        param = url[start_index:end_index + 1]
        print(url)

        param_without_brackets = url[start_index + 1:end_index]
        if param_without_brackets not in curr['required_params']:
            url = url.replace("/" + param, '')

        elif param_without_brackets in curr['required_params']:
            # doesn't work
            break

    if len(query_params) > 0:
        print("QUCDWVCEVCWVW")

        for k, v in query_params.items():
            sep = '?' if url.find('?') == -1 else '&'
            url += sep + k + "=" + v
    # Make sure required parameters are present
    print(url)
    satisfied = False
    missing_params = []
    for x in curr.get('required_params', []):
        if len(x) == 0:
            satisfied = True
        else:
            for i in x:
                if path_params.get(i) or query_params.get(i):

                    break
                else:
                    satisfied = False

            if len(missing_params) == 0:

                satisfied = True
                break
    if satisfied is False:
        return "Broken"

    r = requests.get(url)
    print(r)
    return r.json()


getTeamIds()

getPlayerList()
print(len(players))
# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())

#`print(getInfo("Matt Chapman"))
print(getPlayer("Matt Chapman",["currentAge", "primaryPosition"]))
#print(get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'}))

#print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())
print("okkkk")
print(getInfo("Matt Chapman"))
