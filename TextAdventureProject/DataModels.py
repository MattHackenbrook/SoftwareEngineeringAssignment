import json


class Room:
    def __init__(self, doors, containers, characters, shortDesc, longDesc, visited):
        self.doors = doors
        for key in self.doors:
            self.doors[key] = Door(**(self.doors[key]))
        self.containers = containers
        for key in self.containers:
            self.containers[key] = Container(**(self.containers[key]))
        self.characters = characters
        for character in self.characters:
            self.characters[character] = Character(**(self.characters[character]))
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.visited = visited


class Door:
    def __init__(self, locked, desc):
        self.locked = locked
        self.desc = desc


class Container:
    def __init__(self, items={}, desc=None):
        self.items = items
        try:
            for item in self.items:
                self.items[item] = Item(**(self.items[item]))
        except TypeError:
            pass
        self.desc = desc


class Character:
    def __init__(self, classification, stats, inv, wearing, desc, state):
        self.classification = classification
        self.stats = stats
        self.inv = inv
        for item in self.inv:
            inv[item] = Item(**(inv[item]))
        self.wearing = wearing
        for item in self.wearing:
            wearing[item] = Item(**(wearing[item]))
        self.desc = desc
        self.state = state


class Item:
    def __init__(self, traits, classification, desc):
        self.traits = traits
        self.classification = classification
        self.desc = desc


