from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, "end")
    input_password.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    print("saved")
    value_website_entries = input_website.get()
    value_email_username_entries = input_email_username.get()
    value_password = input_password.get()

    if len(value_website_entries) == 0 or len(value_email_username_entries) == 0 or len(value_password) == 0:
        messagebox.showwarning(title="", message="Warning", detail="Please do not leave any field empty")
    else:
        is_ok_to_save = messagebox.askokcancel(title="", message=f"Website name is: {value_website_entries}", detail=f"These are the info that inserted. Username is: "f"{value_email_username_entries}, Password is: {value_password} \n Is it OK to save?")
        if is_ok_to_save:
            with open("data.txt", "a") as file:
                file.write(f"🌎: {value_website_entries}  ❖❖❖❖  📧: {value_email_username_entries}  ❖❖❖❖  🔐: {value_password} \n")
            input_website.delete(0,"end")
            input_password.delete(0, "end")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=background_image)
canvas.grid(row=0, column=1)

# Labels
label_website_name = Label(text="Website:")
label_website_name.grid(row=1, column=0)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Inputs(Entries)
input_website = Entry(width=38)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_email_username = Entry(width=38)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "farjadhesam@gmail.com")
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

# Buttons
button_generate_password = Button(text="Generate password", command=password_generator)
button_generate_password.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()