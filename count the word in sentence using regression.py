# this code is taken form geeks for geeks.
# the python program to count the words in a sentence 
# using regex  
# we have use split method to count the word in sentence but know we will use regex method 


import re  # this will import regex module

test_string = input (str('Enter the sentence to count the word:'))

print('the original string is :'+ str(test_string) )


# using regex
# to count words in string
# below is the sentence uses the regex 

length = len(re.findall(r'\w+', test_string))

# \w Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].


print('the number of words in string are :' + str(length))

