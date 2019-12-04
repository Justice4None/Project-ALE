import cmd
import textwrap
import sys
import time
import random
screen_width = 100


class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.astrological = ''
        self.position = 'ground'
        self.won = False
        self.solves = 0


player1 = player()

"""
You're basically in a cube, trying to solve each side of the cube to "break it open" and escape.
Here's a diagram!
----------------------------------------------------
        North -v      _.-+
                 _.-""     '
             +:""            '
             | \  v Top Side   '
              | \             _.-+
              |  '.       _.-"   |
    West -->  |    \  _.-"       |  <-- East
               |    +"           |
               +    | South->    |
                \   |          .+
                 \  |       .-'
                  \ |    .-'	<-- Ground/Center
                   \| .-'
                    +'
-----------------------------------------------------
You can travel to any adjcent wall, but not across.  The game will tell you there is a gap in space.
Unfolding walls will change this system.
"""

DESCRIPTION = 'description'
INFO = 'info'
PUZZLE = 'puzzle'
SOLVED = False
SIDE_UP = 'up', 'forward'
SIDE_DOWN = 'down', 'back'
SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'

room_solved = {'top': False, 'north': False, 'ground': False,
               'east': False, 'west': False, 'south': False}

cube = {
    'top': {
        DESCRIPTION: "You find youself standing normally on clouds, stragely.",
        INFO: "Even more strange more strange than standing on clouds is the\nbird that begins speaking to you.\n",
        PUZZLE: "The bird intimidatingly asks:\nI fly without wings. I see without eyes. I move without legs.\nI conjure more love than any lover and more fear than any beast.\nI am cunning, ruthless, and tall; in the end, I rule all.\nWhat am I?",
        SOLVED: "imagination",
        SIDE_UP: 'north',
        SIDE_DOWN: 'south',
        SIDE_LEFT: 'east',
        SIDE_RIGHT: 'west'
    },
    'north': {
        DESCRIPTION: "You find yourself in a frigid artic valley.\nA campfire glows brightly in a nearby cave.",
        INFO: "You now stand face-to-face with a giant yeti.",
        PUZZLE: "The yeti asks you, 'What bites without teeth?'",
        SOLVED: "frost",
        SIDE_UP: 'top',
        SIDE_DOWN: 'ground',
        SIDE_LEFT: 'west',
        SIDE_RIGHT: 'east',
    },
    'ground': {
        DESCRIPTION: "You find yourself in a rather pretty, generic grassy field.\nSomething feels amiss, as if this the core of the world.",
        INFO: "A rather large, though easily overlookable golden key\nstands vertical in the field.\nHow odd.",
        PUZZLE: "The key stands within respectively sized keyhole obscured\nby dirt and grass.  It doesn't seem to turn.",
        SOLVED: False,  # Will work after you solve all other puzzles?
        SIDE_UP: 'north',
        SIDE_DOWN: 'south',
        SIDE_LEFT: 'west',
        SIDE_RIGHT: 'east',
    },
    'east': {
        DESCRIPTION: "You find yourself in lush woodlands, bursting with wildlife\nand a cacaphony of chirping.",
        INFO: "A rough-looking man sits next to a little cabin.\nHis eyes are glued to bird-watching binoculars.",
        PUZZLE: "The rough-looking man asks,\n'What is the airspeed of an unladen European swallow?'",
        SOLVED: "25",
        SIDE_UP: 'north',
        SIDE_DOWN: 'south',
        SIDE_LEFT: 'ground',
        SIDE_RIGHT: 'top',
    },
    'west': {
        DESCRIPTION: 'You find yourself encompassed by strong winds and sandy dunes.',
        INFO: 'A terrified looking man is hiding among some cacti.',
        PUZZLE: "The fearful man asks,\n'What can measure time, while eventually, all crumbles to it?'",
        SOLVED: "sand",
        SIDE_UP: 'north',
        SIDE_DOWN: 'south',
        SIDE_LEFT: 'top',
        SIDE_RIGHT: 'ground',
    },
    'south': {
        DESCRIPTION: "You find yourself next to a still, soothing pond.\nAn old man gazes at a table nearby.",
        INFO: "You greet the old man.\nHe beckons you to look at the intricate twelve-sided table.",
        PUZZLE: "Each side of the table has a unique symbol, though all are familar to you.\nWhich symbol do you sit by?",
        SOLVED: "",  # Should be your astrological sign.
        SIDE_UP: 'ground',
        SIDE_DOWN: 'top',
        SIDE_LEFT: 'west',
        SIDE_RIGHT: 'east',
    }
}


def title_screen_options():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("help"):
        help_menu()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Invalid command, please try again.")
        option = imput("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("quit"):
            sys.exit()
        elif option.lower() == ("help"):
            help_menu()


def title_screen():
    os.system('clear')
    print('#' * 21)
    print("Welcome to test_2.py!")
    print('#' * 21)
    print("Play")
    print('#' * 21)
    print("Help")
    print('#' * 21)
    print("Quit")
    print('#' * 21)


def help_menu():
    print('#' * 21)
    print("Type a command to such as 'move' then 'left'")
    print("to navigate the map of the cube puzzle.\n")
    print('#' * 21)
    print("Commands such as 'look' or 'examine' will")
    print("let you interact with puzzles in rooms.\n")
    print('#' * 21)
    print("Puzzles will require various inputs and")
    print("possibly answers from outside knowledge.\n")
    print('#' * 21)
    print("Please be sure to type in lowercase for ease.\n")
    print('#' * 21)
    print("\n")
    print('#' * 21)
    print("Welcome to test_2.py!")
    print('#' * 21)
    print("Play")
    print('#' * 21)
    print("Help")
    print('#' * 21)
    print("Quit")
    print('#' * 21)


quitgame = 'quit'


def print_location():
    print('\n' + ('#' * (4 + len(player1.position))))
    print('# ' + player1.position.upper() + ' #')
    print('#' * (3 + len(player1.position)))
    print('\n' + (cube[player1.position][DESCRIPTION]))


def prompt():
    if player1.solves == 5:
        print("Something in the world seems to have changed...")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'inspect', 'examine', 'look', 'search']
    while action.lower() not in acceptable_actions:
        print("Unknown action command, please try again.\n")
        action = input("> ")
    if action.lower() == quitgame:
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        move(action.lower())
    elif action.lower() in ['inspect', 'examine', 'look', 'search']:
        examine()


def move(myAction):
    askString = "Where would you like to "+myAction+" to?\n"
    destination = input(askString)
    if destination == 'forward':
        move_dest = cube[player1.position][SIDE_UP]
        move_player(move_dest)
    elif destination == 'left':
        move_dest = cube[player1.position][SIDE_LEFT]
        move_player(move_dest)
    elif destination == 'right':
        move_dest = cube[player1.position][SIDE_RIGHT]
        move_player(move_dest)
    elif destination == 'back':
        move_dest = cube[player1.position][SIDE_DOWN]
        move_player(move_dest)
    else:
        print("Invalid direction command, try using forward, back, left or right.\n")
        move(myAction)


def move_player(move_dest):
    print("\nYou have moved to the " + move_dest + ".")
    player1.position = move_dest
    print_location()


def examine():
    if room_solved[player1.position] == False:
        print('\n' + (cube[player1.position][INFO]))
        print((cube[player1.position][PUZZLE]))
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    else:
        print("There is nothing new for you to see here.")


def checkpuzzle(puzzle_answer):
    if player1.position == 'ground':
        if player1.solves >= 5:
            endspeech = ("Without you having done anything, the key begins to rotate.\nIt begins to raid.\nAll sides of the box begin to crumble inwards.\nLight begins to shine through the cracks in the walls.\nA blinding flash of light hits you.\nYou have escaped!")
            for character in endspeech:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nCONGRATULATIONS!")
            sys.exit()
        else:
            print("Nothing seems to happen.")
    elif player1.position == 'south':
        if puzzle_answer == (player1.astrological):
            room_solved[player1.position] = True
            player1.solves += 1
            print("You have solved the puzzle. Onwards!")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
            print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            examine()
    else:
        if puzzle_answer == (cube[player1.position][SOLVED]):
            room_solved[player1.position] = True
            player1.solves += 1
            print("You have solved the puzzle. Onwards!")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
            print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            examine()
