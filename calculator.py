#importing libraries
from tkinter import *
import tkinter.font as font

#creating window
window = Tk()
window.title("Calculator")
window.geometry("510x530")

#frames
input = Frame(window,bd = 0, height=50, width = 360)
input.pack(side=TOP)

text=StringVar()
input_text = Entry(input, font=('Courier New', 30,),width=50, textvariable= text,bg='white', justify=RIGHT)
input_text.grid(row=0, column=0)
input_text.pack(ipady=30)

buttons = Frame(window, width= 360, height=375, bg="white")
buttons.pack()

#adding buttons
clear_button = Button(buttons,width = 10, height = 3, text = "clear",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black", bg = "#F5F5F5",bd = 0, command = lambda: clear()).grid(row = 0, column = 0, padx = 1, pady = 1)
 
backspace_button = Button(buttons,width = 10, height = 3, text = "<-",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black", bg = "#F5F5F5",bd = 0, command = lambda: backspace()).grid(row = 0, column = 1, padx = 1, pady = 1)

division_button = Button(buttons,width=10,height = 3, text = "/",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click("/")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
seven_button = Button(buttons,width=10,height = 3, text = "7",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight_button = Button(buttons,width=10,height = 3, text = "8",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine_button = Button(buttons,width=10,height = 3, text = "9",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiplication_button = Button(buttons, width=10, height=3, text="*", font=('courier new',15, 'bold'), cursor="hand2",fg="black", bg="#F5F5F5", bd=0, command=lambda: click("*")).grid(row=2, column=3, padx=1, pady=1)
 
four_button = Button(buttons,width=10,height = 3, text = "4",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five_button = Button(buttons,width=10,height = 3, text = "5",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six_button = Button(buttons,width=10,height = 3, text = "6",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
addition_button = Button(buttons,width=10,height = 3, text = "+",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click("+")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
one_button = Button(buttons,width=10,height = 3, text = "1",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two_button = Button(buttons,width=10,height = 3, text = "2",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three_button = Button(buttons,width=10,height = 3, text = "3",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
subtraction_button = Button(buttons,width=10,height = 3, text = "-",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click("-")).grid(row = 0, column = 2, padx = 1, pady = 1)
 
zero_button = Button(buttons,width=10,height = 3, text = "0",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
 
dot_button = Button(buttons,width=10,height = 3, text = ".",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)

comma_button = Button(buttons,width=10,height = 3, text = ",",font=('courier new',15, 'bold'),cursor = "hand2", fg = "black",bg = "#F5F5F5", bd = 0, command = lambda: click(",")).grid(row = 4, column = 2, padx = 1, pady = 1)

equals_button = Button(buttons, width=10, height=7, text="=", font=('courier new',15, 'bold'), cursor="hand2", fg="black",bg="#F5F5F5", bd=0, command=lambda: equal()).grid(row=3, rowspan=2, column=3, padx=1, pady=1)

#funtions
def clear():
    global equation
    equation = ""
    text.set("")
    
def backspace():
    global equation
    equation = equation[ :-1]
    text.set(equation)

def equal():
    global equation
    result = str(eval(equation))
    text.set(result)
    equation = ""

def click(action):
    global equation
    equation = equation + str(action)
    text.set(equation)
    
equation = ""

#command to keep the window activate
window.mainloop()
