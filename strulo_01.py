"""
Strulo 01 - Puzzle Questions
"""

import random

words = ['elephant', 'iguana', 'ostrich', 'impala', 'snake', 'koala']
while True:
	answer = random.choice(words)
	print('The word to guess is {0}'.format(''.join([l for l in answer if l not in 'aeiou'])))
	while True:
		guess = input('Take a guess!\n>> ').lower()
		if guess == answer:
			print('Well Done!')
			break
		else:
			print('Sorry! Try again.')
	