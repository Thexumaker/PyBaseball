import requests
import endpoints
from datetime import datetime, date
from matplotlib.pylab import plt #load plot library
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
import numpy as np
import sqlite3
import string
import pandas as pd

ENDPOINTS = endpoints.ENDPOINTS
d = {}
playerList = {}


def get(path, dict_params):
    """Main get function that given a dictionary of inputs and a path will return the correct results
    Example:
    get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'})"""
    curr = ENDPOINTS.get(path)
    url = curr['url']
    path_params = {}
    query_params = {}
    fields = []
    hydrations = []
    first_field = True


    # search through the dictionary of params, categorize what kind of parameter, make sure they exist and then replace them in the url
    for k, v in dict_params.items():

        if curr['path_params'].get(k):
            path_params.update({k: str(v)})

        elif k in curr['query_params']:
            query_params.update({k: v})
            # DEBUG RIGHT HERe
        else:
            break

    for s, t in path_params.items():
        url = url.replace("{{{}}}".format(s), t)

    while url.find('{') != -1:
        # so if u put in the wrong shit it repeats endlessly
        print(url)
        start_index = url.find('{')
        end_index = url.find('}')
        param = url[start_index:end_index + 1]
        print(url)
        param_without_brackets = url[start_index + 1:end_index]
        for i in curr['required_params']:
            if param_without_brackets in i:
                print('hi')
                url = url.replace(param, curr.get('path_params').get(param_without_brackets)['default'])
                path_params.update({param_without_brackets :curr.get('path_params').get(param_without_brackets)['default']})
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
#print(GenerateWpaGraph(567010))``

# IMPORTNAT
#print(getPlayerInfo("Justin Verlander"))
#print(latestGamePack(133))

# END
#print(get("config", {'ver': 'v1', 'baseballStats': 'baseballStats'}))

# print(requests.get("http://statsapi.mlb.com/api/v1/people/595014").json())
#print(getAttendance('133',{'season':2017}, 'dick'))
#setPlayerList()

#setPlayerList()
#print(getPlayerInfo('Marcus Semien'))
#help(getPlayerInfo)
#testSz = hotColdZones(608369,'hitting', 'onBasePlusSlugging')
#testSz.visualize()
#print(testSz.zoneData)
