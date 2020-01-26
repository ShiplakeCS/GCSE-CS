words = []
compressed_output = ""
punctuation = "!@£$%^&*()_+-=[]{}:\"|;'\<>?,./`~'“#"

in_file_name = input("Enter the name of a file to compress\n> ")

in_file = open(in_file_name, 'r')

print("Compressing... ", end="")

for line in in_file:

    words_in_line = line.split()

    for word in words_in_line:

        add_to_end = " "

        if word[0] in punctuation:
            compressed_output += word[0]
            word = word[1:]

        if len(word) > 0 and word[-1] in punctuation:
            add_to_end = word[-1] + " "
            word = word[:-1]

        if word not in words:
            words.append(word)

        compressed_output += str(words.index(word)) + add_to_end

    compressed_output += "\n"

    #print(".", end="")

in_file.close()

print("\nCompression finished.")

out_file = open(in_file_name + "_compressed.txt", 'w')
words_line = ""
for word in words:
    words_line += word + ","
words_line = words_line[:-1]
out_file.write(words_line + "\n" + compressed_output)
out_file.close()