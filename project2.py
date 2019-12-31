import cmd
import random

with open('words.txt') as f:
		all_words = f.readlines()

all_words = [x.strip('\n') for x in all_words]

s = '' 
for x in range(5): #og
	theword = random.choice(all_words)
	print(theword)
	s+= theword
print(s)

revarr = [s[x] for x in range(len(s)-1, -1, -1)] #reverse
print("".join(revarr))

finalarr = "".join([s[x]+revarr[x] for x in range(len(s))]) #smoosh
print(finalarr)

decodedarr = [finalarr[x] for x in range(0, len(finalarr), 2)] #decode
print("".join(decodedarr))