from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    pass_input.insert(0, "".join(password_list))
    # pyperclip.copy(pass_input.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website:{
            "email":email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="Don`t leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0,'end')
            pass_input.delete(0,'end')


# ---------------------------- Search Password ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No hay datos disponibles")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Error", message="No hay datos disponibles de ese sitio")
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=400,height=400)


# Background img 
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Labels
web_label = Label(text="Website")
web_label.grid(column=0,row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)

pass_label = Label(text="Password")
pass_label.grid(column=0,row=3)

# Entrys
web_input = Entry(width=35)
web_input.grid(column=1,row=1)
web_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1,row=2)

pass_input = Entry(width=31)
pass_input.grid(column=1,row=3)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2,row=1)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2,row=3)

add_button = Button(text="Add", width=26, command=save_data)
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()