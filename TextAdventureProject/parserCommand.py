import CommandModel

#Action = {'THROW': 'TO THROW', 'HIT': 'TO HIT'}

actionWords = ("throw", "hit", "inspect", "take", "use", "unlock", "wear", "eat", "speak", "go/enter", "throw")

helpWords = ("Helper" , "Help")
 
def parserCommand():
    print("\nWhat action do you want to take?: ")
    for choice in Action:
         [print(key, ' : ', value) for key, value in Action.items()]
    choice = ''
    while choice not in Action.keys():
        choice = input("\nWhat is your choice? ")
        choice = str(choice)
    return choice



def parseInput(input, room, console):
    command = {"Action":, "Object":, "Owner":"player", "Target":"", "Room":room}
    command_words = list(input.split(" "))
    roomStuff = roomDict(room)
    doorList = roomStuff["Doors"]
    containerList = roomStuff["Containers"]
    itemList = roomStuff["Items"]
    characterList = roomStuff["Characters"]
    
    for word in command_words:
        word = word.lower()
        if word not in helpWords:
            if word in actionWords:
                command["Action"] = word                
            elif word in doorList:
                command["target"] = word
            elif word in containerList:
                command["target"] = word
            elif word in itemList:
                if command["Action"] == "Take":
                    command["target"] = word
                else:
                    command["object"] = word
            elif word in characterList:
                command["target"] = word
                #new_command.append(characterList[word])
        elif word in helpWords:
            console.helper()
    commandObject = commandModel.command(command["Action"], command["Object"], command["Owner"], command["Targer"], command["Room"])
    return commandObject

def roomDict(room):
    doorList = []
    containerList = []
    itemList = []
    characterList = []
    for x in room["Doors"].keys():
        doorList.append(x)
    for y in room["Container"].keys():
        for z in room["Container"]["Items"].keys():
            itemList.append(z)
    containerList.append(y)
    for a in room["Characters"].keys():
      characterList.append(a)  
    
    roomStuff = {"Doors" : doorList, "Containers" : containerList, "Items" : itemList, "Characters" : characterList}
    
    return roomStuff