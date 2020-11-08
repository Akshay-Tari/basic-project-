# this code is taken form  https://code.sololearn.com/cspLUgHPeAR6/#py


import random           # the random module is intall 

First_Name =("Super", "Real", "Great", "TOP", "Abc", "Brave", "one",             # the random First name are stored 
             "Cool", "great", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual",
             "world", "thank you ", " joe ", "ABCD", "smart", "python")

Second_Name=("coder ","progammer ","developer","data scientis ","random","number ","java ") # the random Second name are stored 

First = random.choice(First_Name)         # function to choice random form First_Name and second_Name
Second = random.choice(Second_Name)

Full_name = (First + " " + Second)      #  It combine the First and Second name and stored in Full_name 

print( 'the random name is : '+ Full_name) # It  will print the random full name as a output
