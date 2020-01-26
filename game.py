import jsonpickle
import os
import sys
import time
import random
from random import randint
import textwrap
screen_width = 100

# Class for the player character


class player:
    def __init__(self):
        self.name = ''
        # The player character's name.

        self.description = ""
        # The player character's written description.

        self.status = ''
        # The player character's written status.

        self.health = 20
        # The player character's health points.

        self.mana = 45
        # The player character's mana points. Mana allows the player character to use magic if they have learned the proper skills and spells to do so safely. Practicing magic without the proper knowledge is very dangerous and can easily lead to death or dismemberment.

        self.copper = 50
        # The player character's on-hand Copper. 10 Copper coins are equivalent to 1 Silver coin.

        self.silver = 20
        # The player character's on-hand Silver. 10 Silver coins are equivalent to 1 Gold coin.

        self.gold = 0
        # The player character's on-hand Gold. Gold is the highest value common coin.

# Class for the player character's core attributes.


class playerAttr:
    def __init__(self):
        self.vigor = 1
        # Vigor defines the player character's physical strength.

        self.brilliance = 1
        # Brilliance defines the player character's intellect.

        self.judgement = 1
        # Judgement defines the player character's understanding of various things.

        self.finesse = 1
        # Finesse defines the player character's agility and dexterity.

        self.physique = 1
        # Physique defines the player character's bodily condition.

        self.appeal = 1
        # Appeal defines the player character's ability to make people like them.

        self.advantage = 1
        # Advantage defines the player charcter's luck.

# Class for the player character's skills.


class playerSkills:
    def __init__(self):
        self.acrobatics = 0
        # The player character's Acrobatics skill is defined by their Finess and Vigor attributes.

        self.hermetics = 0
        # The player character's Hermetics skill is defined by their Brilliance and Judgement attributes.

        self.abjuration = 0
        # The player character's Abjuration skill is defined by their Brilliance attribute.

        self.armorsmith = 0
        # The player character's Armorsmith skill is defined by their Vigor attribute.

        self.weaponsmith = 0
        # The player character's Weaponsmith skill is defined by their Vigor attribute.

        self.block = 0
        # The player character's Block skill is defined by their Physique and Finesse attributes.

        self.blade = 0
        # The player character's Blade skill is defined by their Finess and Brilliance attributes.

        self.conjuration = 0
        # The player character's Conjuration skill is defined by their Judgement and Appeal attributes.

        self.persuasion = 0
        # The player character's Pursuasion skill is defined by their Appeal attribute.

        self.disguise = 0
        # The player character's Disguise skill is defined by their Brilliance and Appeal attributes.

        self.elemental = 0
        # The player character's Elemental skill is defined by their Finess and Brilliance attributes.
