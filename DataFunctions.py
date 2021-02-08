def build_room(Doors, Containers, Characters, ShortDesc, LongDesc, Visited):
    room = {
        "doors": Doors,
        "containers": Containers,
        "characters": Characters,
        "shortDesc": ShortDesc,
        "longDesc": LongDesc,
        "visited": Visited
    }
    return room


def build_door(Locked, Desc):
    door = {
        "locked": Locked,
        "desc": Desc
    }
    return door;


def build_container(items, desc):
    container = {
        "items": items,
        "desc": desc
    }
    return container


def build_stats(str, thr, per, arm, hth):
    stats = {
        "strength": str,
        "thrift": thr,
        "persuasion": per,
        "armour": arm,
        "health": hth
    }
    return stats;


def build_character(stats, inventory, wearing, desc, class_):
    character = {
        "stats": stats,
        "inventory": inventory,
        "wearing": wearing,
        "desc": desc,
        "class": class_
    }
    return character


def wearable_item_traits(damage, armour):
    traits = {
        "damage": damage,
        "armour": armour
    }
    return traits


def readable_item_traits(damage, text):
    traits = {
        "damage": damage,
        "text": text
    }
    return traits


def edible_item_traits(damage, healing):
    traits = {
        "damage": damage,
        "healing": healing
    }
    return traits


def key_item_traits(damage, door_list):
    traits = {
        "damage": damage,
        "doors": door_list
    }
    return traits


def build_item(desc, traits, class_):
    item = {
        "class": class_,
        "desc": desc,
        "traits": traits
    }
    return item

