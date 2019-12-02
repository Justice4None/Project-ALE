import jsonpickle
import os
import sys
import time
from random import randint

go = True
IsShopLocked = False
IsDaggerEquipped = False
IsSwordEquipped = False
IsLeatherHideEquipped = False

SAVEGAME_FILENAME = 'savegame.json'

game_state = dict()


class Human(object):
    def __init__(self, name, health, strength, gold):
        self.name = name
        self.health = health
        self.strength = strength
        self.gold = gold


class AI(object):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength


class Item(object):
    def __init__(self, name, hvalue, strvalue):
        self.name = name
        self.hvalue = hvalue
        self.strvalue = strvalue


def load_game():
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))


def initialize_game():
    global game_state
    player = Human('Lloyd', 100, 10, 1000)
    enemy = AI('Terrance', 50, 20)

    state = dict()
    state['players'] = [player]
    state['npcs'] = [enemy]
    return state


def Shop():
    global game_state
    player = game_state['players'][0]
    dagger = Item('Dagger', 0, 5)
    sword = Item('Sword', 0, 10)
    leather_hide('Leather Hide', 5, 0)
    if IsShopLocked = True:
        print("The shop is locked!\nPlease go back and continue your adventure!")
    else:
        print()
        print("Welcome to the Cuntsville shop! What would you like to buy?\n1. Weapons\n2. Armor\n3. Go back")
        selection = int(input("Enter a value: "))

    if selection == 1:
        if player.gold >= 50:
            print("Weapons shop")
            print("1. Bronze Dagger: $20\n2. Bronze Sword: $50")
            wpnselection = int(input("Enter a value: "))

        if wpnselection == 1:
            global IsDaggerEquipped
            global IsSwordEquipped
            if IsDaggerEquipped == True or IsSwordEquipped == True:
                print("You already have this or another weapon equipped...")
                Game_Loop()
            else:
                dagger = Item('Dagger', 0, 5)
                IsDaggerEquipped = True
                player.strength += dagger.strvalue
                player.gold -= 20
                print("Strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 2:
            if IsDaggerEquipped == True or IsSwordEquipped == True:
                print("You already have this or another weapon equipped...")
                Game_Loop()
            else:
                sword = Item("Sword", 0, 10)
                IsSwordEquipped = True
                player.strength += sword.strvalue
                player.gold -= 50
                print("Strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 3:
            Game_Loop()
