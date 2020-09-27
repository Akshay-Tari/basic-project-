# write a program to lauch a calculator when countdown compete 

import time, subprocess

timeleft = 10                                     #the timer will start form 10

while timeleft > 0:                                 # it will compare the timeleft if it 
                                                    # greater than zero than only it will enter in while loop

    print(timeleft , end= '  ')                        # this will help to print the timeleft 
    time.sleep(1)                                       # it will give delay of 1 second between each count
    
    timeleft = timeleft-1                                 # it will subract the value by 1 till it reach zero.
    
    if timeleft==0:                                          # it will compare the timeleft till it zero
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')  # when it reach zero the selected program is launch 
        
    
    


