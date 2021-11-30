#Level 1 
import random
number = random.randint(1,20)
number2 = random.randint(1,3)
# print(number)
print("\nWelcome to the first level of this number guessing game!")
print('\nFor this next part you will be asked to enter a number between 0 and 20 to try to guess a randomly generated number.')
print("\n CREDITS: HEMIT AND JASKEERAT")
#print(number)

#to show how many hints youve got
print("\n\tYou've only got",
	number2,
	"hints\n")

count = 0

while count < number2:
	count += 1

	guess = int(input('\nPlease enter a number between 0 and 20:'))

	if number == guess:
		print("\nCongratulations you did it in ",
			count, " try/tries")
		break
	elif number > guess:
		print("\nYou guessed too small!")
	elif number < guess:
		print("\nYou Guessed too high!")

if count >= number2 :
	print("\n Better luck next time! The number is %d" % number)



# repeated but everyhing put into an if statement
# level 2
if number == guess:
	print("\nWelcome to level 2 didn't think you would make it this far!")
	number = random.randint(1,30)
	number2 = random.randint(1,3)
	# print(number)
	print('\nFor this next part you will be asked to enter a number between 0 and 30 to try to guess a randomly generated number.')
	# print(number)
	print("\n\tYou've only got",
		number2,
		" hints\n")

	count = 0

	while count < number2:
		count += 1

		guess = int(input('\nPlease enter a number between 0 and 30:'))

		if number == guess:
			print("\nCongratulations you did it in ",
				count, " try/tries")
			break
		elif number > guess:
			print("\nYou guessed too small!")

		elif number < guess:
			print("\nYou Guessed too high!")
           
	if count >= number2 :
		print("\n Better luck next time! The number is %d" % number)

    




#again the same thing but way more harder since this is the finale
# level 3
if number == guess:
	print("\nWelcome to level 3 the last and final level! I will be sure to make this level extra hard.")
	number = random.randint(1,40)
	number2 = random.randint(1,2)
	# print(number)
	print('\nFor this next part you will be asked to enter a number between 0 and 40 to try to guess a randomly generated number.')
	# print(number)
	print("\n\tYou've only got",
		number2,
		" hints\n")

	count = 0

	while count < number2:
		count += 1

		guess = int(input('\nPlease enter a number between 0 and 40:'))

		if number == guess:
			print("\nCongratulations you did it in ",
				count, " try/tries You finished all levels!")
      
			break
		elif number > guess:
			print("\nYou guessed too small!")
		elif number < guess:
			print("\nYou Guessed too high!")

	if count >= number2 :
		print("\n Better luck next time! The number is %d" % number)
