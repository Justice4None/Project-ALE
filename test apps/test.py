# A text based RPG

# Import required modules
import jsonpickle
import os
import sys
import time
from random import randint
# main game

# Variables
go = True
IsShopLocked = False
IsDaggerEquipped = False
IsSwordEquipped = False
IsLeatherHideEquipped = False

SAVEGAME_FILENAME = 'savegame.json'

game_state = dict()

### Classes ###


class Human(object):
    # Represents the human player in the game
    def __init__(self, name, health, strength, gold):
        self.name = name
        self.health = health
        self.strength = strength
        self.gold = gold


class AI(object):
    # Represents the enemy player in the game
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength


class Item(object):
    # represents any item in the game
    def __init__(self, name, hvalue, strvalue):
        self.name = name
        self.hvalue = hvalue
        self.strvalue = strvalue

###end classess###

###functions for loading, saving, and initializing the game###


def load_game():
    """Load game state from a predefined savegame location and return the
    game state contained in that savegame.
    """
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    """Save the current game state to a savegame in a predefined location.
    """
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))


def initialize_game():
    """If no savegame exists, initialize the game state with some
    default values.
    """
    global game_state
    player = Human('Fred', 100, 10, 1000)
    enemy = AI('Imp', 50, 20)

    state = dict()
    state['players'] = [player]
    state['npcs'] = [enemy]
    return state

###End functions for loading, saving, and initalizing the game###

###Main game functions###
# Function for the shop


def Shop():
    global game_state
    player = game_state['players'][0]
    dagger = Item('Dagger', 0, 5)
    sword = Item('Sword', 0, 10)
    leather_hide = Item('Leather Hide', 5, 0)
    if IsShopLocked == True:
        print("The shop is locked!\nPlease go back and continue your adventure!")
    else:
        print()
        print("Welcome to the Larkville shop! What would you like to buy?\n1. Weapons\n2. armor\n3. Go back")
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
                print("strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 2:
            if IsDaggerEquipped == True or IsSwordEquipped == True:
                print("You already have this or another weapon equipped...")
                Game_Loop()
            else:
                sword = Item('Sword', 0, 10)
                IsSwordEquipped = True
                player.strength += sword.strvalue
                player.gold -= 50
                print("strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 3:
            Game_Loop()

    elif selection == 2:
        if player.gold >= 20:
            print("Armor Shop")
            print("1. Leather hide\n2. Go back")
            armselection = int(input("enter a value: "))

        if armselection == 1:
            global IsLeatherHideEquipped
            if IsLeatherHideEquipped == True:
                print("You are already wearing armor!")
                Game_Loop()
            else:
                leather_hide = Item('Leather Hide', 5, 0)
                IsLeatherHideEquipped = True
                player.health += leather_hide.hvalue
                player.gold -= 20
                print("Health increased to: {}".format(player.health))
                Game_Loop()

        elif armselection == 2:
            Game_Loop()

    elif selection == 3:
        Game_Loop()

# Function for combat


def Combat():
    global game_state
    player = game_state['players'][0]
    enemy = game_state['npcs'][0]
    global go
    while go == True:
        dmg = randint(0, player.strength)
        edmg = randint(0, enemy.strength)
        enemy.health -= dmg

        if player.health <= 0:
            os.system('cls')
            print()
            print("You have been slain by the enemy {}...".format(enemy.name))
            go = False
            leave = input("press enter to exit")

        elif enemy.health <= 0:
            os.system('cls')
            print()
            print("You have slain the enemy {}!".format(enemy.name))
            go = False
            leave = input("press any key to exit")

        else:
            os.system('cls')
            with open("test.txt", "r") as in_file:
                text = in_file.read()
            print(text)
            player.health -= edmg
            print()
            print("You attack the enemy {} for {} damage!".format(enemy.name, dmg))
            print("The enemy has {} health left!".format(enemy.health))
            print()
            print("The enemy {} attacked you for {} damage!".format(enemy.name, edmg))
            print("You have {} health left!".format(player.health))
            time.sleep(3)

# The main game loop


def Game_Loop():

    global game_state

    while True:
        print()
        print("You are currently in your home town of Larkville!")
        print("What would you like to do?")
        print("1. Shop\n2. Begin/continue your adventure\n3. View player statistics\n4. save game")
        print()

        try:
            selection = int(input("Enter a value: "))
        except ValueError:
            print()
            print("You can only use the numbers 1, 2, or 3.")
            print()
            Game_Loop()
        if selection == 1:
            Shop()
        elif selection == 2:
            Combat()
        elif selection == 3:
            player = game_state['players'][0]
            print()
            print("Your players stats:\nHealth: {}\nStrength: {}\nGold: {}".format(
                player.health, player.strength, player.gold))
            if IsDaggerEquipped == True:
                print("You have a dagger equipped")
            elif IsSwordEquipped == True:
                print("You have a sword equipped")
            elif IsLeatherHideEquipped == True:
                print("You are wearing a leather hide")
        elif selection == 4:
            game_state = save_game()
        else:
            print()
            print("Oops! Not a valid input")
            print()

###End main game functions###

###The "main" function, not to be confused with anything to do with main above it###


def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    global game_state

    if not os.path.isfile(SAVEGAME_FILENAME):
        game_state = initialize_game()
    else:
        game_state = load_game()
    Game_Loop()


if __name__ == '__main__':
    main()

# end main function###zzzzzzz
