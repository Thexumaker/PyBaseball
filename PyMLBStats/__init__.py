name = "PyMLBStats"
import requests
import Models.backend.baseball as baseballs
import Models.backend.endpoints as endpointss
from Models import StrikeZone
from Models import Person
from Models import Sport
from Models import Team
from datetime import datetime, date
ENDPOINTS = endpointss.ENDPOINTS
currentDate = date.today()




today = currentDate.strftime('%m/%d/%Y')
year = datetime.today().year

def Player(id):
    """Main function to generate a Player object using a playerId
    Returns a Player object
    >>>Marcus_Semien = Player(543760)
    >>>print(type(Marcus_Semien))
    <class 'Models.Person.Player'>
    """
    rData = baseballs.get('person', {'personId': id})
    pModel = Person.Player(rData)
    return pModel
def Sports(id = 1, years = [year]):
    """Main function to generate a Sport object using a LeagueId
    Returns a Sport object
    """
    rData = baseballs.get('sports', {'sportId': id, 'ver': 'v1'})
    sportO = Sport.Sport(rData, years)
    sportO.setPlayerList()
    return sportO
def Teams(id):
    rData = baseballs.get('teams', {'teamId': id})
    pModel = Team.Team(rData)
    return pModel



mlb = Sports(1,[2019])

royals = Teams(118)
print(royals.roster)



#baseball.hotColdZones(Marcus)
#print(Marcus.strikeZone.visualize())
#print(Marcus.hotColdZones().visualize())
