import DataManager
import json
import CompileOutput

dataManager = DataManager()

#check savefile for player in room and return that room
def findPlayer():
    for room in dataManager.rooms:
        if len(room["caracters"]) > 0:
            for thing in room["caracters"]:
                if thing == "Player":
                    return room

def startGame():
    a = """Select Option by typing
    options:
    Newgame
    Loadgame"""
    print(a)
    b = input()
    if b == "Loadgame":
        if dataManager.readData() != False:
            dataManager.DataManager.buildRoomsFromData()
            currRoom = findPlayer()
            print("We last left off...")
            return dataManager.rooms[currRoom]
    else:
        print("Let us begin the story of Prison escape (title pending)\n you wake up in your miserable cell in prison\nthe smell of blood reaches your nose\n something isnt right.\n")
        return dataManager.rooms["Start_Cell"]

def main(): #populate world
    startRoom = startGame()
    console = ConsoleManager(startRoom)
    CompileOutput.PlayerRoomDescription(console)


If __name__ == "__main__":
    main()
