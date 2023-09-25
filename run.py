import getpass
import time
from pyfiglet import figlet_format
from termcolor import cprint
import colorama
from colorama import Fore, Back
from game_text import adventure_text, center_text, get_text
colorama.init(autoreset=True)


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
print()


def return_to_start():
    try:
        text = adventure_text["intro_choiceB"]
        get_text(text)
    except KeyboardInterrupt:
        print("Display interrupted by user")


step1 = ""
while step1 not in {"A", "a", "B", "a"}:
    try:
        step1 = getpass.getpass(
            Fore.YELLOW +
            "Press 'A' to enter or 'B' to quit".center(80, ' ')).upper()
        if step1 == "A":
            text = adventure_text["intro_choiceA"]
            get_text(text)
            print()
        else:
            text = adventure_text["intro_choiceB"]
            get_text(text)
            print()
    except KeyboardInterrupt:
        print("Display interrupted by user")


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
