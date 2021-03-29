import ConsoleManager 
import Translator
import parserCommand


class CompileOutput:

    def playerRoomDescription(console):
        console.printRoom()
        currRoom = console.room
        choice = parserCommand()
        parsed = parserInput(choice, currRoom, console)


