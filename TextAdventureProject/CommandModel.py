from enum import Enum


class Action(Enum):
    THROW = 1
    HIT = 2
    INSPECT = 3
    TAKE = 4
    USE = 5
    SPEAK = 6


class Command:

    def __init__(self, action, obj, owner, target, room):
        self.action = action
        self.object = obj
        self.owner = owner
        self.target = target
        self.room = room
