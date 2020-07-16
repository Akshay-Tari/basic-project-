import random  # we use this modules when we want to pick random values form list
import array   # Array is a container which can hold a fix number of item and these item should be of same type array divide into an element and Index
               #element is item store in an array and index which is used to identity the element


Maxlenght=12  # the maximum lenght of password  is 12 so it depend on the requirement of user we can changed according to the requirement

# the below  are character that we will use to generate the random password the concatenate with random values 

DIGITS    =  ['0','1','2','3','4','5','6','7','8','9',]
Lowercase =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Uppercase =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Symbols   =  ['@','#','$','%','^','&','*','(',')','+','=','|']

Passwordlist=DIGITS+Lowercase+Uppercase+Symbols                 # the password is made of concetation of values



randdigit = random.choice(DIGITS)                               # randomly select at least one character from each set above
randupper = random.choice(Uppercase)
randlower = random.choice(Lowercase)
randsymbol = random.choice(Symbols)

        
Temppass = randdigit + randupper + randlower + randsymbol       #sice we only have 4 character in password list but we required 12


for a in range (3):

    for X in range(Maxlenght-4):                                #convert temporay password into array and shuffle to prevent it form similar pattern 
        Temppass = Temppass + random.choice(Passwordlist)
        Password = ''
        for X in Temppass:
                    Password = Password + X
print(Password)
 

    

