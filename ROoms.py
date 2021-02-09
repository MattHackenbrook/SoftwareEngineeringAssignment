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

#Character = {"Stats":{"Strength":"", "Thrift":"", "Persuasion":"", "Armour":"", "Health":""}, "Inventory":{}, "Wearing":None, "Desc":"", "class":""}

#Item = {"Class":"", "Desc":"", "Traits":{"Damage":0}}

#Room = {"Doors":{}, "Containers":{"Ground",}, "Characters":{}, "ShortDesc":"", "LongDesc":"", "Visited":False}

#presets:
    
Zombie = {"Stats":{"Strength":1, "Thrift":0, "Persuasion":0, "Armour":1, "Health":1}, "Inventory":{}, "Wearing":None, "Desc":"A Zombie, missing a jaw looks around with only one eye that stares hungrily", "Class":"zombie"} 

#Room set up:

#caferteria:
BigSpoon = {"Class":"Misc", "Desc":"A large Wooden Spoon about a foot and a half long, a little chipped at the ends", "Traits":{"Damage":1}}

Soda = {"Class":"Edible", "Desc":"A can of Diet Spripesi Cola Up, its the quenchiest! looks edible", "Traits":{"Damage":1, "Healing":1}}

HardGarbage = {"Class":"Throwable", "Desc":"A hard solid mass of dried up Garvage, who knows what this used to be, its got some weight to it", "Traits":{"Damage":2, "throw":2}}

KitchenDoor = {"Locked":False, "Desc":"Inside you see what looks like a kitchen, and is that food?"}

SouthHallDoor = {"Locked":False, "Desc":"Looks like a hallway but heading in the south direction"}

WestHallDoorCaf = {"Locked":True, "Desc":"Looks like a halway but heading in the weat direction"}

CourtyardDoor = {"Locked":True, "Desc":"looking through you see grass and a big fence"}

VendingMachine = {"Items":{"Can of Spripesi Cola Up":Soda}, "Desc":"A banged up old vending machine, looks like its still powered"}

TrashCan = {"Items":{"Hard Garbage":HardGarbage}, "Desc":"a dirty old trash can with the smell of old garbage coming out of it."}

PileofLeftovers = {"Items":{"Big Spoon":BigSpoon}, "Desc":"A smelly pile of waste that might possibly have been food lying on a table"}

Cafeteria = {"Doors":{"Kitchen Door":KitchenDoor, "South Hall Door":SouthHallDoor, "West Hall Door":WestHallDoorCaf, "Courtyard":CourtyardDoor}, "Containers":{"Ground":None,"Trash Can":TrashCan, "Pile of leftovers":PileofLeftovers, "Vending Machine":VendingMachine}, "Characters":{"Zombie":Zombie}, "ShortDesc":"The moldy and messy Cafeteria appears to be unchanged and still dirty.", "LongDesc":"You walk into a big open room with rectangular dinning tables strewn about.  Old plates of food and broken chairs are thrown around, a smell of mold permeates the air, im glad im not hungry right now", "Visited":False}


#Courtyard:

FrontGateDoor = {"Locked":True, "Desc":"Through the metal Iron bars, it looks like theres another gate accross this control room that leads to the road, freedom."}

GuardRoomDoorExt = {"Locked":True, "Desc":"there are some computer screens that are still lit and something that looks like a metal cylinder."}

CafeteriaDoor = {"Locked":True, "Desc":"Looks like theres a mess of dinning tables and what looks like piles of waste all over."}

SouthHallDoor = {"Locked":True, "Desc":"There is a long dim lit corridor that seems to lead on for a bit."}

ToolShedDoor = {"Locked":True, "Desc":"A small dark room, you see some odd shapes in the shadows"}

Basketball = {"Class":"Throwable", "Desc":"A roughted up faded orange basketball", "Traits":{"Damage":1, "Throw":1}}

Horde = {"Stats":{"Strength":"50", "Thrift":"0", "Persuasion":"0", "Armour":"50", "Health":"50"}, "Inventory":{}, "Wearing":None, "Desc":"A Huge horde of almost 50 zombies wanders around aimlesly together as they look for any way to move around.", "class":"Horde"}

Courtyard = {"Doors":{"Front Gate Door":FrontGateDoor, "Guard Room Door":GuardRoomDoorExt, "Cafeteria Door":CafeteriaDoor, "South Hall Door":SouthHallDoor, "Tool Shed Door":ToolShedDoor}, "Containers":{"Ground":Basketball}, "Characters":{"Horde":Horde}, "ShortDesc":"The dried grass sways in the wind and the concreete walls stand firm", "LongDesc":"A cobblesstone path leads out to the front gate.  Dried grass makes up the field ahead as the concreet walls sourrounding you arecovered by moss with barbed wire wrapped around the top, an orange sphere is vissible in the field", "Visited":False}


#Northhall:

NorthCellBlockDoor = {"Locked":True, "Desc":"Dirty floor and walls and what looks like 2 moving bodies"}

GuardRoomDoorInt = {"Locked":True, "Desc":"there are some computer screens that are still lit and something that looks like a metal cylinder."}

HospitalDoorN = {"Locked":True, "Desc":"A series of what looks like unmade beds with dirty white sheets"}

WestHallDoorN = {"Locked":True, "Desc":"A long dirty corridor, must be the West hallway it looks like it has some other doors"}

Shank = {"Class":"melee", "Desc":"A small plactic toothrush with a sharp filled end", "Traits":{"Damage":3}}

NorthHall = {"Doors":{"North Cell Block Door":NorthCellBlockDoor, "Guard Room Door":GuardRoomDoorInt, "Hospital Door":HospitalDoorN, "West Hall Door":WestHallDoorN}, "Containers":{"Ground":Shank}, "Characters":{}, "ShortDesc":"the long ominous hallway with doors for the Hospital wing, West hallway and north cell block", "LongDesc":"A long dusty hallway stretches ahead with another barred door at the other end, along with others leading to what seems like more cells.  One of these doors has a red cross on it. there are scattered belongings accross the floor", "Visited":False}


#Bloody cell:

SouthCellBlockDoor = {"Locked":False, "Desc":"what looks like the empty cell block, the window is smudged in blood"}   

Limb = {"Class":"Misc", "Desc":"a bloody hand attached to what remains of an arm", "Traits":{"Damage":1}} 

BloodyCell = {"Doors":{"South Cell Block Door":SouthCellBlockDoor}, "Containers":{"Ground":Limb}, "Characters":{}, "ShortDesc":"a bloody mess on the floor from the previous inmates remains", "LongDesc":"A grotestesque scene of blood and gore, it looks as though the inmate who belonged in this cell is now the bloody puddle of red slop in the floor. the cell is turned upsidedown, there must have been a terrible struggle before he was pinned down on the floor and eaten alive. note to self, dont get cornered.", "Visited":False}


#West Cell Block:
    
StartDoor = {"Locked":False, "Desc":"its the door that leads to your cell, nothing new"}

WestHallDoor= {"Locked":False, "Desc":"You see that there is a hallway beyond, this must be the door to the west hall"}

Key = {"Class":"Key", "Desc":"a small key card with some drops of blood", "Traits":{"Damage":0, "opens":[]}}

Corpse = {"Items":{"key":Key}, "Desc":"the mutilated corpse of one of the inmates, Pedro, face first in the ground, his back completly devoured.  his right arm is outstretched looks like he was holding something. Bugger always had sticky fingers"}

WestCellBlock = {"Doors":{"My Cell Door":StartDoor, "West Hall Door":WestHallDoor}, "Containers":{"Ground":None, "Corpse":Corpse}, "Characters":{}, "ShortDesc":"the now completly destroyed cell block lacks any of its former security, or sanitation due to the blodd.  Poor Pedros burial will have to wait", "LongDesc":"The familiar cell block no longer looks the same.  the once clean interior is now spattered with blood, littered with broken furniture, busted cell doors and metal bars, near the exit door you see the body of an inmate, he looks like someone you know.", "Visited":False}


#Waste Dump:

WasteDumpDoor = {"Locked":False, "Desc":"small metal bars attached to a hinge, the sewage tunnel you came through is beyond"}    

HalfZombie = {"Stats":{"Strength":1, "Thrift":-1, "Persuasion":0, "Armour":0, "Health":1}, "Inventory":{}, "Wearing":None, "Desc":"A zombie missing the lower half of its body tried to painfully crawl its way towards you using one of its decaying arms", "class":"legless"}

WasteDump = {"Doors":{"Waste dump door":WasteDumpDoor}, "Containers":{"Ground":None}, "Characters":{"Half Zombie":HalfZombie}, "ShortDesc":"opening up around you is the dump for all the sewage from the entire prison, gross", "LongDesc":"As you travel down this tunnel of refuse you slide out into the open air and land into an even bigger pile of waste as you are dumped out of the prison's sewage, as you are inches away from freedom.  theres seems to be something moving in the waste with you.", "Visited":False}
                                        

#ToolShed

CourtyardDoor = {"Locked":True, "Desc":"This is the door to the Courtyard"}
                                        
Shovel = {"Class":"Key", "Desc":"You pick up a shovel, You can use it to break through somewhere", "Traits":{"Damage":3}}

Box = {"Items":{"Shovel":Shovel}, "Desc":"You see a box with something inside"}

ToolShed = {"Door":CourtyardDoor, "Container's":{"Ground":"", "Box":Shovel}, "Characters":"", "ShortDesc":"The ToolShed", "LongDesc":"As you enter the tool shed you see a locker full of shovels. You remember the countless days you spent digging holes for the prison under the hot sun. The guards would laugh as they poured your water in the hole infront of you, leaving you with a burning sensation in your throat with no way to quench your thirst. 'Im glad those bastards are dead' you say to yourself.", "Visited":False}                                    
        
