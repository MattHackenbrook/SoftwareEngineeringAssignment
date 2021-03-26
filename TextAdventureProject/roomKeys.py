# -*- coding: utf-8 -*-


def roomDict(room):
    doorList = []
    containerList = []
    itemList = []
    characterList = []
    for x in room["Doors"].keys():
        doorList.append(x)
    for y in room["Container"].keys():
        for z in room["Container"]["Items"].keys():
            itemList.apppend(z)
    containerList.append(y)
    for a in room["Characters"].keys():
      characterList.append(a)  
    
    roomStuff = {"Doors" : doorList, "Containers" : containerList, "Items" : itemList, "Characters" : characterList}
    
    return roomStuff
   