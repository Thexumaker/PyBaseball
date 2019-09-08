from Models.backend import baseball
from Models import Person
class League(object):
    def __init__(self, rData):
        self.rData = rData
        self.name = rData.get('name')
        self.abbreviation = rData.get('abbreviation')
        self.numTeams = rData.get('numTeams')
        self.teams
