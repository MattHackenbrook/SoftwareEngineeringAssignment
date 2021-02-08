# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:37:07 2021

@author: 3picm
"""

import json

#with open('C:/Users/3picm/Documents/softeng/SoftwareEngineeringAssignment/Rooms Example J.K.json') as f:
#  data = json.load(f)

#print(data)

#templates

#Door = {"Locked":True, "Health":10, "Desc":""}

#Container = {"Items":{}, "Desc":""}

#Character = {"Stats":{"Strength":"", "Thrift":"", "Persuasion":"", "Armour":"", "Health":""}, "Inventory":{}, "Wearing":None, "Desc":""}

#Item = {"Class":"", "Desc":"", "Traits":{"Damage":0}}

#Room = {"Doors":{}, "Container's":{"Ground**",}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}



#Room set up:

#caferteria:

KitchenDoor = {"Locked":True, "Health":10, "Desc":""}

SouthHallDoor = {"Locked":True, "Health":10, "Desc":""}

WestHallDoor = {"Locked":True, "Health":10, "Desc":""}

CourtyardDoor = {"Locked":True, "Health":10, "Desc":""}

VendingMachine = {"Items":[], "Desc":""}

TrashCan = {"Items":[], "Desc":""}

PileofLeftovers = {"Items":[], "Desc":""}

BigSpoon = {"Class":"Misc", "Desc":"A large Wooden Spoon about a foot and a half long, a little chipped at the ends", "Traits":{"Damage":1}}

PantryKey = {"Class":"Misc", "Desc":"A small metal key that is covered in leftover sauce", "Traits":{"Damage":1}}

Soda = {"Class":"Edible", "Desc":"A can of Diet Spripesi Cola Up, looks edible", "Traits":{"Damage":1, "Healing":2}}

HardLeftover = {"Class":"Misc", "Desc":"A hard solid mass of dried up leftovers, who knows what this used to be, its got some weight to it", "Traits":{"Damage":2}}

ZombieChef = {"Stats":{"Strength":"1", "Thrift":"1", "Persuasion":"1", "Armour":"1", "Health":"1"}, "Inventory":[PantryKey], "Wearing":None, "Desc":"A Zombie wearring a lunchlady outfit, missing a jaw and looks around with only one eye that stares hungrily"}

Cafeteria = {"Doors":{}, "Container's":["Ground**,], "Characters":[ZombieChef], "ShortDesc":"", "LongDesc":"", "Visited":False}

#Courtyard:

Courtyard = {"Doors":[], "Container's":[], "Characters":[], "ShortDesc":"", "LongDesc":"", "Visited":False}

#Northhall:

NorthHall = {"Doors":[], "Container's":[], "Characters":[], "ShortDesc":"", "LongDesc":"", "Visited":False}

#Bloody cell:

BloodyCell = {"Doors":[], "Container's":[], "Characters":[], "ShortDesc":"", "LongDesc":"", "Visited":False}

#West Cell Block:

WestCellBlock = {"Doors":[], "Container's":[], "Characters":[], "ShortDesc":"", "LongDesc":"", "Visited":False}

#Waste Dump:

WasteDump = {"Doors":[], "Container's":[], "Characters":[], "ShortDesc":"", "LongDesc":"", "Visited":False}