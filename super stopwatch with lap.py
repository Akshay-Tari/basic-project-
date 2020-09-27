

# The below code is form book Automate the Boring Stuff with Python by Al Sweigart



import time

print('press Enter to begin. Afterwards, press enter to "click" the stopwatch and press ctrl-c to quite.')
input()
print('started.')
startTime = time.time()   #get the first lap's start time
lastTime = startTime
lapNum = 1

# start tracking the lap times

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime,2)
        print('lap #%s: %s (%s)' % (lapNum, totalTime, lapTime),end = '')
        lapNum += 1
        lastTime = time.time()   # reset the last lap time
        
except KeyboardInterrupt:
    # handle the ctrl-c exception to keep it error message form displayed

    print ('\nDone.')







        

