from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

#Button

def button_Clicked():
    input_str = input.get()
    my_label.config(text=input_str)

my_button = Button(text="Click Me", command=button_Clicked)
my_button.pack()

#Entry

input = Entry()
input.pack()



window.mainloop()

