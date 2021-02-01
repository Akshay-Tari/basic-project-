# creating simple Registration GUI in python
# This code is is taken form https://www.tutorialspoint.com/simple-registration-form-using-python-tkinter

from tkinter import *                        # to import tkinter module
from tkinter import ttk                      #The tkinter.ttk module provides access
                                            # to the Tk themed widget set, introduced in Tk 8.5




window = Tk()                                           # we use the Tk class
window.title("Welcome to Simple Registration")          # it give title to window
window.geometry('350x350')                              # it is use to set the size of the window
window.configure(background = "white")                   # it is use to set the background

a = Label(window, text = "First Name ").grid(row =0, column = 0)
b = Label(window, text = "Second Name").grid(row = 1, column = 0)
c = Label(window, text = "Email Id").grid(row = 2, column = 0)
d = Label(window, text ="Contact Number").grid(row = 3,column =0)

a1 = Entry(window).grid(row = 0, column = 1)            #The Entry widget is used to accept single-line text strings from a user.
                                                        #If you want to display multiple lines of text that can be edited, then you should use the Text widget.
                                                        # If you want to display one or more lines of text that cannot be modified by the user,
                                                        # then you should use the Label widget.
b1 = Entry(window).grid(row = 1, column = 1)
C1 = Entry(window).grid(row = 2, column = 1)
d1 = Entry(window).grid(row = 3, column = 1)

def clicked():                           # the function is created to  Button Click Event
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)                  # label

button = ttk.Button(window, text = "sumbit" ).grid( row = 4, column =0)     # this use to make a button





window.mainloop()                                           # Window.mainloop(), this function calls the endless loop of the window,
                                                            # so will remain open till the user closes it.
