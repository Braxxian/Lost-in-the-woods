import os
import getpass
import time
from pyfiglet import figlet_format
from termcolor import cprint
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)


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
    way further along the path before anyone returns
    """,

    "goblin_dead":
    """you call out loudly 'Hellooooo', you hear running footsteps,
    a hideous goblin, brandishing a sharp knife, charges toward
    you. 'Rabbit thief!' he cries as the steely blade pierces your
    heart. You have died.
    """,

    "trap":
        """A wise choice, few who enter the wood
        ever make it out alive or with their sanity intact
        Goodbye!""",

    "safe":
        """The path rises steeply and becomes ever more narrow,
        close to the edge of a steep drop, you are startled by
        the sound of a piercing scream. Do you run for your life
        or investigate the source of the scream?
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
        time.sleep(0.25)

# credit: for clear_terminal
# fellow student 'Oleksy Lazarenko'


def clear_terminal():
    """
    Check the operating system and use the appropriate clear command
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# branch 'a' functions


def goblin():
    text = adventure_text["goblin"]
    get_text(text)

    choice = ""
    while choice not in {"A", "B"}:
        try:
            choice = getpass.getpass(
                Fore.YELLOW +
                "Type 'A' or 'B'".center(80, ' ')).upper()
            print()
            if choice == "A":
                text = adventure_text["goblin_live"]
                get_text(text)
            else:
                text = adventure_text["goblin_dead"]
                get_text(text)
                break
        except KeyboardInterrupt:
            print("Display interrupted by user")


def branch_a_step(step):
    if step == 1:
        goblin()

    elif step == 2:
        trap()

    elif step == 3:
        safe_home()

    return


def branch_b_step(step):
    if step == 1:
        ghost()

    elif step == 2:
        witch()

    elif step == 3:
        slave()

    return

# Define functions for each branch of the story


def branch_a():
    # Get steps for branch
    for step in range(1, 3):
        branch_a_step(step)


def branch_b():
    for step in range(1, 3):
        branch_b_step(step)

# start function


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
    print()

    user_choice = ""
    while user_choice not in {"A", "B"}:
        try:
            user_choice = getpass.getpass(
                Fore.YELLOW +
                "Press 'A' to go right or B for left".center(80, ' ')).upper()
            if user_choice == "A":
                branch_a()

                play_again = getpass.getpass(
                    Fore.YELLOW +
                    "Play again? (y/n):".center(80, ' ')).lower()

                if play_again == 'yes':
                    start_game()
                else:
                    goodbye = "A wise choice, few who enter the wood ever live"
                    center_bye = center_text(goodbye)
                    print(Fore.YELLOW + center_bye)

                    break

            elif user_choice == "B":
                branch_b()

                play_again = getpass.getpass(
                    Fore.YELLOW +
                    "Play again? (y/n):".center(80, ' ')).lower()

                if play_again == 'yes':
                    start_game()
                else:
                    goodbye = "A wise choice, few who enter the wood ever live"
                    center_bye = center_text(goodbye)
                    print(Fore.YELLOW + center_bye)

                break
            else:
                clear_terminal()
        except ValueError:
            print("Please choose 'A' or 'B'")
        except KeyboardInterrupt:
            print("program interrupted by user")


# credit: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
# Main game loop
if __name__ == "__main__":
    start_game()

"""
step2 = ""
while step2 not in {"A", "a", "B", "a"}:
    try:
        step2 = getpass.getpass(
            Fore.YELLOW +
            "Press 'A' to go right or 'B' to go left".center(80, ' ')).upper()
        print()
        if step2 == "A":
            text = adventure_text["step2_choiceA"]
            get_text(text)
        else:
            text = adventure_text["step2_choiceB"]
            get_text(text)
    except KeyboardInterrupt:
        print("Display interrupted by user")






step3 = ""
while step3 not in {"A", "a", "B", "a"}:
    try:
        step3 = getpass.getpass(
            Fore.YELLOW +
            "Press 'A' to run or 'B' to investigate".center(80, ' ')).upper()
        print()
        if step3 == "A":
            text = adventure_text["step3_choiceA"]
            get_text(text)
        else:
            text = adventure_text["step3_choiceB"]
            get_text(text)
    except KeyboardInterrupt:
        print("Display interrupted by user")
"""
