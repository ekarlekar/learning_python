import cmd

def main():
    with open('words.txt') as f:
	all_words = f.read().split('\n')
	find_word(input("please type a word:"), all_words)

def find_word(find, findin):
for x in range(len(findin)):
	if (find in findin[x]):
		print(findin[x])