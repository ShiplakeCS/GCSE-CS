"""
Programming Techniques examples for OCR J276 GCSE Computer Science
Specification reference 2.2 Programming Techniques

This program contains examples implementations of programming techniques specified
in section 2.2 of the OCR J276 GCSE Computer Science specification.

Specifiation point:
- the use of variables, constants, operators, inputs, outputs and assignments
"""

"""
1. Variables and assignments

Variables are named locations in memory used to temporarily store data during a program's execution.

Variable declaration
--------------------

In some programming languages, variables need to be declared before they can be used to store data.

Declaring a variable means to state its name (identifier) and the type of data that it will contain, for example 
    var player_score Int.

Python doesn't require that variables are explicitly declared before they are used. Instead, they are automatically 
declared upon first use. Python also doesn't require that the type of data being stored is stated, it simply infers the 
data's type from the data that is assigned to (stored in) the variable.

Variable assignment
-------------------

Assignment simply means giving a variable a value. Rather than "setting" a variable to a value or "putting a value in
the variable", the technical term is to "assign a value to a variable."
"""
# The following is an example of how to declare a variable and assign a value to it in Python:

player_name = "Bob"

# Note the format - the variable's identifier (name) always goes on the left, followed by a single = (a single equals
# sign is called the assignment operator) and then the data to be stored.

"""
Using a variable
----------------
# To access a variable's data, simply use the identifier of the variable wherever its data is required.
"""
# The following is an example of how to access the value of a variable via its identifier in Python:

print("Hello " + player_name)
"""
Assigning a new value to a variable
-----------------------------------

It is easy to assign new data to a variable. Simple state the variable's identifier, followed by the assignment operator
(=) and the value to be assigned, just as when assigning the variable's initial value.
"""
# The following example shows a new value being assigned to the player_name variable and then accessing this new value
# from the variable.

player_name = "Mary"
print("Hello " + player_name)

"""
Choosing a sensible variable identifier
---------------------------------------
It is important that variable identifiers (names) are clearly descriptive of the data that they hold. For example, 
player_name is clearly going to be used to store the name of the player in a game. It would be perfectly possble to 
write x = "Mary", but it wouldn't be at all clear what the purpose of variable x is.

Using sensible, clear and descriptive variable identifiers helps to ensure that code is easily understood by yourself
and other developers and will reduce the need for documentation and the likelihood for making errors. If errors do
appear, the code will be easier to understand and therefore the source of errors will be easier to identify and fix.

There are some other rules for chosing identifiers:
    1. Identifiers cannot include spaces. Underscores or "CamelCase" can be used where an identifier is to be made from
        two or more words.
    2. Identifiers can contain letters, numbers and underscore symbols (_) only. However, in Python, variable
        identifiers cannot start with a number but can contain a number anywhere else in the identifier.
    3. Certain words cannot be used as identifiers if they are existing built-in commands, statements or functions. For
        example, you cannot use 'if' as a variable identifier.
    4. Identifiers are case sensitive. For example, myAge and myage are two different identifiers and cannot be used
        interchangably. Forgetting capital letters in identifiers is a very common cause of syntax error.
    5. Identifiers should be short, but not so short as to be meaningless or unclear.

Examples of identifiers in Python
---------------------------------
"""

# The following are two different variables with unique identifiers and values, even though they appear equivalent to us humans:
myAge = 17
myage = 15
print(myAge)
print(myage)

# The following identifiers are far too long for use in a real program - the chance of mistyping them is very high indeed!
thisIsAReallyLongVariableIdentifierWrittenInCamelCase = True
this_is_a_really_long_variable_identifier_written_using_underscores = True

# The following identifier includes all of the permitted character types - letters, numbers (not at the start) and underscores.
player1_score = 1000

"""
2. Constants
------------

Constants are very much like variables, except that their assigned values do not change during the execution (running)
of a program.

Constants are very useul for representing values that you don't want to have to re-type throughout the program, either
because they are awkward or because you would have to replace many instances of a fixed value if you were to change this
value during your design of the program.

In some programming languages, constants are declared using a specific keyword such as let or const. In Python, there is
no specific declaration for a constant, so CAPITAL IDENTIFIERS are used to help identify constants within the program.
"""
# For example, PI is often used in place of the number pi (3.14159265) as in the example below:

PI = 3.14159265

def circle_area(radius):
    return PI * radius * radius

def circle_circumfrence(radius):
    return 2 * PI * radius

"""
In the above example, PI has been declared as a constant value at the start of the program and can be used in place of
the actual value of PI wherever it is needed (within the two subroutines circle_area() and circle_circumfrence().

Contstants can also be used for defining other values that won't change during a program's execution such as the
maximum number items that can be stored in a database:
"""

MAX_ITEMS = 5000

items_list = []

def add_item(item):

    if len(items_list) > MAX_ITEMS:
        print("Sorry! Maximum number of items exceeded!")

    else:
        items_list.append(item)

"""
3. Operators
------------

Operators are symbols and statements that perform specific functions within a program. We have already come across one
operator - the assignment operator (=) which is used to assign a value to a variable.

The values used either side of an operator are called operands. So, in the simple mathematical expression 1 + 2, + is 
the operator and 1 and 2 are the operands.

There are a number of types of operator:
- Mathematical operators
- Relational operators
- Boolean (logical) operators

Mathematical operators
----------------------

Mathematical operators are used to form mathematical statements that will perform calculations. The main operators are:
    
    + addition
    - subtraction
    / division
    * multiplication
    ^ exponentiation (raising to the power of, e.g. 3 ^ 2 is 3 squared) - in Python this is done with **
"""

# Examples

addition = 2 + 5
print(addition)

subtraction = 6 - 2
print(subtraction)

division = 9 / 2
print(division)

multiplication = 4 * 5
print(multiplication)

exponentiation = 2 ** 3  # 2 cubed = 2*2*2
print(exponentiation)

"""
There are two other mathematical operators that you need to know for the OCR GCSE course - MOD and DIV

MOD
---

The MOD operator performs a "modulo" operation which finds the remainder of a divison of two numbers. For example, 5 
divided by 2 is 2.5 - if we were to think of this as fractions we could say that 5 over 2 is 2 and 1 over 2. Therefore 
5 MOD 2 is 1 - because the remainder when 5 is divided by 2 is 1. (2 goes into 5 twice, 2 * 2 is four, leaving a 
remainder of 1 unit).

There is no MOD keyword in Python, instead the % symbol is used instead:
"""

mod_calculation = 5 % 2
print(mod_calculation)

"""
MOD can be useful for determining whether a number is odd or even as every even number will return no remainder when divided by 2
whereas every odd number leaves a remainder of 1:
"""

print(4 % 2)
print(3 % 2)

"""
We could use MOD in a subroutine to test if a given number is odd or even:
"""

def test_if_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(test_if_even(6))
print(test_if_even(7))

"""
MOD can be used to check whether a number is mulitple of any other number:
"""

def test_if_multiple_of_five(number):
    if number % 5 == 0:
        return True
    else:
        return False

print(test_if_multiple_of_five(15))
print(test_if_multiple_of_five(41))

"""
This might be useful if we wanted to pause an output every 10 lines we could do the following:
"""

line_number = 0

while line_number < 30:

    line_number = line_number + 1
    print("Hello!")

    if line_number % 10 == 0:
        input("\nPress Enter to continue...")


"""
DIV
---

The DIV operator performs a special type of division called Integer division or Floor division. The result of a DIV
operation is the WHOLE PART of the result of dividing one number by another. For example 7 DIV 2 = 3. Note that this is
NOT the same as rounding up the result to the nearest whole number. If anything, it's a rounding down operation but it's
easier (and more accurate) to think of DIV as a division where anything after the decimal point has been sliced off and
lost.

As with MOD, Python doesn't have DIV operator, instead it uses two foward slashes - // - to perform this operation:
"""

div_example = 18 // 4  # This will return 4 as 18/4 is 4.5 - the whole number part of this is 4.
print(div_example)

"""
DIV operations are faster for a computer to perform and are useful when a fractional part (the bit after a decimal
point) isn't necessary. For example, if scaling an image down, it's not possible to show a fractional part of a pixel
but only whole pixels, therefore floor division is more appropriate.

As an aside, DIV and MOD can be combined to show the result of a division in fraction form:
"""
def fraction_division(numerator, denominator):

    whole_part = numerator // denominator
    quotient_part = numerator % denominator

    print(str(whole_part) + " and " + str(quotient_part) + "/" + str(denominator))  # the str() function is used to
    # convert the numerical values into strings so that they can be joined with the other string data in the output
    # message. This will be explained in more detail when looking at data types.

fraction_division(19,3)

"""
Relational operators
--------------------

Relational operators are used to determine the relationship between two values, such as whether one is bigger or smaller
than another or whether they are both equal.

The relational operators that you need to know are:

    >   greater than
    <   less than
    >=  greater than or equal to
    <=  less than or equal to
    ==  equal to (note the double equals - that's because a single equals is used to assign values to variables)
    !=  not equal to (something <> is used for not equal to, but not in Python)

The result of all relational operators is either True or False (note the capital T and F!) - these are called "Boolean
values", named after the famous mathematician and logician George Boole.

Because relational operators result in True or False values, they can be used in selection statements such as if/else.
"""
# Try changing the values assigned to each of the 'num' variable below to see the effect on the if statements.

num1 = 4
num2 = 9

if num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is bigger than num2")

num3 = 4
num4 = 4

if num3 == num4:
    print("num3 is the same as num4")
else:
    print("num3 and num4 are different")

num5 = 18
num6 = 17

if num5 >= num6:
    print("num5 is either the same as num6 or it is bigger than num6")
else:
    print("num5 is definitely smaller than num6")

"""
Boolean operators
-----------------

Boolean operators perform logic operations and always result in True and False values. The Boolean operators for GCSE
are:

    AND  - evaluates to True if both operands are True; False if either operand is False
    OR   - evaluates to True if either of the two operands are True; False if both operands are False
    NOT  - inverts / negates a logical value so True becomes False and False becomes True

In Python, the Boolean operators are written in lowercase letters - and, or, not

Boolean operators are used with selection statements to complex "conditions" that must be evaluated before the program
can proceed. Let's use the example of boarding a flight where the traveller must have both their passport and boarding
pass:
"""

got_passport = True
got_boarding_pass = False

if got_passport == True and got_boarding_pass:
    print("You're all set to fly!")
else:
    print("Sorry, you need both your passport and boarding pass to fly.")

"""
For another example, let's combine Boolean opeators together to form event more complex statements.

Let's pretend you are allowed to go out but only if you've done your homework and tidied your room. If you haven't got
any homework then it doesn't matter whether you've done it or not.
"""

# Try playing around with the values set to got_homework, done_homework and tidied_room to see the effects on the
# outcome.

got_homework = True
done_homework = False
tidied_room = True

if tidied_room == True and ((got_homework == True and done_homework == True) or (got_homework == False)):
    print("You can go out!")
else:
    print("Too bad - you've got work to do!")

"""
4. Inputs and Outputs
---------------------

Outputs

We have seen a lot of use of outputs in our programs so far. To output a message to the screen, we use the built-in
print() statement:
"""

print("Hello world!")

"""
In psuedocode, OUTPUT() is sometimes used in place of print().

The print() function shows whatever string data it is provided with. If non-string data is given an attempted is made to 
convert it to a string equivalent in order to show it.

Inputs

A user's input can be taken by the keyboard using the built-in input() function.

Taking an input requires two things:
    1. A variable to assign the input value
    2. An input() function to gather the user's input

In Python, an optional message or prompt can be provided within the input() function that is output to the screen just
prior to waiting for the user's input.

The following code is an example of how to use input() in Python to ask the user for some information, collect it and
assigns it to a variable.
"""

player_name = input("Please enter your name: ")

# We can then access the value that the user has input by referencing the variable that stores the input value:

print("Hi " + player_name + "!")

"""
Taking in numerical inputs

The input() function always collects data as string, because a keyboard can only provide text data. If we want to use
the input as a number for a mathematical or relational operation, we first need to convert it from a string into a
numerical data type, such as an integer, using a method called casting. We will look at this in more detail when we look
at data types, but for now here is a quick example:
"""

player_age = input("Please enter your age: ")

player_age = int(player_age)

if player_age >= 10:
    print("You are old enough to play.")
else:
    print("Sorry, you are too young to play this game.")