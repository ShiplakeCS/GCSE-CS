"""
Pupil Management Database System
AWD 2017

This program is intended to demonstrate the use of multi-dimensional data structures, file reading and writing and 
data entry validation to support the teaching of GCSE Computer Science.
"""

# Create an empty list that will be used to store all of the pupils in the database
pupil_list = []


def add_pupil(pl):
    """
    This procedure captures the details for a new pupils, saves them to a dictionary and then adds that dictionary to
    the list of pupils (passed as parameter pl).
    
    :param pl: list of pupils to add to 
    :return: None
    """

    # Create a blank dictionary ready to store the new pupil's details
    pupil = {'f_name': "",
             's_name': "",
             'DOB': ""}

    # Rather than simply saving whatever the user enters as the dictionary's values, a while loop is used to check
    # the value of what they user has entered. If it's blank then the user is asked to enter the details again. They
    # will continue to be asked to enter details until a non-blank value is entered. This makes the program more robust.
    while pupil['f_name'] == "":
        pupil['f_name'] = input("Enter first name\n> ")

    while pupil['s_name'] == "":
        pupil['s_name'] = input("Enter surname\n> ")

    while pupil['DOB'] == "":
        pupil['DOB'] = input("Enter Date of Birth in the format DD/MM/YY\n> ")

    # Add the new pupil dictionary to the pupil list that was passed to the procedure as an argument (value) to the
    # pl parameter
    pl.append(pupil)  # Add the new pupil to the pupil list

    # Inform the user that the process has completed successfully
    print("Pupil added!")


def display_pupils(pl):
    """
    This procedure displays the details of each of the pupils in the list that is passed via the pl parameter.
    
    :param pl: the list containing the pupils to display 
    :return: None
    """

    # If no pupils have been added to the pupil list passed via parameter pl then we need to show an error message
    # instead of attempting to print out each pupil's details. We can test whether any pupils have been added using
    # the built-in len() function, which returns the number of elements in a list. If it returns 0 then the pupil list
    # list is empty.
    if len(pl) == 0:
        print("+----------------------------+")
        print("| No pupils in the database! |")
        print("+----------------------------+")
        input("\nPress Enter to continue...")
        return  # The 'return' keyword causes the procedure to stop at this point

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
    for pupil in pl:

        pupil_count += 1

        # Print out the details of the pupil by referencing the keys in the pupil's dictionary
        print("|{0:^4}|{1:^12}|{2:^20}|{3:^28}|".format(pupil_count, pupil['f_name'], pupil['s_name'], pupil['DOB'])) # Print fields)

    print(HORIZONTAL_BORDER)

    input("Press Enter to continue...")  # This is a useful trick to get the user to press 'Enter' before moving on


def save_pupil_details(pl):
    """
    This procedure saves the details of the pupils found in the list passed as pl to a file of the user's choosing. The
    output format will be a CSV (comma separated variable) file. This means that each line of the file presents another
    pupil's details, each field being separated by commas. This file format is a simple way of using a text file to 
    store organised data and is compatible with many spreadsheet applications.
    
    :param pl: list of pupils to save to file 
    :return: None
    """

    # Get a file name
    filename = get_non_blank_input("Enter a filename to save the data\n> ")

    # Open the file in 'write' mode ('w') and assign it to variable f
    f = open(filename, 'w')

    # Write the header row, remembering to add the new line special character ('\n') at the end
    f.write("First name, Surname, Date of Birth (DD/MM/YY)\n")

    # For each pupils, write to the file the details stored in the pupil dictionary
    for pupil in pl:
        f.write("{0},{1},{2}\n".format(pupil['f_name'], pupil['s_name'], pupil['DOB']))

    # Close the file once it is finished with - this allows other applications to open it
    f.close()


def load_pupil_details(pl):
    """
    This procedure asks users to enter a filename before opening that file and reading each line, populating the list
    of pupils passed by the pl parameter with dictionaries representing the pupil details on each line of the loaded
    file.
    
    :param pl: The list of pupils to add the data to. 
    :return: None
    """
    # Warn users that they will lose their existing data if they load new data.
    print("+------------------------------------------------------------+")
    print("| Caution! Loading pupil details will overwrite any existing |")
    print("| data in the database!                                      |")
    print("+------------------------------------------------------------+")

    # Ask the user to confirm that they wish to continue loading data. A while loop is used so that they keep being
    # asked if they don't enter 'y' or 'n' at the prompt. The .lower() string method is used to convert whatever is
    # entered into lowercase, that way if they enter 'Y' it will be converted to 'y' and will be correctly responded to.
    confirm = ""
    while confirm.lower() != "y" and confirm.lower() != "n":
        confirm = input("Are you sure you wish to do this (y/n)?\n> ")

    # If the user responds with 'n' to say that they don't want to overwrite the data then inform them that the
    # operation has been cancelled and then exit the function by using the return keyword
    if confirm.lower() == "n":
        print("Operation cancelled!")
        return

    # Clear the pupil list, ready for new data to be loaded
    pl.clear()

    # Get the filename for the data file to load from
    filename = get_non_blank_input("Please enter the name of the file to load the pupil data from\n> ")

    # Try to execute the following code. If anything goes wrong, jump to the 'except' block below.
    try:

        # Open the file that has the name stored in the filename variable. Open it in 'read' mode ('r').
        f = open(filename, 'r')

        # Read the first line of the file - this contains the headers. We don't need it, but by reading it and not
        # saving its data anywhere we move the file onto the second line, which is where our useful data starts.
        f.readline()

        # For each line in the file 'f'...
        for line in f:

            # Provide feedback to the user about what is happening.
            print("Processing line:", line.rstrip("\n"))

            # Strip the '\n' from the end of the line - this will stop a new line character messing up the table layout
            # when the pupil data is displayed later.
            # Once the line has been striped, split it up into different elements in a list whenever a ',' character
            # is found. This list is then assigned to the fields variable.
            fields = line.rstrip("\n").split(",")

            # Create a new dictionary an assign it to the pupil variable. Assign the value in the first element in the
            # fields list (the pupil's first name) to the 'f_name' key in the dictionary. Assign the data in the second
            # element to the 's_name' key and the data in the third element in the fields list to the 'DOB' key.
            pupil = {'f_name': fields[0],
                     's_name': fields[1],
                     'DOB': fields[2]}

            # Append (add) the new pupil to the lit fo pupils, passed to the procedure by the pl parameter.
            pl.append(pupil)

        # Tell the user the data has been successfully loaded.
        print("\nData loaded!\n")

    # If a FileNotFoundError exception is rasied do the following. This will happen if the user enters a filename for a
    # file that doesn't exist. By using try/except blocks we are able to 'catch' the exception (error) rather than
    # have the program crash.
    except FileNotFoundError:
        # Tell the user that the filename that they have entered cannot be found.
        print("Error! No file with that name could be found.")

    # Wait for the user to press the Enter key before moving on.
    input("Press Enter to continue...")


def main_menu():
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
    print("| 3 - Save pupil details to file      |")
    print("| 4 - Load pupil details from file    |")
    print("| 5 - Quit                            |")
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
        save_pupil_details(pupil_list)

    elif option == "4":
        load_pupil_details(pupil_list)

    elif option == "5":
        print("Goodbye!")
        quit()

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

# Start the program by calling the main_menu() procedure. This is done in a while True loop, which will always repeat
# until the program is quit. This means that the user will always be returned to the main menu when a subroutine has
# finished.
while True:
    main_menu()
