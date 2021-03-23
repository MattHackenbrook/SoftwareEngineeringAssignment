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


def parser(input):
    command = ""
    command_words = list(input.split(" "))
    new_command = []
    for word in command_words:
        if word not in Quit_words:
            if word in Action:
                new_command.append(Action[word])
