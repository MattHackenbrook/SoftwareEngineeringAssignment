#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:52:34 2021

@author: user1
"""
import CompileOutput
# import Translator
import WorldHandler
import parserCommand
from CommandModel import Action

class ConsoleManager:

    def __init__(self, room):
        self.room = room
        self.userInput = ""

    def readUserInput(self):
        self.userInput = input("... ")
        if self.userInput == "inventory" or self.userInput == "inv":
            print("Your inventory contains: ")
            for item in self.room[1].characters["Player"].inv.keys():
                print(item)
            return False
        return True

    def printRoom(self):
        try:
            if self.room[1].visited == False:
                print(self.room[1].longDesc)
            else:
                print(self.room[1].shortDesc)
            print("You may find items in/on the: ")
            for container in self.room[1].containers.keys():
                print(container)
            print("\nThis room contains the characters: ")
            for character in self.room[1].characters.keys():
                if character != "Player":
                    print(character)
            print("\nThis room contains doors leading to: ")
            for door in self.room[1].doors.keys():
                print(door)
        except TypeError:
            if self.room.visited == False:
                print(self.room.longDesc)
            else:
                print(self.room.shortDesc)
            print("You may find items in/on the: ")
            for container in self.room.containers.keys():
                print(container)
            print("\nThis room contains the characters: ")
            for character in self.room.characters.keys():
                if character != "Player":
                    print(character)
            print("\nThis room contains doors leading to: ")
            for door in self.room.doors.keys():
                print(door)

    def printFailure(self, command):
        if parserCommand.checkValidCommand(command) == False:
            if command.action == Action.UNLOCK:
                print("the target is already unlocked or you do not have the item that unlocks it")
            if command.action == Action.ENTER:
                print("the door is currently locked")
            elif command.action != "" and command.action != None:
                print("that item or object is not available to you")
            elif command.action != None:
                print("Invalid input. Please try again")
            return False
        else:
            return True

    def endGame(self):
        if WorldHandler().checkEnd() == True:
            print("Game Over")

    def helper(self):
        print('''You have 8 different commands you can use in the game.
1.Unlock
2.Throw
3.Hit
4.Take
5.Inspect
6.Eat
7.Wear
8.Enter 
You can also check your inventory using:
inv

''' + self.room[1].longDesc)
