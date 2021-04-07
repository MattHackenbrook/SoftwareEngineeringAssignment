import DataManager
import CompileOutput
import ConsoleManager
import os
from os import path
from os import remove

#check savefile for player in room and return that room
def findPlayer(dataMan):
    for room in dataMan.rooms.keys():
        if len(dataMan.rooms[room].characters) > 0:
            for thing in dataMan.rooms[room].characters:
                if thing == "Player":
                    return [room, dataMan.rooms[room]]

def startGame():
    a = """Select by typing an options:
    Newgame
    """
    o = """
    Loadgame
    """
    if path.exists("SaveFile.json") ==True:
        c = a + o
        print(c)
        b = input()
        while b.lower() != "loadgame" and b.lower() != "newgame":
            print("invalid input")
            b = input("... ")
        if b.lower == "loadgame":
            dataManager = DataManager.DataManager(False)
            currRoom = findPlayer(dataManager)
            print("We last left off...")
            return currRoom
        else:
            print(
                "Let us begin the story of Prison escape (title pending)\nyou wake up in your miserable cell in prison\nthe smell of blood reaches your nose\nsomething isn't right.\n")
            dataManager = DataManager.DataManager(True)
            return ["Start_Cell" , dataManager.rooms["Start_Cell"]]
    else:
        print(a)
        b = input()
        while b.lower != "newgame":
            print("invalid input")
            b = input("... ")
        print("Let us begin the story of Prison escape (title pending)\nyou wake up in your miserable cell in prison\nthe smell of blood reaches your nose\nsomething isn't right.\n")
        dataManager = DataManager.DataManager(True)
        return ["Start_Cell" , dataManager.rooms["Start_Cell"]]

def main(): #populate world
    startRoom = startGame()
    console = ConsoleManager.ConsoleManager(startRoom)
    CompileOutput.CompileOutput.playerRoomDescription(console)

#main()

if __name__ == "__main__":
    main()
