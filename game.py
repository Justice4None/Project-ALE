import jsonpickle
import os
import sys
import time
import random
from random import randint
import textwrap
screen_width = 100


class player_info:
    def __init__(self):
        self.name = "",
        # The name of your character.
        self.desc = "",
        # The description of your character. Written by the player.
        self.status = "",
        # The status of your character. Automatically generated based on Health, Mana, and Fatigue levels.


class player_piggybank:
    def __init__(self):
        self.copper = 5,
        # How much Copper Coin your character is currently carrying. 10 Copper Coins = 1 Silver Coin.
        self.silver = 1,
        # How much Silver Coin your character is currently carrying. 10 Silver Coins = 1 Gold Coin.
        self.gold = 0,
        # How much Gold Coin your character is currently carrying.


class player_stats:
    def __init__(self):
        self.health = 50,
        # Affects the amount of damage that can be taken before being killed.
        self.mana = 15,
        # Affects the amount of energy available for spellcasting.
        self.fatigue = 30,
        # Affects all actions performed by your character (melee, spells, lockpicking, speech, etc.).
        self.encumberance = 50,
        # Affects carrying capacity and movement speed.
        self.languages = "",
        # What languages your character can fluently speak.


class player_misc:
    def __init__(self):
        self.reputation = "",
        # Your character's reputation with various factions, guilds and people.
        self.bounty = 0,
        # The amount of money being offered for you capture or death, based on what crimes you've been caught committing.


class player_attributes:
    def __init__(self):
        self.strength = 1,
        # Affects weapon damage, weapon durability (degradation rate upon each successful hit; higher Strength results in higher weapon degradation.), and carrying capacity. It also helps determine maximum Fatigue and starting Health.
        self.intelligence = 1,
        # Affects maximum Mana. 15% of Intelligence is the amount of Mana gained per hour of rest. Intelligence also affects Alchemy and Enchanting results.
        self.willpower = 1,
        # Affects spellcasting success rate and resistance to Magicka. It also determines maximum Fatigue.
        self.agility = 1,
        # Affects weapon hit rate, evasion, resistance to staggering and knock down, and success rate of multiple actions. Agility also affects maximum Fatigue.
        self.speed = 1,
        # Affects character movement speed (walking, running, swimming, climbing and levitating.).
        self.endurance = 1,
        # Affects starting and maximum Health, and your maximum Fatigue. Also slows down Fatigue loss while running and fighting.
        self.personality = 1,
        # Affects success rate of persuasion and haggling.
        self.luck = 1,
        # Affects every "dice roll" in the game.


class player_skills:
    def __init__(self):
        self.acrobatics = 0,
        # The Acrobatics skill involves jumping, climbing, and avoiding damage from falls. The higher one's Acrobatics, the higher one can jump vertically, the farther one can jump horizontally, and the greater the height one may fall from (or jump down on purpose). Those skilled in Acrobatics can reach areas others cannot get to. With Acrobatics pushed by magic to abnormally high levels, one can jump and fall rather extreme distances.
        # This skill is extremely useful for travel. Combined with lots of speed, using Acrobatics is by far the fastest way to get from place to place on foot.
        self.armourer = 0,
        # The Armourer skill is used to maintain weapons and armour at top effectiveness. Damaged weapons do less damage. Damaged armour provides less protection against attacks. As wear increases, the diminishing effectiveness  of weapons and armor becomes dramatic.
        # This represents your skill at repairing damaged armour and weapons. To repair an item, you will need the proper tools to do so. This skill can be invaluable if your gear is severely damaged while you are not near enough to a Blacksmith to pay for repairs.
        self.axe = 0,
        # The Axe skill helps your character wield heavy chopping weapons like war axes and battleaxes more effectively.
        self.blunt = 0,
        # The Blunt skill makes your character more effective when using bashing weapons like maces, hammers, clubs or staves.
        self.longblade = 0,
        # The Long Blade skill lets your character use broadswords, sabers, longswords, claymores, katanas and dai-katanas effectively.
        self.