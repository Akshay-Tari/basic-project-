u=int(input('press 1 if you want the percentage\n''press 2 If you want to find the new price increased by X percentage : '))
    
                                                                     # it give the option for user if they want  press 1 or press 2 then they will direct to the chosen option  
if u>2:
    print('Enter only given option ')                                   # it will give  message to enter given option if it is more than 2
                
if u==1:                                                            # it take value form user 
    a=int(input('\n Enter the percent : '))                         
    b=int(input('Enter the total percent of :'))

    percentage=((a/b)*100)


    print(int(percentage),'%')                                        # print the percentage value 



if u==2:
    
    m=float(input('\n Enter the value of 1 item : '))                   # it will take convert the value that will be in float 
    n=int(input('Enter the value that increased by X percentage : '))

    p=((m)*(n/100))                                                     #formula to calculate the value 

    q=(m+p)

    print('The new price is :',q)                                    # print the value 










