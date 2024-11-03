from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Arial", 10)
BLACK = "#252525"
YELLOW = "#FFB200"
GREEN = "#41B06E"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if (len(website_name)==0) or (len(email)==0) or (len(password)==0):
        messagebox.showerror(title="Somthing Want Wrong!", message="Fill All The Inputs Please.")
    else:
        is_ok = messagebox.askyesno(title=website_name, message=f"These are the information\nEmail: {email}\nPassword: {password}\nSave these information?")
        if is_ok:
            with open(file="saved_passwords.txt", mode="a") as file:
                file.write(f"{website_name} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.resizable(False, False)
window.config(padx=40, pady=40, bg=BLACK)

#------------------------------------------------------------------ 0-ROW
# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLACK)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)
#------------------------------------------------------------------ 1-ROW
wbsite_label = Label(text="Website", font=FONT, fg="white", bg=BLACK)
wbsite_label.grid(column=0, row=1)

website_input = Entry(width=50)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
#------------------------------------------------------------------ 2-ROW
email_label = Label(text="Email-Username", font=FONT, fg="white", bg=BLACK)
email_label.grid(column=0, row=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "alishahriarioff@gmail.com")
#------------------------------------------------------------------ 3-ROW
password_label = Label(text="Password", font=FONT, fg="white", bg=BLACK)
password_label.grid(column=0, row=3)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password", border=False, bg=YELLOW, command=generate_password)
generate_pass_btn.grid(column=2, row=3)
#------------------------------------------------------------------ 4-ROW
add_btn = Button(text="Add", width=42, border=False, bg=GREEN, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()