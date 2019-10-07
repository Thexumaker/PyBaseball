from Models import League
from Models.backend import baseball
from Models.backend import endpoints

class Sport(object):
    def __init__(self,rData,years):
        paths = rData.get('sports')[0]
        self.id = paths.get('id')
        self.code = paths.get('code')
        self.link = paths.get('link')
        self.name = paths.get('name')
        self.abbreviation = paths.get('abbreviation')
        self.sortOrder = paths.get('sortOrder')
        self.years = years
        self.teams = self.setTeams()
        self.playerList = self.setPlayerList()
        self.leagues = self.setLeagues()
        self.playersRawData = self.setRawplayerData()
    def setRawplayerData(self,season = [2019]):
        for y in season:

            players = baseball.get('sports_players', {'ver': 'v1', 'season': y, 'sportId': self.id })

        return players

    def setPlayerList(self, season = [2019]):
        players = baseball.get('sports_players', {'ver': 'v1', 'season': season, 'sportId': self.id })

        """Returns a list of all active players within a sport and list of years
        Default is mlb and 2019"""
        pL= {}
        for y in season:
            players = baseball.get('sports_players', {'ver': 'v1', 'season': y, 'sportId': self.id })
            for dict in players.get('people'):

                for k,v in dict.items():

                    if k == 'id':
                        id = v
                    elif k == 'firstName':
                        first_name = v
                    elif k == 'lastName':
                        if "'" in v:
                            v = v.replace("'", '')

                        last_Name = v
                pL["{} {}".format(first_name, last_Name)] = id
        return pL
                #We could create a giant database of player objects instead of just a list?
    def setLeagues(self):
        rL = []
        leagues = baseball.get('league', {'ver': 'v1'})
        for l in leagues.get('leagues'):
            if l.get('sport') != None:
                if l.get('sport')['id'] == 1:
                    l = League.League(l)
                    rL.append(l)
        return rL
    def setTeams(self):
        teams = baseball.get('teams', {'ver' : 'v1', 'sportIds': self.id})
        return teams
