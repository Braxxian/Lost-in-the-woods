from pyfiglet import figlet_format
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
color = "green"
title = (figlet_format("Welcome", font="doom"))
cprint(title, color)

print(Back.LIGHTGREEN_EX + Fore.BLACK +
      "*------------------------*".center(40, ' '))
print(Back.LIGHTGREEN_EX + Fore.BLACK +
      "Lost in the 'Haunted Wood'".center(40, ' '))
print(Back.LIGHTGREEN_EX + Fore.BLACK +
      "*------------------------*".center(40, ' '))
