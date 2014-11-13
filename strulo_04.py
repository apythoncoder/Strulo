"""
Strulo 04 - Cracking a Cipher
"""

import collections
import string 

while True:
	cipher = input('Enter cipher to crack\n>> ')
	cipher = ''.join([l for l in cipher if l in string.ascii_lowercase])
	letters = collections.Counter(cipher)
	print(letters)
	
