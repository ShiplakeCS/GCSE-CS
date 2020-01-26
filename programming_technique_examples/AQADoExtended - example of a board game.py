__author__ = 'AWD'

import random

class Player:
    """
    This class defines Player objects.

    Each Player has a name, a number (either 1 or 2 for player 1 or 2) and an array that contains integers that represent the position on the board of each of its two pieces.
    For example, if Player 1 had a piece on position 3 and another on 5 then piecePositions[0] = 3, piecePositions[1] = 5.

    A number of methods are provided that allow a Player's instance variable values to be set or retrieved.

    Error handling is used to ensure that valid data is provided and that the Player's variables are always assigned suitable values. For example, if a blank string is provided to setPlayerName() then the default name (given at instantiation) is maintained.
    """
    def __init__(self, num=0, name=""):
    # Initialise a Player object with the player number and name provided to the constructor method
        self.name = ""
        self.number = 0
        self.piecePositions = [1,1]
        try:
            self.number = int(num)
        except:
            raise ValueError
        self.name = name

    def setPlayerName(self, name):
        if name!="":
            self.name = name

    def getPlayerName(self):
        return self.name

    """
    def setPlayerNumber(self, num):
        try:
            self.number = int(num)
        except:
            raise ValueError
    """
    def getPlayerNumber(self):
        return self.number

    def setPiece1Pos(self, pos):
        self.piecePositions[0] = pos

    def setPiece2Pos(self, pos):
        self.piecePositions[1] = pos

    """
    def setPiecePositions(self, positions):
        self.piecePositions = positions
    """

    def movePiece(self,piece, spaces):
        self.piecePositions[piece-1] = self.piecePositions[piece-1] + spaces
        if self.piecePositions[piece-1] > 11: # If moving a piece would send it over the finish line, make it stop at the finish
            self.piecePositions[piece-1] = 11
        return self.piecePositions[piece-1]

    """
    def movePiece1(self,spaces):
        self.piecePositions[0] = self.piecePositions[0] + spaces
        if self.piecePositions[0] > 11: # If moving a piece would send it over the finish line, make it stop at the finish
            self.piecePositions[0] = 11
        return self.piecePositions[0]

    def movePiece2(self,spaces):
        self.piecePositions[1] = self.piecePositions[1] + spaces
        if self.piecePositions[1] > 11:
            self.piecePositions[1] = 11
        return self.piecePositions[1]

    def tryMovePiece1(self, spaces):
        # This method returns the position that Piece 1 would be in if a move of 'spaces' was made. It doesn't actually make the move. This allows us to test whether a piece will be moved beyond the bounds of the board before making the move.
        return self.piecePositions[0] + spaces

    def tryMovePiece2(self, spaces):
        # As tryMovePiece1 but for second piece
        return self.piecePositions[1] + spaces
    """

    def getPositions(self):
        return self.piecePositions

    def getPiece1Pos(self):
        return self.piecePositions[0]

    def getPiece2Pos(self):
        return self.piecePositions[1]

def clearScreen():
    print("\n" * 20)

def MainMenu():
    MENU_WIDTH = 40
    clearScreen()
    # Print header of Main Menu
    print("*" * MENU_WIDTH)
    print("*",end="")
    print("AQADO!".center(MENU_WIDTH - 2),end="")
    print("*")
    print("*" * MENU_WIDTH)

    # Print options
    print("1 - Enter player names")
    print("2 - Play game")
    print("3 - Quit")
    print("*" * MENU_WIDTH)

    # Capture user input
    validInput = False
    while not(validInput):
        choice = input("Please enter your choice, either 1, 2 or 3: ")
        if choice == "1" or choice == "2" or choice == "3":
            validInput = True
            return choice

        elif not(choice.isnumeric()):
            print(messageInABox("You didn't enter a number!"))

        choice = input("Please enter your choice, either 1, 2 or 3: ")

def setPlayerNames():
    global player1
    global player2

    #clearScreen()
    print("-" * 40)
    player1.setPlayerName(input("Enter Player 1's name: "))
    player2.setPlayerName(input("Enter Player 2's name: "))
    print("-" * 40)

def displayBoard():
    global player1
    global player2

    clearScreen()
    showPlayerNamesKey()

    for row in range(1,12)[::-1]: # This line sets up a loop that will occur 11 times, with the value of 'row' being changing from 11 to 10 to 9 ... to 1 with each iteration
        print("+--+" + "-"*20 + "+")
        print("|" + str(row).center(2) + "|", end="")
        if player1.getPiece1Pos() == row:
            print("O".center(5), end="")
        else:
            print(" " * 5, end="")
        if player1.getPiece2Pos() == row:
            print("O".center(5), end="")
        else:
            print(" " * 5, end="")
        if player2.getPiece1Pos() == row:
            print("X".center(5), end="")
        else:
            print(" " * 5, end="")
        if player2.getPiece2Pos() == row:
            print("X".center(5), end="")
        else:
            print(" " * 5, end="")
        if row == 11:
            print("| - FINISH")
        elif row == 5:
            print("| - SAFE")
        elif row == 1:
            print("| - START")
        else:
            print("|")

    print("+--+" + "-"*20 + "+")

def showPlayerNamesKey():

    playerKeyString = "O - " + player1.getPlayerName() + " | X - " + player2.getPlayerName()
    print(messageInABox(playerKeyString))


def rollDice(player):
    dice = random.randint(1,4)
    print("%s rolled a %i!" % (player.getPlayerName(), dice))
    if dice == 1:
        print("You can move one of your pieces ONE space nearer to FINISH")
    elif dice == 2:
        print("You can move one of your pieces TWO spaces nearer to FINISH")
    elif dice == 3:
        print("You can move one of your pieces THREE spaces nearer to FINISH")
    elif dice == 4:
        print("You need to move one of your pieces ONE space BACK towards START")

    return dice

def checkPlayerCanMove(player, dice):

    # Player cannot move if:
    #   Both pieces are on start and a 4 is rolled

    if player.getPositions()[0] == 1 and player.getPositions()[1] == 1 and dice == 4:
        # if both pieces are on row 1 and dice is 4 (move back) then return False
        print("Both of your pieces are on the start and you have rolled a 4.")
        return False
    else:
        return True

def diceToSpaces(dice):

    if dice == 1:
        spaces = 1
    elif dice == 2:
        spaces = 2
    elif dice == 3:
        spaces = 3
    elif dice == 4:
        spaces = -1

    return spaces

def messageInABox(message):
    msgInBox = "+" + "-" * len(message) + "+\n" + "|" + message + "|\n" + "+" + "-" * len(message) + "+"
    return msgInBox

def checkValidMove(player, piece, dice):

    #If piece will end up on a safe space then the move is valid
    testPos = player.getPositions()[piece-1] + diceToSpaces(dice)

    if testPos == 1 or testPos == 5 or testPos == 11:
        return True

    # Check if a move of 'spaces' spaces would land on a space already occupied by player's other space
    if piece == 1:
        if player.getPiece1Pos() + diceToSpaces(dice) == player.getPiece2Pos():
            print(messageInABox("You cannot move here as your other piece is already on that space."))
            return False
    elif piece == 2:
        if player.getPiece2Pos() + diceToSpaces(dice) == player.getPiece1Pos():
            print(messageInABox("You cannot move here as your other piece is already on that space."))
            return False

    # Check if selected piece is on the start and the dice rolls a 4 (spaces = -1, as rolling a 4 resuls in a backwards 1 (-1) move)
    if player.getPositions()[piece - 1] == 1 and dice == 4:
            print(messageInABox("You cannot move a piece backwards if it is already at the start."))
            return False

    # Check if selected piece is on the finish as the dice rolls a 1-3 (spaces > 0 as rolling 1-3 = a forward move)
    if player.getPositions()[piece - 1] == 11 and dice != 4:
            print(messageInABox("You cannot move a piece forwards that is already at the finish."))
            return False

    return True

def getPieceToMove():

    validChoice = False

    while validChoice == False:
        piece = input("Select a piece to move (1 or 2): ")
        if piece.isnumeric() == False:
            validChoice = False

        else:
            piece = int(piece)
            if (int(piece) == 1) or (int(piece) == 2):
                validChoice = True
                return piece

        print(messageInABox("Invalid selection! Please choose either 1 or 2."))

def makeMove(player,piece,dice):
    global player1
    global player2

    newPos = player.movePiece(piece,diceToSpaces(dice))

    # Having made the move, check if another player's piece needs to move back to start

    # If new poisition of moved piece is a safe spot then no need to do anything further
    if newPos == 1 or newPos == 5 or newPos == 11:
        return

    # Else, if Player 1 is current player, then check Player 2's piece positions. If either is on the same position as newPos then move it back to start.
    elif player.getPlayerNumber() == 1:
        if player2.getPiece1Pos() == newPos:
            player2.setPiece1Pos(1)
        elif player2.getPiece2Pos() == newPos:
            player2.setPiece2Pos(1)

    elif player.getPlayerNumber() == 2:
        if player1.getPiece1Pos() == newPos:
            player1.setPiece1Pos(1)
        elif player1.getPiece2Pos() == newPos:
            player1.setPiece2Pos(1)

    #print("moved piece. Players piece are now: " + str(player.getPositions()))

def checkForWinner(player):
    if player.getPiece1Pos() == 11 and player.getPiece2Pos() == 11:
        clearScreen()
        winnerMessage = "Game over! %s is the winner!" % player.getPlayerName()
        print("*" * (len(winnerMessage) + 4))
        print("* " + winnerMessage + " *")
        print("*" * (len(winnerMessage) + 4))
        return True
    else:
        return False

def playGame():
    global player1
    global player2

    # Set up main game play loop

    # Whilst winner = False, keep going through loop of showing the board, asking

    activePlayer = player1

    winner = False

    while winner == False:
        displayBoard()
        print ("%s's turn..." % activePlayer.getPlayerName(), end="")
        dice = rollDice(activePlayer)
        if checkPlayerCanMove(activePlayer, dice) == False:
            wait = input(messageInABox("There is no valid move for %s to make. Press Enter to continue..." % activePlayer.getPlayerName()))

        else:
            validPiece = False
            while validPiece == False:
                piece = getPieceToMove()
                if checkValidMove(activePlayer,piece,dice):
                    validPiece = True
                    makeMove(activePlayer,piece,dice)
                    winner = checkForWinner(activePlayer)

        # Switch active player for next go
        if activePlayer == player1:
            activePlayer = player2
        else:
            activePlayer = player1

    wait = input("Press Enter to return to the Main Menu...")



if __name__ == '__main__':

    # Create two variables, player1 and player2, each one assigned the value of a unique Player object
    player1 = Player(1, "Player 1")  # Create a Player object, with player number set to 1 and name set to "Player 1"
    player2 = Player(2, "Player 2")

    activePlayer = player1

    # Call the MainMenu function to show the Main Menu. Assign the returned value (the user's menu choice) to a variable called 'choice'.
    choice = MainMenu()

    # As long as the user keeps making choices other than "3 - Quit", keep going around the main loop of showing the Main Menu, do the chosen option, show the main menu again, etc
    while choice != "3":

        if choice == "1":
            # If user has selected option 1 from the Main Menu, call setPlayerNames() procedure
            setPlayerNames()
            #print(player1.getPlayerName())
            #print(player2.getPlayerName())
            clearScreen()

        elif choice == "2":
            playGame()

        choice = MainMenu()

    quit()
