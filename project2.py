import cmd
import random

with open('words.txt', 'r') as f:
		all_words = f.readLines()

print(all_words)

all_words = [x.strip('\n') for x in all_words]

s = '' 
for x in range(5):
	print(random.choice(all_words))

















#print(s)

# revstring = ''

# for i in s:
# 	revstring = i + revstring
# print(revstring)

# finalS = ''

# for x in range(len(s)*2):
# 	finalS += s[x] + revstring[x]
# print(finalS)