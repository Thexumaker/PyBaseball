import requests
import constants
from datetime import datetime, date
#print(requests.get("https://statsapi.mlb.com/api/v1/awards/MLBHOF/recipients").json())
dick = 69
stuff = [['id','id2','id3'], ['is'], ['stuff']]
query_params = {'teamIds': '119', 'dick': 'dics'}
print(query_params.get('dicks', False))
a = []
for x in stuff:
    print("this is x:")
    print(x)
    print("/n")
    a.extend([a for a in x if a not in query_params])
    print(a)

currentDate = date.today()

today = currentDate.strftime('%m/%d/%Y')
print(today)
