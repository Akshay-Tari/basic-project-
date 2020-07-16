n = int(input('how many terms?'))               # take input from user to nth term

n1, n2 = 0,1                                    # start from counting 0
count = 0

if n <= 0:
    print('please enter positive integer')
elif n == 1:                                    # it will compare if user enter n value =1 then it will print the value of n1 
    print('Fibonacci sequence upto',n,':')
    print(n1)
else:
    print('Fibonacci sequence',)
    while count < n:                             # it will count the  step if it is more than  n than it will stop 
        print(n1, end = ',')                    # this line help me to print number in same line till end with symbol ,
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1                               # Fibonacci series are made by adding adding first digit + second digit = third digit
                                                 # then again second digit + Third digit = fouth digit the process repeat again and again
                                                 # till count value  is less than n value  
       


