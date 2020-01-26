import random


def choose_random_player():
    input("Press Enter to decide who will go first...")
    first_player = random.randint(0, 1)
    if first_player == 0:
        print("Player 1, you go first!")
        return 1
    else:
        print("Player 2, you go first!")
        return 2


def swap_player_turns(current_player):
    if current_player == 1:
        return 2

    else:
        return 1


def get_player_name(player_num):
    if player_num == 1:
        return "Player 1"
    else:
        return "Player 2"


def get_player_piece(player_num):
    if player_num == 1:
        return "0"
    else:
        return "X"


def show_intro():
    print("Welcome to Noughts and Crosses!")
    print("-------------------------------")
    print("Player 1, you are 0s.")
    print("Player 2, you are Xs.")
    print()


def display_board(row1, row2, row3):
    print("    1   2   3")
    print("  +---+---+---+")
    print("A | {} | {} | {} |".format(row1[0], row1[1], row1[2]))
    print("  +---+---+---+")
    print("B | {} | {} | {} |".format(row2[0], row2[1], row2[2]))
    print("  +---+---+---+")
    print("C | {} | {} | {} |".format(row3[0], row3[1], row3[2]))
    print("  +---+---+---+")


def check_empty_space(check_row, check_col, row1, row2, row3):
    if check_row == "A" and row1[check_col] == " ":
        return True
    elif check_row == "B" and row2[check_col] == " ":
        return True
    elif check_row == "C" and row3[check_col] == " ":
        return True
    else:
        return False


def check_for_winner(row1, row2, row3):
    if ((row1[0] == row1[1] == row1[2]) and \
    (row1[0] != " " and row1[1] = " " and row1[2] != " ")) or \
            ((row2[0] == row2[1] == row2[2]) and \
            (row2[0] != " " and row2[1] != " " and row2[2] != " ")) or \
            ((row3[0] == row3[1] == row3[2]) and \
            (row3[0] != " " and row3[1] != " " and row3[2] != " ")) or \
            ((row1[0] == row2[0] == row3[0]) and \
            (row1[0] != " " and row2[0] != " " and row3[0] != " ")) or \
            ((row1[1] == row2[1] == row3[1]) and \
            (row1[1] != " " and row2[1] != " " and row3[1] != " ")) or \
            ((row1[2] == row2[2] == row3[2]) and \
            (row1[2] != " " and row2[2] != " " and row3[2] != " ")) or \
            ((row1[0] == row2[1] == row3[2]) and \
            (row1[0] != " " and row2[1] != " " and row3[2] != " ")) or \
            ((row1[2] == row2[1] == row3[0]) and \
            (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        return True

    else:
        return False


def player_turn(current_player, row1, row2, row3):
    name = get_player_name(current_player)
    piece = get_player_piece(current_player)

    chosen_location = input(name + ", where would you like to go? \
    Enter in the format RowColumn, for example if you \
    wanted to go to the top-left, you would enter A1\n> ")

    row = chosen_location[0].upper()
    col = int(chosen_location[1]) - 1

    valid_move = check_empty_space(row, col, row1, row2, row3)

    if valid_move == False:
        print("You can't go there! You'll now miss your turn.")

    else:
        if row == "A":
            row1[col] = piece
        elif row == "B":
            row2[col] = piece
        elif row == "C":
            row3[col] = piece


def play_game():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]

    winner = False

    current_player = choose_random_player()

    display_board(row1, row2, row3)

    while winner == False:

        player_turn(current_player, row1, row2, row3)

        display_board(row1, row2, row3)

        if check_for_winner(row1, row2, row3) == True:

            print(get_player_name(current_player) + " is the winner!")
            winner = True

        current_player = swap_player_turns(current_player)


# Run our subroutines!
show_intro()
play_game()
