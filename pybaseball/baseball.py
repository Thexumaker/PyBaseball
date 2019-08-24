from datetime import datetime
import requests
import constants
import paths
PATHS = paths.PATHS
from datetime import datetime, date

d = {}
players = {}
# If teamids is empty get all teams with their ids
currentDate = date.today()

today = currentDate.strftime('%m/%d/%Y')

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


def getInfo(name):
    r = []
    args = ["currentAge", "primaryPosition", "id"]
    ids = players[name]
    r_url = constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(requests.get(r_url).json()["people"][0][arg])
    return r
# Stuff good


def seasonStats(personId,type,group):
    """"Returns a player's season/career stats and wether it's hitting or pitching or fielding"""

    #playerInfo = get('people', {'personIds':personId})


    teamStats = get('person',{ 'ver':'v1' , 'personId':personId,'hydrate':['stats(group={},type={})'.format(group,type),'currentTeam']})
    return teamStats
    #iterate of stats and find the right player id
    #career stats broken
    #fix the season :2019
    #make function to get team id

def latestGamePack(team):
    """Returns latest game pack number for a specified team
    >>>latestGamePack(117)
    565664
    """
    lgr= get('schedule', {'ver':'v1', 'sportId':1, 'date':today, 'teamId':team, 'fields':['dates','games','gamePk'] })
    return lgr['dates'][0]['games'][0]['gamePk']


def getAttendance(Id, params, fields):
    """Returns Attendance stats
    -Id Required: LeagueId, TeamId, LeagueListID
        - just one of them
    -params: 'season', 'gameType', 'startDate', 'endDate'
    -fields stills working on
    -ok
    """
    qP = {'ver': 'v1', 'teamId': Id}
    for k, v in params.items():
        qP.update({k: v})
    result = get('attendance', qP)
    return result


def getPlayerInfo(name):
    """A function to return the age, position and player id of a given player name"""
    r = []
    ids = players[name]
    r_url = get('people', {'personIds': ids,
                           'ver': 'v1'})
    #constants.BASE_URL + "/people/{}".format(ids)

    return r_url


def get(path, dict_params):
    """Main get function that given a dictionary of inputs and a path will return the correct results
    Example:
    get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'})"""
    curr = PATHS.get(path)
    url = curr['url']
    path_params = {}
    query_params = {}
    fields = []
    hydrations = []
    first_field = True
    print(dict_params)
    # search through the dictionary of params, categorize what kind of parameter, make sure they exist and then replace them in the url
    for k, v in dict_params.items():
        if curr['path_params'].get(k):
            path_params.update({k: str(v)})
            print(path_params)
        elif k in curr['query_params']:
            query_params.update({k: v})
            # DEBUG RIGHT HERe
        else:
            break
    print(query_params)
    for s, t in path_params.items():

        url = url.replace("{{{}}}".format(s), t)
    print("broke here")
    while url.find('{') != -1:
        # so if u put in the wrong shit it repeats endlessly
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
            url = url.replace(param, curr.get('path_params').get(param_without_brackets)['default'] )

    if len(query_params) > 0:
        for k, v in query_params.items():
            if k == 'fields' or k == 'hydrate':
                sep = '?' if url.find('?') == -1 else '&'
                url += sep + k + "="
                total = len(v)
                counter = 1
                for i in v:
                    sep = '%2c' if counter < total else ''
                    counter += 1
                    qurl = i + sep
                    url += qurl
            else:
                sep = '?' if url.find('?') == -1 else '&'
                v = str(v)
                url += sep + k + "=" + v
        # For if fields in the query

    # Make sure required parameters are present
    print(url)
    satisfied = False
    missing_params = []
    for x in curr.get('required_params', []):
        if len(x) == 0:
            break
        else:
            for i in x:
                if path_params.get(i) or query_params.get(i) or i in fields or i in hydrations:
                    satisfied=True
            if satisfied != True:
                missing_params.extend(x)


    if len(missing_params) != 0:
        return 'missing params {}'.format(missing_params)

    r = requests.get(url)
    if r.status_code not in [200,201]:
        return r.status_code
    else:
        return r.json()



getTeamIds()

getPlayerList()

# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())

# `print(getInfo("Matt Chapman"))

# IMPORTNAT
#print(getPlayerInfo("Justin Verlander"))
#print(latestGamePack(117))
print(seasonStats(543760,'season','hitting'))
# END
#print(get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'}))

# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())
#print(getAttendance('133',{'season':2017}, 'dick'))
