import requests
import constants
from datetime import datetime, date
import paths

PATHS = paths.PATHS

#print(requests.get("https://statsapi.mlb.com/api/v1/awards/MLBHOF/recipients").json())
path = 'person'
curr = PATHS.get(path)
url = 'fehjsbfhejsbhfjes'
print(curr.get('path_params').get('ver')['default'])
url.replace('fehj', 'dickckckckckc')
print(url)

sql_command = """CREATE TABLE contacts (
    playerId INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL);"""

crsr.execute(sql_command)
