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

#creates a new game (Working)
def newgame():
    global player
    user_name = input("Please enter your name here: ")
    difficulty = input("Please enter a difficulty level here (easy, medium, hard, impossible): ")
    health = starting_health(difficulty)
    player = User(user_name, health, difficulty, 0, 0, 1)
    return player

#start of the program (WORKING, ADD ROOMS AS IT GOES)
def start():
    print("Do you wish to load a saved game or start a new one?")
    action = input("> ")
    """If statement to decide if loading or creating a new game"""
    for x in load:
        if x == action:
            loadgame('save.bin')
            loaded_user = loadgame('save.bin')
            room_num = loaded_user.room
            if room_num == 1:
                room1()
            elif room_num == 2:
                room2()
            elif room_num == 3:
                room3()
            elif room_num == 4:
                room4()
            else:
                print("error finding save file")
        else:
            pass
    if action == 'new':
        newgame()
        player.room == 1
        room1()
    else:
        print("Better select 'new' or 'load'")
        start()

#determination of difficulty (WORKING)
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

#function to save game (WORKING)
def savegame(filename):
    file_out = open(filename, 'wb')
    pickle.dump(player, file_out)
    file_out.close()

#function to load game (WORKING)
def loadgame(filename):
    try:
        file_in = open(filename, 'rb')
    except:
        print("Error opening save file")

    res = pickle.load(file_in)
    return res

#Pygame image display function (WORKING)
def disp_image(photo_file):
    pygame.init()

    carryOn = True
 
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1400,1000))
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                  carryOn = False 
 
     # --- Game logic
        loaded_photo = pygame.image.load(photo_file)
        screen.blit(loaded_photo, (0,0))
     # --- update the screen
        pygame.display.flip()
     
     # --- Limit to 60 frames per second
        clock.tick(60)
 
    pygame.quit()


#Start of rooms in dungeon crawl
def room1():

    disp_image("c:/Users/Jacob/OneDrive/Documents/Python homework/Final Project folder/First doors.PNG")

    print(" ")
    print("It was a dark and stormy night...")
    print("I mean, of course it was, that's how all these things seem to start I guess...")
    print("but it seems you don't really know that since you are deep underground in a dungeon of some kind.")
    print(" ")
    print("There are 3 doors in front of you in this barely lit room. To the left is a solid oak door. In front of you is a futuristic steel door, and to your right is an antique door with a brass knocker.")
    print(" ")    
    print("Through which door do you proceed?")
    action = input("> ")
    if action == "left":
        room2()
    elif action == "forward":
        room3()
    elif action == "right":
        room4()
    elif action == "save":
        savegame('save.bin')
        print("Saving completed,")
        room1()
    else:
        print("Well you can't just sit there all day, or maybe you can, or maybe you'll starve, who knows.")
        print("You should definitely enter just 'left', 'right', or 'forward'")
        room1()

def room2():
    print("room 2")

def room3():
    print("room3")

def room4():
    print("room4")
    


#to create ease for the user  (Not working as of right now, much)

left = ["Go Left", "go Left", "Go left", "go left", "Left", "left", "LEFT"]
right = ["Go Right", "go Right", "Go right", "go right", "right", "Right", "RIGHT"]
forward = ["Go Forward", "Go forward", "go Forward", "go forward", "Forward", "forward", "FORWARD", "forwards"]
back = ["Go back", "Go Back", "go Back", "go back", "back", "Back", "BACK", "backwards"]
attack = ["kill", "Attack", "attack"]
save = ["Save", "SAVE", "save game", "save"]
load = ["Load", "LOAD", "load", "load game"]
new_game = ["New Game", "New game", "new game", "NEW GAME", "new", "New", "NEW"]


start()


