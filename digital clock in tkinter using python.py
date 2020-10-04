# this code is taken form coding with Evan youtube channel 




from tkinter import *  # '*' It just means that you import all(methods, variables,...) 
from time import strftime  # The strftime() method can be used to create formatted strings.


root = Tk()         # To initialize tkinter
root.title('clock') # it give the title 


def time():                            # function  
    string = strftime('%H:%M:%S:%p')   # string format in hour minute second 
    label.config(text = string)
    label.after(1000,time)



label =Label(root, font=("ds-digital",80),bg = "white", foreground = "black")  # specific format to display the time include background text etc
label.pack(anchor = 'center')    # it will place in the center 
time()                           # The time() function returns the number of seconds passed since epoch
  
mainloop()                      # mainloop() tells Python to run the Tkinter in event loop
