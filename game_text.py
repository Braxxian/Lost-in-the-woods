import time
from colorama import Fore
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
        """

}
