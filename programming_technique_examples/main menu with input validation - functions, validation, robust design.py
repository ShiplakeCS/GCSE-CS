"""
Menu Helper Function
----------------------

This program demonstrates how you can write a helper function to make it really easy to show consistent main menu screens.

Combine this with other helper functions to obtain valid input from the user and you'll be sure to have a robust and efficient
program!

"""

def showMenu(title, options, width=40):
	
	# Decalre constants for each of the Unicode border characters that we want to use to draw a border around our menu - see http://jrgraphix.net/r/Unicode/2500-257F
	TOP_LEFT_DBL = chr(0x2554) # Unicode character 0x2554 (remeber, 0x means a hex/base-16 number
	TOP_RIGHT_DBL = chr(0x2557)
	MID_LEFT_SNG = chr(0x255F)
	MID_RIGHT_SNG = chr(0x2562)
	BOTTOM_LEFT_DBL = chr(0x255A)
	BOTTOM_RIGHT_DBL = chr(0x255D)
	HORIZ_DBL = chr(0x2550)
	HORIZ_SNG = chr(0x2500)
	VERT_DBL = chr(0x2551)
	
	# Print the top border, making its width equal to the value of th width parameter. Remember that when you use * with a string, it duplicates it for as many times as you specify.
	print(TOP_LEFT_DBL + (HORIZ_DBL * (width - 2) + TOP_RIGHT_DBL))
	
	# Print the title of the menu, centered
	print(VERT_DBL + title.center(width - 2) + VERT_DBL)
	
	# Print a single horizontal line separating the menu header from the main contents
	print(MID_LEFT_SNG + (HORIZ_SNG * (width - 2) + MID_RIGHT_SNG))
	
	# Print a message asking the user to select an option
	print(VERT_DBL + "Please select an option:".ljust(width-2, " ") + VERT_DBL)
	
	# Print a blank line to give some space before the options
	print(VERT_DBL + " " * (width - 2) + VERT_DBL)
	
	# Print the options that have been passed in the options list. Also, collect a list a valid option choices for use later
	
	validChoices = [] # Empty list that will hold each option's number
	
	for item in options: # for each item in the options list, do the following
		
		optionString = VERT_DBL + " {0} - {1}".format(options.index(item) + 1, item) # start a string that will be used to present the option. It starts with the double vertical wall, followed by a string that contains the number of the option in the list (plus 1, because indexes in arrays start at 0) and the text of the option itself
		optionString = optionString.ljust(width - 1, " ") # Take the option string that we have started and make it left justified within a block that is 1 character less than the width of the menu
		optionString = optionString + VERT_DBL # Finally, add a final double vertical wall to the right of the option string
		print(optionString) # Print the complete option string
		validChoices.append(str(options.index(item) + 1))
	
	# Print bottom border
	print(BOTTOM_LEFT_DBL + (HORIZ_DBL * (width - 2)  + BOTTOM_RIGHT_DBL))

	return validChoices


def getValidChoice(message, options: list):
    # message - a string value that will be presented as the prompt
    # options - a List containing the valid options that the user can enter

    lower_options = [] # Create a new empty list to store lowercase versions of the valid options

    for option in options:
        lower_options.append(option.lower()) # Fill the lower_options list with lowercase versions of the options - this means that the entry 'a' and 'A' will be considered equivalent

    choice = input(message + ": ") # Added extra space on the end because no one ever remembers this...

    if choice.lower() in lower_options:
        return choice # the choice made is in our list of valid choices, so we can go ahead and return it to the part of the program that asked for it

    else:
        print("\nI'm sorry, that isn't an option on the menu. Please select one of the following options: ", end="")
        for option in options:
            print(option + ", ", end="") # This is optional, but is nice as it shows the user all of the valid options that they can choose from.
        input("\n\nPress Enter to try again...\n") # This is a neat trick - using input to wait for the user to continue. You don't need to assign its output to a variable as you are not going to use it for anything.
        return getValidChoice(message, options) # Here we are calling the function to run again, because the user obviously needs to make another choice. We write 'return' before it so that, once called, the valid that this new instance of the function returns is then retruend on to the function that called getValidChoice initially.



# Finally, we need to call our procedure in order to display the menu
menuOptions = showMenu("MY AMAZING GAME!", ["Play game", "Enter player names", "Show high scores", "Quit"])
choice = getValidChoice("Please select an option from the menu: ", menuOptions)

print("User entered: {0}".format(choice))
