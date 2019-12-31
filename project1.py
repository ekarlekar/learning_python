import cmd

with open('words.txt') as f:
	all_words = f.read().split('\n')

s = input("please type a word:")

for x in range(len(all_words)):
	if (s in all_words[x]):
		print(all_words[x])