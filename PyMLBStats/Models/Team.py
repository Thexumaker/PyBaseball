from Models.backend import baseball
from Models import Person
from datetime import datetime, date
currentDate = date.today()
today = currentDate.strftime('%m/%d/%Y')
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
    def latestGamePack(self,date = today):
        """Returns latest game pack number for a specified team
        >>>latestGamePack(117)
        565664
        """
        lgr= baseballs.get('schedule', {'ver':'v1', 'sportId':1, 'date':date, 'teamId':self.id, 'fields':['dates','games','gamePk'] })
        return lgr['dates'][0]['games'][0]['gamePk']
