words = []
output = ""
punctuation = "!@£$%^&*()_+-=[]{}:\"|;'\<>?,./`~'“#"

in_file_name = input("Enter the name of a file to decompress\n> ")

in_file = open(in_file_name, 'r')

words = in_file.readline().strip().split(',')

for line in in_file:

    indicies = line.split(" ")

    for index in indicies:

        add_to_end = ""

        if index != "\n":

            if index[0] in punctuation:

                output += index[0]
                index = index[1:]

            if len(index) > 0 and index[-1] in punctuation:

                add_to_end += index[-1]
                index = index[:-1]

            add_to_end += " "

            output += words[int(index)] + add_to_end

    output += "\n"

in_file.close()

out_file = open(in_file_name + "_decompressed.txt", 'w')

out_file.write(output)

out_file.close()
