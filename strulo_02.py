"""
Strulo 02 - Substitution Ciphers
"""

import string

while True:
	alphabet = string.ascii_lowercase
	keyword = input('Enter a keyword\n>> ').lower()
	string_to_decode = input('Enter a string to decode\n>> ').lower()
	key = ''.join([l for l in alphabet if l not in keyword])
	key = keyword + key
	output = ''
	print(key)
	for l in string_to_decode:
		i = alphabet.index(l)
		output += key[i]
	print(output)
	