class Person(object):
    basicInfoPath = None
    def __init__(self, rData):
        basicInfoPath = rData.get('people')[0]
        self.id = basicInfoPath.get('id')
        self.fullName = basicInfoPath.get('fullName')
        self.firstName = basicInfoPath.get('firstName')
        self.lastName = basicInfoPath.get('lastName')
class Player(Person):
    def __init__(self, rData):
        super().__init__(rData)
        basicInfoPath = rData.get('people')[0]
        self.primaryNumber = basicInfoPath.get('primaryNumber')
        self.primaryPosition = basicInfoPath.get('primaryPosition')['name']
