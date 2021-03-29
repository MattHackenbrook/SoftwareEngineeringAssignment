import ConsoleManager 
#import Translator
import WorldHandler
from parserCommand import parserCommand
from parserCommand import parseInput


class CompileOutput:
    @staticmethod
    def playerRoomDescription(console):
        console.printRoom()
        currRoom = console.room
        print("what would you like to do?")
        print("For help enter 'help'")
        userInput = console.ReadUserInput()
        if userInput =="help":
            console.helper() 
        parsed = parseInput(userInput, currRoom, console)
        wH = WorldHandler(parsed)
        #recurse


