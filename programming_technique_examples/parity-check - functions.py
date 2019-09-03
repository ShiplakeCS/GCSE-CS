def checkParity(message):
	sum_of_1s = 0
	
	for digit in message:
		if digit == " ":
			pass
		else:
			sum_of_1s += int(digit)
	
	
	if sum_of_1s % 2 == 0:
		return "Even"
	else:
		return "Odd"

message = input("Enter the message: ")
parity = input("Select intended parity (E for even or O for odd): ")

messageParity = checkParity(message)

if parity.lower() == "e" and messageParity == "Even":
	print("Message has been correctly received!")

elif parity.lower() == "o" and messageParity == "Odd":
	print("Message has been correctly received!")

else:
	print("Message has become corrupted.")
