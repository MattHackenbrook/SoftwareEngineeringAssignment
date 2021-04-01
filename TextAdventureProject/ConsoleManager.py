#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:52:34 2021

@author: user1
"""
import CompileOutput
#import Translator
import WorldHandler
import parserCommand


class ConsoleManager:
    
    def __init__(self, room):
        self.room = room
        self.userInput = ""
            
    def readUserInput(self):
        self.userInput = input("... ")
        return self.userInput
        
        
    def printRoom(self):
        if self.room.visited == False:
           print(self.room.longDesc)
        else:
            print(self.room.shortDesc)
    
    def printFailure(self, command):
        if parserCommand.checkValidCommand(command) == False:
             print("Invalid input. Please try again")
             return False
        else:
            return True
    
    def endGame(self):
        if WorldHandler().checkEnd() == True:
            print("Game Over")
    
    def helper(self):
        print('''You have 7 different commands you can use in the game.
                 1.Use
                 2.Throw
                 3.Hit
                 4.Take
                 5.Inspect
                 6.Speak
                 7.Go 
                  ''' + self.room.longDesc)
                  
                
