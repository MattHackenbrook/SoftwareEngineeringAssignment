Action = {'THROW': 'TO THROW',
          'HIT': 'TO HIT'}

helpWords = ("Helper" , "Help")
 
def parserCommand(Action):
    print("\nWhat action do you want to take?: ")
    for choice in Action:
         [print(key, ' : ', value) for key, value in Action.items()]
    choice = ''
    while choice not in Action.keys():
        choice = input("\nWhat is your choice? ")
        choice = str(choice)
    return choice



def parseInput(input, room, console):
    command = ""
    command_words = list(input.split(" "))
    new_command = []
    roomStuff = roomDict(room)
    doorList = roomStuff["Doors"]
    containerList = roomStuff["Containers"]
    itemList = roomStuff["Items"]
    characterList = roomStuff["Characters"]
    
    for word in command_words:
        if word not in helpWords:
            if word in doorList:
                new_command.append(doorList[word])
        if word not in helpWords:
            if word in containerList:
                new_command.append(containerList[word])
        if word not in helpWords:
            if word in itemList:
                new_command.append(itemList[word])
        if word not in helpWords:
            if word in characterList:
                new_command.append(characterList[word])
        elif word in helpWords:
            console.helper()
    for word in new_command[:2]:
        command = command + word + " "
    command = command.strip()
    return command

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