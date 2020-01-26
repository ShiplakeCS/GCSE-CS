"""
Pupil Management Database System
Updated Jan 2020 - AWD

This program is intended to demonstrate the use of multi-dimensional data structures, file reading and writing and 
data entry validation to support the teaching of GCSE Computer Science.
"""


def get_non_blank_input(message):
    """
    A 'helper' function that asks the user for input and checks that they haven't simply pressed 'Enter' without typing
    anything in. If they do, the while loop will cause the message (passed to the function via the message parameter)
    to be displayed again. This will repeat until a non-blank input is entered.

    Once a non-blank input has been entered, it is returned to the part of the program that called it where it can be
    used in just the same way as the standard input() function - i.e. its return value can be assigned to a variable,
    printed out, used in an if test, etc.

    :param message: The message to display to the user
    :return: The response entered by the user
    """

    response = ""

    while response == "":
        response = input(message)

    return response


def add_pupil(pl):
    """
    This procedure captures the details for a new pupils, saves them to a list and then adds that list to
    the list of pupils (passed as parameter pl).
    
    :param pl: list of pupils to add to 
    :return: None
    """

    # Create a blank list ready to store the new pupil's details
    pupil = []

    pupil.append(get_non_blank_input("Enter first name\n> "))

    pupil.append(get_non_blank_input("Enter surname\n> "))

    pupil.append(get_non_blank_input("Enter Date of Birth in the format DD/MM/YY\n> "))

    # Add the new pupil to the pupil list that was passed to the procedure as an argument (value) to the
    # pl parameter
    pl.append(pupil)  # Add the new pupil to the pupil list

    # Inform the user that the process has completed successfully
    print("Pupil added!")


def display_pupils(pupil_list):
    """
    This procedure displays the details of each of the pupils in the list that is passed via the pl parameter.
    
    :param pupil_list: the list containing the pupils to display
    :return: None
    """

    # If pupils have been entered in the pupil ist, the following lines will run...
    pupil_count = 0

    # Define a constant (HORIZONTAL_BORDER) used to store a reusable border in the output table (this is a time-saving
    # technique)
    HORIZONTAL_BORDER = "+" + "-" * 4 + "+" + "-" * 12 + "+" + "-" * 20 + "+" + "-" * 28 + "+"

    # Print column headers for the table
    print(HORIZONTAL_BORDER)
    print("|{0:^4}|{1:^12}|{2:^20}|{3:^28}|".format("#","First name", "Surname", "Date of Birth (DD/MM/YY)")) # Print headers
    print(HORIZONTAL_BORDER)

    # For every pupil in the pupil list (referenced in the parameter variable pl)...
    for pupil in pupil_list:

        pupil_count += 1

        # Print out the details of the pupil by referencing the keys in the pupil's dictionary
        print("|{0:^4}|{1:^12}|{2:^20}|{3:^28}|".format(pupil_count, pupil[0], pupil[1], pupil[2])) # Print fields)

    print(HORIZONTAL_BORDER)




def load_pupil_details():
    """
    This function opens and reads the 'pupils.csv' file and returns a multidimensional list that contains the details of
    all pupils.
    
    :param pupil_list: The list of pupils to add the data to.
    :return: None
    """
    # Try to execute the following code. If anything goes wrong, it will jump to the 'except' block below.

    pupil_list = []

    try:

        # Open the file in 'read' mode ('r').
        f = open('pupils.csv', 'r')

        # Read the first line of the file - this contains the headers. We don't need it, but by reading it and not
        # saving its data anywhere we move the file onto the second line, which is where our useful data starts.
        f.readline()

        # For each line in the file 'f'...
        for line in f:

            # Strip the '\n' from the end of the line - this will stop a new line character messing up the table layout
            # when the pupil data is displayed later.
            stripped_line = line.strip()

            # Provide feedback to the user about what is happening.
            print("Processing line:", stripped_line)

            # Once the line has been striped, split it up into different elements in a list whenever a ',' character
            # is found. This list is then assigned to the fields variable.
            pupil_list.append(stripped_line.split(","))

        # Tell the user the data has been successfully loaded.
        print("\nData loaded!\n")

    # If a FileNotFoundError exception is rasied do the following. This will happen if the user enters a filename for a
    # file that doesn't exist. By using try/except blocks we are able to 'catch' the exception (error) rather than
    # have the program crash.
    except FileNotFoundError:
        # Tell the user that the filename that they have entered cannot be found.
        print("Houston, we've had a problem... The pupils.csv file could not be found.")

    return pupil_list


def show_main_menu():
    """
    This procdure displays the main menu for the program and responds to the choice entered by the user, calling the
    appropriate subroutine to carry out their desired action. Before doing this, their input is compared to the values
    in the 'valid_choices' list to ensure that they have made a valid selection. If they haven't then they are asked to 
    enter their choice again.
    
    :return: None 
    """

    global pupil_list  # Use the global pupil_list variable within this procedure

    # Display the main menu options
    print("\n" * 40)  # Clear the screen by printing 40 blank lines
    print("+-------------------------------------+")
    print("| PUPIL MANAGEMENT SYSTEM - MAIN MENU |")
    print("+-------------------------------------+")
    print("| Please select an option:            |")
    print("|                                     |")
    print("| 1 - Show all pupil details          |")
    print("| 2 - Add a pupil                     |")
    print("| 3 - Search for a pupil              |")
    print("| 0 - Quit                            |")
    print("+-------------------------------------+")

    # Get the user to select an option. The valid_choices list is used to check that the option entered by the user
    # is a valid one. If it isn't then they will be asked to select another otion.
    valid_choices = ['1','2','3','4','5']
    option = ""
    while option not in valid_choices:
        option = get_non_blank_input("Please enter the number for your chosen option\n> ")

    # Respond the user's choice by calling the appropriate subroutine.
    if option == "1":
        display_pupils(pupil_list)

    elif option == "2":
        add_pupil(pupil_list)

    elif option == "3":
        search_pupil(pupil_list)

    elif option == "0":
        print("Goodbye!")
        quit()


def show_single_pupil_details(pupil):

    HORIZONTAL_BORDER = "+" + "-" * 12 + "+" + "-" * 20 + "+" + "-" * 28 + "+"

    # Print column headers for the table
    print(HORIZONTAL_BORDER)
    print("|{0:^12}|{1:^20}|{2:^28}|".format("First name", "Surname", "Date of Birth (DD/MM/YY)")) # Print headers
    print(HORIZONTAL_BORDER)

    # Print out the details of the pupil by referencing the keys in the pupil's dictionary
    print("|{0:^12}|{1:^20}|{2:^28}|".format(pupil[0], pupil[1], pupil[2])) # Print fields)

    print(HORIZONTAL_BORDER)


def search_pupil(pupil_list):

    pass # replace with your code



# Create an empty list that will be used to store all of the pupils in the database
pupil_list = load_pupil_details()

# Start the program by calling the main_menu() procedure. This is done in a while True loop, which will always repeat
# until the program is quit. This means that the user will always be returned to the main menu when a subroutine has
# finished.

while True:

    show_main_menu()
    # Wait for the user to press the Enter key after each action and before showing the menu again.
    input("Press Enter to continue...")