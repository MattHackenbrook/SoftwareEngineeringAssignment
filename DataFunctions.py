def build_room(Doors, Containers, Characters, ShortDesc, LongDesc, Visited):
    room = {
        "Doors": Doors,
        "Containers": Containers,
        "Characters": Characters,
        "ShortDesc": ShortDesc,
        "LongDesc": LongDesc,
        "Visited": Visited
    }
    return room


def build_door(Locked, Desc):
    door = {
        "Locked": Locked,
        "Desc": Desc
    }
    return door;


def build_container(items, desc):
    container = {
        "Items": items,
        "Desc": desc
    }
    return container


def build_stats(str, thr, per, arm, hth):
    stats = {
        "Strength": str,
        "Thrift": thr,
        "Persuasion": per,
        "Armour": arm,
        "Health": hth
    }
    return stats;


def build_character(stats, inventory, wearing, desc, class_):
    character = {
        "Stats": stats,
        "Inventory": inventory,
        "Wearing": wearing,
        "Desc": desc,
        "Class": class_
    }
    return character


def wearable_item_traits(damage, armour):
    traits = {
        "Damage": damage,
        "Armour": armour
    }
    return traits


def readable_item_traits(damage, text):
    traits = {
        "Damage": damage,
        "Text": text
    }
    return traits


def edible_item_traits(damage, healing):
    traits = {
        "Damage": damage,
        "Healing": healing
    }
    return traits


def key_item_traits(damage, door_list):
    traits = {
        "Damage": damage,
        "Doors": door_list
    }
    return traits


def build_item(desc, traits, class_):
    item = {
        "Class": class_,
        "Desc": desc,
        "Traits": traits
    }
    return item

