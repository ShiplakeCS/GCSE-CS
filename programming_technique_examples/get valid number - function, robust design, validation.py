"""
CHALLENGE: Write a function that will ask a user for a number and check to see if it is within a specified range.
If not, the user will be asked to try again. Once a valid number has been entered it is returned to the part of the
program that asked for it.

Your function should:
- Accept a parameter that specifies the message that should be shown to the user as the input prompt
- Accept an OPTIONAL parameter that specifies the minimum acceptable number
- Accept an OPTIONAL parameter that specified the maximum acceptable number
- return the valid number

Tips:
- You want your function to be re-usable as multipurpose so it's probably best to work with floats rather than ints,
  otherwise it will not work for future applications where decimal points are required.
- You can use other in-built functions as part of your function to test the data entry
- You can use loops, try/except and recursion (functions that call themselves) as you see fit

"""

def getValidNumber(message, min=None, max=None):

    try:
        num = float(input(message + ': ')) # if the value entered isn't a number, the casting to a float will fail and raise a ValueError which is caught below and will cause the function to be run again.

        if min is not None and num < min: # If a minimum value is set and the number entered is less than the minimum, raise a ValueError that will be caught below and cause the function to run again.
            raise ValueError

        if max is not None and num > max: # if a maximium value is set and the number enteres is greater than the maximum, raise a ValueError that will be caught below and cause the function to run again.
            raise ValueError

        return num

    except ValueError: # A ValueError has been raised so something isn't right with the input. The following block of code will give the user some feedback and allow them to try again.

        print("\nPlease ensure that you enter a number", end='') # Tell the user what's gone wrong.
        if min is not None and max is not None: # The information in the error message will differ depending on whether a min, max or both are specified.
            print(" between %f and %f." % (min, max))
        elif min is not None:
            print(" greater than or equal to %f." % min)
        elif max is not None:
            print(" less than or equal to %f." % max)
        else:
            print(".")
        print("") # Prints a blank line (space) between error message and next attempt at entering valid data.

        return getValidNumber(message, min, max) # call the function again, ensuring that we pass any parameter values on to the second instance of this function

valid_num = getValidNumber("Please enter a number between 1.24 and 9.87", 1.24, 9.87)
print("\nUser entered: %f\n" % valid_num)

valid_num = getValidNumber("Please enter a number greater than -5", -5) # No maximum so we can simply ignore it and the default None will be used (specified in the def statement)
print("\nUser entered: %f\n" % valid_num)

valid_num = getValidNumber("Please enter a number less than 1010",None,1010) # No minimum, but we have to provide something for its parameter so we use None
print("\nUser entered: %f\n" % valid_num)
