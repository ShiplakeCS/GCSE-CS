from random import randint  # Needed for dice simulation

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
current_player_name = p1_name


# >>>>>>>> DEFINE YOUR SUBROUTINES <<<<<<<<

def clear_screen():
    print("\n" * 20)


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
        set_player_names()  # Replace with the sub-routine that you write to change player's names

    elif menu_choice == "2":
        play_game()  # Replace with the sub-routine that you write to start the game

    elif menu_choice == "3":
        sure = input("Are you sure you want to quit? (y/n) ")
        if sure.lower() == "y" or sure.lower() == "yes":
            print("Thanks for playing! Bye.")
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
    for row in reversed(range(1, 12)):

        # generate the start of each row (its number of label on the left hand side)
        if row == 11:
            row_string = "| FINISH - 11 |"
        elif row == 5:
            row_string = "| SAFE   -  5 |"
        elif row == 1:
            row_string = "| START  -  1 |"
        else:
            row_string = "|" + str(row).rjust(12) + " |"

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


def set_player_names():
    global p1_name, p2_name

    p1 = input("Enter Player 1's name (leave blank for default value): ")
    p2 = input("Enter Player 2's name (leave blank for default value): ")

    if p1 != "":
        p1_name = p1

    if p2 != "":
        p2_name = p2


def roll_die():
    input("Press Enter to roll the die...")

    value = randint(1, 4)

    if value == 1:
        action_message = "Select a piece to move ONE space nearer to the finish."
    elif value == 2:
        action_message = "Select a piece to move TWO spaces nearer to the finish."
    elif value == 3:
        action_message = "Select a piece to move THREE spaces nearer to the finish."
    elif value == 4:
        action_message = "Select a piece to move BACK ONE SPACE nearer to the start."

    if player_turn == 1:
        name = p1_name
    else:
        name = p2_name

    set_colour("BLUE")
    print("\n{0} rolled a {1}! {2}\n".format(name, value, action_message))
    set_colour("RESET")

    return value


def check_player_can_move(die):
    if die == 4:

        if player_turn == 1:

            if p1_c1 == 1 and p1_c2 == 1:
                return False

        elif player_turn == 2:

            if p2_c1 == 1 and p2_c2 == 1:
                return False

    return True


def change_turn():
    global player_turn, current_player_name

    if player_turn == 1:
        player_turn = 2
        current_player_name = p2_name
    else:
        player_turn = 1
        current_player_name = p1_name


def check_counter_can_move(counter, die):
    if die == 4:
        counter_moves = -1
    else:
        counter_moves = die

    # Test 1 - a player's counter cannot move to the same space as their other counter unless it's a safe space
    # Test 2 - if selected counter is at the start and the player rolls a 4 then they cannot move that piece
    # Test 3 - covered
    # Test 4 - if the selected counter is at the finish and the die roll is not a 4 then the player cannot move that piece

    safe_spaces = [1, 5, 11]

    if player_turn == 1:

        if counter == "A":

            if (p1_c1 + counter_moves) == p1_c2 and p1_c2 not in safe_spaces:
                return False

            if p1_c1 == 1 and die == 4:
                return False

            if p1_c1 == 11 and die != 4:
                return False

        elif counter == "B":

            if (p1_c2 + counter_moves) == p1_c1 and p1_c1 not in safe_spaces:
                return False

            if p1_c2 == 1 and die == 4:
                return False

            if p1_c2 == 11 and die != 4:
                return False

    elif player_turn == 2:

        if counter == "A":

            if (p2_c1 + counter_moves) == p2_c2 and p2_c2 not in safe_spaces:
                return False

            if p2_c1 == 1 and die == 4:
                return False

            if p2_c1 == 11 and die != 4:
                return False

        elif counter == "B":

            if (p2_c2 + counter_moves) == p2_c1 and p2_c1 not in safe_spaces:
                return False

            if p2_c2 == 1 and die == 4:
                return False

            if p2_c2 == 11 and die != 4:
                return False

    return True


def move_piece(die):
    global p1_c1, p1_c2, p2_c1, p2_c2

    piece_to_move = input("Which piece would you like to move (A/B): ").upper()

    if piece_to_move not in ["A", "B"]:
        set_colour("RED")
        print("\nYou must enter either A or B to select your piece!")
        set_colour("RESET")
        input("\nPress Enter to continue...")
        move_piece(die)

    if check_counter_can_move(piece_to_move, die) == True:

        if die == 4:
            counter_moves = -1
        else:
            counter_moves = die

        safe_spaces = [1, 5, 11]

        if player_turn == 1:

            if piece_to_move == "A":

                p1_c1 = p1_c1 + counter_moves

                if p1_c1 > 11:
                    p1_c1 = 11

                if p1_c1 not in safe_spaces:

                    if p2_c1 == p1_c1:
                        p2_c1 = 1

                    if p2_c2 == p1_c1:
                        p2_c2 = 1

            elif piece_to_move == "B":

                p1_c2 = p1_c2 + counter_moves

                if p1_c2 > 11:
                    p1_c2 = 11

                if p1_c2 not in safe_spaces:

                    if p2_c1 == p1_c2:
                        p2_c1 = 1

                    if p2_c2 == p1_c2:
                        p2_c2 = 1

        elif player_turn == 2:

            if piece_to_move == "A":

                p2_c1 = p2_c1 + counter_moves

                if p2_c1 > 11:
                    p2_c1 = 11

                if p2_c1 not in safe_spaces:

                    if p1_c1 == p2_c1:
                        p1_c1 = 1

                    if p1_c2 == p2_c1:
                        p1_c2 = 1

            elif piece_to_move == "B":

                p2_c2 = p2_c2 + counter_moves

                if p2_c2 > 11:
                    p2_c2 = 11

                if p2_c2 not in safe_spaces:

                    if p1_c1 == p2_c2:
                        p1_c1 = 1

                    if p1_c2 == p2_c2:
                        p2_c2 = 1

    else:
        set_colour("RED")
        print("\nYou cannot move that piece, you must select your other piece instead!")
        set_colour("RESET")
        input("\nPress Enter to try again...")
        move_piece(die)


def check_winner():
    if p1_c1 == 11 and p1_c2 == 11:
        return True

    if p2_c1 == 11 and p2_c2 == 11:
        return True

    return False


def reset_board():
    global p1_c1, p1_c2, p2_c1, p2_c2, player_turn, current_player_name

    p1_c1 = 1
    p1_c2 = 1
    p2_c1 = 1
    p2_c2 = 1

    player_turn = 1
    current_player_name = p1_name


def play_game():
    reset_board()

    game_won = False

    while game_won == False:

        show_board()

        die = roll_die()

        if check_player_can_move(die):

            move_piece(die)

            if check_winner() == True:
                game_won = True
                show_board()
                set_colour("YELLOW")
                print("\n*** {0} wins! Congratulations! ***".format(current_player_name))
                set_colour("RESET")
                input("\nPress Enter to return to the Main Menu...")


        else:
            print("There are no legal moves for {0} to make!".format(current_player_name))
            input("Press Enter to change turns...")

        change_turn()


# >>>>>> START THE PROGRAM BY CALLING THE MAIN MENU <<<<<<<
while True:
    main_menu()  # calling main_menu() in a loop ensures that it will be shown after each sub-process has completed



