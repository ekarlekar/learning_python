import sys
import time 
import cmd

with open('words.txt') as f: 
	all_words = f.read().split('\n')

if(len(sys.argv) < 2): 
	num_to_print = int(input("please input a number: "))
else: 
	num_to_print = int(sys.argv[1])

if(num_to_print > 25): 
	print("Yo thats too big, pick something smaller")
else: 
	for x in range(num_to_print): 
		print(all_words[x])

	lst = all_words[:num_to_print]
	for x in range(len(lst)): 
		print("------- " + lst[x])


