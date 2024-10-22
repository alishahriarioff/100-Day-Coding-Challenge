from tkinter import *

FONT = ("Arial", 16)

def calculate():
    km = round(int(input.get()) * 1.609344)
    resualt_label.config(text=str(km))

window = Tk()
window.title("Mile To Kilometers App")
# window.minsize(width=400, height=200)
window.config(padx=40, pady=40)



input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Mile", font=FONT)
miles_label.grid(column=2, row=0)

#-----------------------------------------------------------

equal_label = Label(text="Is Equal To:", font=FONT)
equal_label.grid(column=0, row=1)

resualt_label = Label(text="0", font=FONT)
resualt_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=FONT)
kilometer_label.grid(column=2, row=1)

#-----------------------------------------------------------

button = Button(text="Calculate", font=FONT, command=calculate)
button.grid(column=1, row=2)

window.mainloop()