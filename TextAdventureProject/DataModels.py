class Room:
    def __init__(self, doors, containers, characters, shortDesc, longDesc, visited):
        self.doors = doors
        self.containers = containers
        self.characters = characters
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.visited = visited


class Door:
    def __init__(self, locked, desc):
        self.locked = locked
        self.desc = desc


class Container:
    def __init__(self, items, desc):
        self.items = items
        self.desc = desc


class Character:
    def __init__(self, characterClass, stats, inv, wearing):
        self.characterClass = characterClass
        self.stats = stats
        self.inv = inv
        self.wearing = wearing


class Item:
    def __init__(self, trait, itemClass, desc):
        self.trait = trait
        self.itemClass = itemClass
        self.desc = desc
