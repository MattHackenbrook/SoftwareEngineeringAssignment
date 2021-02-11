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

ToolShed = {"Door":CourtyardDoor, "Container's":{"Ground":"", "Box":Box}, "Characters":"", "ShortDesc":"The ToolShed", "LongDesc":"As you enter the tool shed you see a locker full of shovels. You remember the countless days you spent digging holes for the prison under the hot sun. The guards would laugh as they poured your water in the hole infront of you, leaving you with a burning sensation in your throat with no way to quench your thirst. 'Im glad those bastards are dead' you say to yourself.", "Visited":False}                                    
        

#South Hall:

WestHallDoor = {"Locked":True, "Desc":"This leads to the West Hall"}

WashroomDoor = {"Locked":False, "Desc":"You can hear water running as you continue walking. This must be the door to the washroom"}

SouthCellBlockDoor = {"Locked":False, "Desc":"You see blood stains on the ground infront of the door. This leads to the South Cell Block"}

JanitorClosetDoor = {"Locked":True, "Desc":"This leads to the Janitor's Closet. There might be something useful in there"}

CafeteriaDoor = {"Locked":False, "Desc":"This leads to the Cafeteria."}

Zombie = {"Stats":{"Strength":1, "Thrift":0, "Persuasion":0, "Armour":1, "Health":1}, "Inventory":{}, "Wearing":None, "Desc":"A Zombie", "Class":"zombie"}

SouthHall = {"Doors":{"West Hall Door":WestHallDoor, "Washroom Door":WashroomDoor, "South Cell Block Door":SouthCellBlockDoor, "Janitor's Closet Door":JanitorClosetDoor, "Cafeteria Door":CafeteriaDoor}, "Containers":{"Ground":""}, "Characters":{"Zombie":Zombie, "Zombie2":Zombie}, "ShortDesc":"The South Hall", "LongDesc":"The South Hall looks completely abandoned just like West Hall did. You see several corpses with missing limbs and what looks like bites that have been taken out of them. As you take a closer look you see a corpse with its eyes wide open and quickly realize it was your good friend Jeff. You take a moment to close his eyes and pray that he is in a better place now. A tear runs down your face as you get up and continue to move on trying to escape this hellhole.", "Visited":False}

#Hospital Ward:


WestHallDoor = {"Locked":True, "Desc":"This leads to the West Hall"}

NorthHallDoor = {"Locked":True, "Desc":"Leads to the North Hall"}

NurseZombie = {"Stats":{"Strength":1, "Thrift":0, "Persuasion":0, "Armour":1, "Health":1}, "Inventory":{}, "Wearing":None, "Desc":"A zombie wearing a nurse uniform", "Class":"zombie"}

Pills = {"Class":"Edible", "Desc":"You find some pills, they might be able to recover some health, or just get you really high.", "Traits":{"Healing":5}}

SurgicalKnife = {"Class":"melee", "Desc":"You find a surgical knife with some blood still left on it. This place was never that clean anyway", "Traits":{"Damage":3}}

Cabinet = {"Items":{"Pills":Pills}, "Desc":"As you approach the cabinet, you can see some things inside that might be useful"}

Tray = {"Items":{"Surgical Knife":SurgicalKnife}, "Desc":"You see a surgical knife layed out on the tray"}

HospitalWard = {"Doors":{"West Hall Door": "North Hall Door":NorthHallDoor}, "Containers":{"Ground":"","Cabinet":Cabinet, "Tray":Tray}, "Characters":{"Nurse Zombie":NurseZombie}, "ShortDesc":"The Hospital Ward", "LongDesc":"You open the door and see a bed and a tray in the middle of the room. You look to your right and see the medical cabinet in the corner. 'There must be something in here I can use' you say to yourself. As you search the room you remember the time that Ivan almost beat you to death because you didn't give him your cookies. You spent a week in pain recovering in the Hopsital Ward, but it was nice not having to be in that cell for a little bit", "Visited":False}


#Washroom

SouthHallDoor = {"Locked":False, "Desc":"This leads to the South Hall"}

SewerDoor = {"Locked":True, "Desc":"You see a crack in the floor that looks like it might lead somewhere. You need a something strong like a sledgehammer to break through."}

Pipe = {"Class":"melee", "Desc":"This pipe must have fallen from the ceiling after the pipes burst", "Traits":{"Damage":2}}

Washroom = {"Doors":{"South Hall Door":SouthHallDoor, "Sewer":SewerDoor}, "Containers":{"Ground":Pipe}, "Characters":"", "ShortDesc":"The Washroom", "LongDesc":"You can hear the slow fall of water dripping from the ceiling, you take a step forward and feel something wet at your feet. You look down to see you are standing in a pool of blood. The washroom has been the place of many unspeakable acts, but thankfully you have never dropped the soap and are safe from the traumatizing experience other inmates faced. As you examine the room you notice a giant crack in the floor and see a small pipe next to it.", "Visited":False}

#Ivan's Cell

NorthCellBlockDoor = {"Locked":False, "Desc":"This leads to the North Cell Block"}

Sledgehammer = {"Class":"melee", "Desc":"A giant sledgehammer, good for smashing.", "Traits":{"Damage":7}}

Ivan = {"Stats":{"Strength":"20", "Thrift":"1", "Persuasion":"0", "Armour":"5", "Health":"10"}, "Inventory":{"Sledgehammer":Sledgehammer}, "Wearing":None, "Desc":"Ivan is a 7ft tall giant. No one in the prison messes with him because he will literally kill you. He can be a great ally, but an even worse enemy.", "class":""}

IvanCell = {"Doors":{"NorthCellBlockDoor":NorthCellBlockDoor}, "Containers":{"Ground":""}, "Characters":{"Ivan":Ivan}, "ShortDesc":"Ivan's Cell", "LongDesc":"This cell belongs to Ivan. The beast of the prison. You heard stories about how he killed 10 men with only his fists. You do not want to run into this guy", "Visited":False}

#Janitor’s Closet:

HalfUsedCrackPipe = {"Class":"Misc", "Desc":"Joe Dirt's half used crack pipe, if i smoke it should help with my withdrawals", "Traits":{"Healing":1}}

BandAids = {"Class":"Misc", "Desc":"Band-aids may come in handy if i run into zombies or worse", "Traits":{"Healing":3}}

SouthHallDoor = {"Locked":False, "Desc":"Looks like a hallway but heading in the south direction"}

JoesDrawer = {"Items":{"Half Used Crack Pipe":HalfUsedCrackPipe,"Band Aids":BandAids },"Desc":"Joe Dirt's draw is left open, he must of left in a rush"}

JanitorsCloset = {"Doors":{"South Hall Door":SouthHallDoor}, "Containers":{"Ground":None, "JoesDrawer":JoesDrawer}, "Characters":{}, "ShortDesc":"The Janitor’s Closet is a small room in the south hall.", "LongDesc":"The Janitor’s Closet is a small room in the south hall. Joe Dirt's the prison Janitor, he doens't carry a weapon but he's always high, his stash might be inside the closet. As you approach you don't hear any zombies inside", "Visited":False}


#West Hall:

WestCellBlockDoor = {"Locked":True, "Desc":"Dirty floor and walls , zombie free for now"}

EasterEggRoomDoor = {"Locked":True, "Desc":"there seems to be music playing and fuzz images in the back of the room, need to get closer"}

HospitalDoorW = {"Locked":True, "Desc":"A series of what looks like unmade beds with dirty white sheets"}

NorthHallDoorW = {"Locked":True, "Desc":"A long dirty corridor, must be the North hallway it looks like it has some other doors"}

SouthHallDoorW = {"Locked":True, "Desc":"A long dirty corridor, must be the South hallway it looks like it has some other doors"}

Syringe = {"Class":"melee", "Desc":"A used syringe, can be used to poision", "Traits":{"Damage":5}}

WestHall = {"Doors":{"West Cell Block Door":WestCellBlockDoor, "Easter Egg Room Door":EasterEggRoomDoor, "Hospital Door":HospitalDoorW, "North Hall Door":NorthHallDoorW, "South Hall Door":SouthHallDoorW}, "Containers":{"Ground":Syringe}, "Characters":{}, "ShortDesc":"the long ominous hallway with doors for the Hospital wing, north and south hallway and West cell block", "LongDesc":"", "Visited":False}



#Guard room:

CourtYardDoor = {"Locked":True, "Desc":"You can see into the courtyard, from what you can tell this is how you entered the prison, but now there's a bunch of zomies roaming around"}

NorthHallDoorG = {"Locked":False, "Desc":"A long dirty corridor, must be the North hallway it looks like it has some other doors"}

BulletProofVest = {"Class":"Misc", "Desc":"A old vest with stab marks, but it's bullet proof", "Traits":{"Damage":1, "Health":15}}

Gun = {"Class":"Misc", "Desc":"The Guards Gun still has ammo, this will come in handy real soon", "Traits":{"Damage":15}}

PrisonGuard = {"Stats":{"Strength":10, "Thrift":2, "Persuasion":0, "Armour":15, "Health":15}, "Inventory":{"Gun":Gun}, "Wearing":"Bullet Proof Vest":BulletProofVest, "Desc":"A Guard is hiding under his desk, he's been beaten and is scared", "Class":"PrisonGuard"} 

WestHall = {"Doors":{"CourtYard Door":CourtYardDoor, "North Hall Door":NorthHallDoorG, "Containers":{"Ground":BulletProofVest,Gun}, "Characters":{"Prison Guard":PrisonGuard}, "ShortDesc":"The guards room is dimminly lit, maybe everyone left but its worth checking out for weapons", "LongDesc":"", "Visited":False}

