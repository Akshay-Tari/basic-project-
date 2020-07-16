import array    # it will import arrayAn array is a collection of items
                #stored at contiguous memory locations.
                #The idea is to store multiple items of the same type together. 

month = array.array('i',[0,31,28,31,30,31,30,31,30,31,30,31]) # the i represent integer size of 2 bytes and it store the days in month
count = 0

d = int(input("Enter the day:"))                # taking input from user 
months = int(input('Enter the months:'))
year = int(input('Enter a year: '))
days = int(input('Enter a number of days to find future days :'))

if year%4==0:                                # february        
    month[2]=28
while count < days:                         # it compare the count with days if it is smaller it will add 1 initial count is 0
    d = d+1
    count = count+1
    if d > month[months]:                   
        d=1
        months=months+1
    if months>12:
        months=1
        year = year+1
        if year%4==0:
            month[2]=29
        else:
            month[2]=28
print('future date = ',end='')        # it will print the output
print(d,end='-')
print(months,end='-')
print(year)

    
