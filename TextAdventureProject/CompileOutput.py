import ConsoleManager 
#import Translator
import WorldHandler
import StartupProcedure
from parserCommand import parseInput
import sys


class CompileOutput:
    @staticmethod
    def playerRoomDescription(console):
        valid = False
        console.printRoom()
        while valid == False:
            print("what would you like to do?")
            print("For help enter 'help'\n")
            print("to end game enter exit\n")
            console.readUserInput()
            if console.userInput.lower() == "help":
                console.helper()
            if console.userInput.lower() == "exit":
                sys.exit("thank you for playing")
            else:
                parsed = parseInput(console, "Player")
                valid = console.printFailure(parsed)
        wH = WorldHandler.WorldHandler(parsed)
        if console.endGame(wH.data):
            sys.exit("thank you for playing")
        curRoom = StartupProcedure.findPlayer(wH.data)[0]        
        console.room = [curRoom, wH.data.rooms[curRoom]]
        CompileOutput.playerRoomDescription(console)
        #and then restart the turn sequence


def checkEnd(dataMan):
    curRoom = StartupProcedure.findPlayer(dataMan)
    if curRoom == None:
        print("You have died\n")
        return True
    else:
        if curRoom[0] == "Waste_Dump":
            print("you find your way out of the dirty waste dump and take your first breath of somewhat fresh air, a world free of zombies awaits!")
            return True
    return False
        
        
        
        
        