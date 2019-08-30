
import requests
import constants
import paths
from datetime import datetime, date
from matplotlib.pylab import plt #load plot library
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
import numpy as np
import sqlite3
import string
import pandas as pd
import StrikeZone

PATHS = paths.PATHS


d = {}
playerList = {}

# If teamids is empty get all teams with their ids
currentDate = date.today()

today = currentDate.strftime('%m/%d/%Y')
connection = sqlite3.connect("Players.db")
crsr = connection.cursor()




""" Lets say i want to get spinrate i'm gonna have to go game by game thru hydrations and calculate"""
def setPlayerList(sport = 1, season = [2019]):
    """Returns a list of all active players within a sport and list of years
    Default is mlb and 2019"""

    for y in season:
        players = get('sports_players', {'ver': 'v1', 'season': y, 'sportId': sport })

        for dict in players.get('people'):
            print(dict)
            for k,v in dict.items():

                if k == 'id':
                    id = v
                elif k == 'firstName':
                    first_name = v
                elif k == 'lastName':
                    if "'" in v:
                        v = v.replace("'", '')

                    last_Name = v
            playerList[id] = [first_name, last_Name]
            sql_command = """INSERT INTO contacts VALUES ({},'{}', '{}');""".format(id,first_name,last_Name)
            print(sql_command)
            crsr.execute(sql_command)
    # If we skip this, nothing will be saved in the database.
    connection.commit()

    # close the connection
    connection.close()
    return playerList



def getInfo(name):
    r = []
    args = ["currentAge", "primaryPosition", "id"]
    ids = players[name]
    r_url = constants.BASE_URL + "/people/{}".format(ids)
    for arg in args:
        r.append(requests.get(r_url).json()["people"][0][arg])
    return r
# Stuff good



def boxscore():
    """ Generate boxscore"""
def linescore():
    """Generate linescore"""
def hotColdZones(playerID, group = 'hitting'):
    #find his current team and if he's a hitter or pitcher then
    """Not sure if this only works for current year or if i can get year by year data
    This should only be his batting averages, etc and then give a hot/cold color
    Versus say advancedstats i can get every single pitch and then add it to the strikezone map? but they should be seperate data
    Also the graphs shouldnt be returned as its a visual tool, maybe they could be saved but for data science purposes it should be returning a list or dictionary of results """
    zoneData = get('person',{ 'ver':'v1' , 'personId':playerID,'hydrate':['stats(group={},type={})'.format(group,'hotColdZones'),'currentTeam']})
    zonesData = {}
    for stat in zoneData.get('people')[0].get('stats'):
        for types in stat.get('splits'):
            zonesData[types.get('stat')['name']] = types.get('stat')['zones']
            #create a list of Zones, up to 9
            #using that list of zones make a strike zone
            #make a list of strike zone data for each value
    return zonesData

def vStrikeZoneData(data):
    sz = StrikeZone.strikeZone('dick')
    zone = [1,2,3,4,5,6,7,8,9]
    zoneData = []
    for k,v in data.items():
        if k == 'sluggingPercentage':
            for i in v:

                if int(i.get('zone')) > 9:
                    break
                else:
                    zoneData.append(float(i.get('value')))

    sz.updateStrikeZone(zone,zoneData)
    sz.visualize()













def advancedStats():
    """Still not sure how to proceed however for spin rate and what stats to put in per player, also have to fix
    season stats"""


def GenerateWpaGraph(GamePck):
    """Returns a list of the homeTeam wPA and generates the Win probability graph of a specified game """
    game = get('game_winProbability', {'ver': 'v1','gamePk': GamePck})

    atbat = [0]
    home = 50

    homeL = [50]

    for item in game:
        for key, val in item.items():
            if key == 'atBatIndex':
                atbat.append(val)

            if key == 'homeTeamWinProbabilityAdded':

                home += val
                homeL.append(home)

    c = ['g' if a >= 50 else 'r' for a in homeL]
    lines = [((x0,y0), (x1,y1)) for x0, y0, x1, y1 in zip(atbat[:], homeL[:], atbat[1:], homeL[1:])]
    coloredLines = LineCollection(lines, colors = c, linewidths = (2,))
    fig,ax = plt.subplots(1)
    ax.add_collection(coloredLines)
    ax.autoscale_view()
    plt.show()
    return homeL

def seasonStats(personId,type = 'gameLog',group = 'hitting'):

    """Returns a player's season/career stats and wether it's hitting or pitching or fielding
        fix and improve this later"""

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
    print("Working through here")
    while url.find('{') != -1:
        # so if u put in the wrong shit it repeats endlessly
        print(url)
        start_index = url.find('{')
        end_index = url.find('}')
        param = url[start_index:end_index + 1]
        print(url)
        param_without_brackets = url[start_index + 1:end_index]
        if param_without_brackets in curr['required_params']:
            url = url.replace(param, curr.get('path_params').get(param_without_brackets)['default'])
        elif param_without_brackets not in curr['required_params']:
            url = url.replace("/" + param, '')


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



# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())

# `print(getInfo("Matt Chapman"))
#print(GenerateWpaGraph(567010))

# IMPORTNAT
#print(getPlayerInfo("Justin Verlander"))
#print(latestGamePack(133))

# END
#print(get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'}))

# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())
#print(getAttendance('133',{'season':2017}, 'dick'))
#setPlayerList()
print(vStrikeZoneData(hotColdZones(608369)))
