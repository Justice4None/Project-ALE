# Python Text RPG #
# By William Dunn #

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# Player Setup #


class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mana = 0
        self.astrological = ''
        self.food = 0
        self.water = 0
        self.rest = 0
        self.status_effects = []
        self.location = 'start'


my_player = player()

# Title Screen #


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()  # Placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("creatures"):
        creature_menu()
    while option.lower() not in ['play', 'help', 'quit', 'creatures']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()  # Placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('###########################')
    print('# Tales of Olora Text RPG #')
    print('###########################')
    print('#          Play           #')
    print('#          Help           #')
    print('#          Quit           #')
    print('###########################')
    print('#   Copyright 2019 J4N    #')
    print('###########################')
    title_screen_selections()


def help_menu():
    print('###########################')
    print('# Tales of Olora Text RPG #')
    print('###########################')
    print('# Type north, south, east #')
    print('#     or west to move.    #')
    print('###########################')
    print('# Type basic commands to  #')
    print('#      execute them.      #')
    print('###########################')
    print('# Type "look" to inspect  #')
    print('#       something.        #')
    print('###########################')
    print('# You need to sleep, eat  #')
    print('# & drink to stay alive.  #')
    print('#  Type "eat -food-" to   #')
    print('# eat, "drink -liquid- to #')
    print('#  drink, and "sleep" to  #')
    print('#  rest your weary body.  #')
    print('###########################')
    print('#   Copyright 2019 J4N    #')
    print('###########################')
    title_screen_selections()


def creature_menu():
    print('###########################')
    print('#          Human          #')
    print('  ')
    print('           ')

# Game Functionality #


# Map #
#####
              -----------
             /           \
            / *          /
        __--          * /
       /           __---
       \        * / 
        \         |
         \        \ 
          \  *    /  
          |      /
          |    _/
          |   /
          \ */
           --
#####
# Zones are numbered from North to South, the Northern-most Zone being Zone 1 #
# Player starts in Zone 2 #

DESCRIPTION = 'description'
EXAMINATION = 'examine'
NORTH = 'north', 'up'
SOUTH = 'south', 'down'
EAST = 'east', 'right'
WEST = 'west', 'left'

explored_places = {'z1': False, }
