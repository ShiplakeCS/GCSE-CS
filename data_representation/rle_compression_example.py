"""
Run Length Encoding (RLE) lossless compression example.

This algorithm applies RLE compression to a string on a character-by-character basis.

It works by keeping track of the most recent unique letter/character that it has seen as it iterates through all of the letters in the string. If the currently inspected letter is the same as the most recent unique letter then the count variable is incremented. When a new unique character is encountered, the previous unique character and its count is added to the output string and the most recent unique character variable is updated and the count reset to 1.

BTW, RLE is not an efficient means of compressing text, but you can see the principle of the technique from this example.
"""

text = "aaabbcddddeeffffgg"  # Message to compress
rle = ""  # Placeholder for output string

most_recent_unique_character = text[0]  # The first "most recent unique character" is the first character in the sequence
count = 1  # Assuming an input string length > 0, the rle encoding will contain at least 1 of the first characters, so start with count = 1.


x = 1  # An iterator variable used by the while loop, starting at 1, not 0, as we dont need to inspect the first character in the input string

while x < len(text):  # Start a while loop to work through all the characters in the text to compress
    if text[x] != most_recent_unique_character:  # If the current character is not the most recent unique character
        rle += most_recent_unique_character + str(count)  # add the most recent unique character and its count to the rle (output) string
        most_recent_unique_character = text[x]  # Update the most recent unique character to the current character
        count = 1  # Restart the count for the new character at 1
    else:
        count +=1  # If the current character is the same as the most recently seen unique character then just add 1 to the count for that character
    x += 1  # Move on to the next character in the input string

rle += most_recent_unique_character + str(count)  # Once the final character has been inspected, add the final unique character and its count to the RLE output string

print(rle)  # Print the rle encoding for the message