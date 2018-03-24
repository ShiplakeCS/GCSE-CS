# Sub-routine (procedure) used to change the output colour (needed for Task 2)
def set_colour(col):

    # If you are interested in learning more about how this procedure works, check out the following links:
    # https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences
    # http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#colors

    if col == "RESET":
        print("\u001b[39;49m", end="")
    elif col == "RED":
        print("\u001b[31m", end="")
    elif col == "BLUE":
        print("\u001b[34m", end="")
    elif col == "GREEN":
        print("\u001b[32m", end="")
    elif col == "YELLOW":
        print("\u001b[33m", end="")
    elif col == "PINK":
        print("\u001b[35m", end="")
    elif col == "CYAN":
        print("\u001b[36m", end="")
    elif col == "GREY":
        print("\u001b[37m", end="")
    elif col == "BLACK":
        print("\u001b[30m", end="")
