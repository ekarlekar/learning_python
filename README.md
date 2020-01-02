# learning_python

## first part  

- term to search for (letter, phrase, etc) in command line
- search list of words for that
- print what it matches 
**luh mao** *this ugly as heck*

to run project1:  
```
$ python3 project1.py
``` 

## second part  

- select five words at random  
- print them
- concatenate  
	- forward
	- backward
	- forwardsbackwards (smushed)
	- suck  
	
to run project2:  
```
$ python3 project2.py
``` 
## testing 

to run tests:  
```
$ pytest 
``` 
### test on project1:

*file name:* test_project1.py  

**decscription**   
I ran one test which tested the method find_words, with cases including:
- where the list has words that contain the word  
- where the list has some elements that contain the word and some that do not
- where the list does not contain the word
- spaces for both the list and the word
- blanks for both the list and the word

### test on project2:
*file name:* test_project2.py

**decscription**   
	I ran four test which tested the methods *create_rev_array*, *create_smoosh_array*, *create_decoded_array*, and a combination of all 3. 

the test that tested all 3 decoded a smooshed array made from a certain list and verified that it equaled itself in the end


 
