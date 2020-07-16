import time  # this will import the time module


def timeconvert(sec): # this will create a function 
    mins = sec // 60 
    sec  = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("time laspsed ={0}:{1}:{2}". format(int(hours),int(mins),round(sec)))

input("press Enter to start ")
starttime = time.time()

input('press Enter to stop ')
endtime = time.time()

timelapsed = endtime - starttime
timeconvert(timelapsed)




