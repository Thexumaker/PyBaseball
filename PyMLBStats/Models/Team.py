from Models.backend import baseball
from Models import Person
class Team(object):
    def __init__(self, rData):
        rData = rData.get('teams')[0]
        print(rData)
        self.rData = rData
        self.name = rData.get('name')
        self.id = rData.get('id')
        self.abbreviation = rData.get('abbreviation')
        self.teamName = rData.get('teamName')
        self.teamCode = rData.get('teamCode')
        # self.division
        self.roster = self.setRoster()
        # self.sport
        # self.coaches
        # self.minorLeague
        # self.league
    def setRoster(self):
        rData = baseball.get('team_roster', {'ver': 'v1', 'teamId': self.id})
        #fix later
        return rData
