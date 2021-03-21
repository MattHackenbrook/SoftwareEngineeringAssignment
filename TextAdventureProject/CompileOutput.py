import ConsoleManager 
import Translator

class CompileOutput:

    def __init__(self, room):
        self.currentRoom = room
        self.console = ConsoleManager(room)

    def playerRoomDescription(self):
        self.console.printRoom()
        #print("For help enter 'help'")
        userInput = self.console.ReadUserInput()
        if userInput =="help":
            self.console.helper()
        else:
            #call translator to start input chain
