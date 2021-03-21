import DataManager
import json
import CompileOutput

dataManager = DataManager()

def startGame():
    a = """Select Option by typing
    options:
    Newgame
    Loadgame"""
    print(a)
    b = input()
    if b == "Loadgame": #need another way to verify that there is indeed a game to load, in case where user loads when the savefile is the same as startfile
        dataManager.DataManager.buildRoomsFromData()#reload datamanager with savefile instead of startfile
        print("We last left off...")
        return dataManager.rooms["w.e room the player left off"] #how do we know which cell the player is in when they load??
    else:
        print("Let us begin the story of Prison escape (title pending)\n you wake up in your miserable cell in prison\nthe smell of blood reaches your nose\n something isnt right.\nwhat do you do?")
        return dataManager.rooms["Start_Cell"]

def main(): #populate world
    startRoom = startGame()
    compiler = CompileOutput(startRoom)
    compiler.PlayerRoomDescription()# problem hereas well


If __name__ == "__main__":
    main()
