Action = {'THROW': 'TO THROW',
          'HIT': 'TO HIT'}


 
def parserCommand(Action):
    print("\nWhat action do you want to take?: ")
    for choice in Action:
         [print(key, ' : ', value) for key, value in Action.items()]
    choice = ''
    while choice not in Action.keys():
        choice = input("\nWhat is your choice? ")
        choice = str(choice)
    return choice

def parse_input(input):
    command = ""
    command_words = list(input.split(" "))
    new_command = []
    
    for word in command_words:
        if word not in QUIT_HELP:
            if word in doorList:
                new_command.append(doorList[word])
        if word not in QUIT_HELP:
            if word in containerList:
                new_command.append(containerList[word])
        if word not in QUIT_HELP:
            if word in itemList:
                new_command.append(itemList[word])
        if word not in QUIT_HELP:
            if word in characterList:
                new_command.append(characterList[word])

    for word in new_command[:2]:
        command = command + word + " "
    command = command.strip()
    return command
