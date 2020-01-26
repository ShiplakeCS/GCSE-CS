"""
CHALLENGE: Write a function that continues to ask a user for some input until a valid input has been provided.

 You can:
 - Use loops or try/except to check for valid entry
 - Use loops or recursion for re-running your function should you need to

 Your function should:
 - Accept a 'message' parameter that is presented to the user at the input prompt
 - Accept as parameter a list or range of acceptable values (i.e. if your menu has options 1 to 4, you should be able to
   tell your funciton this via a parameter so it knows the bounds to check within. You should NOT hard-code any
   particular range of valid options into your function otherwise it cannot be re-used for other menus!
- Allow users to enter letters as either capital or lowercase letters and them treated as the same
- Keep asking the user for their input until a valid option is entered
- Show an error message when they enter an invalid option before asking them to enter it again
- Present a list of valid options if they enter an invalid one
- Return the valid input once one has been entered

Tips:
- There is a really useful keyword 'in' that can be used to test if a value is found in a list, for example: if name in
  class would be true if name was 'Bob' and class was ["Bob", "Jane", "Freddie"] but would be false if name was 'Carl'.
  Try using this keyword to test if the user's input is found in the lest of acceptable choices.
- At this stage, don't worry about casting strings to integers to handle numerical input, just accept character/string
  forms of numbers, otherwise your function won't be able to handle a mix of letter and number inputs and it's important
  that you write a function that can be re-used in many different contexts.

"""

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
        print("\nI'm sorry, I didn't recognise that choice. Please select one of the following options: ", end="")
        for option in options:
            print(option + ", ", end="") # This is optional, but is nice as it shows the user all of the valid options that they can choose from.
        input("\n\nPress Enter to try again...\n") # This is a neat trick - using input to wait for the user to continue. You don't need to assign its output to a variable as you are not going to use it for anything.
        return getValidChoice(message, options) # Here we are calling the function to run again, because the user obviously needs to make another choice. We write 'return' before it so that, once called, the valid that this new instance of the function returns is then retruend on to the function that called getValidChoice initially.

# Examples of use
valid_choice = getValidChoice("Please enter a direction, either up, down, left or right", ["up", "down", "left", "right"])
print("User entered: %s\n" % valid_choice) # This is an example of how to use string formatting to substitute a string value where the %s appears. This can be a neater way that writing lots of parts of text as strings that are joined together with '+'

valid_choice = getValidChoice("Please select a menu option, A, B or C", ["A", "B", "C"])
print("User entered: %s\n" % valid_choice)

valid_choice = getValidChoice("Please enter a number between 1 and 5", ["1", "2", "3", "4", "5"])
print("User entered: %s\n" % valid_choice)
