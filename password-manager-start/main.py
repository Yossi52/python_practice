from tkinter import *
from tkinter import messagebox
from random import choices, randint, shuffle
import pyperclip


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
    web_input = web_entry.get()
    email_input = email_entry.get()
    pw_input = pw_entry.get()

    if web_input == "" or email_input == "" or pw_input == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_input,
                                       message=f"These are the details entered: \nEmail: {email_input}"
                                               f"\nPassword: {pw_input}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web_input} | {email_input} | {pw_input}\n")
            web_entry.delete(0, END)
            pw_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white")
email_label.config(padx=10)
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:", bg="white")
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=45)
web_entry.grid(sticky='e', row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=45)
email_entry.insert(0, "email@gmail.com")
email_entry.grid(sticky='e', row=2, column=1, columnspan=2)
pw_entry = Entry(width=21)
pw_entry.grid(sticky='w', row=3, column=1)

# Buttons
generate_pw_button = Button(text="Generate Password",width=15, command=create_password)
generate_pw_button.grid(sticky="e", row=3, column=2)
add_button = Button(text="add", width=44, command=save)
add_button.grid(sticky='e', row=4, column=1, columnspan=2)


window.mainloop()
