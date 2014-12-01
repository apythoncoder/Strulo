import os
from collections import defaultdict

def gen_fake(word):
	fakes = []
	for i in range(len(word)):
		fakes.append(word[:i]+'!'+word[i+1:])
	return fakes
	
def gen_ladder(start, end):
	ladders = [[start]] # To be filled with different ways of getting to the end
	while True:
		new_ladders = []
		for ladder in ladders:
			if ladder[-1] == end: # If last rung of ladder is the end
				return ladder
			else:
				for fake in gen_fake(ladder[-1]):
					for word in connections[fake]:
						if word != ladder[-1]: # Stops duplicates
							new_ladders.append(ladder+[word])
		ladders = new_ladders

# Sets path as root of script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
with open('four_letters.txt') as f:
	word_list = [word.strip() for word in f]

connections = defaultdict(set)
for word in word_list:
	for fake in gen_fake(word):
		connections[fake].add(word)

start = input('Enter a start word\n>> ')
end = input('Enter an end word\n>> ')

ladder = gen_ladder(start, end)
print('The ladder is: {0}'.format('\n'.join(w for w in ladder)))