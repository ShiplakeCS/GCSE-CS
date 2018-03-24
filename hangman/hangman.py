"""
Hangman game

Adam Dimmick, 2018

--

Use to teach many GCSE CS principles, including:
 - program (solution) design / decomposition and abstraction
 - pseudocode to real code
 - loops
 - subroutines
 - selection
 - Boolean returns
 - file handling
 - lists / arrays
 - global constants
 - debugging to find out state of variables at breakpoints (e.g. what the word to guess is)

Things to add to teach even more:
 - input validation
    currently there is nothing stopping players from entering multiple letters at the prompt
    Could then teach testing / creating test plans with different test data
    Unit testing - testing each subroutine independently

 - difficulty levels:
    easy = 3 - 5 letter words, unlimited turns
    medium = 6 - 8 letter words, 15 guesses
    hard = 9+ letter words, 12 guesses

    Needs an algorithm to process word list and add words to three lists for easy, medium and hard words

 - main menu to select difficulty level or load a different words file
 - exception handling - if word file cannot be found
 - could use as back-end for a web-based hangman game (Flask) that provides an input form and shows the state of the
    hangman as different PNG graphics, selected as appropriate.

Word file source: https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt

"""
from random import choice

# Define global constants
WORD_FILE = 'google-10000-english-no-swears.txt'
MAX_GUESSES = 12


def load_words(file_name=WORD_FILE):

    with open(file_name, 'r') as world_file:
        word_list = world_file.readlines()

    return word_list


def say_hello():
    print("Hi there!")


def get_guess_word():

    # load words
    word_list = load_words()

    # choose a random word to guess
    return choice(word_list).rstrip("\n").upper()


def letter_is_correct(letter, guess_word):

    if letter.upper() in guess_word:
        print("\n" + u"\U0001F44D" + " Good guess!\n")
        return True
    else:
        print("\n" + u"\u2620" + " Nope, try again!")
        return False


def game_over(incorrect_guesses, max_guesses=MAX_GUESSES):

    if incorrect_guesses >= max_guesses:
        print("\nYou lose! :(\n")
        return True
    else:
        return False


def show_guessed_letters(guesses):
    print("You have guessed the following letters:")
    output = ""
    for letter in guesses:
        output += letter + ", "
    print(output + "\n")


def game_won(correct_letters, guess_word):

    for letter in guess_word:
        if letter not in correct_letters:
            return False

    print("\nYOU WIN!\n")
    return True


def show_letters_and_blanks(guess_word, guessed_letters):

    output = ""

    for letter in guess_word:
        if letter in guessed_letters:
            output += letter
        else:
            output += "-"

    print("\nWORD TO GUESS: " + output + "\n")


def show_hangman(incorrect_guesses):

    hangman = ""

    if incorrect_guesses == 1:
        hangman = "\n" * 9
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 2:
        hangman = "\n" * 7
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 3:
        hangman = "\n" * 4
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 4:
        hangman =           "   -+-------\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 5:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 6:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 7:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 8:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     -+-\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 9:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     -+-\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 10:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     -+-\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     /\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 11:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |      O\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     -+-\n"
        hangman = hangman + "    |      |\n"
        hangman = hangman + "    |     /\\\n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "    |    \n"
        hangman = hangman + "------------------\n"

    if incorrect_guesses == 12:
        hangman =           "   -+------+\n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |  \n"
        hangman = hangman + "    |    O-+----/\n"
        hangman = hangman + "------------------\n"


    clear_screen()
    print(hangman)
    print("Number of incorrect guesses:", incorrect_guesses)

def clear_screen():
    print("\n" * 40)

def play_hangman():

    guess_word = get_guess_word()

    incorrect_guesses = 0

    letters_guessed = []

    correct_letters = []

    # Main gameplay loop
    while not game_won(correct_letters, guess_word) and not game_over(incorrect_guesses):

        show_hangman(incorrect_guesses)

        show_letters_and_blanks(guess_word, correct_letters)
        show_guessed_letters(letters_guessed)

        guess = input("Enter a letter to guess: ").upper()

        if guess in letters_guessed:
            print("You've already guessed that letter!")

        else:

            letters_guessed.append(guess)

            if letter_is_correct(guess, guess_word):
                correct_letters.append(guess)
            else:
                incorrect_guesses += 1



    print("Game finished! The guess word was:", guess_word)


play_hangman()

say_hello()