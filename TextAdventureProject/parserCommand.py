import CommandModel

# Action = {'THROW': 'TO THROW', 'HIT': 'TO HIT'}

actionWords = ("throw", "hit", "inspect", "take", "unlock", "wear", "eat", "enter")

helpWords = ("Helper", "Help")


# def parserCommand():
#     print("\nWhat action do you want to take?: ")
#     for choice in Action:
#          [print(key, ' : ', value) for key, value in Action.items()]
#     choice = ''
#     while choice not in Action.keys():
#         choice = input("\nWhat is your choice? ")
#         choice = str(choice)
#     return choice


def parseInput(console, owner):
    inp = str(console.userInput)
    room = console.room[1]
    command = {"Action": "", "Object": "", "Owner": owner, "Target": "", "Room": console.room[0]}
    command_words = list(inp.split(" "))
    roomStuff = roomDict(room)
    doorList = roomStuff["Doors"]
    containerList = roomStuff["Containers"]
    itemList = roomStuff["Items"]
    invList = roomStuff["Inventory"]
    characterList = roomStuff["Characters"]
    characterList.remove(owner)  # so you cant kill yourself
    # itemObjectsList = getItemObject(itemList, room)
    invObjectsList = getInvObjects(invList, room)
    doorObjectsList = getDoorObjects(doorList, room)

    for word in command_words:
        if word.lower() in actionWords:            
            command["Action"] = word.lower()
        elif word.title() in doorList:
            if command["Action"] == "inspect":
                command["Target"] = word.title()
            elif command["Action"] == "unlock":
                if doorObjectsList[word.title()].locked == False:  # check to see if door is even able to be unlocked, if door is already unlocked, u cannot unlock it again so returns invalid by setting target to empty string
                    command["Target"] = ""
                else:
                    command["Target"] = word
            elif command["Action"] == "enter":
                if doorObjectsList[word.title()].locked == True:  # same here but for when u try to enter a locked door
                    command["Target"] = ""
                else:
                    command["Target"] = word.title()
            else:
                command["Target"] = word.title()
        elif word.title() in containerList:
            command["Target"] = word.title()
        elif word.title() in itemList:
            if command["Action"] == "Take":
                command["Target"] = word.title()
            if command["Action"] == "inspect":
                command["Target"] = word.title()
            else:
                command["Object"] = word
        elif word.title() in invList:
            if command["Action"] == "inspect":
                command["Target"] = word.title()
            if command["Action"] == "unlock":
                if invObjectsList[owner][word.title()].classification == "Key":
                    command["Object"] == word.title()
            elif command["Action"] == "eat":
                if invObjectsList[owner][word.title()].classification == "Edible":
                    command["Object"] = word.title()
            elif command["Action"] == "wear":
                if invObjectsList[owner][word.title()].classification == "Wearable":
                    command["Object"] = word.title()
            else:
                command["Object"] = word.title()
        elif word.title() in characterList:
            command["target"] = word.title()
    if command["Object"] == "":
        command["Object"] = None    
    command["Action"] = getEnum(command["Action"].lower())
    commandObject = CommandModel.Command(command["Action"], command["Object"], command["Owner"], command["Target"],
                                         command["Room"])
    return commandObject


def getEnum(word):
    if word == "throw":
        return CommandModel.Action.THROW
    if word == "hit":
        return CommandModel.Action.HIT
    if word == "inspect":
        return CommandModel.Action.INSPECT
    if word == "take":
        return CommandModel.Action.TAKE
    if word == "eat":
        return CommandModel.Action.EAT
    if word == "wear":
        return CommandModel.Action.WEAR
    if word == "unlock":
        return CommandModel.Action.UNLOCK
    if word == "enter":
        return CommandModel.Action.ENTER
        


def getItemObjects(items, room):
    itemsList = {}
    for each in items:
        for container in room.container.keys():
            itemsList[each] = room.container[container].items.values()
    return itemsList


def getDoorObjects(doors, room):
    doorsList = {}
    for each in doors:
        for door in room.doors.keys():
            if door == each:
                doorsList[each] = room.doors[door]
    return doorsList


def getInvObjects(invList, room):
    invObjectList = {}
    for each in invList:
        invObjectList[each] = {}
        for item in room.characters[each].inv.keys():
            invObjectList[each][item] = room.characters[each].inv[item]
    return invList


def checkValidCommand(command):
    if command.target == "" and command.action == "inspect":
        command.target = command.room
    if command.target == "" and command.action == "eat" or command.action == "wear" or command.action == "unlock":
        command.target = None
    if command.action == "" or command.target == "":
        return False
    else:
        return True


def roomDict(room):
    doorList = []
    containerList = []
    itemList = []
    invList = {}
    characterList = []
    for x in room.doors.keys():
        doorList.append(x)
    for y in room.containers.keys():
        for z in room.containers[y].items.keys():
            itemList.append(z)
        containerList.append(y)
    for a in room.characters.keys():
        characterList.append(a)
        invList[a] = []
        for b in room.characters[a].inv.keys():
            invList[a].append(b)

    roomStuff = {"Doors": doorList, "Containers": containerList, "Items": itemList, "Inventory": invList,
                 "Characters": characterList}

    return roomStuff
