"""
Strulo 03 - Decode/Encode
"""

import string

while True:
	alphabet = string.ascii_lowercase
	while True:
		try:
			decode = int(input('Do you want to decode (1) or encode (2)?\n>> '))
			break
		except ValueError:
			print('Sorry, I didn\'t recoginse that - care to try again?')
			
	keyword = input('Enter a keyword\n>> ').lower()
	string_to_decode = input('Enter a string to decode/encode\n>> ').lower()
	key = ''.join([l for l in alphabet if l not in keyword])
	key = keyword + key 
	output = ''
	for l in string_to_decode:
		if l in alphabet:
			if decode == 1:
				i = key.index(l)
				output += alphabet[i]
			else:
				i = alphabet.index(l)
				output += key[i]
	print(output)
	