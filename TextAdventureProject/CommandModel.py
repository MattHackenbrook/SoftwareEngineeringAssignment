from enum import Enum


class Action(Enum):
    THROW = 1
    HTI = 2
    INSPECT = 3
    TAKE = 4
    USE = 5


class Command:

    def __init__(self, action, obj, owner, target):
        self.action = action
        self.object = obj
        self.owner = owner
        self.target = target
