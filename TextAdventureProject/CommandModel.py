from enum import Enum


class Action(Enum):
    THROW = 1
    HIT = 2
    INSPECT = 3
    TAKE = 4
    EAT = 5
    WEAR = 6
    UNLOCK = 7
    ENTER = 8



class Command:

    def __init__(self, action, obj, owner, target, room):
        self.action = action
        self.object = obj
        self.owner = owner
        self.target = target
        self.room = room
