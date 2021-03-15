#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:52:34 2021

@author: user1
"""

class ConsoleManager:
    
    def __init__(self, room, command):
        self.room = room
        self.command = command
            
    
    def printRoom(self):
        return CompileOutput().playerRoomDescription(self.room)
        
    
    def printSuccess(self):
        if Translator().checkValidInput(self.command) == True:
            print("Sucess.")
        else:
            print("Invalid input. Please try again")
    
    if WorldHandler().checkEnd() == True:
        print("Game Over")
    
            