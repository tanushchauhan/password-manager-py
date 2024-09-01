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

# save pass

def saveThePass():
    global alert
    if alert != None:
        alert.destroy()
        alert = None
    web_data = web.get()
    email_data = email.get()
    password_data = password.get()
    if web_data != "" and password_data != "" and email_data != "":

        data_abhi = {
            web_data: {
            "Email/Username": email_data,
            "password": password_data
            }
        }
        try:
            with open("data.json", "r") as file:
                data_his = json.load(file)
                try:
                    x = data_his[web_data]
                    z = messagebox.askokcancel("Overwrite?", "There is already an entry with that same website name, do you want to overwrite that?")
                    if z:
                        data_his.update(data_abhi)
                        with open("data.json", "w") as file:
                            json.dump(data_his, file, indent=4)
                        web.delete(0,END)
                        password.delete(0,END)
                except KeyError:
                    data_his.update(data_abhi)
                    with open("data.json", "w") as file:
                        json.dump(data_his, file, indent=4)
                    web.delete(0,END)
                    password.delete(0,END)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_abhi, file, indent=4)


    else:
        messagebox.showinfo(title="ERROR", message="Plese make sure you fill every field!")

window = Tk()
window.title("Password Manager")
# window.minsize(220,220)
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#labels
website = Label(text="Website:",)
website.grid(row=1, column=0)

Email_user = Label(text="Email/Username:",)
Email_user.grid(row=2, column=0)

Pass = Label(text="Password:",)
Pass.grid(row=3, column=0)

# entries
web = Entry(width=18)
web.focus()
web.grid(row=1, column=1)

email = Entry(width=35)

emailToPut = ""

try:
    with open("config.txt", "r+") as file:
        l = file.readline()
        emailToPut = l
except FileNotFoundError:
    emailToPut = "test@test.test"


email.insert(0, emailToPut)
email.grid(row=2, column=1, columnspan=2)

password = Entry(width=18)
password.grid(row=3, column=1)

#buttons

btn_gen = Button(text="Generate Password", command=genPass)
btn_gen.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=saveThePass)
btn_add.grid(row=4, column=1, columnspan=2)

btn_gen = Button(text="Search", command=searchPass, width=13)
btn_gen.grid(row=1, column=2)

window.mainloop()