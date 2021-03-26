import ConsoleManager 
import Translator
import parserCommand


class CompileOutput:

    def playerRoomDescription(console):
        console.printRoom()
        choice = parserCommand()
        parsed = parser(choice)
