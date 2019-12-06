import random
import time
import pygame
import sys
import pickle

#Stores info on the game User
class User():
    def __init__(self, user_name, health, difficulty, pickaxe, ladder, room): #Enter in the tools available in the game here and room number (for saves)
        self.user_name = user_name
        self.health = health
        self.difficulty = difficulty
        self.room = room

#creates a new game
def newgame():
    user_name = input("Please enter your name here:")
    difficulty = input("Please enter a difficulty level here (easy, medium, hard, impossible):")
    return user_name, difficulty

#start of the program
def start():
    print("Do you wish to load a saved game or start a new one?")
    action = input()
    """If statement to decide if loading or creating a new game"""
    if load in action:
        loadgame()
    elif new_game in action:
        newgame()

#determination of difficulty
def starting_health(difficulty):
    while starting_health != 1 or starting_health !=3 or starting_health != 5 or starting_health != 7:
        if difficulty == "easy":
            return 7
        elif difficulty == "medium":
            return 5
        elif difficulty == "hard":
            return 3
        elif difficulty == "impossible":
            return 1
        else:
            difficulty = input("Please enter difficulty as exactly 'easy', 'medium', 'hard', or 'impossible':")

#function to save game
def savegame():
    with open('savefile', 'w') as f:
        pickle.dump(f)

#function to load game
def loadgame():
    with open('savefile') as f:
        pickle.load(f)

#to create ease for the user
left = ["Go Left", "go Left", "Go left", "go left", "Left", "left", "LEFT"]
right = ["Go Right", "go Right", "Go right", "go right", "right", "Right", "RIGHT"]
forward = ["Go Forward", "Go forward", "go Forward", "go forward", "Forward", "forward", "FORWARD", "forwards"]
back = ["Go back", "Go Back", "go Back", "go back", "back", "Back", "BACK", "backwards"]
attack = ["kill", "Attack", "attack"]
save = ["Save", "SAVE", "save game", "save"]
load = ["Load", "LOAD", "load", "load game"]
new_game = ["New Game", "New game", "new game", "NEW GAME", "new", "New", "NEW"]


start()


