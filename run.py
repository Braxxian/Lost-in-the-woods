# import dependencies
import sys
import os
import getpass
import time
from pyfiglet import figlet_format
from termcolor import cprint
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

# game text dictionary
adventure_text = {
    "goblin":
        """The path leads to a small clearing. In the center is
        a campfire with a cooked rabbit on a spit. It looks
        delicious! Will you [A] Grab the rabbit and get out of here
        before the camp owner returns? or [B]call out to see if the
        owner is nearby?
        """,

    "goblin_live":
        """You take the rabbit and start eating while hastily making your
        way further along the path before anyone returns.Looking over your
        shoulder you see an angry goblin by the fire.That was a close one!
        """,

    "goblin_dead":
        """You call out loudly 'Hellooooo', you hear running footsteps,
        a hideous goblin, brandishing a sharp knife, charges toward
        you. 'Rabbit thief!' he cries as the steely blade pierces your
        heart. You have died.
        """,

    "trap":
        """Further along you hear a pitiful cry.As you approach the source
        of the sound, you see a large jaguar caught in a steel trap. It looks
        in a lot of pain. Will you [A]approach and set it free or[B] keep your
        distance and move on?
        """,

    "trap_dead":
        """You felt sorry for the poor creature, but it is a big, dangerous
        beast. Travelling further down the way your progress is halted by
        an angry black bear. Frothing at the mouth it looks rabid! As it tears
        into your flesh, your last thought is how if you had a jaguar friend
        you might have survived.
        """,

    "trap_live":
        """As fearsome a sight as the cat is, you are overcome with compassion
        and bravely approach. The jaguar seems to sense your good intention and
        gratefully allows you to free him. Further down the way, your path is
        suddenly blocked by a rabid bear, which lunges at you! The Jaguar leaps
        to the aid of his rescuer and the bear, out-matched,
        retreats back into the wood
        """,

    "safe_home":
        """Your trusty cat companion guards you to the end of the wood.
        congratulations! you survived ! You make it safely back home,
        """,

    "ghost":
        """Taking the path left along a narrow track, you eventually find a
        derelict chapel with an over-grown long neglected graveyard.
        A strange mist rises from the ground,
        slowly taking the form of a shadowy spectre.
        The phantom raises a pointy finger toward a tomb.
        It seems to be inviting you to read  the tomb's inscription.
        Will you ['A'] approach the tomb or ['B'] flee in terror
        as fast as your legs will carry you!
        """,

    "ghost_dead":
        """figuring a ghost can't actually harm you and driven by curiosity,
        you approach the overgrown tomb. Brushing aside the ivy, you read the
        inscription...a name....YOUR name and the date, 100 years ago!
        How could you not have noticed the clothes you are wearing before!
        clothes from a hundred years ago.
        You are dead and have been for a long time.
        """,

    "ghost_live":
        """You don't know the meaning of this spectres gesture and you don't
        intend to stick around to find out! You run as fast as possible until
        sure of your escape. Ahead in the distance is a cottage, with a light
        in the window, maybe they can help you?
        """,

    "witch":
        """Approaching the cottage, you see an old woman trying to draw water
        from the well. She curses under her breath as she tries to pull up
        the bucket, but she doesn't seem to have the strength.
        Will you [A] offer some assistance or [B] try to sneak into the house
        unobserved?
        """,

    "witch_live":
        """While she is busy, you find the cottage door open and peek inside,
        A wonderful rich aroma, irresitible. You enter, see the warm fire,
        the fur rug and heady from the incense you lie down. 
        """,

    "witch_dead":
        """'Why thank you kind sir', grins the toothless hag,
        'the rope is short, you'll have to lean in!'
        As you take the rope, the old lady throws back her hood to reveal
        the face of a hideous witch, she cackles madly as she pushes you
        to a wet grave. You died.
        """,


    "slave":
        """When you awake, you realize you are in love! This wonderful,
        wizened creature with evil eyes, needs you. You are her willing
        slave and go to get the water! Happy to serve her forever!
        """,






}


# center text
def center_text(text, terminal_width=80):
    padding = (terminal_width - len(text)) // 2
    centered_text = " " * padding + text
    return centered_text


# read and print text
def get_text(text):
    for line in text.splitlines():
        stripped_line = line.strip()
        centered_line = center_text(stripped_line, terminal_width=80)
        print(Fore.LIGHTGREEN_EX + centered_line)
        time.sleep(0.5)


# credit: for clear_terminal: fellow student 'Oleksy Lazarenko'
def clear_terminal():
    """
    Check the operating system and use the appropriate clear command
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


# play again or end program
def replay():
    try:
        play_again = getpass.getpass(
            Fore.YELLOW +
            "Play again? (y/n):".center(80, ' ')).lower()

        if play_again == 'y':
            start_game()
        elif play_again == 'n':
            print(Fore.YELLOW +
                  "-----------------------------------------".center(80, ' '))
            goodbye = "A wise choice, few who enter the wood ever live"
            center_bye = center_text(goodbye)
            print(Fore.YELLOW + center_bye)
            print(Fore.YELLOW +
                  "-----------------------------------------".center(80, ' '))
            sys.exit()
    except ValueError:
        print("Please choose 'y' or 'n'")
    except KeyboardInterrupt:
        print("program interrupted by user")


#  get player input and print text response
def player_choice(alive_text, dead_text):
    choice = ""
    while choice not in {"A", "B"}:
        try:
            choice = getpass.getpass(
                Fore.YELLOW +
                "Make your choice 'A' or 'B'".center(80, ' ')).upper()
            print()
            if choice == "A":
                text = adventure_text[alive_text]
                get_text(text)
            elif choice == "B":
                text = adventure_text[dead_text]
                get_text(text)
                replay()
        except ValueError:
            print("invalid input, please choose 'A' or 'B' ")
        except KeyboardInterrupt:
            print("Display interrupted by user")


# branch 'a'  encounter functions

# goblin encounter 1
def goblin():
    print()
    text = adventure_text["goblin"]
    get_text(text)
    player_choice("goblin_live", "goblin_dead")


# cat encounter 2
def trap():
    text = adventure_text["trap"]
    get_text(text)
    player_choice("trap_live", "trap_dead")


# ending 1
def safe_home():
    print()
    text = adventure_text["safe_home"]
    get_text(text)
    print()
    replay()


# branch 'b'  encounter functions

# ghost encounter 1
def ghost():
    text = adventure_text["ghost"]
    get_text(text)
    print()
    player_choice("ghost_alive", "ghost_dead")


# witch encounter 2
def witch():
    text = adventure_text["witch"]
    get_text(text)
    print()
    player_choice("witch_alive", "witch_dead")

# loop through steps for each branch
# if player still alive


def branch_a():
    for step in range(1, 4):
        branch_a_step(step)


def branch_b():
    for step in range(1, 4):
        branch_b_step(step)


# call game functions for each step in the branch

# Branch 'a'
def branch_a_step(step):
    if step == 1:
        goblin()

    elif step == 2:
        trap()

    elif step == 3:
        safe_home()

    return


# Branch 'b'
def branch_b_step(step):
    if step == 1:
        ghost()

    elif step == 2:
        witch()

    elif step == 3:
        slave()

    return


# start game function
def start_game():
    # ascii heading
    color = "green"
    title = (figlet_format("Dare you enter ? !", font="doom"))
    cprint(title, color)

    # game title
    print(Back.LIGHTGREEN_EX + Fore.BLACK +
          "*------------------------*".center(80, ' '))
    print(Back.LIGHTGREEN_EX + Fore.BLACK +
          "Lost in the Haunted Wood".center(80, ' '))
    print(Back.LIGHTGREEN_EX + Fore.BLACK +
          "*------------------------*".center(80, ' '))
    print()

    # intro text
    line1 = "Do you have what it takes to escape"
    center_line1 = center_text(line1)
    for letter in center_line1:
        print(Fore.LIGHTGREEN_EX + letter, end='', flush=True)
        time.sleep(0.05)
    print()

    line2 = "from the woods, beware, your choices"
    center_line2 = center_text(line2)
    for letter in center_line2:
        print(Fore.LIGHTGREEN_EX + letter, end='', flush=True)
        time.sleep(0.05)
    print()

    line3 = "will decide your fate!"
    center_line3 = center_text(line3)
    for letter in center_line3:
        print(Fore.LIGHTGREEN_EX + letter, end='', flush=True)
        time.sleep(0.05)

    # get user input to invoke gameplay functions
    user_choice = ""
    while user_choice not in {"A", "B"}:
        try:
            print()
            user_choice = getpass.getpass(
                Fore.YELLOW +
                "Press 'A' to go right or B for left".center(80, ' ')).upper()
            if user_choice == "A":
                branch_a()
                replay()
            elif user_choice == "B":
                branch_b()
                replay()

        except ValueError:
            print("Please choose 'A' or 'B'")
        except KeyboardInterrupt:
            print("control 'C' keyboard interupted gameplay")


# credit: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
# Main game loop
if __name__ == "__main__":
    start_game()
