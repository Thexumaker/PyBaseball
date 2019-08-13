import statsapi
import requests
today = statsapi.schedule()
endpoint = 'http://lookup-service-prod.mlb.com'
response = requests.get(endpoint)
#print('The A\'s won %s games in 2018.' % sum(1 for x in statsapi.schedule(team=133,start_date='01/01/2018',end_date='12/31/2018') if x.get('winning_pitcher','')=='Blake Treinen'))
#print(statsapi.get('attendance', {'teamId':143, 'leagueId': 104, 'leagueListid':104}))
print(requests.get("http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='chapman%25'").json()['search_player_all']['queryResults']['row'][1])
