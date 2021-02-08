import json

Prison_Rooms = {
    "toolShed":{
        "LongDesc":'''As you enter the tool shed you see a locker full of shovels. 
                You remember the countless days you spent digging holes for the prison
                under the hot sun. The guards would laugh as they poured your water
                in the hole infront of you, leaving you with a burning sensation
                in your throat with no way to quench your thirst. "Im glad those
                bastards are dead" you say to yourself.''',
                "ShortDesc":"The ToolShed",
                "Visited":False,
                "Doors":{
                    "Courtyard":{
                        "Locked":False,
                        "Health": 10,
                        "Desc":'''You can hear the screams from the horde of 
                                  zombies in the courtyard'''}
                    },
                "Container":"Shovel",    
                "Characters": "none"
    },
                "Items":{
                    "Shovel":{
                        "Class":"Special Item",
                        "Desc":'''You pick up a shovel, You can use it to break 
                                through somewhere''',
                        "Traits":{
                        "Damage":3,    
                            }
                        
                                
                        }        
             }
}

x = json.dumps(Prison_Rooms)
print(x)
