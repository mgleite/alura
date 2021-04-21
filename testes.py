numbers = [1, 467, 4523879, 24724, 238947823759832]
guess = 0

while guess not in numbers:
	print("type q to quit")
	guess = input("Guess a number")
	if guess == "q":
		print("The end")
		break
	else:
		guess = int(guess)
		if guess not in numbers:
			print("You chose poorly")
		else:
			print("You win!")
