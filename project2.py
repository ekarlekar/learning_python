import cmd

with open('words.txt') as f:
		all_words = f.read().split('/n')
s = '' 
for x in range(5):
	s+ = random.choice(all_words)
print(s)
revstring = ''
for i in s:
	revstring = i + revstring
print(revstring)
finalS = ''
for x in range(len(s)*2))
	finalS += s[x] + revstring[x]
print(finalS)