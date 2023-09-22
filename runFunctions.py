def center_text(text, terminal_width=40):
    padding = (terminal_width - len(text)) // 2
    centered_text = " " * padding + text
    return centered_text
