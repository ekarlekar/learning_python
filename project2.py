import cmd
import random

def main():
	with open('words.txt') as f:
			all_words = f.readlines()
	all_words = [x.strip('\n') for x in all_words]
	s = og_array(5,all_words)
	print(s)
	print(create_rev_array(s))
	print(create_smoosh_array(s))
	print(create_decoded_array(s))

def og_array(n, words):
	s = '' 
	for x in range(n): #og
		theword = random.choice(words)
		print(theword)
		s+= theword
	return s


def create_rev_array(s):
	revarr = [s[x] for x in range(len(s)-1, -1, -1)] #reverse
	return "".join(revarr)

def create_smoosh_array(s):
	revarr = create_rev_array(s)
	finalarr = "".join([s[x]+ revarr[x] for x in range(len(s))]) #smoosh
	return finalarr

def create_decoded_array(s):
	finarr = create_smoosh_array(s)
	decodedarr = [finarr[x] for x in range(0, len(finarr), 2)] #decode
	return "".join(decodedarr)

if __name__ == '__main__':
	main()