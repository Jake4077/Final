import random
import time
import pygame
import sys

from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1600,900))
pygame.display.set_caption('FInal Game')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# User class to keep track of info of player in game
class User():
    def __init__(self, user_name, health, difficulty, pickaxe, ladder, ): #Enter in the tools available in the game here
        self.user_name = user_name
        self.health = health
        self.difficulty = difficulty

user_name = input("Please enter your name here:") #Inputs need to be transfered to Pygame
difficulty = input("Please enter a difficulty level here (easy, medium, hard, impossible):")
#function for input of health
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

health = starting_health(difficulty)

player = User(user_name, health, difficulty, 0, 0)
    

