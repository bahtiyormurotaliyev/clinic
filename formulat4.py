class GP:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

class Driver:
    def __init__(self, name):
        self.name = name
        self.races = []

    def getRaced(self):
        return [race.name for race in self.races]

    def addRace(self, race):
        self.races.append(race)

    def getPoints(self):
        points_table = {
            1: 25,
            2: 18,
            3: 15,
            4: 12,
            5: 10,
            6: 8,
            7: 6,
            8: 4,
            9: 2,
            10: 1
        }
        total_points = 0
        for race in self.races:
            position = race.getPosition()
            total_points += points_table.get(position, 0)
        return total_points
class GP:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

class Driver:
    def __init__(self, name):
        self.name = name
        self.races = []

    def getRaced(self):
        return [race.name for race in self.races]

    def addRace(self, race):
        self.races.append(race)

    def getPoints(self):
        points_table = {
            1: 25,
            2: 18,
            3: 15,
            4: 12,
            5: 10,
            6: 8,
            7: 6,
            8: 4,
            9: 2,
            10: 1
        }
        total_points = 0
        for race in self.races:
            position = race.getPosition()
            total_points += points_table.get(position, 0)
        return total_points
