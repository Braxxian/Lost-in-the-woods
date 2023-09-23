import getpass
import time
from pyfiglet import figlet_format
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back
from runFunctions import center_text, get_text
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

choice1 = ""
while choice1 not in {"A", "a", "B", "a"}:

    choice1 = getpass.getpass(Fore.YELLOW +
                              "Press 'A' to enter or 'B' to quit\n".center(80, ' ')).upper()
if choice1 == "A":
    text = "storyfiles\\intro_choiceA.txt"
    get_text(text)
else:
    text = "storyfiles\\intro_choiceB.txt"
    get_text(text)
