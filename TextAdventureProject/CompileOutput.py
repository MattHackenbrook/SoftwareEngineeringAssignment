import ConsoleManager 
#import Translator
import WorldHandler
from parserCommand import parserCommand
from parserCommand import parseInput


class CompileOutput:
    @staticmethod
    def playerRoomDescription(console):
        valid = False
        console.printRoom()
        while valid == False:
            print("what would you like to do?")
            print("For help enter 'help'\n")
            console.ReadUserInput()
            if console.userInput == "help":
                console.helper()
            else:
                parsed = parseInput(console)
                valid = console.printFailure(parsed)
        wH = WorldHandler(parsed)
        #do something with w.e is returned from world handler start compile
        #and then restart the turn sequence

