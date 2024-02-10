from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No User Data", message="No user info exists")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="User Info", message=f'Email: {email} \nPassword: {password}')
        else:
            messagebox.showinfo(title="No User Data For Website", message="No user info exists for that website")





# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letter_list = [choice(letters) for _ in range(nr_letters)]
    symbol_list = [choice(numbers) for _ in range(nr_symbols)]
    number_list = [choice(symbols) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)

    pw_entry.delete(0, END)
    pw_entry.insert(END, password)

    pyperclip.copy(password)
    messagebox.showinfo(title="Password Copied", message="Password copied to clipboard.")



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Empty Input", message="Fields must be filled.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
#
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

#Buttons
gen_pw_button = Button(text="Generate Password", command=generate_pw)
gen_pw_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

#Entries
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END, "email")
email_entry.grid(row=2, column=1, columnspan=2)

pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)


window.mainloop()