# Import Statements
import random
import string
import os
import time

#Sets path as root of script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Makes a list of words from the dictionary file
with open('dictionary.txt', 'r') as thefile:
	all_words = thefile.read().split()

# These strings are stored in a variable to avoid clogging up code later on.
# The {x}s in the strings will be replaced later on, using .format()
main_text = """\
The word to guess is: {0}.
Letters guessed are: {1}.
Wrong attempts left: {2}
"""
end_game = """\
You\'ve lost the game!
The word to guess was {0}
Better luck next time"""

# The While loop allows the game to repeat
while True:
	# Picks a random item from the list of words
	answer = random.choice(all_words)
	
	# Uncomment the next line to show the answer for debugging)
	#print(answer)
	attempts_left = 10 # Change this to vary the difficult of the game
	formatted_word = ('_ ' * len(answer)).split() # Makes a list to check the guess against
	guessed_letters = [] # Will be filled with the used letters
	
	# The main game bit
	while True:
		os.system('clear') 	# Clears the screen
		# Formats the main blurb. The join function turns the lists into a string
		print(main_text.format((' '.join(l for l in formatted_word)),(', '.join(l for l in guessed_letters)),attempts_left))
		
		# While loop allows user to indefinitely enter a guess until it's in the alphabet 
		while True:
			guess = input('Enter a letter to guess\n>> ').lower() # Changes it into lowercase
			if guess in string.ascii_lowercase:
				break # Exits loop
			else:
				print('Please try again')
		
		# Checks for empty string
		if not guess:
			pass
			
		elif guess in answer:
			# Gets all instances of the guess in the answer
			occurences = [i for i in range(len(answer)) if answer.startswith(guess, i)]
			for letter in occurences:
				formatted_word[letter] = guess
		
		# Stops duplicates in guessed_letters
		elif not guess in guessed_letters:
			guessed_letters.append(guess) 
			attempts_left -= 1
		
		else:
			print('You\'ve already guessed "{0}"'.format(guess))
			time.sleep(1) # Allows user time to read
			
			
		if attempts_left is 0:
			print(end_game.format(answer))
			time.sleep(2)
			break
		elif not '_' in formatted_word:
			print('You\'ve won the game!')
			time.sleep(2)
			break

