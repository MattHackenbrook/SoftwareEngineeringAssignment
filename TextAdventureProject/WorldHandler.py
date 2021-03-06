import CommandModel
import DataManager
import RunWorldAi
import DataModels

class WorldHandler:

    def __init__(self, cmd):
        self.data = DataManager.DataManager(False)
        self.rooms = self.data.rooms
        # for room in self.rooms.keys():
        #     if "Player" in self.rooms[room].characters.keys():
        #         cmd.room = room
        self.playerCommand = CommandModel.Command(cmd.action, cmd.object, cmd.owner, cmd.target, cmd.room)
        self.commandList = self.getCommandList()
        self.playerResult = self.runCommand(self.playerCommand)
        for command in self.commandList:
            aiResult = self.runCommand(command)
            if "Player" in self.rooms[command.room].characters:
                print(command.owner, aiResult)
        self.checkDeaths()
        self.data.writeData()
        #send playerResult to compileOutput
        print("You " + self.playerResult + "\n")

    # def __init__(self, cmd):
    #     self.playerCommand = CommandModel.Command(cmd.action, cmd.object, cmd.owner, cmd.target, cmd.room)
    #     self.data = DataManager.DataManager(False)
    #     self.rooms = self.data.rooms
    #     self.commandList = self.getCommandList()
    #     self.playerResult = self.runCommand(self.playerCommand)
    #     for command in self.commandList:
    #         self.runCommand(command)
    #     self.checkDeaths()
    #     self.data.writeData()
    #     #send playerResult to compileOutput
    #     #print(self.playerResult)


    def getCommandList(self):
        AI = RunWorldAi.WorldAi(self.data)
        return AI.commandList

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
        if cmd.owner == "Player":
            command.room.visited = True
        command.owner = command.room.characters[cmd.owner]
        if cmd.object is not None:
            try:
                command.object = command.owner.inv[cmd.object]
            except KeyError:
                command.object = None
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
            for invItem in command.owner.inv.keys():
                if cmd.target == invItem:
                    command.target = command.owner.inv[invItem]
            if command.target is not None:
                return command
        return command

    def unlock(self, cmd):
        command = self.populateCommand(cmd)
        if cmd.target is None or cmd.object is None:
            return "Invalid command"
        for door in command.object.traits["Opens"]:
            rooms = door.split('.')
            if rooms[0] == cmd.room:
                if rooms[1] == cmd.target:
                    self.rooms[cmd.target].doors[cmd.room].locked = False
                    command.target.locked = False
                    return " opened the " + cmd.target + " with the " + cmd.object
            if rooms[1] == cmd.room:
                if rooms[0] == cmd.target:
                    self.rooms[cmd.target].doors[cmd.room].locked = False
                    command.target.locked = False
                    return " opened the " + cmd.target + " with the " + cmd.object
        return " cannot open the " + cmd.target + " with the " + cmd.object

    def wear(self, cmd):
        command = self.populateCommand(cmd)
        if command.owner.wearing != {}:
            item = list(command.owner.wearing.keys())[0]                
            command.owner.inv[item] = command.owner.wearing[item]
            command.owner.wearing.pop(item)
        command.owner.wearing[cmd.object] = command.object        
        command.owner.inv.pop(cmd.object)
        return " wear the " + cmd.object

    def eat(self, cmd):
        command = self.populateCommand(cmd)
        command.owner.stats["health"] += command.object.traits["Healing"]
        del command.owner.inv[cmd.object]
        return " eat the " + cmd.object

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
                return " see " + command.target.desc + extra
            else:
                return " inspect the floor." + extra
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
            elif cmd.target in command.room.doors:
                return "see " + command.room.doors[cmd.target].desc
        return "see " + command.target.desc + extra
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
        return " took the " + cmd.target

    def throw(self, cmd):
        command = self.populateCommand(cmd)
        if command.target is None or command.object is None:
            return "Invalid command"
        del command.owner.inv[cmd.object]
        command.target.stats["health"] = int(command.target.stats["health"]) - command.object.traits["Damage"]
        command.room.containers["Ground"].items[cmd.object] = command.object
        if cmd.target == "Player":
            print(cmd.owner, " threw ", cmd.object, " at you!")
        elif cmd.object == "Bomb" and cmd.owner == "Player":
            print("You threw a very large bomb... not a good idea.")
            command.owner.stats["health"] = 0
        return " threw the " + cmd.object + " at " + cmd.target

    def hit(self, cmd):
        command = self.populateCommand(cmd)
        if command.target is None or command.object is None:
            return " Made an invalid command"
        try:
            wearing = list(command.target.wearing.keys())[0]
            armour = command.target.wearing[wearing].traits["Armour"]
            if armour <= 0:
                armour = 1
            command.target.stats["health"] = (int(command.target.stats["health"]) - command.object.traits["Damage"] / armour)
        except:
            health = int(command.target.stats["health"])
            health -= command.object.traits["Damage"]
            command.target.stats["health"] = health
        if cmd.object == "Bomb" and cmd.owner == "Player":
            print("You smashed a very large bomb... not a good idea.")
            command.owner.stats["health"] = 0
        return " hit the " + cmd.target + " with the " + cmd.object

    def enter(self, cmd):
        command = self.populateCommand(cmd)
        self.rooms[cmd.target].characters[cmd.owner] = command.owner
        del command.room.characters[cmd.owner]
        return " enter the " + cmd.target


    def checkDeaths(self):
        for roomKey in self.rooms.keys():
            room = self.rooms[roomKey]
            toDelete = []
            for character in room.characters.keys():
                if int(room.characters[character].stats["health"]) <= 0:
                    room.characters[character].inv = {
                        **room.characters[character].inv,
                        **room.characters[character].wearing
                    }
                    room.containers[character] = DataModels.Container(
                        room.characters[character].inv, "The corpse of " + character
                    )
                    toDelete.append(character)
            for character in toDelete:
                if "Player" in self.rooms[roomKey].characters.keys():
                    print(character, " died!")
                del room.characters[character]
