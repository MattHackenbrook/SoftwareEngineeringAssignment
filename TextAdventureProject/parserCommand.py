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
    room = console.room
    command = {"Action": "", "Object": "", "Owner": owner, "Target": "", "Room": room}
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
        word = word.lower()
        if word not in helpWords:
            if word in actionWords:
                command["Action"] = word
            elif word in doorList:
                if command["Action"] == "inspect":
                    command["Target"] = word
                elif command["Action"] == "unlock":
                    if doorObjectsList[
                        word].locked == False:  # check to see if door is even able to be unlocked, if door is already unlocked, u cannot unlock it again so returns invalid by setting target to empty string
                        command["Target"] = ""
                    else:
                        command["Target"] = word
                elif command["Action"] == "enter":
                    if doorObjectsList[word].locked == True:  # same here but for when u try to enter a locked door
                        command["Target"] = ""
                    else:
                        command["Target"] = word
                else:
                    command["Target"] = word
            elif word in containerList:
                command["Target"] = word
            elif word in itemList:
                if command["Action"] == "Take":
                    command["Target"] = word
                if command["Action"] == "inspect":
                    command["Target"] = word
                else:
                    command["Object"] = word
            elif word in invList:
                if command["Action"] == "inspect":
                    command["Target"] = word
                if command["Action"] == "unlock":
                    if invObjectsList[owner][word].classification == "Key":
                        command["Object"] == word
                elif command["Action"] == "eat":
                    if invObjectsList[owner][word].classification == "Edible":
                        command["Object"] = word
                elif command["Action"] == "wear":
                    if invObjectsList[owner][word].classification == "Wearable":
                        command["Object"] = word
                else:
                    command["Object"] = word
            elif word in characterList:
                command["target"] = word
        elif word in helpWords:
            console.helper()
    commandObject = CommandModel.Command(command["Action"], command["Object"], command["Owner"], command["Target"],
                                         command["Room"])
    return commandObject


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
    for each in invList:
        for item in room.characters[each].inv.keys():
            invList[each][item] = {item, room.characters[each].inv[item]}
    return invList


def checkValidCommand(command):
    if command.target == "" and command.action == "inspect":
        command.target = command.room
    if command.target == "" and command.action == "eat" or command.action == "wear" or command.action == "unlock":
        command.target = None
    if command.object == "" and command.action == "enter":
        command.object = None
    if command.action == "" or command.target == "":
        return False
    else:
        return command


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
