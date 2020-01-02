import cmd

def main():
	with open('words.txt') as f:
		all_words = f.read().split('\n')
		list_to_print = find_word(input("please type a word:"), all_words)
		print_list(list_to_print)

def find_word(find, findin):
	listcopy = []
	if(find == None):
		return listcopy
	for x in range(len(findin)):
		if (find in findin[x]):
			listcopy.append(findin[x])
	return listcopy

def print_list(l):
	for x in range(len(l)):
		print (l[x])


if __name__ == '__main__':
	main()