import json
from json import JSONEncoder
import DataModels


class RoomEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class DataManager:

    def __init__(self, isFirst):
        self.rooms = {}
        if(isFirst):
            self.filePath = 'StartFile.json'
        else:
            self.filePath = 'SaveFile.json'
        self.buildRoomsFromData()
        self.filePath = 'SaveFile.json'

    def readData(self):
        with open(self.filePath, 'r') as saveFile:
            return json.load(saveFile)

    def writeData(self):
        with open(self.filePath, 'w') as saveFile:
            roomsJson = json.dump(self.rooms, saveFile, indent=4, cls=RoomEncoder)

    def buildRoomsFromData(self):
        data = self.readData()
        for room in data:
            self.rooms[room] = DataModels.Room(**data[room])

