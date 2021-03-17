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
