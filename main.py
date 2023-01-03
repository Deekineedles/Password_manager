from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def search():
    w = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.askokcancel(title=w, message=f"Email: {data[w]['email']}\nPassword: {data[w]['password']}")
    except KeyError:
        messagebox.askretrycancel(title="Error", message=f"{w} does not exist")
    except FileNotFoundError:
        messagebox.askokcancel(title="Data file not found", message="Please add data before attempting to search")

def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter_list = [random.choice(letters) for _ in range(nr_letters)]

    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letter_list + number_list + symbol_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    w = website_entry.get()
    e = email_entry.get()
    p = password_entry.get()
    data_complete = {
        w: {
            "email": e,
            "password": p,
        }
    }

    if len(e) < 1 or len(p) < 1 or len(e) < 1:
        messagebox.askretrycancel(title="Field Error", message="Please fill the website password and email"
                                                               " fields before adding")
    else:
        is_ok = messagebox.askokcancel(title=w, message=f"These are the details entered: \nEmail: {e} \nPassword: "
                                                        f"{p} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    data1 = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(data_complete, data, indent=4)
            else:
                # Updating old data with new data
                data1.update(data_complete)
                with open("data.json", "w") as data:
                # Saving updated data
                    json.dump(data1, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "jeremymlamb1996@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=password_generator, width=14)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", command=add_info, width=36)
add_button.grid(column=1, row=5, columnspan=2)
window.mainloop()

