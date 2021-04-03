import CommandModel
import DataManager
import DataModels
import parserCommand
import random
import CommandModel

ivanActionWords = ("throw", "hit", "take", "unlock", "enter")
zombieActionWords = ("throw", "hit", "enter", "Stay")

class WorldAi:

    def __init__(self, data):
        self.worldCaracters = self.findCaracters(data)
        self.commandList = []
        for each in self.worldCaracters:
            generatedCommand = self.generateCommand(each, self.worldCaracters[each])
            if generatedCommand != None:
                self.commandList.append()
         

    def findCaracters(self, data):
        caracters = {}
        for room in data.rooms:
            if len(room.caracters) > 0:
                for caracter in room.caracters:
                    if caracter != "Player":
                        caracters[caracter] = room
        return caracters

    def generateCommand(self, caracter, room):
        roomStuff = parserCommand.roomDict(room)
        roomStuff["Characters"].remove(caracter)
        doorObjectsList = parserCommand.getDoorObjects(roomStuff["Doors"], room)
        command = {"Action":"", "Object":"", "Owner":caracter, "Target":"", "Room":room}
        if caracter == "Ivan":
            command["Action"] = random.choice(ivanActionWords)
            if command["Action"] == "throw":
                command["Object"] = random.choice(roomStuff["Inventory"])
                command["Target"] = random.choice(roomStuff["Characters"]) #if other options, put another randomyzer for picking other things
            if command["Action"] == "hit":
                command["Object"] = random.choice(roomStuff["Inventory"])
                command["Target"] = random.choice(roomStuff["Characters"])
            if command["Action"] == "take":
                command["Object"] = None
                command["Target"] = random.choice(roomStuff["Items"])
            if command["Action"] == "unlock":
                command["Target"] = random.choice(roomStuff["Doors"])
                if doorObjectsList[command["Target"]].locked == False:
                    command["Object"] = None
                else:
                    command["Object"] = "Sledgehammer"
            if command["Action"] == "enter":
                command["Target"] = random.choice(roomStuff["Doors"])
                if doorObjectsList[command["Target"]].locked == True:
                    command["Object"] = "Sledgehammer"
                else:
                    command["Object"] = None
        else:
            for person in roomStuff["Characters"]:
                if "Zombie" in person:
                    roomStuff["Characters"].remove(person)
            command["Action"] = random.choice(zombieActionWords)
            if command["Action"] == "throw":
                if len(roomStuff["Characters"]) == 0:
                    command["Object"] = None
                    command["Target"] = None
                    command["Action"] == "enter"
                else:
                    command["Object"] = random.choice(roomStuff["Inventory"])
                    command["Target"] = random.choice(roomStuff["Characters"]) #if other options, put another randomyzer for picking other things
            if command["Action"] == "hit":
                if len(roomStuff["Characters"]) == 0:
                    command["Object"] = None
                    command["Target"] = None
                    command["Action"] == "enter"
                else:   
                    command["Object"] = random.choice(roomStuff["Inventory"])
                    command["Target"] = random.choice(roomStuff["Characters"])
            if command["Action"] == "enter":
                command["Target"] = random.choice(roomStuff["Doors"])
                if doorObjectsList[command["Target"]].locked == True:
                    command["Object"] = None
                    command["Action"] = "stay"
                else:
                    command["Object"] = None
            if command["Action"] == "stay":
                return None
        commandObject = CommandModel.Command(command["Action"], command["Object"], command["Owner"], command["Target"], command["Room"])
        return commandObject
