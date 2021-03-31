import DataManager
import CompileOutput
import ConsoleManager
import os
from os import path
from os import remove

dataManager = DataManager.DataManager()

#check savefile for player in room and return that room
def findPlayer():
    for room in dataManager.rooms:
        if len(room["caracters"]) > 0:
            for thing in room["caracters"]:
                if thing == "Player":
                    return room

def startGame():
    a = """Select by typing an options:
    Newgame
    """
    o = """
    Loadgame
    Deletegame"""
    if path.exists("SaveFile.json") ==True:
        a = a + o  
        print(a)
        b = input()
        if b == "Loadgame":
            dataManager.buildRoomsFromData()
            currRoom = findPlayer()
            print("We last left off...")
            return dataManager.rooms[currRoom]
        elif b == "Deletegame":
            os.remove("SaveFile.json")
    print(a)
    b = input()
    if b != "Newgame":
        print("no savefile currently availble")
    elif b == "Newgame":
        print("Let us begin the story of Prison escape (title pending)\nyou wake up in your miserable cell in prison\nthe smell of blood reaches your nose\nsomething isn't right.\n")
        return dataManager.rooms["Start_Cell"]

def main(): #populate world
    startRoom = startGame()
    console = ConsoleManager.ConsoleManager(startRoom)
    CompileOutput.CompileOutput.playerRoomDescription(console)

main()

#if __name__ == "__main__":
#    main()
