import random, time

# Set global constants
BOARDSIZE = 10 # 10
NUM_BOMBS = 5 # 5
HEALTH_IMPACT = 50 # 50
SCORE_BASE = 50
CLEAR_UNCHECKED = 0
BOMB_UNCHECKED = 1
CLEAR_CHECKED = 2
BOMB_CHECKED = 3

# Escape character sequences for different colours - see https://pypi.python.org/pypi/colorama
BLUE_TEXT = "\033[34;1m"
RED_TEXT = "\033[31;1m"
RESET_TEXT = "\033[0m"

# Layout/appearance constants
ASCII_A = 65
CELL_SIZE = 3
LEFT_MARGIN = 4
BORDER_WIDTH = 50
#BOMB_UNCHECKED_SYMBOL = "!"
BOMB_UNCHECKED_SYMBOL = "!"
BOMB_CHECKED_SYMBOL = RED_TEXT + "X".center(CELL_SIZE," ") + RESET_TEXT
CLEAR_CHECKED_SYMBOL = "*"
CLEAR_UNCHECKED_SYMBOL = " "


# Special Unicode characters - http://unicode-table.com/en/
BLOCK_CHAR = "\u2588"
DBLWALL_CHAR = " \u2551"
DBL_BORDER_DOWN_RIGHT = "\u2554"
DBL_BORDER_DOWN_LEFT = "\u2557"
DBL_BORDER_UP_RIGHT = "\u255A"
DBL_BORDER_UP_LEFT = "\u255D"
DBL_BORDER_HORIZONTAL = "\u2550"
DBL_BORDER_VERTICAL = "\u2551"
DBL_BORDER_SINGLE_LEFT = "\u2562"
DBL_BORDER_SINGLE_RIGHT = "\u255F"
SGL_BORDER_HORIZONTAL = "\u2500"



# Create empty global board dictionary, used to store the values of all cells in the board
board = {}
score = 0
health = 100
bombsFound = 0
movesMade = 0
consecutiveClearMoves = 0
gameOver = False
gameWon = False
continueGame = True


# Formatting procedures
def clearScreen():
    print("\n" * 20)

def setRedText():
    print(RED_TEXT, end="")

def resetText():
    print(RESET_TEXT,end="")

def setBlueText():
    print(BLUE_TEXT, end="")

# Gameplay functions/procedures

def initialiseBoard():

    global board

    blankRow = []

    for row in range(0, BOARDSIZE):
        blankRow.append(0)

    for col in range(0, BOARDSIZE):
        board[chr(ASCII_A+col)] = list(blankRow)


def placeBombs(numBombs):
    # This procedure will randomly place bombs around the board.
    # The numBombs parameter allows us to state how many bombs we want when we call the procedure.
    # A while loop is used to repeat the process of randomly choosing a column and row for as many bombs as are required.
    global board
    placedBombs = 0
    while placedBombs < numBombs:
        randCol = ASCII_A + random.randint(0,BOARDSIZE-1) # This line selects a random number between 0 and the size of the board (usually 10) and adds it to the ASCII/Unicode value of the 'A' character. This means that we can generate a random letter for the column by starting with A and increasing by between 0 and 10 letters.
        randRow = random.randint(0, BOARDSIZE-1)
        if board[chr(randCol)][randRow] != BOMB_UNCHECKED: # Here we check that we haven't already randomly selectled this location to place a bomb.
            board[chr(randCol)][randRow] = BOMB_UNCHECKED # If the randomly chosen location hasn't been marked as containing a bomb, then set it as having a bomb
            placedBombs += 1


def checkForBomb(col, row):
    global board
    if board[col][row] == BOMB_UNCHECKED:
        return True
    else:
        return False


def previouslyChecked(col, row):
    global board
    if board[col][row] == CLEAR_CHECKED or board[col][row] == BOMB_CHECKED:
        return True
    else:
        return False


def getPlayerSpace():
    location = input("Enter a grid co-ordinate to move Mr. Bombastic to (e.g. A3): ")
    col = location[0] # first character of input is the row
    col =col.upper()
    row = location[1:] # second character onwards is the row
    row = int(row) - 1 # cast row value to integer and subtract 1 (as arrays/list indices start at 0, but our grid is shown as starting at 1
    return col, row


def playerMove():
    global board, health, movesMade, bombsFound, score, consecutiveClearMoves, gameOver, gameWon, continueGame
    col, row = getPlayerSpace()
    validMove = False
    message = ""
    while validMove == False:
        if previouslyChecked(col, row):
            print("You have already moved to this space. Please select another location.")
            col, row = getPlayerSpace()
        else:
            if checkForBomb(col,row):
                board[col][row] = BOMB_CHECKED
                message = RED_TEXT + "BOOM!" + RESET_TEXT + " You hit a bomb!"
                health = health - HEALTH_IMPACT
                consecutiveClearMoves = 0
                bombsFound += 1
            else:
                board[col][row] = CLEAR_CHECKED
                message = "Phew! No bomb here!"
                consecutiveClearMoves += 1
                score = score + (SCORE_BASE * consecutiveClearMoves)
            movesMade += 1
            showBoard()
            print(message)
            validMove = True

    # Check if game is over or won
    if health == 0:
        gameOver = True
        continueGame = False

    elif (movesMade - bombsFound) == ((BOARDSIZE * BOARDSIZE) - NUM_BOMBS):
        gameWon = True
        continueGame = False


# Graphics procedures

def showIntro():
    clearScreen()
    setBlueText()
    print("BBB    BBB   BB BB  BBB    BB    BBB  BBB  BBB    BB".replace("B", BLOCK_CHAR)) # B characters are replaced with a solid block (unicode 2558)
    print("B  B  B   B  B B B  B  B  B  B  B      B    B    B   B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B B B  B  B  B  B  B      B    B    B".replace("B", BLOCK_CHAR))
    print("BBB   B   B  B B B  BBB   BBBB   BB    B    B    B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B   B  B  B  B  B     B   B    B    B".replace("B", BLOCK_CHAR))
    print("B  B  B   B  B   B  B  B  B  B     B   B    B    B   B".replace("B", BLOCK_CHAR))
    print("BBB    BBB   B   B  BBB   B  B  BBB    B   BBB    BB".replace("B", BLOCK_CHAR))
    resetText()
    print("\n(C) Copyright 2016 Shiplake Games Ltd.\n")
    input("Press Enter to continue...")

def showBoard():
    global board

    clearScreen()
    showStatsHeader()
    # print column headings
    print(" " * LEFT_MARGIN ,end="")
    for col in range(0,BOARDSIZE):
        print(chr(ASCII_A+col).center(CELL_SIZE+1," "), end="")
    print("\n" + "=" * LEFT_MARGIN,end="")
    print("=" * BOARDSIZE * (CELL_SIZE+1))

    for row in range(0, BOARDSIZE):
        print (str(row+1).rjust(LEFT_MARGIN-2," ") + DBLWALL_CHAR ,end="")
        for col in range(0,BOARDSIZE):
            symbol = ""
            if board[chr(ASCII_A + col)][row]==CLEAR_UNCHECKED:
                symbol = CLEAR_UNCHECKED_SYMBOL
            elif board[chr(ASCII_A + col)][row]==BOMB_UNCHECKED:
                #setRedText()
                symbol = BOMB_UNCHECKED_SYMBOL
            elif board[chr(ASCII_A + col)][row]==CLEAR_CHECKED:
                symbol = CLEAR_CHECKED_SYMBOL
            elif board[chr(ASCII_A + col)][row]==BOMB_CHECKED:
                symbol = BOMB_CHECKED_SYMBOL
            #resetText()
            print(symbol.center(CELL_SIZE," "),end="|")

        print("")
        print("-" * (LEFT_MARGIN + (BOARDSIZE * (CELL_SIZE+1))))
    showStatsFooter()

def showStatsHeader():
    global health
    global score
    print(DBL_BORDER_DOWN_RIGHT + (DBL_BORDER_HORIZONTAL * (BORDER_WIDTH - 2)) + DBL_BORDER_DOWN_LEFT)
    print(DBL_BORDER_VERTICAL + "MR. BOMBASTIC".center(BORDER_WIDTH - 2, " ") + DBL_BORDER_VERTICAL)
    print(DBL_BORDER_SINGLE_RIGHT + (SGL_BORDER_HORIZONTAL * (BORDER_WIDTH -2)) + DBL_BORDER_SINGLE_LEFT)

    statString = "health: %3i%%          score:%5i" % (health, score)
    print(DBL_BORDER_VERTICAL + statString.center(BORDER_WIDTH - 2, " ") + DBL_BORDER_VERTICAL)
    print(DBL_BORDER_UP_RIGHT + (DBL_BORDER_HORIZONTAL * (BORDER_WIDTH - 2)) + DBL_BORDER_UP_LEFT)


def showStatsFooter():
    global bombsFound, consecutiveClearMoves, movesMade
    print("Board Clearance: %i / %i\nBombs found: %i\tConsecutive Clear Moves: %i" % (movesMade,(BOARDSIZE*BOARDSIZE), bombsFound, consecutiveClearMoves))
    print(SGL_BORDER_HORIZONTAL * BORDER_WIDTH)


# Main game play loop
showIntro()
initialiseBoard()
placeBombs(NUM_BOMBS)
showBoard()
while continueGame:
    playerMove()

if gameOver:
    showBoard()
    print("GAME OVER! Final score: %s" % score)

elif gameWon:
    showBoard()
    print("WINNER! Mr. Bombastic has cleared the board!")
