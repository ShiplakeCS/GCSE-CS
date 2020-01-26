# How many DVDs?

data_size = float(input("How much data do you need to backup (in GB)? "))

quotient = data_size // 4.7

remainder = data_size % 4.7

total_required = int(quotient)

if remainder != 0:

    total_required = total_required + 1

print("You will need " + str(total_required) + " DVDs to back up " + str(data_size) + "GB of data.")