import os
import getpass
import time
from pyfiglet import figlet_format
from termcolor import cprint
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

adventure_text = {
    "intro_choiceA":
        """You know you've been here before, in a dream maybe ?
        The dark wood rustles in the night wind
        rubbing your eyes, you see two paths, dimly lit in the moonlight
        Will you go left or right?""",

    "intro_choiceB":
        """A wise choice, few who enter the wood
        ever make it out alive or with their sanity intact
        Goodbye!""",

    "step2_choiceA":
        """The path rises steeply and becomes ever more narrow,
        close to the edge of a steep drop, you are startled by
        the sound of a piercing scream. Do you run for your life
        or investigate the source of the scream?
        """,
    "step2_choiceB":
    """After a while the path levels out and turns into a small
    clearing. There is a small campfire and a cooked rabbit on
    a spit. Do you eat the rabbit or call out if anyone is nearby?
    """
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


def clear_terminal():
    """
    Check the operating system and use the appropriate clear command
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def branch_a_step(step):
    print("branch A works")

    return


def branch_b_step(step):
    print("branch B works")

    return
