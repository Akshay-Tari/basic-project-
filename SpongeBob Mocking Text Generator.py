# this code is taken form  https://www.geeksforgeeks.org/python-spongebob-mocking-text-generator-gui-using-tkinter/

# import all function from the tkinter

from tkinter import *

import random  # import library


def clearall():
    text1_field.delete(1.0, END)  # whole content of text area is deleted
    text2_field.delete(1.0, END)


def generate():  # function that generate mocking text
    input_text = text1_field.get("1.0", "end")[:-1]  # get input form text box
    output_text = ""  # variable declaration for the output text

    for char in input_text:  # check the cases for every individual character
        if char.isalpha():  # check if the character is an alphabet
            if random.random() > 0.5:
                output_text += char.upper()  # convert to upper case

            else:
                output_text += char.lower()


    text2_field.insert('end -1 chars', output_text)  # if character is not and alphabet add it as it is


# driver code

if __name__ == "__main__":

    root = Tk()  # create a GUI window
    root.configure(background='gray')  # set the background colour of GUI window
    root.geometry("400x350")  # set the width*height
    root.title("Generator")

    headlabel1 = Label(root, text = 'welcome to spongeBob mocking text generator', fg = 'black', bg = "yellow")

    label1 = Label(root, text = "Input text", fg = 'black', bg = 'white')
    label2 = Label(root, text = "Output text", fg = 'black', bg = 'white')

    headlabel1.grid(row=0, column=1)  # grid method is use for placing in table like structure

    label1.grid(row=1, column=0, padx=10)  # padx keyword use to set paading along X axis
    label2.grid(row=3, column=0, padx=10)

    text1_field = Text(root, height=5, width=25, font="lucida 13")
    text2_field = Text(root, height=5, width=25, font="lucida 13")

    text1_field.grid(row=1, column=1, padx=10, pady=10)
    text2_field.grid(row=3, column=1, padx=10, pady=10)

    button1 = Button(root, text="Generate", bg="white", fg="black", command=generate)

    button1.grid(row=2, column=1)

    button2 = Button(root, text="Clear", bg="white", fg="black", command = clearall)
    button2.grid(row=4, column=1)

    root.mainloop()
