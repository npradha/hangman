import random

print("Welcome to Hangman!")
while True:
	colors = ['red', 'orange', 'yellow','green','blue','purple','white','black']
	animals = ['dog', 'cat','fish','lion','giraffe','tiger']
	states = ['texas', 'arkansas','california', 'new jersey', 'ohio','illinois','indiana']
	allLists = [colors, animals, states]
	
	print("Choose a category: \n")
	print("1: Colors")
	print("2: Animals")
	print("3: States")
	print("4: Random")
	
	choice = input()
	
	if choice == 1:
		word = random.choice(colors)
	elif choice == 2:
		word = random.choice(animals)
	elif choice ==  3:
		word = random.choice(states)
	elif choice == 4:
		word = random.choice(random.choice(allLists))	
	else:
		print("Invalid Input. Try Again!\n")
		continue;
	print("Your word has " + str(len(word)) + " letters")
	guesses = len(word) + 3
	print("You have " + str(guesses) + " guesses to start out with")
	wordGuess = ["-"] * len(word)
	print(wordGuess)

	while guesses!=0 and  wordGuess!=word:
		print("Make a guess\n")
		letter = raw_input()
		letter = letter.lower()
		if letter in word:
			print("The letter " + letter + " is in the word!")
			guesses = guesses - 1
		else:
			print("Sorry! The letter " + letter + " is not in the word")
			guesses = guesses - 1
		print("You have " + str(guesses) + " guesses left")
			
	if guesses == 0:
		print("Sorry you ran out of guesses\n")
		print("The word was " + word)
	else:
		print("Congratulations! You guesses the word with " + str(guesses) + " left!\n")

	print("Do you want to play again? (y/n)")
	answer = raw_input()
	if answer == 'y':
		continue;
	else:
		break;
print("Thanks for playing!!")
	

