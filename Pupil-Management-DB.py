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


# Call the add_pupil() procedure, passing it the pupil_list to save the new pupil into
add_pupil(pupil_list)