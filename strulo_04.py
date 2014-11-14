"""
Strulo 04 - Cracking a Cipher
"""

import collections
import string 
path_to_english_file = '/Users/jacob/Desktop/Python/Strulo/english.txt'
while True:
	alphabet = string.ascii_lowercase
	# a)
	plain_file = ''
	with open(path_to_english_file) as file:
		for word in file:  
			for c in word:
				c = c.lower() 
				if c in alphabet:
					plain_file += c
	letters = collections.Counter(plain_file)
	print(letters)
	# print(letters)
	
	# b)
	cipher = input('Enter cipher to crack\n>> ')
	key = collections.Counter(cipher)
	letters = ''.join(l for l in list(letters.keys()))

	keyword = ''.join(l for l in list(key.keys()))
	
	key = ''.join([l for l in alphabet if l not in keyword])
	key = keyword + key 
	
	# print(key)
	output = ''
	for l in cipher:
		if l in alphabet:
			i = letters.index(l)
			output += key[i]
	print(output)
