# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:37:07 2021

@author: 3picm
"""

import json
#to convert json to python
#with open('C:/Users/3picm/Documents/softeng/SoftwareEngineeringAssignment/Rooms Example J.K.json') as f:
#  data = json.load(f)

#print(data)

#to convert python to json
#X = json.dumps(room object)
#print(X)

#templates

#Door = {"Locked":True, "Desc":""}

#Container = {"Items":{}, "Desc":""}

#Character = {"Stats":{"Strength":"", "Thrift":"", "Persuasion":"", "Armour":"", "Health":""}, "Inventory":{}, "Wearing":None, "Desc":""}

#Item = {"Class":"", "Desc":"", "Traits":{"Damage":0}}

#Room = {"Doors":{}, "Containers":{"Ground**",}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}

#presets:
    
Zombie = {"Stats":{"Strength":1, "Thrift":0, "Persuasion":0, "Armour":1, "Health":1}, "Inventory":{}, "Wearing":None, "Desc":"A Zombie, missing a jaw looks around with only one eye that stares hungrily"}

#Room set up:

#caferteria:
BigSpoon = {"Class":"Misc", "Desc":"A large Wooden Spoon about a foot and a half long, a little chipped at the ends", "Traits":{"Damage":1}}

Soda = {"Class":"Edible", "Desc":"A can of Diet Spripesi Cola Up, its the quenchiest! looks edible", "Traits":{"Damage":1, "Healing":1}}

HardGarbage = {"Class":"Misc", "Desc":"A hard solid mass of dried up Garvage, who knows what this used to be, its got some weight to it", "Traits":{"Damage":2}}

KitchenDoor = {"Locked":False, "Desc":"Inside you see what looks like a kitchen, and is that food?"}

SouthHallDoor = {"Locked":False, "Desc":"Looks like a hallway but heading in the south direction"}

WestHallDoor = {"Locked":True, "Desc":"Looks like a halway but heading in the weat direction"}

CourtyardDoor = {"Locked":True, "Desc":"looking through you see grass and a big fence"}

VendingMachine = {"Items":{"Can of Spripesi Cola Up":Soda}, "Desc":"A banged up old vending machine, looks like its still powered"}

TrashCan = {"Items":{"Hard Garbage":HardGarbage}, "Desc":"a dirty old trash can with the smell of old garbage coming out of it."}

PileofLeftovers = {"Items":{"Big Spoon":BigSpoon}, "Desc":"A smelly pile of waste that might possibly have been food lying on a table"}

Cafeteria = {"Doors":{"Kitchen Door":KitchenDoor, "South Hall Door":SouthHallDoor, "West Hall Door":WestHallDoor, "Courtyard":CourtyardDoor}, "Containers":{"Ground":None,"Trash Can":TrashCan, "Pile of leftovers":PileofLeftovers, "Vending Machine":VendingMachine}, "Characters":{"Zombie":Zombie}, "ShortDesc":"The moldy and messy Cafeteria appears to be unchanged and still dirty.", "LongDesc":"You walk into a big open room with rectangular dinning tables strewn about.  Old plates of food and broken chairs are thrown around, a smell of mold permeates the air, im glad im not hungry right now", "Visited":False}


#Courtyard:

Courtyard = {"Doors":{}, "Containers":{}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}


#Northhall:

NorthHall = {"Doors":{}, "Containers":{}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}


#Bloody cell:

BloodyCell = {"Doors":{}, "Containers":{}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}


#West Cell Block:

WestCellBlock = {"Doors":{}, "Containers":{}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}


#Waste Dump:

WasteDump = {"Doors":{}, "Containers":{}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}
                                        

#ToolShed

CourtyardDoor = {"Locked":True, "Desc":"This is the door to the Courtyard"}
                                        
Shovel = {"Class":"Key", "Desc":"You pick up a shovel, You can use it to break through somewhere", "Traits":{"Damage":3}}

Box = {"Items":{Shovel:Shovel}, "Desc":"You see a box with something inside"}

ToolShed = {"Door":CourtyardDoor, "Container's":{"Ground":"none", "Box":Shovel}, "Characters":"none", "ShortDesc":"The ToolShed", "LongDesc":'''As you enter the tool shed you see a locker full of shovels. You remember the countless days you spent digging holes for the prison under the hot sun. The guards would laugh as they poured your water in the hole infront of you, leaving you with a burning sensation in your throat with no way to quench your thirst. "Im glad those bastards are dead" you say to yourself.''', "Visited":False}                                    
        
