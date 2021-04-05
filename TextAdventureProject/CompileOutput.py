import ConsoleManager 
#import Translator
import WorldHandler
from parserCommand import parseInput


class CompileOutput:
    @staticmethod
    def playerRoomDescription(console):
        valid = False
        console.printRoom()
        while valid == False:
            print("what would you like to do?")
            print("For help enter 'help'\n")
            console.readUserInput()
            if console.userInput == "help":
                console.helper()
            else:
                parsed = parseInput(console, "Player")
                valid = console.printFailure(parsed)
        wH = WorldHandler(valid)
        #print()
        #and then restart the turn sequence

