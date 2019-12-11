import jsonpickle
import os
import sys
import time
import random
from random import randint
import textwrap
screen_width = 100

# Class for the player character
# I'm using a D&D-style money system.
# 10 Copper = 1 Silver
# 10 Silver = 1 Gold
class player:
    def __init__(self):
        self.name = ''
        self.status = ''
        self.health = 20
        self.mana = 45
        self.copper = 50
        self.silver = 20
        self.gold = 0

