from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random

alert = None

# search

def searchPass():
    global alert

    if alert != None:
        alert.destroy()
        alert = None
    
    try:
        with open("data.json", "r") as file:
            data_search = json.load(file)
            date_after_search = data_search[web.get()]
            email.delete(0, END)
            email.insert(0, date_after_search["Email/Username"])
            password.delete(0, END)
            password.insert(0, date_after_search["password"])
            pyperclip.copy(date_after_search["password"])
    
    except FileNotFoundError:
        alert = Label(text="There are no passwords saved!",fg="Red")
        alert.grid(row=5, column=1)
    
    except KeyError:
        alert = Label(text="Website Not Found!",fg="Red")
        alert.grid(row=5, column=1)

# pass gen

def genPass():

    # the pass with be a random collection of some items from the below 3 lists
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    gg = "".join(password_list)
    password.delete(0, END)
    password.insert(0, gg)

    #copying pass
    pyperclip.copy(gg)

window = Tk()
window.title("Password Manager")
# window.minsize(220,220)
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
# entries
web = Entry(width=18)
web.focus()
web.grid(row=1, column=1)

email = Entry(width=35)
email.insert(0, "test@test.test")
email.grid(row=2, column=1, columnspan=2)

password = Entry(width=18)
password.grid(row=3, column=1)
