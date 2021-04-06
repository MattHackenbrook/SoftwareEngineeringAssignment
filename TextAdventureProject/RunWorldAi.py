import CommandModel
import DataManager
import DataModels
import parserCommand
import random
import CommandModel

npcActionWords = ("take", "unlock", "enter", "stay")
zombieActionWords = ("enter", "stay")
hostileActionWords = ("throw", "hit")
stateWords = ("idle", "wander")

class WorldAi:

    def __init__(self, data):
        self.worldCaracters = self.findCaracters(data)
        self.commandList = []
        for each in self.worldCaracters:
            generatedCommand = self.generateCommand(each, self.worldCaracters[each], data)
            if generatedCommand != None:
                self.commandList.append(generatedCommand)
        #print("commands generated")
         

    def findCaracters(self, data): #this needs to get caracter object
        caracters = {}
        for room in data.rooms.items():
            currChars = room[1].characters
            if len(currChars) > 0:
                for caracter in currChars:
                    if caracter != "Player":
                        caracters[caracter] = room
        return caracters

    def generateCommand(self, caracter, room, data):
        roomStuff = parserCommand.roomDict(room[1])
        roomStuff["Characters"].remove(caracter)
        roomStuff["Inventory"].pop(caracter)
        caracterObject = getCharObject(caracter, room[1])
        characterObjects = getCharObjects(roomStuff["Characters"], room[1])
        doorObjectsList = parserCommand.getDoorObjects(roomStuff["Doors"], room[1])
        
        command = {"Action":"", "Object":"", "Owner":caracter, "Target":"", "Room":room[0]}
        
        
        if checkHostile(caracterObject, characterObjects):
            setState(caracter, caracterObject, data, "aggressive")
            command["Action"] = random.choice(hostileActionWords)
            #if command["Action"] == "throw":
            command["Object"] = random.choice(roomStuff["Inventory"][caracter])
            if caracterObject.classification == "NPC":
                command["Target"] = random.choice(roomStuff["Characters"])
            else:
                while characterObjects[command["Target"]].classification == "Zombie":
                    command["Target"] = random.choice(roomStuff["Characters"])
            #if command["Action"] == "hit": #this is redundant, can be removed as long as there is no distinguishing between hit or throw for npc or zombies.
                # command["Object"] = random.choice(roomStuff["Inventory"][caracter])
                # if caracterObject.classification == "NPC":
                #     command["Target"] = random.choice(roomStuff["Characters"])
                # else:
                #     while characterObjects[command["Target"]].classification == "Zombie":
                #         command["Target"] = random.choice(roomStuff["Characters"])
        else:
            setState(caracter, caracterObject, data, random.choice(stateWords))
            if caracterObject.state == "idle":
                command["Action"] = "stay"
            if caracterObject.classification == "NPC":
                command["Action"] = random.choice(npcActionWords)
                if command["Action"] == "take" and caracterObject.state == "wander":
                    command["Object"] = None
                    if len(roomStuff["Items"]) > 0:
                        command["Target"] = random.choice(roomStuff["Items"])
                    else:
                        command["Target"] = None #ask about this default actions if first try is unusable for npc only
                        command["Action"] = "stay" 
                if command["Action"] == "unlock" and caracterObject.state == "wander":
                    command["Target"] = random.choice(roomStuff["Doors"])
                    if doorObjectsList[command["Target"]].locked == False:
                        command["Object"] = None 
                        command["Action"] = "enter"
                    else:
                        if caracter == "Ivan":
                            command["Object"] = "Sledgehammer"
                        else:
                            command["Object"] = None 
                            command["Action"] = "stay"
                if command["Action"] == "enter" and caracterObject.state == "wander":
                    command["Target"] = random.choice(roomStuff["Doors"])
                    if doorObjectsList[command["Target"]].locked == True:
                        if caracter == "Ivan":
                            command["Action"] = "unlock"
                            command["Object"] = "Sledgehammer" #ask about this
                        else:
                            command["Action"] = "stay" 
                    else:
                        command["Object"] = None
            else:
                command["Action"] = random.choice(zombieActionWords)
                if command["Action"] == "enter" and caracterObject.state == "wander":
                    command["Target"] = random.choice(roomStuff["Doors"])
                    if doorObjectsList[command["Target"]].locked == True:
                        command["Action"] = "stay"
                    else:
                        command["Object"] = None      
        if command["Action"] == "stay":
            commandObject = None
        else:
            command["Action"] = parserCommand.getEnum(command["Action"].lower())
            commandObject = CommandModel.Command(command["Action"], command["Object"], command["Owner"], command["Target"], command["Room"])
        return commandObject
        
    # def getCharClass(self, charObject):
    #     return charObject.classification

    # def getCharState(self, charObject):
    #     return charObject.state

def getCharObject(name, room):
   for each in room.characters:
       if each == name:
           return room.characters[each]

def getCharObjects(chars, room):
    charsList = {}
    for each in chars:
        for char in room.characters.keys():
            if char == each:
                charsList[each] = room.characters[char]
    return charsList

def checkHostile(charObject, charObjects):
    for each in charObjects:
        if charObject.classification == "NPC" and charObjects[each].classification == "Zombie":
            charObject.state = "aggressive" 
        if charObject.classification == "Zombie" and charObjects[each].classification == "NPC":
            charObject.state = "aggressive"
        if charObject.classification == "Zombie" and charObjects[each].classification == "Player":
            charObject.state = "aggressive"            
        if charObject.state == "aggressive":
            return True        
    return False

def setState(caracter, charObject, data, state):
    for room in data.rooms:
        for each in data.rooms[room].characters:
            if each == caracter:
                data.rooms[room].characters[caracter].state = state
                charObject.state = state
                return True
    
    

#testing
#data = DataManager.DataManager(True)
#worldAI = WorldAi(data)
#worldAI = WorldAi(data)
#worldAI = WorldAi(data)
#worldAI = WorldAi(data)