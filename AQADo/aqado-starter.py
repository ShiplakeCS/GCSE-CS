from random import randint  # Needed for dice simulation

# >>>>>>>> DEFINE YOUR SUBROUTINES <<<<<<<<


def clear_screen():
    print("\n" * 40)


def set_colour(col):

    '''
    If you are interested in learning more about how this procedure works, check out the following links:
    https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences
    http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#colors
    '''

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


def main_menu():
    clear_screen()
    set_colour("BLUE")
    print("\
        █████╗  ██████╗  █████╗ ██████╗  ██████╗ ██╗\n\
        ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗██║\n\
        ███████║██║   ██║███████║██║  ██║██║   ██║██║\n\
        ██╔══██║██║▄▄ ██║██╔══██║██║  ██║██║   ██║╚═╝\n\
        ██║  ██║╚██████╔╝██║  ██║██████╔╝╚██████╔╝██╗\n\
        ╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝")
    set_colour("RESET")
    print()
    print("MAIN MENU".center(60))
    print()
    print("1. Enter player names")
    print("2. Play gmae")
    print("3. Quit")

    menu_choice = input("\nEnter your choice (1, 2 or 3): ")

    if menu_choice not in ["1", "2", "3"]:
        input("\nSorry, that isn't a valid option!\n\nPress Enter to try again...")

    elif menu_choice == "1":
        pass # Replace with the sub-routine that you write to change player's names

    elif menu_choice == "2":
        pass # Replace with the sub-routine that you write to start the game

    elif menu_choice == "3":
        sure = input("Are you sure you want to quit? (y/n) ")
        if sure.lower() == "y" or sure.lower() == "yes":
            quit()


def show_turn():

    if player_turn == 1:
        print("{0}'s turn!".format(p1_name))
    else:
        print("{0}'s turn!".format(p2_name))


def show_board():

    global p1_c1, p1_c2, p2_c1, p2_c2

    # print the board header
    print("========================================")
    print("|              AQADO!                  |")
    print("+======================================+")

    # for each row (from 11 - 1)...
    for row in reversed(range(1,12)):

        # generate the start of each row (its number of label on the left hand side)
        if row == 11:
            row_string = "| FINISH - 11 |"
        elif row == 5:
            row_string = "| SAFE   -  5 |"
        elif row == 1:
            row_string = "| START  -  1 |"
        else:
            row_string = "|" + str(row).rjust(12)+ " |"

        # generate the end of each row, containing a counter if the counter's value is the same as the row number
        if row == p1_c1:
            row_string = row_string + "  1A  "
        else:
            row_string = row_string + "      "

        if row == p1_c2:
            row_string = row_string + "  1B  "
        else:
            row_string = row_string + "      "

        if row == p2_c1:
            row_string = row_string + "  2A  "
        else:
            row_string = row_string + "      "

        if row == p2_c2:
            row_string = row_string + "  2B  "
        else:
            row_string = row_string + "      "

        # generate the very end of the row
        row_string = row_string + "|"

        # print the row
        print(row_string)

        # print a border beneath the row
        print("+" + "-" * (len(row_string) - 2) + "+")

    show_turn()  # Call show_turn to show whose go it is


# >>>>> GLOBAL VARIABLES <<<<<<<

# Player names
p1_name = "Player 1"
p2_name = "Player 2"

# Player counter positions
p1_c1 = 1
p1_c2 = 1
p2_c1 = 1
p2_c2 = 1

player_turn = 1

# >>>>>> START THE PROGRAM BY CALLING THE MAIN MENU <<<<<<<
while True:
    main_menu()  # calling main_menu() in a loop ensures that it will be shown after each sub-process has completed


