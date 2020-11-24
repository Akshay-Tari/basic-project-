# This is the python program which help us to calculate the simple interest and compound  interest


a = int(input('press 1 if you want to calculate the Simple interest \n''press 2 If you want to find the compound interest  : '))  # it will take input form user for the option 1 or 2




# Simple Interest is calculated on the Principal Amount for the entire tenure
# It is beneficial when you have borrowed money
#Simple Interest=P×r×t where: P=Principal amount ,r=Annual interest rate , t =Term of loan in years




if a==1:                                                       # if condition use to provide the option for user if user press 1 it will calculate the simple interest

    print('\n''To calculate the simple interest''\n')

    P = int(input('Enter the principle amount: '))                   # taking user input 
    r = float(input('Enter the annual interest rate: '))
    t = int(input('Enter the term of loan in years: '))


    Simple_interest = P*r*t                                      # simple interest formula 
    print('\n''simple interest is : ',Simple_interest)






# Compounded Interest is calculated on Principal + Accumulated Interest periodically.
# It is beneficial when you have deposited or invested your money.
# Compound Interest=P×(1+r)t-P  P=Principal amount, r=Annual interest rate ,n= Number of years.


if a==2:

    print('\n''To calculate the compound interest''\n')

    P = int(input('Enter the principle amount: '))
    r = float(input('Enter the annual interest rate: '))
    t = int(input('Enter the number of  years: '))


    Compound_Interest = P*(pow((1+r/100),t))                                # compund  interest formula 
    print('\n''the compound interest is :',Compound_Interest)




if a>2:
    print('Enter only given option ')  


