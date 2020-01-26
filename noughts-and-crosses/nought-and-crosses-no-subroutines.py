import random

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

winner = False

current_player = 1

print("Welcome to Noughts and Crosses!")
print("-------------------------------")
print("Player 1, you are 0s.")
print("Player 2, you are Xs.")
print()
input("Press Enter to decide who will go first...")

first_player = random.randint(0,1)
if first_player == 0:
    print("Player 1, you go first!")
    current_player = 1
else:
    print("Player 2, you go first!")
    current_player = 2

while winner == False:

    print("    1   2   3")
    print("  +---+---+---+")
    print("A | {} | {} | {} |".format(row1[0], row1[1], row1[2]))
    print("  +---+---+---+")
    print("B | {} | {} | {} |".format(row2[0], row2[1], row2[2]))
    print("  +---+---+---+")
    print("C | {} | {} | {} |".format(row3[0], row3[1], row3[2]))
    print("  +---+---+---+")

    if current_player == 1:
        name = "Player 1"
        piece = "0"
    else:
        name = "Player 2"
        piece = "X"
    chosen_location = input(name + ", where would you like to go? Enter in the format RowColumn, for example if you wanted to go to the top-left, you would enter A1\n> ")
    row = chosen_location[0].upper()
    col = int(chosen_location[1]) - 1
    invalid_move = False
    if row == "A":
        if row1[col] == " ":
            row1[col] = piece
        else:
            invalid_move = True
    elif row == "B":
        if row2[col] == " ":
            row2[col] = piece
        else:
            invalid_move = True
    elif row == "C":
        if row3[col] == " ":
            row3[col] = piece
        else:
            invalid_move = True

    if invalid_move == True:
        print("You can't go there! You'll now miss your turn.")

    else:

        # Check for a winner...

        if ((row1[0] == row1[1] == row1[2]) and (row1[0] != " " and row1[1] != " " and row1[2] != " ")) or \
                ((row2[0] == row2[1] == row2[2]) and (row2[0] != " " and row2[1] != " " and row2[2] != " ")) or \
                ((row3[0] == row3[1] == row3[2]) and (row3[0] != " " and row3[1] != " " and row3[2] != " ")) or \
                ((row1[0] == row2[0] == row3[0]) and (row1[0] != " " and row2[0] != " " and row3[0] != " ")) or \
                ((row1[1] == row2[1] == row3[1]) and (row1[1] != " " and row2[1] != " " and row3[1] != " ")) or \
                ((row1[2] == row2[2] == row3[2]) and (row1[2] != " " and row2[2] != " " and row3[2] != " ")) or \
                ((row1[0] == row2[1] == row3[2]) and (row1[0] != " " and row2[1] != " " and row3[2] != " ")) or \
                ((row1[2] == row2[1] == row3[0]) and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):

            print("    1   2   3")
            print("  +---+---+---+")
            print("A | {} | {} | {} |".format(row1[0], row1[1], row1[2]))
            print("  +---+---+---+")
            print("B | {} | {} | {} |".format(row2[0], row2[1], row2[2]))
            print("  +---+---+---+")
            print("C | {} | {} | {} |".format(row3[0], row3[1], row3[2]))
            print("  +---+---+---+")

            print(name + " is the winner!")
            winner = True

    if current_player == 1:
        current_player = 2
    else:
        current_player = 1