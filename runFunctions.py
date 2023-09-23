
# center text
def center_text(text, terminal_width=80):
    padding = (terminal_width - len(text)) // 2
    centered_text = " " * padding + text
    return centered_text

# read and print text


def get_text(text):
    try:
        with open(text, "r", encoding="utf-8",
                  errors="ignore") as file:
            lines = file.readlines()
            for line in lines:
                stripped_line = line.strip()
                centered_line = center_text(stripped_line, terminal_width=80)
                print(centered_line)
                time.sleep(0.5)

    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Display interrupted by user")
