# this code is taken form geeks for geeks.
# the python program to count the words in a sentence 
# using split method


#  input is taken form user and convert into string and store in test_string

test_string = input(str('enter the string to count the words in sentence :'))

# It display the original sentence

print('the orginal string is :' + test_string )

# there is difference between the split and len in split in only words form sentence
# and in len in also count the blank spaces in the sentence
# below you can find the difference between split and len

# it only calculate the wrods not included space in sentence 

length = len(test_string.split())
print('using split function :',length)

# it print the len form the sentence including spaces 
print('using len function ',len(test_string))
