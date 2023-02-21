from tkinter import *


def button_clicked():
    mile = float(mile_input.get())
    km = mile * 1.609344
    new_text = "%.3f" %km
    km_label.config(text=new_text)


window = Tk()
window.minsize(width=250, height=150)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

# Entry
mile_input = Entry(width=5)
mile_input.insert(END, string="0")
mile_input.grid(row=0, column=1)

# Label
label1 = Label(text="Miles")
label1.config(padx=10, pady=5)
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.config(padx=10, pady=5)
label2.grid(row=1, column=0)

km_label = Label(text="0")
km_label.config(padx=10, pady=5)
km_label.grid(row=1, column=1)

label3 = Label(text="Km")
label3.config(padx=10, pady=5)
label3.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()