from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

#Mileage Entry
input = Entry(width=7)
input.insert(END, string="0")
input.grid(row=0, column=1)

#Km Value
km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1, padx=5, pady=2)

#Km Label
km_label = Label(text="Km")
km_label.grid(row=1, column=2, padx=5, pady=2)

#Calc Button

def calculate ():
    miles_value = round(float(input.get()), 2)
    km_value = 1.6*miles_value
    km_value_label.config(text=f"{km_value}")

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1, padx=5, pady=2)

#Output Label

output_label = Label

#Is Equal To Label
equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0, padx=5, pady=2)

#Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2, padx=5, pady=2)


window.mainloop()