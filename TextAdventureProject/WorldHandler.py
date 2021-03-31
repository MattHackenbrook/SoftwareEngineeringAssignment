import CommandModel
import DataManager
import DataModels

class WorldHandler:

    def __init__(self, cmd):
        self.playerCommand = CommandModel.Command(cmd.action, cmd.object, cmd.owner, cmd.target, cmd.room)
        self.data = DataManager.DataManager()
        self.rooms = self.data.rooms
        self.commandList = self.getCommandList()
        self.playerResult = self.runCommand(self.playerCommand)
        for command in self.commandList:
            self.runCommand(command)
        self.checkDeaths()
        self.data.writeData()
        #send playerResult to compileOutput
        print(self.playerResult)


    def getCommandList(self):
        commandList = []
        return commandList

    def runCommand(self, cmd):
        if cmd.action == CommandModel.Action.USE:
            return self.use(cmd)
        elif cmd.action == CommandModel.Action.INSPECT:
            return self.inspect(cmd)
        elif cmd.action == CommandModel.Action.TAKE:
            return self.take(cmd)
        elif cmd.action == CommandModel.Action.THROW:
            return self.throw(cmd)
        elif cmd.action == CommandModel.Action.HIT:
            return self.hit(cmd)
        elif cmd.action == CommandModel.Action.SPEAK:
            return self.speak(cmd)
        else:
            print("No action for " + str(cmd.action))

    def populateCommand(self, cmd):
        command = CommandModel.Command(cmd.action, None, None, None, None)
        command.room = self.rooms[cmd.room]
        command.owner = command.room.characters[cmd.owner]
        if cmd.object is not None:
            command.object = command.owner.inv[cmd.object]
        if cmd.target is not None:
            command.target = None
            for container in command.room.containers.keys():
                if cmd.target == container:
                    command.target = command.room.containers[container]
            if command.target is not None:
                return command
            for door in command.room.doors.keys():
                if cmd.target == door:
                    command.target = command.room.doors[door]
            if command.target is not None:
                return command
            for character in command.room.characters.keys():
                if cmd.target == character:
                    command.target = command.room.characters[character]
            if command.target is not None:
                return command
            for container in command.room.containers.keys():
                for item in command.room.containers[container].items.keys():
                    if cmd.target == item:
                        command.target = command.room.containers[container].items[item]
        return command

    def use(self, cmd):
        command = self.populateCommand(cmd)

    def unlock(self, cmd):
        command = self.populateCommand(cmd)
        for door in command.object.traits["Opens"]:
            rooms = door.split('.')
            if rooms[0] == cmd.room:
                if rooms[1] == cmd.target:
                    command.target.locked = False
                    return "Opened " + cmd.target + " with " + cmd.object
            if rooms[1] == cmd.room:
                if rooms[0] == cmd.target:
                    command.target.locked = False
                    return "Opened " + cmd.target + " with " + cmd.object
        return "Cannot open" + cmd.target + " with " + cmd.object

    def wear(self, cmd):
        command = self.populateCommand(cmd)


    def eat(self, cmd):
        command = self.populateCommand(cmd)


    def inspect(self, cmd):
        command = self.populateCommand(cmd)
        return command.target.desc

    def take(self, cmd):
        command = self.populateCommand(cmd)
        command.owner.inv[cmd.target] = command.target
        for container in command.room.containers:
            for item in container.items.keys():
                if cmd.target == item:
                    del container[item]
        return "Take " + cmd.target

    def throw(self, cmd):
        command = self.populateCommand(cmd)
        del command.owner.inv[cmd.object]
        command.target.stats["health"] -= command.object.traits["Damage"]
        command.room.containers["Ground"].items[cmd.object] = command.object
        return "Throw " + cmd.object + " at " + cmd.target

    def hit(self, cmd):
        command = self.populateCommand(cmd)
        command.target.stats["health"] -= command.object.traits["Damage"]
        return "Hit " + cmd.target + " with " + cmd.object

    def speak(self, cmd):
        command = self.populateCommand(cmd)
        return "Speak"

    def checkDeaths(self):
        for roomKey in self.rooms.keys():
            room = self.rooms[roomKey]
            toDelete = []
            for character in room.characters.keys():
                if int(room.characters[character].stats["health"]) <= 0:
                    room.containers[character] = DataModels.Container(room.characters[character].inv,
                                                                      "The corpse of " + character)
                    toDelete.append(character)
            for character in toDelete:
                del room.characters[character]

#cmd = CommandModel.Command(CommandModel.Action.HIT, "Teeth", "Zombie", "Zombie2", "South_Hall")
#wh = WorldHandler(cmd)

