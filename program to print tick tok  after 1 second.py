import time                       # this will imort time module 
a=int(input('enter the value to print tick tock for n times ')) # ir will take input form user 
for i in range(a):                # loop
    print('Tick')                  
    time.sleep(1)                 # delay for 1 second 
    print('Tock')
    time.sleep(1)
print('time over ')               #comes outside the loop and print time over 
