import CommandModel
import DataManager
import DataModels

class WorldHandler:

    def __init__(self, cmd):
        self.playerCommand = CommandModel.Command(cmd.action, cmd.object, cmd.owner, cmd.target, cmd.room)
        self.data = DataManager.DataManager(False)
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
        if cmd.action == CommandModel.Action.WEAR:
            return self.wear(cmd)
        if cmd.action == CommandModel.Action.UNLOCK:
            return self.unlock(cmd)
        if cmd.action == CommandModel.Action.ENTER:
            return self.enter(cmd)
        if cmd.action == CommandModel.Action.EAT:
            return self.eat(cmd)
        elif cmd.action == CommandModel.Action.INSPECT:
            return self.inspect(cmd)
        elif cmd.action == CommandModel.Action.TAKE:
            return self.take(cmd)
        elif cmd.action == CommandModel.Action.THROW:
            return self.throw(cmd)
        elif cmd.action == CommandModel.Action.HIT:
            return self.hit(cmd)
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
        if command.owner.wearing != {}:
            item = command.owner.wearing.keys()[0]
            command.owner.inv[item] = command.owner.wearing[item]
        command.owner.wearing[cmd.object] = command.object
        return "Wear " + cmd.object

    def eat(self, cmd):
        command = self.populateCommand(cmd)
        command.owner.stats["health"] += command.object.traits["Healing"]
        del command.owner.inv[cmd.object]
        return "Eat " + cmd.object

    def inspect(self, cmd):
        command = self.populateCommand(cmd)
        extra = ""
        try:
            if command.target.items != None:
                if command.target.items == {}:
                    extra = " It is empty."
                else:
                    extra = " It contains a "
                    first = True
                    for item in command.target.items.keys():
                        if first:
                            extra += item
                            first = False
                        else:
                            extra += ", a " + item
            if cmd.target != "Ground":
                return command.target.desc + extra
            else:
                return "The floor." + extra
        except:
            if cmd.target == cmd.room:
                command.target = command.room
                if command.target.containers != None:
                    if command.target.containers == {}:
                        extra = " It is empty."
                    else:
                        extra = " Its containers are a "
                        first = True
                        for container in command.target.containers.keys():
                            if first:
                                extra += container
                                first = False
                            else:
                                extra += ", a " + container
            return command.target.longDesc + extra
        return command.target.desc + extra
    def take(self, cmd):
        command = self.populateCommand(cmd)
        command.owner.inv[cmd.target] = command.target
        ctr = None
        toDelete = None
        for container in command.room.containers.values():
            for item in container.items.keys():
                if cmd.target == item:
                    toDelete = item
                    ctr = container
        del ctr.items[toDelete]
        return "Take " + cmd.target

    def throw(self, cmd):
        command = self.populateCommand(cmd)
        del command.owner.inv[cmd.object]
        command.target.stats["health"] -= command.object.traits["Damage"]
        command.room.containers["Ground"].items[cmd.object] = command.object
        return "Throw " + cmd.object + " at " + cmd.target

    def hit(self, cmd):
        command = self.populateCommand(cmd)
        try:
            armour = command.target.wearing.traits["armour"]
            if armour <= 0:
                armour = 1
            command.target.stats["health"] -= command.object.traits["Damage"] / armour
        except:
            command.target.stats["health"] -= command.object.traits["Damage"]
        return "Hit " + cmd.target + " with " + cmd.object

    def enter(self, cmd):
        command = self.populateCommand(cmd)
        self.rooms[cmd.target].characters[cmd.owner] = command.owner
        del command.room.characters[cmd.owner]
        return "Enter " + cmd.target


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

cmd = CommandModel.Command(CommandModel.Action.ENTER, None, "Zombie James", "South_Hall", "North_Hall")
wh = WorldHandler(cmd)

