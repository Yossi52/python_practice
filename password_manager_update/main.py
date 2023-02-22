from tkinter import *
from tkinter import messagebox
from random import choices, randint, shuffle
import pyperclip
import json


BACKGROUND_COLOR = "#E6FEFC"


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            info = data[website]
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {info['email']}\n\nPassword: {info['password']}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for  the {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letter = [letter for letter in choices(letters, k=randint(8, 10))]
    pw_number = [number for number in choices(numbers, k=randint(2, 4))]
    pw_symbol = [symbol for symbol in choices(symbols, k=randint(2, 4))]
    pw_list = pw_letter + pw_number + pw_symbol
    shuffle(pw_list)
    password = "".join(pw_list)

    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_input = web_entry.get().title()
    email_input = email_entry.get()
    pw_input = pw_entry.get()
    new_data = {
        web_input: {
            "email": email_input,
            "password": pw_input
        }
    }

    if web_input == "" or email_input == "" or pw_input == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pw_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", bg=BACKGROUND_COLOR)
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg=BACKGROUND_COLOR)
email_label.config(padx=10)
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:", bg=BACKGROUND_COLOR)
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=28)
web_entry.grid(sticky='w', row=1, column=1)
web_entry.focus()
email_entry = Entry(width=45)
email_entry.insert(0, "email@gmail.com")
email_entry.grid(sticky='e', row=2, column=1, columnspan=2)
pw_entry = Entry(width=28)
pw_entry.grid(sticky='w', row=3, column=1)

# Buttons
generate_pw_button = Button(text="Generate Password", width=15, command=create_password)
generate_pw_button.grid(sticky="e", row=3, column=2)
add_button = Button(text="add", width=44, command=save)
add_button.grid(sticky='e', row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(sticky="e", row=1, column=2)


window.mainloop()
