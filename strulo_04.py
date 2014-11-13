"""
Strulo 04 - Cracking a Cipher
"""

import collections
import string 

while True:
	alphabet = string.ascii_lowercase
	# a)
	cipher = input('Enter cipher to crack\n>> ')
	cipher = ''.join([l for l in cipher if l in alphabet])
	letters = collections.Counter(cipher)
	# print(letters)
	
	# b)
	keyword = ''.join(l for l in list(letters.keys()))
	key = ''.join([l for l in alphabet if l not in keyword])
	key = keyword + key 
	# print(key)
	output = ''
	for l in cipher:
		i = alphabet.index(l)
		output += key[i]
	print(output)
