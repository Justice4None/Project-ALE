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


class player_skills_strength:
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
        self.longblade = 0
        # The Long Blade skill lets your character use broadswords, sabers, longswords, claymores, katanas and dai-katanas effectively.


class player_skills_intelligence:
    def __init__(self):
        self.alchemy = 0,
        # Alchemy allows your character to identify magical properties in ingredients and create potions to generate useful temporary or onetime effects, such as healing, cure disease, water-walking, mana shielding, and fortifying body attributes. A higher Alchemy skill allows you to see more effects of ingredients when you inspect them.
        # The higher your character's Alchemy skill is, the more successful and powerful your created potions will be. You will also gather more ingredients with a higher Alchemy skill, and you will be albe to substitute certain ingredients for eachother.
        self.conjuration = 0,
        # Conjuration allows your character to dominate the minds of mundane and magical creatures, summon otherworldly weapons and armour, and occasionally, beings.
        # Conjuration also lets your character delve into the realm of Necromancy. If your character's mortal soul is damaged, or "wounded", enough, they can eclipse the mortal world and become a Lich. Liches cannot move in daylight, nor can they directly harm mortals. Liches can interact through the world with undead serveants and mortal worshippers.
        self.enchant = 0,
        # Enchanting is the process of permanently applying a magical effect to an item by harnessing the power of either the Aether or Abyss. This skill governs the creation, use, and recharging of enchanted items. Skilled enchanters are more likely to be successful at creating new items, their enchanted items use less power and are recharged more efficiently.
        self.security = 0,
        # The Security skill lets your character open locked doors and containers with lockpicks or wax keys, disarm traps with disarming kits or probes, and re-seal sealed documents after reading them. This skill is essential for agents and thieves alike. Unlocking a locked object is a crime, so make sure you're alone before you go snooping around in places you don't belong.
        self.medical = 0
        # The Medical skill lets your character diagnose and treat wounds and diseases without specific items or materials (i.e., medical kits and bandages). This skill is automatically used when your character rests for the night, but only if they sleep in a proper bed or have enough friendly/allied NPC's around.


class player_skills_willpower:
    def __init__(self):
        self.alteration = 0,
        # Alteration allows your character to manipulate the physical world and its natural properties. Alteration effects include water breathing and walking, jumping, levitating, burdening, opening and locking, and creating shield barriers against both physical and magical damage.
        self.destruction = 0,
        # Destruction allows your character to harm living and unliving things with magick. This usually included elemental damaged, draining, vulnerability, and disintegration effects.
        self.mysticism = 0,
        # Mysticism allows your character to shape and focus otherworldly forces to teleport the caster's body, manipulate the world with telekinesis, absorb or reflect magical energies, and sence unsee objects at a distance.
        # Mysticism is also the art of fortune-telling and future-reading. While used sparcely, this ability may come in handy...
        self.restoration = 0,
        # Restoration allows your character to heal, restore and fortify the body's attributes and abilities, cure disease and protect it from other malign influences.
        # Restoration can also aid in Necromancy (to a certain extent.).
        self.thaumaturgy = 0
        # Thaumaturgy allows your character to manipulate space and time in various ways, ranging from minute changes to world-altering phenomena.
        # Thaumaturgy takes a lifetime to master, and those who overstep their abilities have a way of vanishing...

class player_skills_agility:
    def __init__(self):
        self.block = 0,
        # Block allows your character to use shields to block any melee attack. Shields will not protect you from most ranged attacks, specifically magical ranged attacks. A successful block removes some of the damage from the oncoming attack, but at the expense of Fatigue loss.
        self.lightarmour = 0,
        # Light Armour lets your character move and defend while wearing light-weight, flexible armours like leather and fur more efficiently.
        self.marksman = 0,
        # The Marksman skill affects the use of ranged weapons such as short and long bows, crossbows, and throwing knives. Weapons that use the Marksman skill gain a bonus to damage if your character has a high Strength attribute.
        self.sneak = 0,
        # Sneak is the art of moving unseen and unheard. Those skilled in Sneak are also adept pickpockets. If a target is successfully hit while you are sneaking, the damage is multiplied by a certain amount based on the weapon's damage, your Strength attribute, and your Sneak skill.

class player_skills_speed:
    