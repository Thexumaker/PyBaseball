from Models.backend import baseball
from Models import StrikeZone
class Person(object):
    basicInfoPath = None
    def __init__(self, rData):
        basicInfoPath = rData.get('people')[0]
        self.id = basicInfoPath.get('id')
        self.fullName = basicInfoPath.get('fullName')
        self.firstName = basicInfoPath.get('firstName')
        self.lastName = basicInfoPath.get('lastName')
        self.birthDate = basicInfoPath.get('birthDate')
        self.currentAge = basicInfoPath.get('currentAge')
        self.birthCity = basicInfoPath.get('birthCity')
        self.birthStateProv = basicInfoPath.get('birthStateProv')
        self.birthCountry = basicInfoPath.get('birthCountry')
        self.weight = basicInfoPath.get('weight')
        self.height = basicInfoPath.get('height')

class Player(Person):
    def __init__(self, rData):
        super().__init__(rData)
        basicInfoPath = rData.get('people')[0]
        self.primaryNumber = basicInfoPath.get('primaryNumber')
        self.primaryPositionCode = basicInfoPath.get('primaryPosition')['code']
        self.primaryPositionName = basicInfoPath.get('primaryPosition')['name']
        self.primaryPositionType = basicInfoPath.get('primaryPosition')['type']
        self.primaryPositionAbbrev = basicInfoPath.get('primaryPosition')['abbreviation']
        self.active = basicInfoPath.get('active')
        self.draftYear = basicInfoPath.get('draftYear')
        self.batSideC = basicInfoPath.get('batSide')['code']
        self.batSideD = basicInfoPath.get('batSide')['description']

        self.strikeZone = None
        self.group = self.setGroup()
        self.team = self.setTeam()
    def setGroup(self):
        if self.primaryPositionAbbrev in ['SS', '3B', '2B','1B','C','CF','LF','RF']:
            r = 'hitting'
            return r
        else:
            r = 'pitching'
            self.group = r
    def setTeam(self):
        data = baseball.get('person',{ 'ver':'v1' , 'personId':self.id,'hydrate':['currentTeam']} )
        return data.get('people')[0].get('currentTeam')



    def seasonStats(self,type = 'gameLog'):

        """Returns a player's season/career stats and wether it's hitting or pitching or fielding
            fix and improve this later"""

        #playerInfo = get('people', {'personIds':personId}
        teamStats = baseball.get('person',{ 'ver':'v1' , 'personId':self.id,'hydrate':['stats(group={},type={})'.format(self.group,type),'currentTeam']})
        return teamStats
        #iterate of stats and find the right player id
        #career stats broken
        #fix the season :2019
        #make function to get team id
    def hotColdZones(self, group = 'hitting', zoneType = 'onBasePlusSlugging'):
        #find his current team and if he's a hitter or pitcher then
        """Returns ZoneData for player """
        zoneData = baseball.get('person',{ 'ver':'v1' , 'personId':self.id,'hydrate':['stats(group={},type={})'.format(group,'hotColdZones'),'currentTeam']})
        zonesData = {}
        sz = StrikeZone.strikeZone('{} {}'.format(self.id, zoneType))
        for stat in zoneData.get('people')[0].get('stats'):
            for types in stat.get('splits'):
                zonesData[types.get('stat')['name']] = types.get('stat')['zones']
                #create a list of Zones, up to 9
                #using that list of zones make a strike zone
                #make a list of strike zone data for each value
        sz.zoneData = zonesData
        zone = [1,2,3,4,5,6,7,8,9]
        zoneLData = []
        for k,v in zonesData.items():
            if k == zoneType:
                for zData in v:
                    if int(zData.get('zone')) > 9:
                        break
                    else:
                        zoneLData.append(float(zData.get('value')))

        sz.updateStrikeZone(zone,zoneLData)
        self.strikeZone = sz
        return sz
