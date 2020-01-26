from time import sleep
from random import randint

hungry = False
nappyFull = False
tired = False

def action():
	global hungry, tired, nappyFull
	print("What would you like to do?\n1-Feed the baby\n2-Change the baby's nappy\n3-Give the baby a nap")
	choice = input("Enter a number >")
	print("-------------------------")
	if choice == "1":
		print("Feeding the baby...")
		hungry = False
	elif choice == "2":
		print("Chaning the nappy. Urgh...")
		nappyFull = False
	elif choice == "3":
		print("Putting baby to sleep...")
		tired = False
	else:
		print("Sorry, that's not a valid option. Try agian.\n")
		action()
	print("-------------------------")
	print("Checking again in 3 seconds...")
	sleep(3)
	checkBaby()

def checkBaby():
	global hungry, nappyFull, tired
	if hungry==True or tired==True or nappyFull==True:
		print("*" * 30)
		print("WAAAAAAAA!!!!! They baby is crying!!")
		print("*" * 30)
		action()
	else:
		print("Baby seems happy. Checking again in 5 seconds...")
		sleep(5)
		randomProblem()
		checkBaby()

def randomProblem():
	global hungry, tired, nappyFull
	i = randint(1,3)
	if i == 1:
		hungry = True
	elif i == 2:
		nappyFull = True
	elif i == 3:
		tired = True

randomProblem()
checkBaby()
